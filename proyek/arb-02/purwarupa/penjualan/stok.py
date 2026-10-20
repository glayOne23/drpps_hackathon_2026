"""Aturan stok SIGAP (lihat Tabel C.2 proposal).

| Kejadian                       | Stok fisik | Stok dipesan | Stok tersedia |
|--------------------------------|------------|--------------|---------------|
| Barang masuk                   | +q         |              | +q            |
| Pesanan diterima server        |            | +q           | −q            |
| Pesanan dibatalkan sebelum kirim |          | −q           | +q            |
| Konfirmasi kirim (FEFO)        | −q         | −q           | tetap         |
| Penyesuaian (opname)           | ± selisih  |              | ± selisih     |

Setiap perubahan berjalan dalam satu transaksi dengan penguncian baris produk (SELECT ... FOR UPDATE),
dan setiap perubahan menulis satu baris MutasiStok.
"""
from datetime import date

from django.db import IntegrityError, transaction
from django.utils import timezone

from .models import Batch, MutasiStok, Outlet, PengirimanBatch, Pesanan, PesananItem, Produk


class Konflik(Exception):
    """Permintaan sah tetapi bertentangan dengan keadaan stok atau status pesanan."""


def _kunci_produk(ids):
    # Urutan id tetap agar dua transaksi yang mengunci produk yang sama tidak saling menunggu (deadlock).
    return {p.id: p for p in Produk.objects.select_for_update().filter(id__in=sorted(set(ids))).order_by("id")}


def _mutasi(produk, jenis, fisik, dipesan, referensi, oleh, batch=None, alasan=""):
    MutasiStok.objects.create(
        produk=produk, batch=batch, jenis=jenis, perubahan_fisik=fisik, perubahan_dipesan=dipesan,
        fisik_sesudah=produk.stok_fisik, dipesan_sesudah=produk.stok_dipesan,
        referensi=referensi, oleh=oleh, alasan=alasan,
    )


def barang_masuk(produk, no_batch, kedaluwarsa, jumlah, masuk_pada, oleh="Admin gudang"):
    with transaction.atomic():
        p = _kunci_produk([produk.id])[produk.id]
        b = Batch.objects.create(produk=p, no_batch=no_batch, kedaluwarsa=kedaluwarsa,
                                 jumlah_masuk=jumlah, sisa=jumlah, masuk_pada=masuk_pada)
        p.stok_fisik += jumlah
        p.save(update_fields=["stok_fisik"])
        _mutasi(p, "masuk", jumlah, 0, f"batch {no_batch}", oleh, batch=b)
        return b


def _hasil_duplikat(pesanan):
    return {"status": "duplikat", "pesanan_id": pesanan.id, "status_awal": pesanan.status,
            "pesan": "Pesanan ini sudah pernah diterima; tidak dicatat ulang."}


def terima_pesanan(client_uuid, outlet_id, item, dibuat_di_hp=None, sales="Sales A"):
    """Simpan pesanan dari HP tepat satu kali dan kurangi stok tersedia (stok dipesan bertambah)."""
    lama = Pesanan.objects.filter(client_uuid=client_uuid).first()
    if lama:
        return _hasil_duplikat(lama)
    try:
        with transaction.atomic():
            produk = _kunci_produk(int(it["produk_id"]) for it in item)
            ps = Pesanan.objects.create(client_uuid=client_uuid, outlet_id=outlet_id, sales=sales,
                                        status="diterima", dibuat_di_hp=dibuat_di_hp)
            baris, total, ada_terima, semua_terima = [], 0, False, True
            for it in item:
                p, j = produk.get(int(it["produk_id"])), int(it["jumlah"])
                if p is None or j <= 0:
                    continue
                tersedia = p.stok_tersedia
                if j <= tersedia:
                    p.stok_dipesan += j
                    p.save(update_fields=["stok_dipesan"])
                    _mutasi(p, "pesan", 0, j, f"pesanan #{ps.id}", sales)
                    terima, ket, ada_terima = j, "diterima", True
                    total += j * p.harga
                else:
                    terima, ket, semua_terima = 0, f"ditolak: sisa stok tersedia {tersedia}", False
                PesananItem.objects.create(pesanan=ps, produk=p, jumlah_diminta=j, jumlah_diterima=terima,
                                           harga=p.harga, keterangan=ket)
                baris.append({"produk": p.nama, "diminta": j, "diterima": terima, "keterangan": ket})
            ps.status = "diterima" if semua_terima else ("diterima_sebagian" if ada_terima else "ditolak")
            ps.total = total
            ps.save(update_fields=["status", "total"])
    except IntegrityError:
        # Kode yang sama tiba bersamaan dari dua permintaan: yang kalah menjadi duplikat.
        return _hasil_duplikat(Pesanan.objects.get(client_uuid=client_uuid))
    return {"status": ps.status, "pesanan_id": ps.id, "baris": baris,
            "diterima_server": ps.diterima_server.isoformat()}


