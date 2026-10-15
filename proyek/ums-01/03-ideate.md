# 3 · Ideate — UMS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **UMS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · **3 Ideate** · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/dpm-drpps-ums.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · s.d. 20 Okt, diulang saat hackathon · Proposal: Bag. 4 butir 2 · PJ: koordinator teknis + seluruh tim
> Panduan metode: [_template/03-ideate.md](../_template/03-ideate.md)

## 1. How Might We

| Sudut | Bagaimana kita bisa ... |
|---|---|
| Perkuat yang baik | ... memanfaatkan 35 inovasi dan relasi inovator ↔ produk yang sudah ada di iHub? |
| Jelajahi kebalikannya | ... membuat industri yang datang membawa masalah, lalu kampus yang dicocokkan? |
| Ubah status quo | ... membuat setiap inovasi baru otomatis mendapat daftar calon mitra dan peta celah? |
| Pecah masalah | ... (a) data rapi, (b) pencocokan, (c) kesiapan regulasi, (d) dokumen penawaran, (e) tindak lanjut? |
| Hilangkan yang buruk | ... meniadakan penyusunan *product brief* dari nol? |
| Ubah kata sifat | ... membuat katalog terasa hidup, bukan statis? |
| Pertanyakan asumsi | ... menghubungkan produk dengan pengguna akhir (RS, masyarakat), bukan hanya industri? |
| Analogi | ... mencocokkan produk dan mitra seperti platform rekrutmen mencocokkan kandidat dan lowongan? |

## 2. Competitive audit (draf)

| Solusi | Langsung/tidak | Kekuatan | Kelemahan | Penilaian |
|---|---|---|---|---|
| iHub saat ini | — | Data terstruktur, relasi inovator–produk `[sumber: H]` | Statis; tidak ada pencocokan/kesiapan/pipeline `[sumber: H]` | Cukup |
| Forum *business matching* manual | — | Interaksi langsung `[sumber: H]` | Tidak skalabel `[asumsi]` | [cek] |
| Katalog inovasi perguruan tinggi lain / platform nasional | Langsung | [cek] | [cek] | [cek] |
| Platform transfer teknologi (marketplace teknologi) | Tidak langsung | [cek] | [cek] | [cek] |

## 3. Kandidat ide

