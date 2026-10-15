# 01 · Kebutuhan Mitra

> Bagian dari [Dokumen UMS HI Hackathon 2026](README.md). Ringkasan umum kebutuhan keempat mitra dan enam tantangan.
> Rincian tiap mitra ada di folder [mitra/](mitra/). Kode sumber [P], [W], [S], [R], [A], [L], [H] dijelaskan di [README](README.md#sumber).

---

## 1. Ringkasan mitra dan tantangan

Pedoman [P] menyebut tiga mitra program: **RS AR Fachruddin UMS, CV Arbain, dan PT LKPI**. Laman resmi [W] menambahkan satu tantangan internal dari **DPM DRPPS UMS**, yang diumumkan saat sosialisasi [S]. Total ada **4 pihak dan 6 tantangan**.

| Mitra | Profil singkat | Kode | Tantangan | Jenis solusi | Detail |
|---|---|---|---|---|---|
| **RS UMS A.R. Fachrudin** | RS baru milik UMS di Jl. Adi Sucipto 167, Laweyan, Surakarta. 32 tenaga medis, 18 spesialisasi, 37 tempat tidur | RS-01 | Sistem Cerdas Manajemen Jadwal Dokter, Otomatisasi Notifikasi Pasien, dan Interoperabilitas Layanan RS | Perangkat lunak: notifikasi, dashboard, desain integrasi SATUSEHAT/BPJS | [rs-ums-ar-fachrudin.md](mitra/rs-ums-ar-fachrudin.md) · [proyek](../proyek/rs-01/README.md) |
| **CV Arbain Jaya Mandiri** | Produsen dan jasa maklon herbal, madu, kosmetik (standar CPOTB-BPOM) di Mojosongo, Jebres, Surakarta. Menjual B2B ke apotek, toko obat, minimarket | ARB-01 | Agen AI untuk Otomatisasi Pemasaran, Penjualan B2B, dan Optimasi SEO AI | Perangkat lunak: AI agent/LLM | [cv-arbain.md](mitra/cv-arbain.md) · [proyek](../proyek/arb-01/README.md) |
| | | ARB-02 | Sistem CRM Terpadu: Integrasi Data Pelanggan B2B, Aktivitas Sales, dan Manajemen Stok | Perangkat lunak: aplikasi web/mobile | [cv-arbain.md](mitra/cv-arbain.md) · [proyek](../proyek/arb-02/README.md) |
| **PT Likuid Pharmalab Indonesia (LKPI)** | Manufaktur antiseptik, disinfektan, BMHP di Baki, Sukoharjo (ISO 13485, CPAKB, ±8 tahun). >40 produk, 2.000+ pelanggan RS/klinik | LKPI-01 | Inovasi Formulasi Disinfektan dengan Karakteristik Aroma yang Sesuai Kebutuhan Pengguna | Formulasi kimia/farmasi | [pt-lkpi.md](mitra/pt-lkpi.md) · [proyek](../proyek/lkpi-01/README.md) |
| | | LKPI-02 | Inovasi Peralatan Otomatisasi Produksi dan Sistem Penakaran Presisi (Precision Dosing) Sediaan Cair Medis | Perangkat keras: mekanik/mekatronika | [pt-lkpi.md](mitra/pt-lkpi.md) · [proyek](../proyek/lkpi-02/README.md) |
| **DPM DRPPS UMS** | Unit hilirisasi riset kampus, pengelola UMS Innovation Hub (35 inovasi, 6 produk, 32 inovator) | UMS-01 | Solusi Pendukung Komersialisasi Produk Kesehatan Hasil Riset UMS | Perangkat lunak: AI/data, platform pencocokan | [dpm-drpps-ums.md](mitra/dpm-drpps-ums.md) · [proyek](../proyek/ums-01/README.md) |

Aturan pemilihan [P]: **satu tim mengajukan satu proposal untuk satu tantangan.** Nama mitra dan kode tantangan di proposal harus sama dengan pilihan di formulir. Pendekatan teknologi boleh berbeda dari "arah solusi awal" selama tetap menjawab kebutuhan mitra.

---

## 2. Inti kebutuhan per tantangan

| Kode | Masalah inti | Yang diminta | Target terukur |
|---|---|---|---|
| RS-01 | Jadwal dokter spesialis sering berubah mendadak (dokter praktik di 2–3 tempat, sering tertahan kasus *cito*); pemberitahuan ke pasien manual via WhatsApp dan sering tidak terbaca | Notifikasi dua arah real-time (konfirmasi/*reschedule*), dashboard koordinasi antarunit, desain integrasi SIMRS–SATUSEHAT–BPJS, kanal umpan balik pasien | Notifikasi terkirim < 1 menit setelah status diperbarui |
| ARB-01 | Branding, marketing, dan selling masih manual; kalah visibilitas di Google dan mesin pencari AI; respons ke pembeli lambat; penjualan di bawah target | "Digital team" berisi beberapa agen AI: analisis pesaing, konten SEO/GEO, gambar/video, penjadwalan media sosial dan iklan, penjawab pertanyaan 24 jam. Manusia tetap memegang negosiasi | Efisiensi waktu konten, jawaban akurat 24 jam, visibilitas naik |
| ARB-02 | Data pelanggan, aktivitas sales, dan stok tersebar di buku catatan dan chat | Satu platform: aktivitas sales (kunjungan, prospek, target), data pelanggan (profil, riwayat, interaksi), stok otomatis + peringatan stok menipis | Data terhubung real-time tanpa input ulang; akurasi stok naik |
| LKPI-01 | Parfum, H₂O₂, dan surfaktan tidak kompatibel; H₂O₂ termolabil | Formula disinfektan ruangan beraroma yang homogen dan stabil, dengan rasionalisasi ilmiah dan data uji awal | Tidak ada pemisahan fase; aroma stabil; lulus uji stabilitas dipercepat dan antimikroba |
| LKPI-02 | Penakaran BAYzime (20 ml per 2,5 L air) dari jeriken 5 L masih pakai gelas takar, sering tumpah dan tidak akurat | Pompa/dispenser 20 ml pada jeriken 5 L, **atau** alat otomasi lini produksi cair | Deviasi volume < 5% |
| UMS-01 | Produk riset kesehatan UMS sulit diserap industri dan masyarakat; belum ada alat sistematis untuk mencocokkan produk dengan mitra | Pencocokan produk ↔ kebutuhan industri, kalkulator kesiapan TKT/HKI/izin edar, generator *product brief*, *pipeline* tindak lanjut kemitraan; terintegrasi dengan iHub | Rekomendasi relevan; diuji pada 3–5 produk nyata UMS |

---

## 3. Temuan kunci dari situs mitra

Ringkasan temuan yang paling memengaruhi isi proposal. Data lengkap dan cara memperolehnya ada di file turunan.

### RS UMS A.R. Fachrudin [R] → [detail](mitra/rs-ums-ar-fachrudin.md#2-temuan-dari-situs-rs-rsumsacid)

- Situs punya API publik `/api/jadwal`, tetapi jadwal hanya pola mingguan statis (hari + jam). **Tidak ada field tanggal, status, atau pengganti**, sehingga perubahan harian tidak bisa dicatat di sistem.
- "Pendaftaran Online" ternyata tautan WhatsApp. Belum ada booking, antrean, atau akun pasien, jadi daftar pasien per slot (penerima notifikasi) belum tersedia secara digital.
- 54 dari 103 slot praktik mulai pukul 13.00 ke atas, dan 13 dari 32 dokter hanya praktik 1–2 kali seminggu.
- Ketersediaan tempat tidur diperbarui manual lewat Google Sheets.

### CV Arbain Jaya Mandiri [A] → [detail](mitra/cv-arbain.md#2-temuan-dari-situs-mitra-jasamaklonherbalcom)

- Blog situs berisi **6.841 artikel** (6.216 di antaranya terbit pada 2025, ±17 per hari), dengan judul yang sangat mirip satu sama lain. Penerbitan berhenti sejak 28 Juli 2026. Masalah visibilitas kemungkinan bukan soal jumlah konten.
- Beberapa deskripsi produk grosir memuat klaim kesehatan (mis. "untuk penderita diabetes & kolesterol"), relevan dengan batasan regulasi klaim di ARB-01.
- Semua jalur prospek (formulir konsultasi, tombol produk) berakhir di **satu nomor WhatsApp**, tanpa basis data — akar masalah "data tercecer di chat" di ARB-02.
- Bisnis maklon (12 kategori) sama besarnya dengan penjualan ke outlet, padahal ARB-02 hanya menyebut outlet.

### PT LKPI [L] → [detail](mitra/pt-lkpi.md#2-temuan-dari-situs-mitra-likuidcoid)

- Sudah punya **SASKLIN Disinfectant Spray** (benzalkonium chloride + H₂O₂, tanpa parfum) dan beberapa antiseptik beraroma berbasis alkohol. LKPI-01 tampaknya menggabungkan keduanya.
- **BAYzime (20 ml/2,5 L) dan BAYcide HLD (20 ml/1 L) memakai takaran 20 ml yang sama** dan sama-sama dijual dalam jeriken 5 L. Satu pompa bisa melayani dua produk di alur CSSD.
- Banyak produk dijual dalam jeriken 5 L dan 20 L, relevan untuk opsi otomasi pengisian di lini produksi.

### DPM DRPPS UMS [H] → [detail](mitra/dpm-drpps-ums.md#211-referensi-tambahan-platform-ums-innovation-hub-yang-sudah-ada)

- Katalog iHub berisi 35 inovasi terstruktur (±40 field), 8 di antaranya bidang kesehatan. Data ini bisa langsung dipakai untuk demo.
- 20 dari 35 inovasi belum diadopsi dan hanya 3 yang punya legalitas edar.
- Belum ada pencocokan otomatis, profil kebutuhan industri, checklist izin edar, atau *pipeline* kemitraan.

---

## 4. Keterkaitan antar-mitra

Mitra-mitra ini saling terhubung. Tiap tim tetap hanya memilih satu tantangan, tetapi keterkaitan ini bisa memperkuat bagian "dukungan mitra" dan "rencana hilirisasi" di proposal.

| Keterkaitan | Manfaat untuk proposal |
|---|---|
| CV Arbain Jaya Mandiri sudah tercatat di iHub sebagai mitra inovasi **Sampo Herbal 4H** (UMS) | Contoh nyata hilirisasi untuk UMS-01; CV Arba'in bisa menjadi profil "calon mitra industri" dalam demo pencocokan |
| PT LKPI dan CV Arba'in sama-sama manufaktur produk kesehatan di Solo Raya | Keduanya kandidat mitra industri untuk produk riset UMS di UMS-01 |
| RS UMS punya instalasi bedah/kamar operasi; LKPI menjual BAYzime untuk CSSD | RS UMS bisa menjadi lokasi uji pompa takar LKPI-02 (laman [W] menyebut akses uji di RS UMS dan RSGM) |
| ARB-01 (agen AI) dan ARB-02 (CRM) di mitra yang sama | Agen AI bisa membaca stok/prospek dari CRM; sebutkan sebagai rencana integrasi lanjutan |

---

## 5. Perbandingan cepat antar-tantangan

| Aspek | RS-01 | ARB-01 | ARB-02 | LKPI-01 | LKPI-02 | UMS-01 |
|---|---|---|---|---|---|---|
| Bentuk luaran | Software + desain integrasi | Software AI | Software web/mobile | Sampel formula + data uji | Alat fisik + CAD/BoM | Software AI/data |
| Kepastian lingkup | Sedang | Rendah (keinginan sangat luas) | Tinggi | Tinggi | Tinggi (fokus pompa 20 ml) | Sedang |
| Data dari mitra | Skenario kasus nyata | Katalog produk + skenario penjualan | Dummy data | Parameter mutu + lab mitra | Sampel kemasan + spesifikasi | Katalog produk + profil TKT |
| Data publik yang sudah tersedia | API jadwal dokter (`/api/jadwal`) | Situs + 6.841 artikel blog | 16 produk grosir, alur prospek WhatsApp | Katalog produk & komposisi | Rasio pengenceran BAYzime/BAYcide | Katalog 35 inovasi + 32 inovator |
| Tempat uji | Lingkungan RS | Tim marketing/sales mitra | Simulasi data dummy | Laboratorium mitra | Uji repeatability, sampel kemasan | 3–5 produk nyata UMS |
| Target terukur | Notifikasi < 1 menit | Efisiensi waktu, respons 24 jam | Data real-time, akurasi stok | Homogen, lulus uji stabilitas dan antimikroba | Deviasi < 5% | Relevansi pencocokan |
| HKI | Tidak disebut | Tidak disebut | Tidak disebut | **Milik penuh LKPI, tanpa royalti** | **Milik tim, royalti bila diadopsi** | Tidak disebut |
| Regulasi utama | KODERSI, UU PDP, SATUSEHAT, BPJS | Klaim produk herbal/kesehatan (BPOM) | — | Keamanan ruang medis, izin edar PKRT | Ketahanan material terhadap bahan kimia | TKT, HKI, izin edar |
| Disiplin inti | Informatika, kesehatan/RS, UX | Informatika (AI), pemasaran, farmasi | Informatika, bisnis/operasi | Farmasi, kimia, mikrobiologi | Teknik mesin/elektro, desain produk | Informatika (AI), bisnis, regulasi |

---

## 6. Perbedaan informasi antar-sumber

| Hal | Pedoman [P] | Sosialisasi [S] | Laman [W] / situs mitra | Pegangan |
|---|---|---|---|---|
| Batas pendaftaran | 15 Oktober 2026 | MC menyebut 10 Oktober; narasumber menyebut "pertengahan Oktober" | **20 Oktober 2026, 23.59 WIB** (diperpanjang) [W] | [W] — terbaru |
| Seleksi | 16–24 Oktober | 16–24 Oktober | 21–24 Oktober [W] | [W] |
| Jumlah mitra | 3 (RS, CV Arbain, PT LKPI) | 3 + tantangan internal DPM | 4 pihak, 6 tantangan [W] | [W] |
| Hadiah | Tidak dirinci | "Lebih dari 80 juta" tunai | Tunai total Rp50 juta; total manfaat 5 pemenang Rp75 juta; plus Rp5 juta × 10 finalis lain [W] | [W] |
| Nama PT LKPI | PT LKPI | "PT Liquid Pharmalab Indonesia" | PT Likuid Pharmalab Indonesia [W], [L] | [L] |
| Nama RS | RS AR Fachruddin UMS | — | RS AR Fachrudin UMS [W]; "RS UMS A.R. Fachrudin" [R] | [R] untuk nama resmi; konfirmasi ke panitia untuk proposal |
| Nama CV Arbain | CV Arbain | "CV Arbain", "CV Arbain Maju Jaya" | CV Arba'in [W]; **CV Arbain Jaya Mandiri** [A], [H] | [A] untuk nama badan usaha |
| Lokasi CV Arbain | — | Sukoharjo | Jl. Letjen Sutoyo 185, Mojosongo, Jebres, **Surakarta** [A] | [A]; mungkin ada lokasi produksi lain, konfirmasi ke mitra |

Pedoman [P] meminta peserta memakai informasi di laman resmi sebagai versi terbaru. Bila ada perbedaan, ikuti [W] dan konfirmasi ke umsihub.official@gmail.com.