def batalkan(pesanan_id, alasan, oleh="Admin penjualan"):
    if not alasan:
        raise Konflik("alasan pembatalan wajib diisi")
    with transaction.atomic():
        ps = Pesanan.objects.select_for_update().get(id=pesanan_id)
        if ps.status not in ("diterima", "diterima_sebagian"):
            raise Konflik(f"pesanan berstatus {ps.status} tidak dapat dibatalkan")
        items = list(ps.item.filter(jumlah_diterima__gt=0))
        produk = _kunci_produk(i.produk_id for i in items)
        for it in items:
            p = produk[it.produk_id]
            p.stok_dipesan -= it.jumlah_diterima
            p.save(update_fields=["stok_dipesan"])
            _mutasi(p, "batal", 0, -it.jumlah_diterima, f"pesanan #{ps.id}", oleh, alasan=alasan)
        ps.status, ps.dibatalkan_pada, ps.alasan_batal = "batal", timezone.now(), alasan
        ps.save(update_fields=["status", "dibatalkan_pada", "alasan_batal"])
    return {"status": "batal", "pesanan_id": ps.id}


def kirim(pesanan_id, oleh="Admin gudang"):
    """Konfirmasi kirim: ambil dari batch dengan kedaluwarsa terdekat (FEFO) dan catat outlet penerima batch."""
    with transaction.atomic():
        ps = Pesanan.objects.select_for_update().get(id=pesanan_id)
        if ps.status not in ("diterima", "diterima_sebagian"):
            raise Konflik(f"pesanan berstatus {ps.status} tidak dapat dikirim")
        items = list(ps.item.filter(jumlah_diterima__gt=0))
        produk = _kunci_produk(i.produk_id for i in items)
        dikirim = []
        for it in items:
            p, perlu = produk[it.produk_id], it.jumlah_diterima
            if p.stok_fisik < perlu:
                raise Konflik(f"stok fisik {p.nama} hanya {p.stok_fisik}; pesanan perlu perhatian admin")
            for b in Batch.objects.select_for_update().filter(produk=p, sisa__gt=0).order_by("kedaluwarsa", "id"):
                if perlu == 0:
                    break
                ambil = min(b.sisa, perlu)
                b.sisa -= ambil
                b.save(update_fields=["sisa"])
                PengirimanBatch.objects.create(item=it, batch=b, jumlah=ambil)
                p.stok_fisik -= ambil
                p.stok_dipesan -= ambil
                perlu -= ambil
                _mutasi(p, "kirim", -ambil, -ambil, f"pesanan #{ps.id}", oleh, batch=b)
                dikirim.append({"produk": p.nama, "batch": b.no_batch, "jumlah": ambil})
            if perlu:
                raise Konflik(f"sisa batch {p.nama} tidak cukup")
            p.save(update_fields=["stok_fisik", "stok_dipesan"])
        ps.status, ps.dikirim_pada = "dikirim", timezone.now()
        ps.save(update_fields=["status", "dikirim_pada"])
    return {"status": "dikirim", "pesanan_id": ps.id, "batch": dikirim}


