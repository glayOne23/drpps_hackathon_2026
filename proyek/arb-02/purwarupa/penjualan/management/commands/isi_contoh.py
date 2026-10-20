from django.core.management.base import BaseCommand

from penjualan.stok import isi_data_contoh


class Command(BaseCommand):
    help = "Hapus data lalu isi data contoh fiktif (5 produk dengan batch, 4 outlet)."

    def handle(self, *args, **options):
        isi_data_contoh()
        self.stdout.write(self.style.SUCCESS("Data contoh SIGAP sudah diisi."))
