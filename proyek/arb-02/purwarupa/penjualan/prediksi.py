"""Prediksi penjualan (peramalan permintaan) per produk untuk saran jumlah produksi.

Permintaan mingguan = riwayat dari luar SIGAP (PermintaanMingguan, mis. rekap Excel lama) + pesanan di SIGAP.
Dari pesanan SIGAP dihitung jumlah yang DIMINTA, termasuk baris yang ditolak karena stok kurang (permintaan yang
tidak terlayani tetap permintaan); pesanan yang dibatalkan tidak dihitung.

Metode: exponential smoothing dengan tren (Holt). Parameter alpha dan beta dipilih dari kisi 0,1–0,9 dengan galat
ramalan satu langkah terkecil. Hanya minggu yang sudah lengkap yang dipakai; minggu berjalan ditampilkan terpisah.
Akurasi diukur dengan menyisihkan 4 minggu terakhir, lalu dibandingkan dengan ramalan naif (minggu depan = minggu
terakhir) memakai WAPE = Σ|aktual − ramalan| / Σ aktual.
"""
import math
import random
from datetime import timedelta

from django.db.models import Sum
from django.db.models.functions import TruncWeek
from django.utils import timezone

from .models import PermintaanMingguan, PesananItem, Produk

H = 4          # jumlah minggu yang diramal
UJI = 4        # minggu terakhir yang disisihkan untuk mengukur akurasi
MIN_LATIH = 8  # minggu minimum untuk melatih model saat uji akurasi
KISI = [i / 10 for i in range(1, 10)]


def senin(tgl):
    return tgl - timedelta(days=tgl.weekday())


def _pesanan_per_minggu(produk):
    baris = (PesananItem.objects.filter(produk=produk).exclude(pesanan__status="batal")
             .annotate(minggu=TruncWeek("pesanan__diterima_server"))
             .values("minggu").annotate(jumlah=Sum("jumlah_diminta")))
    return {timezone.localtime(b["minggu"]).date(): b["jumlah"] for b in baris}


def deret_mingguan(produk, minggu_ini):
    """Daftar (minggu, jumlah) untuk minggu lengkap sebelum minggu_ini; minggu tanpa data diisi 0."""
    data = {r.minggu: r.jumlah for r in PermintaanMingguan.objects.filter(produk=produk, minggu__lt=minggu_ini)}
    for m, j in _pesanan_per_minggu(produk).items():
        if m < minggu_ini:
            data[m] = data.get(m, 0) + j
    if not data:
        return []
    deret, m = [], min(data)
    while m < minggu_ini:
        deret.append((m, data.get(m, 0)))
        m += timedelta(days=7)
    return deret


def _holt(y, a, b):
    level = y[0]
    tren = (y[min(3, len(y) - 1)] - y[0]) / max(1, min(3, len(y) - 1))
    sse = 0.0
    for t in range(1, len(y)):
        ramal = level + tren
        sse += (y[t] - ramal) ** 2
        level_baru = a * y[t] + (1 - a) * (level + tren)
        tren = b * (level_baru - level) + (1 - b) * tren
        level = level_baru
    return level, tren, sse


def ramal(y, h=H):
    """Ramalan h minggu ke depan beserta parameter terpilih."""
    if len(y) < 2:
        rata = float(y[0]) if y else 0.0
        return [rata] * h, None, None
    _, a, b = min((_holt(y, a, b)[2], a, b) for a in KISI for b in KISI)
    level, tren, _ = _holt(y, a, b)
    return [max(0.0, level + k * tren) for k in range(1, h + 1)], a, b


def _galat(aktual, ramalan):
    return sum(abs(x - f) for x, f in zip(aktual, ramalan)), sum(aktual)