def sesuaikan(produk_id, jumlah_fisik, alasan, oleh="Admin gudang"):
    """Opname: bandingkan hitungan rak dengan stok fisik (bukan stok tersedia), lalu sesuaikan batch."""
    if jumlah_fisik < 0 or not alasan:
        raise Konflik("jumlah fisik dan alasan wajib diisi")
    with transaction.atomic():
        p = _kunci_produk([produk_id])[produk_id]
        sebelum = p.stok_fisik
        selisih = jumlah_fisik - sebelum
        batch = list(Batch.objects.select_for_update().filter(produk=p).order_by("kedaluwarsa", "id"))
        if not batch:
            raise Konflik(f"{p.nama} belum punya batch")
        if selisih > 0:
            b = next((x for x in batch if x.sisa > 0), batch[-1])
            b.sisa += selisih
            b.save(update_fields=["sisa"])
            p.stok_fisik = jumlah_fisik
            _mutasi(p, "penyesuaian", selisih, 0, "stock opname", oleh, batch=b, alasan=alasan)
        elif selisih < 0:
            kurang = -selisih
            for b in batch:  # kurangi mulai batch tertua (bawaan); batch lain dipakai bila belum cukup
                if kurang == 0:
                    break
                ambil = min(b.sisa, kurang)
                if ambil == 0:
                    continue
                b.sisa -= ambil
                b.save(update_fields=["sisa"])
                p.stok_fisik -= ambil
                kurang -= ambil
                _mutasi(p, "penyesuaian", -ambil, 0, "stock opname", oleh, batch=b, alasan=alasan)
        else:
            _mutasi(p, "penyesuaian", 0, 0, "stock opname", oleh, alasan=alasan)
        p.save(update_fields=["stok_fisik"])
    return {"status": "disesuaikan", "stok_fisik_sistem": sebelum, "stok_fisik_hitung": jumlah_fisik,
            "selisih": selisih, "stok_dipesan": p.stok_dipesan, "stok_tersedia": p.stok_tersedia,
            "perlu_perhatian": p.stok_fisik < p.stok_dipesan}


def telusur(no_batch):
    b = Batch.objects.select_related("produk").get(no_batch=no_batch)
    rows = (PengirimanBatch.objects.filter(batch=b)
            .select_related("item__pesanan__outlet").order_by("item__pesanan__dikirim_pada"))
    return {
        "no_batch": b.no_batch, "produk": b.produk.nama, "kedaluwarsa": b.kedaluwarsa.isoformat(), "sisa": b.sisa,
        "penerima": [{"outlet": r.item.pesanan.outlet.nama, "pesanan_id": r.item.pesanan_id, "jumlah": r.jumlah,
                      "dikirim_pada": r.item.pesanan.dikirim_pada.isoformat()} for r in rows],
    }


def isi_data_contoh():
    """Hapus semua data lalu isi data contoh fiktif (nomor BPOM fiktif, bukan data mitra)."""
    with transaction.atomic():
        for model in (MutasiStok, PengirimanBatch, PesananItem, Pesanan, Batch, Produk, Outlet):
            model.objects.all().delete()
        for kode, nama, jenis in [
            ("OT001", "Apotek Sehat Jebres", "apotek"),
            ("OT002", "Apotek Mojosongo Farma", "apotek"),
            ("OT003", "Minimarket Barokah Solo", "minimarket"),
            ("OT004", "Toko Obat Waras", "toko obat"),
        ]:
            Outlet.objects.create(kode=kode, nama=nama, jenis=jenis, sales="Sales A")
        data = [
            # kode, nama, harga, stok minimum, [(no batch, kedaluwarsa, jumlah, tanggal masuk)]
            ("MDP250", "Madu Plus Propolis 250 ml", 95000, 10,
             [("MP-2609", date(2027, 9, 30), 25, date(2026, 9, 10)),
              ("MP-2603", date(2027, 3, 31), 15, date(2026, 10, 1))]),  # masuk belakangan, kedaluwarsa lebih dulu
            ("JKA200", "Jamu Kunyit Asam 200 ml", 15000, 10, [("JK-2612", date(2026, 12, 31), 24, date(2026, 9, 1))]),
            ("KHB060", "Kapsul Habbatussauda isi 60", 55000, 10, [("KH-2702", date(2027, 2, 28), 12, date(2026, 9, 5))]),
            ("MDH500", "Madu Hutan 500 ml", 120000, 8, [("MH-2708", date(2027, 8, 31), 30, date(2026, 9, 20))]),
            ("SKR330", "Sari Kurma 330 g", 45000, 6, [("SK-2705", date(2027, 5, 31), 18, date(2026, 9, 25))]),
        ]
        for i, (kode, nama, harga, minimum, batch) in enumerate(data, 1):
            p = Produk.objects.create(kode=kode, nama=nama, satuan="botol", harga=harga,
                                      no_bpom=f"TR-CONTOH-{i:03d}", stok_min=minimum)
            for no_batch, ed, jumlah, masuk in batch:
                barang_masuk(p, no_batch, ed, jumlah, masuk)
