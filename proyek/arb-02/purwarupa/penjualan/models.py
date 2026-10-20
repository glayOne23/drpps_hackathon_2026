"""Model data SIGAP: outlet, produk (stok fisik dan dipesan), batch, pesanan, pengiriman per batch, mutasi stok.

Stok tersedia = stok fisik − stok dipesan. Stok fisik selalu sama dengan jumlah sisa semua batch produk itu.
PositiveIntegerField membuat PostgreSQL menolak stok bernilai minus.
"""
from django.db import models


class Outlet(models.Model):
    kode = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=120)
    jenis = models.CharField(max_length=30)
    sales = models.CharField(max_length=60)

    def __str__(self):
        return self.nama


class Produk(models.Model):
    kode = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=120)
    satuan = models.CharField(max_length=20)
    harga = models.PositiveIntegerField()
    no_bpom = models.CharField("nomor registrasi BPOM", max_length=40)
    stok_fisik = models.PositiveIntegerField(default=0)
    stok_dipesan = models.PositiveIntegerField(default=0)
    stok_min = models.PositiveIntegerField("stok minimum", default=0)

    class Meta:
        verbose_name_plural = "produk"

    @property
    def stok_tersedia(self):
        return self.stok_fisik - self.stok_dipesan

    def __str__(self):
        return self.nama


class Batch(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.PROTECT, related_name="batch")
    no_batch = models.CharField(max_length=30, unique=True)
    kedaluwarsa = models.DateField()
    jumlah_masuk = models.PositiveIntegerField()
    sisa = models.PositiveIntegerField()
    masuk_pada = models.DateField()

    class Meta:
        verbose_name_plural = "batch"

    def __str__(self):
        return self.no_batch


class Pesanan(models.Model):
    STATUS = [
        ("diterima", "Diterima"),
        ("diterima_sebagian", "Diterima sebagian"),
        ("ditolak", "Ditolak"),
        ("dikirim", "Dikirim"),
        ("batal", "Batal"),
    ]
    client_uuid = models.UUIDField("kode unik dari HP", unique=True)
    outlet = models.ForeignKey(Outlet, on_delete=models.PROTECT)
    sales = models.CharField(max_length=60)
    status = models.CharField(max_length=20, choices=STATUS)
    total = models.PositiveBigIntegerField(default=0)
    dibuat_di_hp = models.DateTimeField(null=True, blank=True)
    diterima_server = models.DateTimeField(auto_now_add=True)
    dikirim_pada = models.DateTimeField(null=True, blank=True)
    dibatalkan_pada = models.DateTimeField(null=True, blank=True)
    alasan_batal = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "pesanan"


class PesananItem(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE, related_name="item")
    produk = models.ForeignKey(Produk, on_delete=models.PROTECT)
    jumlah_diminta = models.PositiveIntegerField()
    jumlah_diterima = models.PositiveIntegerField()
    harga = models.PositiveIntegerField()
    keterangan = models.CharField(max_length=120)


class PengirimanBatch(models.Model):
    item = models.ForeignKey(PesananItem, on_delete=models.PROTECT, related_name="pengiriman")
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, related_name="pengiriman")
    jumlah = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "pengiriman batch"


class MutasiStok(models.Model):
    JENIS = [
        ("masuk", "Barang masuk"),
        ("pesan", "Pesanan diterima"),
        ("batal", "Pesanan dibatalkan"),
        ("kirim", "Pengiriman"),
        ("penyesuaian", "Penyesuaian (opname)"),
    ]
    produk = models.ForeignKey(Produk, on_delete=models.PROTECT, related_name="mutasi")
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, null=True, blank=True)
    jenis = models.CharField(max_length=20, choices=JENIS)
    perubahan_fisik = models.IntegerField(default=0)
    perubahan_dipesan = models.IntegerField(default=0)
    fisik_sesudah = models.PositiveIntegerField()
    dipesan_sesudah = models.PositiveIntegerField()
    referensi = models.CharField(max_length=60)
    oleh = models.CharField(max_length=60)
    alasan = models.CharField(max_length=200, blank=True)
    waktu = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "mutasi stok"
        ordering = ["-id"]
