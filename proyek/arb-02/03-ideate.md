# 3 · Ideate — ARB-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-02** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · **3 Ideate** · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · s.d. 20 Okt, diulang saat hackathon · Proposal: Bag. 4 butir 2 · PJ: koordinator teknis + seluruh tim
> Panduan metode: [_template/03-ideate.md](../_template/03-ideate.md)

## 1. How Might We

| Sudut | Bagaimana kita bisa ... |
|---|---|
| Perkuat yang baik | ... memakai kebiasaan sales yang sudah memakai WA sebagai cara input data? |
| Jelajahi kebalikannya | ... membuat sales hampir tidak perlu mengetik sama sekali? |
| Ubah status quo | ... membuat satu kali pencatatan pesanan langsung memperbarui pelanggan, kinerja, dan stok? |
| Pecah masalah | ... (a) input lapangan, (b) stok otomatis, (c) laporan manajemen? |
| Hilangkan yang buruk | ... meniadakan penyalinan dari buku ke catatan lain? |
| Ubah kata sifat | ... membuat pencatatan terasa membantu sales, bukan beban? |
| Pertanyakan asumsi | ... tetap bekerja tanpa sinyal internet? |
| Analogi | ... membuat input pesanan secepat kasir minimarket memindai barang? |

## 2. Competitive audit (draf)

| Solusi | Langsung/tidak | Kekuatan | Kelemahan | Penilaian |
|---|---|---|---|---|
| Cara saat ini (buku + chat) | — | Tanpa biaya, sudah terbiasa | Tercecer, tidak sinkron `[sumber: S]` | Kurang |
| Spreadsheet bersama | Tidak langsung | Murah, mudah | Tidak offline, rawan salah, tidak ada peringatan `[asumsi]` | [cek] |
| Aplikasi CRM/sales force automation SaaS | Langsung | Fitur lengkap `[asumsi]` | Biaya langganan, terlalu kompleks untuk UMKM `[asumsi]` | [cek] |
| Aplikasi kasir/inventori UMKM | Tidak langsung | Stok dan transaksi `[asumsi]` | Tidak untuk kunjungan sales lapangan `[asumsi]` | [cek] |
| Sistem inventori batik yang pernah dibuat dosen (disebut di sosialisasi) | Analogi | Pemantauan pesanan, stok, grafik produk laris `[sumber: S]` | Konteks berbeda | Inspirasi |

**Celah (draf):** solusi yang sederhana untuk UMKM, bekerja offline di lapangan, dan menangkap prospek dari WhatsApp `[asumsi]`.

## 3. Crazy 8s

*(Diisi tim. Sesi yang disarankan: HMW "analogi kasir" dan "tanpa sinyal".)*

## 4. Kandidat ide

| No | Ide | Menjawab | Asal |
|---|---|---|---|
| I1 | **Aplikasi sales offline-first** (PWA/mobile): check-in kunjungan, input pesanan cepat, sinkron saat online | US1, H1 | Batasan mitra `[sumber: W]` |
| I2 | **Stok otomatis + peringatan stok menipis** | US2, US3, H2 | Keinginan mitra `[sumber: S]` |
| I3 | **Profil outlet**: riwayat transaksi, catatan interaksi, jatuh tempo | US5 | Keinginan mitra `[sumber: S]` |
| I4 | **Dashboard manajemen**: kinerja sales, outlet aktif, perputaran stok | US4, H4 | Keluaran mitra `[sumber: W]` |
| I5 | **Rekomendasi kunjungan / pengingat pesan ulang** dari pola riwayat | US6, H3 | Catatan proposal |
| I6 | **Tangkap prospek WhatsApp** → kartu prospek otomatis | US7 | Temuan situs `[sumber: A]` |
| I7 | **Input cepat**: pindai barcode, suara-ke-teks, pesanan ulang satu ketukan | US1 | HMW "analogi kasir" |
| I8 | **Alat migrasi data** dari spreadsheet/foto catatan | US8 | Keluaran mitra `[sumber: W]` |
| I9 | **Prediksi kebutuhan restock** per SKU | Kedalaman teknologi | Catatan proposal |

## 4a. Rincian ide

Perkiraan upaya: **Rendah** = beberapa jam saat hackathon · **Sedang** = 1 hari · **Tinggi** = butuh data/akses yang belum ada atau lebih dari 3 hari. Semua rincian adalah usulan tim `[asumsi]` kecuali bertanda sumber.