| No | Ide | Menjawab | Asal |
|---|---|---|---|
| I1 | **Mesin pencocokan** produk ↔ kebutuhan industri (NLP/embedding atas deskripsi, keunggulan, potensi) dengan penjelasan alasan | US1, H1 | Arah solusi `[sumber: W]` |
| I2 | **Formulir profil kebutuhan industri** singkat di iHub | US5 | Celah iHub `[sumber: H]` |
| I3 | **Kalkulator kesiapan**: TKT, KI, dan checklist jalur izin edar per kategori (BPOM obat tradisional/suplemen, AKD, PKRT, PKMK, notifikasi kosmetik) | US3, H3 | Arah solusi `[sumber: W]` |
| I4 | **Generator *product brief*/pitch** dari field katalog | US2, H2 | Arah solusi `[sumber: W]` |
| I5 | ***Pipeline* kemitraan**: prospek → pertemuan → negosiasi → MoU/lisensi | US4, H4 | Arah solusi `[sumber: W]` |
| I6 | **Normalisasi data katalog** (fakultas, sektor, nama mitra) | US6 | Masalah data `[sumber: H]` |
| I7 | **Pencocokan dengan mitra hackathon** sebagai demo (mis. CV Arba'in, PT LKPI sebagai profil industri) | US1 | Keterkaitan antar-mitra |
| I8 | **Konektor ke iHub** (API baca + widget) | K5 | Batasan `[sumber: W]` |

## 3a. Rincian ide

Perkiraan upaya: **Rendah** = beberapa jam saat hackathon · **Sedang** = 1 hari · **Tinggi** = butuh data/akses yang belum ada atau lebih dari 3 hari. Semua rincian adalah usulan tim `[asumsi]` kecuali bertanda sumber.

### I1 · Mesin pencocokan produk ↔ industri
- **Apa:** rekomendasi calon mitra industri untuk setiap produk riset, lengkap dengan alasannya.
- **Cara kerja:** produk (deskripsi, keunggulan, manfaat, potensi, sektor, TKT dari iHub `[sumber: H]`) dan profil industri (bidang, produk, kebutuhan, kapasitas) diubah menjadi representasi teks → dihitung skor kemiripan → disaring dengan aturan (sektor dan jalur regulasi cocok, TKT minimum) → ditampilkan 5 teratas dengan penjelasan "cocok karena ...".
- **Teknologi:** *sentence embedding* multibahasa, pencarian vektor, LLM untuk penjelasan.
- **Menjawab:** US1, H1, K1.
- **Kelebihan:** inti permintaan mitra `[sumber: W]`; data produk sudah tersedia.
- **Risiko / pertanyaan:** profil industri belum ada. Bisa dimulai dari mitra hackathon, database mitra iHub, dan data publik. Relevansi dinilai oleh pakar.
- **Upaya:** Sedang · **Peran:** inti

### I2 · Formulir profil kebutuhan industri
- **Apa:** 5–8 isian (bidang, produk, tantangan, minat kerja sama — lisensi/riset bersama/produksi —, kapasitas) + kolom teks bebas yang diolah AI.
- **Menjawab:** US5; sumber data untuk I1.
- **Upaya:** Rendah · **Peran:** pendukung

### I3 · Kalkulator kesiapan komersialisasi dan regulasi
- **Apa:** peta celah per produk.
- **Cara kerja:** pilih jenis produk → pohon keputusan menentukan jalur izin edar (obat tradisional/OHT/fitofarmaka, suplemen, kosmetik, PKMK, alat kesehatan menurut kelas risiko, PKRT) → checklist dokumen dan uji → digabung dengan status dari iHub (TKT, KI, legalitas) → skor kesiapan dan daftar celah.
- **Teknologi:** mesin aturan berbasis basis pengetahuan regulasi, dengan sumber regulasi ditampilkan.
- **Menjawab:** US3, H3, K3.
- **Kelebihan:** menjawab temuan bahwa 32 dari 35 inovasi belum punya legalitas edar `[sumber: H]`.
- **Risiko / pertanyaan:** ketepatan regulasi harus divalidasi pakar; tampilkan sebagai panduan, bukan keputusan resmi.
- **Upaya:** Sedang · **Peran:** inti

### I4 · Generator *product brief*
- **Apa:** ringkasan satu halaman per produk untuk forum *business matching*.
- **Cara kerja:** dari data katalog disusun: masalah, solusi, bukti (TKT, hasil uji), KI, status regulasi, peluang pasar, skema kerja sama, dan kontak. Ada versi untuk industri, investor, dan RS. Inovator meninjau sebelum dipakai.
- **Teknologi:** LLM + templat; ekspor PDF.
- **Menjawab:** US2, H2, K2.
- **Risiko / pertanyaan:** klaim berlebihan, sehingga perlu tinjauan inovator; data kosong di katalog.
- **Upaya:** Rendah–Sedang · **Peran:** inti

### I5 · *Pipeline* kemitraan
- **Apa:** papan status prospek: teridentifikasi → dihubungi → pertemuan → negosiasi → MoU/lisensi → selesai/gagal, dengan pengingat tindak lanjut dan alasan gagal.
- **Menjawab:** US4, H4.
- **Upaya:** Rendah · **Peran:** inti

### I6 · Normalisasi data katalog
- **Apa:** merapikan data iHub sebagai fondasi.
- **Cara kerja:** menyeragamkan nama fakultas ("FT" vs "Fakultas Teknik"), mengisi sektor yang kosong (10 inovasi) dengan klasifikasi otomatis, mengekstrak nama mitra dari teks bebas, dan menandai field yang kosong `[sumber: H]`.
- **Teknologi:** aturan + LLM / pengenalan entitas.
- **Menjawab:** US6.
- **Kelebihan:** hasilnya langsung terlihat; **bisa menjadi bukti awal Lampiran C** karena datanya sudah tersedia.
- **Upaya:** Rendah · **Peran:** fondasi

### I7 · Demo dengan mitra hackathon
- **Apa:** profil CV Arba'in dan PT LKPI dipakai sebagai contoh industri. CV Arbain Jaya Mandiri sudah menjadi mitra Sampo Herbal 4H `[sumber: H]`.
- **Risiko / pertanyaan:** perlu izin memakai profil; hanya untuk demo.
- **Upaya:** Rendah · **Peran:** demo

### I8 · Konektor iHub
- **Apa:** API baca katalog (atau ekspor JSON), widget "mitra yang cocok" di halaman inovasi iHub.
- **Risiko / pertanyaan:** perlu akses dari pengelola; teknologi iHub belum pasti `[asumsi]`.
- **Upaya:** Sedang · **Peran:** integrasi

## 3b. Paket solusi untuk dibahas

| Paket | Isi | Kekuatan | Risiko |
|---|---|---|---|
| **A · Minimum** | I6 + I1 + I4 | Cepat terlihat; memakai data nyata | Belum menyentuh regulasi dan tindak lanjut |
| **B · Disarankan** | A + I3 + I5 + I7 | Mencakup keempat keluaran yang diminta mitra `[sumber: W]` | I3 butuh validasi pakar regulasi |
| **C · Ambisius** | B + I2 + I8 (berjalan di iHub) | Langsung dipakai DPM | Bergantung akses teknis iHub |

## 3c. Pertanyaan pemandu brainstorming

1. Dari mana profil kebutuhan industri didapat saat demo, kalau belum ada data?
2. Seberapa dalam kalkulator regulasi bisa dibuat secara bertanggung jawab? Siapa pakar yang memvalidasi?
3. Produk mana yang dijadikan 3–5 studi kasus, dan apakah inovatornya bisa diajak bicara minggu ini?
4. Bagaimana membuktikan bahwa ini bukan "katalog statis" (batasan mitra)?
5. Apakah integrasi ke iHub cukup berupa desain + API, atau harus berjalan langsung?

## 4. Memilih ide

*(Nilai 1–3 per kriteria, diisi tim.)*

**Usulan inti untuk proposal** `[asumsi]`: I1 + I3 + I4 + I5 (empat keluaran yang diminta mitra); I6 sebagai langkah awal pipeline data; I2 dan I8 untuk integrasi.

## 5. Goal statement (draf)

> Platform kami akan memungkinkan **Tim Hilirisasi UMS mendapat rekomendasi mitra industri, peta celah kesiapan, dan *product brief* untuk setiap produk riset kesehatan secara otomatis**, yang akan memengaruhi **tim hilirisasi, inovator, dan calon mitra industri** dengan **mempercepat produk riset menuju kerja sama**. Kami akan mengukur efektivitasnya dengan **relevansi rekomendasi, waktu menyusun *product brief*, dan jumlah prospek yang ditindaklanjuti**.

## 6. Rancangan solusi untuk proposal

| Elemen | Isian |
|---|---|
| Cara kerja | [diisi setelah ide dipilih] |
| Teknologi inti | [mis. embedding/NLP untuk pencocokan, LLM untuk *product brief*, aturan berbasis regulasi untuk kalkulator kesiapan] |
| Bagian yang dikerjakan tim | |
| Kebaruan | |
| Kelayakan | Data katalog sudah tersedia `[sumber: H]` |
| Komponen lokal | Basis pengetahuan regulasi produk kesehatan Indonesia |
| Peluang KI | Ketentuan KI belum disebut — tanyakan |

## Checklist selesai

- [x] HMW, competitive audit (draf), kandidat ide, goal statement (draf)
- [x] Rincian ide, paket solusi, pertanyaan pemandu brainstorming
- [ ] Crazy 8s; ide dinilai dan dipilih

<!-- nav-bottom:start -->

---

◂ [2 Define](02-define.md) · [▴ Atas](#) · [4 Prototype](04-prototype.md) ▸  
3 Ideate di proyek lain: [RS-01](../rs-01/03-ideate.md) · [ARB-01](../arb-01/03-ideate.md) · [ARB-02](../arb-02/03-ideate.md) · [LKPI-01](../lkpi-01/03-ideate.md) · [LKPI-02](../lkpi-02/03-ideate.md) · [Template](../_template/03-ideate.md)
<!-- nav-bottom:end -->
