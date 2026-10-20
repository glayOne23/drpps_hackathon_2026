# SIGAP: purwarupa Django + PostgreSQL (ARB-02)

Purwarupa ini menjadi bukti Lampiran C.5 proposal [Proposal_AntechAsync_SIGAP.docx](../Proposal_AntechAsync_SIGAP.docx). Aturan stok yang dipakai sama dengan Tabel C.2 proposal dan §5 [draf solusi](../draf-solusi-gabungan.md).

## Yang sudah berjalan

- **Halaman sales satu halaman** (`/`) untuk HP.
  - Pesanan selalu disimpan dulu di IndexedDB (Dexie.js) dengan kode unik.
  - Pesanan dikirim otomatis saat sinyal ada. Pemicunya: event `online`, pengecekan tiap 15 detik, atau tombol **Kirim sekarang**.
  - Tidak memakai PWA. Halaman harus sudah terbuka sebelum sinyal hilang.
- **Aturan stok** (`penjualan/stok.py`): stok tersedia = stok fisik − stok dipesan.
  - Pesanan menaikkan stok dipesan.
  - Konfirmasi kirim menurunkan stok fisik dan stok dipesan, mengambil batch dengan kedaluwarsa terdekat (FEFO), dan mencatat outlet penerima tiap batch.
  - Batal mengembalikan stok dipesan.
  - Opname membandingkan hitungan rak dengan stok fisik.
  - Semua perubahan berjalan di `transaction.atomic` dengan `select_for_update()` dan tercatat di `MutasiStok`.
- **Kode unik `client_uuid`**: pengiriman ulang dijawab `duplikat`, sehingga pesanan tercatat tepat sekali.
- **Prediksi penjualan** (`penjualan/prediksi.py`, `GET /api/prediksi`): ramalan permintaan 4 minggu per produk untuk saran produksi.
  - Permintaan mingguan = riwayat dari luar SIGAP (`PermintaanMingguan`, mis. rekap Excel lama) + pesanan SIGAP. Baris yang ditolak karena stok kurang ikut dihitung; pesanan batal tidak.
  - Metode: exponential smoothing dengan tren (Holt), parameter dipilih otomatis, Python murni tanpa pustaka tambahan.
  - Akurasi: 4 minggu terakhir disisihkan, lalu WAPE dibandingkan dengan ramalan naif (minggu depan = minggu terakhir).
  - Saran produksi = perkiraan 4 minggu + stok minimum − stok tersedia (minimal 0), beserta "stok cukup untuk ± hari".
  - **Riwayat 26 minggu di data contoh adalah data sintetis** (`isi_riwayat_sintetis`, benih acak tetap), bukan data mitra.
- **Panel uji admin** (`/panel/`): stok fisik/dipesan/tersedia, batch dan kedaluwarsa, telusur batch, prediksi penjualan (grafik + tabel), pesanan, dan mutasi.
- **Django admin** (`/admin/`) untuk semua tabel. Buat akun dengan `python manage.py createsuperuser`.

**Belum dibuat:** login dan hak akses per peran, kunjungan hari ini, check-in GPS, impor Excel, dan dashboard direktur lengkap. Data contoh bersifat fiktif, termasuk nomor BPOM `TR-CONTOH-…`.

## Menjalankan

Persyaratan: Python 3.12+, PostgreSQL 14+, Node.js 18+ (hanya untuk Dexie dan uji otomatis), dan Google Chrome.

```bash
# 1. PostgreSQL (contoh dengan Docker; atau pakai server PostgreSQL yang sudah ada)
docker run -d --name sigap-pg -e POSTGRES_USER=sigap -e POSTGRES_PASSWORD=sigap -e POSTGRES_DB=sigap \
  -p 127.0.0.1:5432:5432 postgres:16-alpine

# 2. Python
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py isi_contoh          # isi data contoh (5 produk dengan batch, 4 outlet)

# 3. Dexie untuk halaman sales
npm install && npm run siapkan

# 4. Jalankan
python manage.py runserver 0.0.0.0:8000
```

Buka `http://127.0.0.1:8000/` (sales) dan `http://127.0.0.1:8000/panel/` (panel). Untuk mencoba di HP pada Wi-Fi yang sama, buka `http://<IP-komputer>:8000/` dulu, lalu nyalakan mode pesawat.

Koneksi basis data diatur lewat variabel `SIGAP_DB_HOST`, `SIGAP_DB_PORT`, `SIGAP_DB_NAME`, `SIGAP_DB_USER`, dan `SIGAP_DB_PASSWORD`. Nilai bawaannya `127.0.0.1:5432`, `sigap`/`sigap`/`sigap`.

## Uji otomatis (menghasilkan bukti)

```bash
SIGAP_PYTHON=.venv/bin/python npm run uji
```

Skrip `uji/e2e.js` menjalankan migrasi, menyalakan server Django di port 8099, dan mengisi ulang data contoh. Setelah itu skrip membuka Chrome dengan tampilan HP dan memeriksa 22 hal:
- mode tanpa sinyal dan pengiriman tepat sekali;
- stok tersedia vs stok fisik;
- konfirmasi kirim dengan FEFO, batal, dan opname tanpa selisih palsu;
- dua pesanan bersamaan dan dua ponsel tanpa sinyal yang memesan stok terakhir;
- telusur batch;
- prediksi penjualan: saran produksi sesuai rumus, baris ditolak ikut dihitung, dan WAPE model lebih kecil daripada ramalan naif pada data sintetis.

Hasilnya tersimpan di `bukti/`:

| File | Isi |
|---|---|
| `hasil_uji.txt` | Laporan LULUS/GAGAL tiap pemeriksaan, beserta versi Python, Django, dan PostgreSQL |
| `01`–`04` | Halaman sales: online, tanpa sinyal, terkirim otomatis, pesanan melebihi stok ditolak |
| `05_panel_stok_batch_telusur.png` | Panel: stok fisik/dipesan/tersedia, batch, telusur batch MP-2603 |
| `06a`, `06b` | Dua ponsel tanpa sinyal memesan stok terakhir: satu diterima, satu ditolak |
| `07_panel_lengkap_pesanan_mutasi.png` | Panel lengkap dengan prediksi, pesanan, dan riwayat mutasi |
| `08_prediksi_penjualan.png` | Panel prediksi penjualan: grafik riwayat (sintetis) + ramalan 4 minggu, saran produksi, WAPE model vs naif |

Gambar Lampiran C.5a–d di proposal disusun dari tangkapan layar ini dan disimpan di [../lampiran/](../lampiran/). Hasil terakhir: **22/22 lulus** (20 Okt 2026; Python 3.12.3, Django 6.0.9, PostgreSQL 16.14, Chrome 152). WAPE gabungan pada 4 minggu uji (data sintetis): model 23,0%, ramalan naif 28,7%; model lebih akurat pada 4 dari 5 produk.