### I1 · Aplikasi sales offline-first
- **Apa:** aplikasi di HP sales yang tetap jalan tanpa sinyal.
- **Cara kerja:** sales check-in kunjungan (waktu + lokasi), memilih outlet, lalu mengisi pesanan dari daftar SKU favorit outlet itu. Data disimpan di HP dan dikirim otomatis saat sinyal kembali. Bila terjadi konflik (dua sales menjual stok terakhir), sistem memberi peringatan saat sinkronisasi.
- **Teknologi:** *Progressive Web App* (service worker + penyimpanan lokal), antrean sinkronisasi, backend REST.
- **Menjawab:** US1, H1, K2, K5; batasan sinyal lemah `[sumber: W]`.
- **Kelebihan:** menjawab batasan teknis utama mitra; tidak perlu dipasang lewat toko aplikasi.
- **Risiko / pertanyaan:** konflik stok saat offline; HP sales mungkin berspesifikasi rendah.
- **Upaya:** Sedang · **Peran:** inti

### I2 · Stok otomatis + peringatan stok menipis
- **Apa:** stok gudang dihitung dari barang masuk dikurangi pesanan yang dikonfirmasi.
- **Cara kerja:** pesanan punya status (draf → dikonfirmasi → dikirim). Tiap SKU punya ambang minimum; admin gudang mendapat notifikasi saat stok di bawah ambang. Opsional: pencatatan batch dan tanggal kedaluwarsa, karena produk herbal punya masa simpan `[asumsi]`.
- **Menjawab:** US2, US3, H2, K3.
- **Risiko / pertanyaan:** stok awal harus akurat, jadi perlu *stock opname* sebelum mulai.
- **Upaya:** Rendah–Sedang · **Peran:** inti

### I3 · Profil outlet
- **Apa:** data outlet, kontak, lokasi, riwayat transaksi, catatan kunjungan, dan jatuh tempo pembayaran `[sumber: W]`.
- **Menjawab:** US5.
- **Upaya:** Rendah · **Peran:** inti

### I4 · Dashboard manajemen
- **Apa:** kunjungan per sales, jumlah dan nilai pesanan, target vs capaian, outlet aktif/tidak aktif, perputaran stok, stok menipis.
- **Menjawab:** US4, H4, K4; keluaran yang diminta mitra `[sumber: W]`.
- **Upaya:** Rendah–Sedang · **Peran:** inti

### I5 · Rekomendasi kunjungan dan pengingat pesan ulang
- **Apa:** daftar "outlet yang waktunya pesan ulang minggu ini".
- **Cara kerja:** sistem memperkirakan jarak waktu pembelian per outlet dan per SKU dari riwayat transaksi, lalu mengurutkan outlet berdasarkan nilai dan jarak. Untuk outlet baru dipakai rata-rata outlet sejenis.
- **Teknologi:** statistik selang waktu / peramalan sederhana; optimasi rute (opsional).
- **Menjawab:** US6, H3; unsur *deeptech* agar tidak dinilai sekadar aplikasi pencatatan.
- **Risiko / pertanyaan:** data riwayat belum ada. Mulai dari migrasi data + data dummy, dan jelaskan bahwa fitur ini makin akurat seiring bertambahnya data.
- **Upaya:** Sedang · **Peran:** komponen *deeptech*

### I6 · Tangkap prospek WhatsApp
- **Apa:** pesan templat dari situs (mis. "saya ingin maklon Haircare") `[sumber: A]` otomatis menjadi kartu prospek berisi jenis kebutuhan, nomor, dan waktu; admin melanjutkan statusnya.
- **Teknologi:** webhook WhatsApp Business API; alternatif semi-manual: admin menyalin chat ke formulir cepat.
- **Menjawab:** US7; kaitan dengan ARB-01.
- **Risiko / pertanyaan:** biaya dan akses API.
- **Upaya:** Sedang · **Peran:** pendukung

### I7 · Input cepat
- **Apa:** mempercepat pencatatan di lapangan.
- **Pilihan:** pesan ulang satu ketukan (menyalin pesanan terakhir) — upaya Rendah; pindai barcode produk — Sedang; input suara → daftar barang — Tinggi.
- **Menjawab:** US1, K2 ("hitungan detik" `[sumber: W]`).
- **Peran:** pendukung (pesan ulang satu ketukan disarankan masuk inti)