def uji_akurasi(y):
    """Sisihkan UJI minggu terakhir; kembalikan (galat model, galat naif, total aktual) atau None bila data kurang."""
    if len(y) < MIN_LATIH + UJI:
        return None
    latih, aktual = y[:-UJI], y[-UJI:]
    model, _, _ = ramal(latih, UJI)
    naif = [latih[-1]] * UJI
    g_model, total = _galat(aktual, model)
    g_naif, _ = _galat(aktual, naif)
    return g_model, g_naif, total


def _wape(galat, total):
    return round(100 * galat / total, 1) if total else None


def semua():
    minggu_ini = senin(timezone.localdate())
    hasil, sum_model, sum_naif, sum_total = [], 0.0, 0.0, 0
    for p in Produk.objects.order_by("id"):
        deret = deret_mingguan(p, minggu_ini)
        y = [j for _, j in deret]
        ramalan, a, b = ramal(y) if y else ([0.0] * H, None, None)
        kebutuhan = math.ceil(sum(ramalan))
        saran = max(0, kebutuhan + p.stok_min - p.stok_tersedia)
        per_hari = sum(ramalan) / (H * 7)
        uji = uji_akurasi(y)
        if uji:
            sum_model, sum_naif, sum_total = sum_model + uji[0], sum_naif + uji[1], sum_total + uji[2]
        berjalan = _pesanan_per_minggu(p).get(minggu_ini, 0)
        hasil.append({
            "kode": p.kode, "nama": p.nama, "stok_tersedia": p.stok_tersedia, "stok_min": p.stok_min,
            "riwayat": [{"minggu": m.isoformat(), "jumlah": j} for m, j in deret],
            "jumlah_minggu": len(y),
            "rata_4_minggu": round(sum(y[-4:]) / len(y[-4:]), 1) if y else 0,
            "ramalan": [round(f, 1) for f in ramalan],
            "kebutuhan_4_minggu": kebutuhan,
            "minggu_berjalan": berjalan,
            "cukup_hari": round(p.stok_tersedia / per_hari) if per_hari > 0 else None,
            "saran_produksi": saran,
            "alasan": f"perkiraan 4 minggu {kebutuhan} + stok minimum {p.stok_min} − stok tersedia {p.stok_tersedia}",
            "alpha": a, "beta": b,
            "wape_model": _wape(uji[0], uji[2]) if uji else None,
            "wape_naif": _wape(uji[1], uji[2]) if uji else None,
            "sumber_riwayat": sorted(set(PermintaanMingguan.objects.filter(produk=p).values_list("sumber", flat=True))),
        })
    return {
        "minggu_ini": minggu_ini.isoformat(), "produk": hasil,
        "wape_gabungan_model": _wape(sum_model, sum_total), "wape_gabungan_naif": _wape(sum_naif, sum_total),
        "metode": "exponential smoothing dengan tren (Holt); uji 4 minggu terakhir; WAPE dibanding ramalan naif",
    }


# Pola data sintetis per produk: (rata-rata awal per minggu, tren per minggu, simpangan acak)
POLA_SINTETIS = {
    "MDP250": (9.0, 0.12, 1.5),
    "JKA200": (7.0, 0.0, 1.5),
    "KHB060": (3.5, 0.08, 1.0),
    "MDH500": (5.0, 0.05, 1.2),
    "SKR330": (6.0, -0.06, 1.2),
}


def isi_riwayat_sintetis(minggu=26, benih=2026):
    """Isi riwayat permintaan sintetis (bukan data mitra) untuk minggu-minggu lengkap sebelum minggu ini."""
    acak = random.Random(benih)
    minggu_ini = senin(timezone.localdate())
    for p in Produk.objects.order_by("id"):
        dasar, tren, sd = POLA_SINTETIS.get(p.kode, (5.0, 0.0, 1.0))
        for i in range(minggu):
            nilai = max(0, round(dasar + tren * i + acak.gauss(0, sd)))
            PermintaanMingguan.objects.create(produk=p, minggu=minggu_ini - timedelta(weeks=minggu - i),
                                              jumlah=nilai, sumber="sintetis")
