"""API JSON untuk halaman sales (HP) dan panel uji. Purwarupa: tanpa login; hak akses per peran menyusul."""
import json
import uuid
from datetime import timedelta

import django
from django.db import connection
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from . import stok
from .models import Batch, MutasiStok, Outlet, Pesanan, Produk

HARI_MENDEKATI_KEDALUWARSA = 90


def _json(request):
    try:
        return json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        return {}


def _produk_json(p):
    return {
        "id": p.id, "kode": p.kode, "nama": p.nama, "satuan": p.satuan, "harga": p.harga, "no_bpom": p.no_bpom,
        "stok_fisik": p.stok_fisik, "stok_dipesan": p.stok_dipesan, "stok_tersedia": p.stok_tersedia,
        "stok_min": p.stok_min, "menipis": p.stok_tersedia <= p.stok_min,
        "perlu_perhatian": p.stok_fisik < p.stok_dipesan,
    }


@require_GET
def versi(request):
    with connection.cursor() as c:
        c.execute("SHOW server_version")
        pg = c.fetchone()[0]
    return JsonResponse({"django": django.get_version(), "postgresql": pg})


@require_GET
def katalog(request):
    return JsonResponse({
        "produk": [_produk_json(p) for p in Produk.objects.order_by("id")],
        "outlet": list(Outlet.objects.order_by("id").values("id", "kode", "nama", "jenis")),
        "waktu_server": timezone.now().isoformat(),
    })


@csrf_exempt
@require_POST
def pesanan_baru(request):
    d = _json(request)
    item = d.get("item") or []
    try:
        kode = uuid.UUID(str(d.get("client_uuid", "")))
    except ValueError:
        kode = None
    if kode is None or not isinstance(item, list) or not item:
        return JsonResponse({"error": "client_uuid dan item wajib diisi dengan benar"}, status=422)
    hasil = stok.terima_pesanan(kode, int(d.get("outlet_id", 0)), item, d.get("dibuat_di_hp") or None)
    return JsonResponse(hasil, status=200 if hasil["status"] == "duplikat" else 201)


def _aksi(fungsi, *args):
    try:
        return JsonResponse(fungsi(*args))
    except stok.Konflik as e:
        return JsonResponse({"error": str(e)}, status=409)
    except (Pesanan.DoesNotExist, Produk.DoesNotExist, Batch.DoesNotExist, KeyError):
        return JsonResponse({"error": "data tidak ditemukan"}, status=404)


@csrf_exempt
@require_POST
def pesanan_batal(request, pesanan_id):
    return _aksi(stok.batalkan, pesanan_id, _json(request).get("alasan", ""))


@csrf_exempt
@require_POST
def pesanan_kirim(request, pesanan_id):
    return _aksi(stok.kirim, pesanan_id)


@csrf_exempt
@require_POST
def penyesuaian(request):
    d = _json(request)
    return _aksi(stok.sesuaikan, int(d.get("produk_id", 0)), int(d.get("jumlah_fisik", -1)), d.get("alasan", ""))


@require_GET
def telusur_batch(request, no_batch):
    return _aksi(stok.telusur, no_batch)


@require_GET
def ringkasan(request):
    batas = timezone.localdate() + timedelta(days=HARI_MENDEKATI_KEDALUWARSA)
    pesanan = []
    for ps in Pesanan.objects.select_related("outlet").prefetch_related("item__produk").order_by("-id")[:20]:
        pesanan.append({
            "id": ps.id, "outlet": ps.outlet.nama, "status": ps.status,
            "dibuat_di_hp": ps.dibuat_di_hp.isoformat() if ps.dibuat_di_hp else None,
            "diterima_server": ps.diterima_server.isoformat(),
            "item": [{"produk": i.produk.nama, "diminta": i.jumlah_diminta, "diterima": i.jumlah_diterima,
                      "keterangan": i.keterangan} for i in ps.item.all()],
        })
    return JsonResponse({
        "produk": [_produk_json(p) for p in Produk.objects.order_by("id")],
        "batch": [{"no_batch": b.no_batch, "produk": b.produk.nama, "kedaluwarsa": b.kedaluwarsa.isoformat(),
                   "sisa": b.sisa, "mendekati_kedaluwarsa": b.kedaluwarsa <= batas}
                  for b in Batch.objects.select_related("produk").order_by("produk_id", "kedaluwarsa")],
        "pesanan": pesanan,
        "mutasi": [{"waktu": m.waktu.isoformat(), "produk": m.produk.nama,
                    "batch": m.batch.no_batch if m.batch else "", "jenis": m.jenis,
                    "fisik": m.perubahan_fisik, "dipesan": m.perubahan_dipesan,
                    "fisik_sesudah": m.fisik_sesudah, "dipesan_sesudah": m.dipesan_sesudah,
                    "referensi": m.referensi, "alasan": m.alasan}
                   for m in MutasiStok.objects.select_related("produk", "batch")[:30]],
        "waktu_server": timezone.now().isoformat(),
    })


@csrf_exempt
@require_POST
def reset(request):
    stok.isi_data_contoh()
    return JsonResponse({"status": "data contoh dikembalikan ke awal"})
