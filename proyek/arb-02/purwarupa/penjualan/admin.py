from django.contrib import admin

from .models import Batch, MutasiStok, Outlet, PengirimanBatch, Pesanan, PesananItem, Produk


@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = ("kode", "nama", "jenis", "sales")
    search_fields = ("kode", "nama")


@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ("kode", "nama", "no_bpom", "stok_fisik", "stok_dipesan", "stok_tersedia", "stok_min")
    readonly_fields = ("stok_fisik", "stok_dipesan")  # stok hanya berubah lewat aturan stok, bukan diketik


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("no_batch", "produk", "kedaluwarsa", "jumlah_masuk", "sisa", "masuk_pada")
    list_filter = ("produk",)


class PesananItemInline(admin.TabularInline):
    model = PesananItem
    extra = 0
    readonly_fields = ("produk", "jumlah_diminta", "jumlah_diterima", "harga", "keterangan")


@admin.register(Pesanan)
class PesananAdmin(admin.ModelAdmin):
    list_display = ("id", "outlet", "sales", "status", "total", "dibuat_di_hp", "diterima_server")
    list_filter = ("status",)
    inlines = [PesananItemInline]


@admin.register(PengirimanBatch)
class PengirimanBatchAdmin(admin.ModelAdmin):
    list_display = ("batch", "item", "jumlah")


@admin.register(MutasiStok)
class MutasiStokAdmin(admin.ModelAdmin):
    list_display = ("waktu", "produk", "batch", "jenis", "perubahan_fisik", "perubahan_dipesan",
                    "fisik_sesudah", "dipesan_sesudah", "referensi", "oleh")
    list_filter = ("jenis", "produk")