### I8 · Migrasi data
- **Apa:** templat spreadsheet untuk mengimpor outlet, produk, dan stok awal. Opsi lanjutan: membaca foto catatan dengan OCR.
- **Menjawab:** US8; keluaran "skema migrasi data awal" `[sumber: W]`.
- **Upaya:** Rendah (spreadsheet) · **Peran:** pendukung

### I9 · Prediksi kebutuhan restock
- **Apa:** saran jumlah produksi/pembelian per SKU.
- **Cara kerja:** peramalan permintaan dari total pesanan per SKU, ditambah waktu tunggu produksi.
- **Teknologi:** *moving average* / *exponential smoothing*.
- **Risiko / pertanyaan:** sama dengan I5: butuh data riwayat.
- **Upaya:** Sedang · **Peran:** *deeptech* / lanjutan

## 4b. Paket solusi untuk dibahas

| Paket | Isi | Kekuatan | Risiko |
|---|---|---|---|
| **A · Minimum** | I1 + I2 + I3 + I4 | Persis tiga fitur yang diminta mitra `[sumber: S]` | Mudah dinilai "aplikasi CRUD biasa" |
| **B · Disarankan** | A + I5 + I7 (pesan ulang satu ketukan) + I8 (spreadsheet) | Ada unsur cerdas yang jelas; siap dipakai | I5 lemah tanpa data riwayat |
| **C · Ambisius** | B + I6 + I9 | Terhubung ke prospek WhatsApp dan perencanaan produksi | Lingkup melebar |

## 4c. Pertanyaan pemandu brainstorming

1. Apa yang membuat solusi ini lebih dari sekadar aplikasi pencatatan di mata juri *deeptech*?
2. Apakah alur klien maklon perlu ikut, atau cukup outlet?
3. Seberapa parah masalah sinyal di lapangan: apakah mode offline wajib atau cukup "toleran koneksi lambat"?
4. Data apa yang bisa diminta dari mitra minggu ini untuk membuat demo terasa nyata?
5. Bagaimana memastikan sales mau memakai aplikasi (insentif, kemudahan)?

## 5. Memilih ide

*(Nilai 1–3 per kriteria, diisi tim.)*

**Usulan inti untuk proposal** `[asumsi]`: I1 + I2 + I3 + I4 sebagai fungsi inti; I5/I9 sebagai komponen kecerdasan (*deeptech*) agar tidak sekadar aplikasi CRUD; I6–I8 sebagai pendukung.

## 6. Goal statement (draf)

> Aplikasi kami akan memungkinkan **sales mencatat kunjungan dan pesanan dalam hitungan detik meski offline, yang langsung memperbarui stok dan data pelanggan**, yang akan memengaruhi **sales, admin gudang, dan direktur CV Arba'in** dengan **data yang selalu sinkron dan peluang penjualan yang tidak terlewat**. Kami akan mengukur efektivitasnya dengan **waktu input per pesanan, selisih stok, dan jumlah input berulang**.

## 7. Rancangan solusi untuk proposal

| Elemen | Isian |
|---|---|
| Cara kerja | [diisi setelah ide dipilih] |
| Teknologi inti | [mis. PWA offline-first + sinkronisasi, basis data terpusat, model prediksi pesan ulang/restock] |
| Bagian yang dikerjakan tim | |
| Kebaruan | |
| Kelayakan | |
| Komponen lokal | |
| Peluang KI | Ketentuan KI belum disebut — tanyakan |

## Checklist selesai

- [x] HMW, competitive audit (draf), kandidat ide, goal statement (draf)
- [x] Rincian ide, paket solusi, pertanyaan pemandu brainstorming
- [ ] Crazy 8s; ide dinilai dan dipilih

<!-- nav-bottom:start -->

---

◂ [2 Define](02-define.md) · [▴ Atas](#) · [4 Prototype](04-prototype.md) ▸  
3 Ideate di proyek lain: [RS-01](../rs-01/03-ideate.md) · [ARB-01](../arb-01/03-ideate.md) · [LKPI-01](../lkpi-01/03-ideate.md) · [LKPI-02](../lkpi-02/03-ideate.md) · [UMS-01](../ums-01/03-ideate.md) · [Template](../_template/03-ideate.md)
<!-- nav-bottom:end -->
