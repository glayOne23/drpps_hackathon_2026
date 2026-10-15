# 3 · Ideate — ARB-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · **3 Ideate** · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · s.d. 20 Okt, diulang saat hackathon · Proposal: Bag. 4 butir 2 · PJ: koordinator teknis + seluruh tim
> Panduan metode: [_template/03-ideate.md](../_template/03-ideate.md)

## 1. How Might We

| Sudut | Bagaimana kita bisa ... |
|---|---|
| Perkuat yang baik | ... memanfaatkan 6.800 artikel yang sudah ada sebagai bahan, bukan beban? |
| Jelajahi kebalikannya | ... menerbitkan lebih sedikit konten tetapi lebih sering dikutip AI? |
| Ubah status quo | ... membuat calon klien mendapat jawaban lengkap tanpa menunggu admin? |
| Pecah masalah | ... (a) tampil di jawaban AI, (b) menjawab prospek 24 jam, (c) mengukur hasil pemasaran? |
| Hilangkan yang buruk | ... meniadakan pertanyaan berulang yang menyita waktu admin? |
| Ubah kata sifat | ... membuat pemasaran terasa terkendali, bukan kewalahan? |
| Pertanyakan asumsi | ... mencari prospek tanpa menunggu mereka datang (lead generation proaktif)? |
| Analogi | ... membuat agen bekerja seperti staf baru yang dilatih dengan SOP perusahaan? |

## 2. Competitive audit (draf)

| Solusi | Langsung/tidak | Kekuatan | Kelemahan | Penilaian |
|---|---|---|---|---|
| Cara saat ini (manual + blog massal) | — | Volume konten besar `[sumber: A]` | Tidak menaikkan visibilitas; respons lambat `[sumber: S]` | Kurang |
| Situs maklon herbal pesaing di Solo Raya/Jawa | Langsung | [cek: tampil di AI/Google?] | [cek] | [cek] |
| Chatbot WhatsApp siap pakai | Tidak langsung | Cepat dipasang `[asumsi]` | Jawaban kaku; tidak paham katalog maklon `[asumsi]` | [cek] |
| Alat AI penulisan konten umum | Tidak langsung | Murah, cepat `[asumsi]` | Tanpa pemeriksa klaim; konten generik `[asumsi]` | [cek] |

**Celah (draf):** tidak ada solusi yang menggabungkan pengetahuan katalog maklon, kepatuhan klaim produk herbal, dan pengukuran visibilitas di mesin AI `[asumsi]`.

## 3. Crazy 8s

*(Diisi tim. Sesi yang disarankan: HMW "pecah masalah" (a) dan (b).)*

## 4. Kandidat ide

| No | Ide | Menjawab | Asal |
|---|---|---|---|
| I1 | **Agen penjawab B2B** (WA) dengan RAG atas katalog, MOQ, legalitas, harga; serah-terima ke admin untuk negosiasi | US1, US2, US7, H1 | Arah solusi `[sumber: W]` |
| I2 | **Agen konten GEO/SEO**: menulis halaman jawaban atas pertanyaan nyata calon klien, studi kasus, FAQ terstruktur (schema) | US3, US4, H2 | Temuan blog massal |
| I3 | **Pemeriksa klaim** produk herbal/kosmetik sebelum konten terbit | K5, H3 | Batasan mitra + temuan situs |
| I4 | **Pemantau visibilitas AI**: rutin menanyakan pertanyaan tetap ke mesin AI dan mencatat penyebutan merek | US3, K4 | Catatan proposal |
| I5 | **Dashboard** prospek, percakapan, konversi, dan biaya API | US5 | Arah solusi `[sumber: W]` |
| I6 | **Agen analisis pesaing** berkala | US6 | Keinginan mitra `[sumber: S]` |
| I7 | **Agen pemetaan prospek B2B** (apotek/minimarket/pemilik merek baru) | US8 | Arah solusi `[sumber: W]` |
| I8 | **Agen gambar/video promosi** dan penjadwal media sosial | Keinginan mitra `[sumber: S]` | Keinginan mitra |
| I9 | **Kurasi blog**: gabungkan/hapus artikel duplikat, perbaiki yang berpotensi | H2 | Temuan blog massal |

## 4a. Rincian ide

Perkiraan upaya: **Rendah** = beberapa jam saat hackathon · **Sedang** = 1 hari · **Tinggi** = butuh data/akses yang belum ada atau lebih dari 3 hari. Semua rincian adalah usulan tim `[asumsi]` kecuali bertanda sumber.

### I1 · Agen penjawab B2B
- **Apa:** asisten WhatsApp yang menjawab calon pembeli 24 jam dari basis pengetahuan resmi mitra.
- **Cara kerja:** basis pengetahuan berisi 12 kategori maklon, 16 produk grosir `[sumber: A]`, MOQ, kisaran harga, legalitas, alur maklon, dan FAQ. Agen mengenali jenis penanya (klien maklon / outlet / lainnya), menggali kebutuhan (produk, volume, anggaran, waktu), lalu menyerahkan prospek serius ke admin beserta ringkasannya. Negosiasi tetap oleh manusia `[sumber: S]`.
- **Teknologi:** LLM + RAG (pencarian berbasis *embedding*), WhatsApp Business API, aturan pembatas jawaban.
- **Menjawab:** US1, US2, US7, H1, K2, K3.
- **Kelebihan:** langsung menjawab "respons lambat"; manfaatnya bisa diukur saat demo.
- **Risiko / pertanyaan:** agen mengarang harga/legalitas. Agen hanya boleh menjawab dari basis pengetahuan; di luar itu dialihkan ke admin. Perhatikan juga biaya API.
- **Butuh dari mitra:** katalog, kebijakan harga, contoh chat (anonim).
- **Upaya:** Sedang · **Peran:** inti

### I2 · Agen konten GEO/SEO
- **Apa:** pembuat halaman yang menjawab pertanyaan nyata calon klien, bukan artikel massal.
- **Cara kerja:** daftar pertanyaan diambil dari chat dan audit visibilitas → agen menyusun draf halaman mendalam (panduan maklon per kategori, FAQ, studi kasus klien dengan izin) yang memuat fakta unik mitra → disertai data terstruktur (schema.org: organisasi, produk, FAQ) → admin meninjau sebelum terbit.
- **Teknologi:** LLM + templat, pembuat data terstruktur, API penerbitan blog.
- **Menjawab:** US3, US4, H2, K1, K4.
- **Kelebihan:** menyasar penyebab yang diduga: konten banyak tetapi tidak unik `[sumber: A]`.
- **Risiko / pertanyaan:** konten AI terasa generik bila tanpa fakta dari mitra; efek visibilitas baru terlihat setelah berminggu-minggu.
- **Upaya:** Sedang · **Peran:** inti

### I3 · Pemeriksa klaim produk
- **Apa:** penyaring sebelum konten terbit.
- **Cara kerja:** aturan + klasifikasi LLM menandai klaim berisiko untuk obat tradisional, suplemen, dan kosmetik (mis. "menyembuhkan", "untuk penderita [penyakit]"), lalu mengusulkan kalimat pengganti. Daftar klaim yang diizinkan per produk diambil dari mitra/izin edar.
- **Teknologi:** aturan kata kunci + LLM.
- **Menjawab:** H3, K5; batasan regulasi klaim `[sumber: W]`.
- **Kelebihan:** pembeda yang jelas; contoh kasus nyata sudah ada di deskripsi produk grosir `[sumber: A]`.
- **Risiko / pertanyaan:** perlu acuan regulasi resmi; hasilnya ditandai "perlu ditinjau", bukan nasihat hukum.
- **Upaya:** Rendah–Sedang · **Peran:** inti

### I4 · Pemantau visibilitas AI
- **Apa:** pengukur apakah merek disebut mesin AI.
- **Cara kerja:** 20–50 pertanyaan tetap (mis. "maklon herbal Solo BPOM MOQ rendah") dijalankan berkala ke beberapa mesin AI/pencarian → catat apakah CV Arba'in disebut, di posisi berapa, dan pesaing mana yang disebut → grafik tren.
- **Teknologi:** API LLM dengan pencarian web, penjadwal, penyimpanan.
- **Menjawab:** K4.
- **Kelebihan:** mengukur tujuan utama mitra; baseline bisa dibuat **sekarang**, sebelum 20 Okt.
- **Risiko / pertanyaan:** jawaban AI berubah-ubah, jadi tiap pertanyaan dijalankan beberapa kali dan dirata-rata; perhatikan ketentuan layanan API.
- **Upaya:** Rendah–Sedang · **Peran:** inti (pengukuran)

### I5 · Dashboard pemasaran
- **Apa:** satu layar berisi prospek masuk, kualifikasi, eskalasi, waktu respons, konversi (dari status yang diisi admin), biaya API, dan visibilitas AI.
- **Menjawab:** US5.
- **Upaya:** Rendah · **Peran:** inti

### I6 · Agen analisis pesaing
- **Apa:** ringkasan mingguan aktivitas pesaing maklon (produk baru, promosi, harga yang diumumkan).
- **Risiko / pertanyaan:** ketentuan *scraping* situs; manfaatnya bagi keputusan mitra perlu dibuktikan.
- **Upaya:** Sedang · **Peran:** lanjutan

### I7 · Agen pemetaan prospek
- **Apa:** mencari calon pembeli B2B (apotek/toko herbal di suatu area dari data publik, pemilik merek baru di marketplace) dan menyiapkan draf pesan penawaran untuk sales.
- **Risiko / pertanyaan:** etika penjangkauan dan risiko spam; kualitas data.
- **Upaya:** Sedang–Tinggi · **Peran:** lanjutan

### I8 · Agen gambar/video dan jadwal media sosial
- **Apa:** kalender konten → draf *caption* + gambar → disetujui admin → terbit terjadwal. Semua melewati I3.
- **Risiko / pertanyaan:** kualitas visual produk nyata; biaya.
- **Upaya:** Sedang · **Peran:** lanjutan

### I9 · Kurasi blog
- **Apa:** analisis 6.841 artikel yang sudah ada `[sumber: A]`.
- **Cara kerja:** kelompokkan artikel berdasarkan kemiripan isi → tandai yang duplikat/tipis → rekomendasi gabung, hapus, atau alihkan → prioritas perbaikan.
- **Teknologi:** *embedding* + *clustering*; data diambil dari feed publik blog.
- **Kelebihan:** memanfaatkan aset yang ada; datanya bisa diambil sekarang dan **bisa menjadi bukti awal Lampiran C**.
- **Risiko / pertanyaan:** menghapus konten bisa menurunkan kunjungan; keputusan akhir di tangan mitra.
- **Upaya:** Sedang · **Peran:** pendukung + bukti awal

## 4b. Paket solusi untuk dibahas

| Paket | Isi | Kekuatan | Risiko |
|---|---|---|---|
| **A · Minimum** | I1 + I3 + I5 | Fokus respons 24 jam yang aman; demo jelas | Tidak menyentuh visibilitas AI (keluhan utama mitra) |
| **B · Disarankan** | I1 + I2 + I3 + I4 + I5, dengan I9 sebagai bukti awal | Menjawab dua keluhan utama dan terukur | Beban kerja tinggi; hasil visibilitas baru terlihat di pendampingan |
| **C · Ambisius** | B + I6 + I7 + I8 | Mendekati "digital team" yang diminta mitra `[sumber: S]` | Terlalu luas untuk 3 hari |

## 4c. Pertanyaan pemandu brainstorming

1. Apa yang lebih mendesak bagi mitra: respons cepat ke prospek, atau tampil di Google/AI? Apakah urutan pengerjaan perlu berubah?
2. Bagaimana membuktikan kenaikan visibilitas AI dalam waktu program yang singkat?
3. Agen untuk klien maklon, outlet, atau keduanya?
4. Apa batas yang tidak boleh dilewati agen (harga, janji waktu produksi, klaim)?
5. Bagaimana menjaga biaya API tetap terjangkau untuk UMKM?

## 5. Memilih ide

*(Nilai 1–3 per kriteria, diisi tim.)*

**Usulan inti untuk proposal** `[asumsi]`: I1 + I3 + I4 + I5 sebagai fungsi inti (terukur saat demo); I2 sebagai agen konten; I6–I8 sebagai rencana pengembangan setelah hackathon. Alasan: cakupan keinginan mitra sangat luas, sedangkan waktu hackathon 3 hari.

## 6. Goal statement (draf)

> Tim digital AI kami akan memungkinkan **CV Arba'in menjawab calon pembeli B2B 24 jam dan menerbitkan konten patuh aturan yang dikutip mesin AI**, yang akan memengaruhi **tim pemasaran dan calon klien maklon** dengan **respons lebih cepat dan visibilitas lebih tinggi tanpa menambah karyawan**. Kami akan mengukur efektivitasnya dengan **waktu respons, akurasi jawaban, % penyebutan merek di mesin AI, dan biaya per bulan**.

## 7. Rancangan solusi untuk proposal

| Elemen | Isian |
|---|---|
| Cara kerja | [diisi setelah ide dipilih] |
| Teknologi inti | [mis. LLM + RAG atas katalog, orkestrasi multi-agen, WA Business API, data terstruktur schema.org] |
| Bagian yang dikerjakan tim | |
| Kebaruan | |
| Kelayakan (biaya API, kemudahan dipakai UMKM) | |
| Komponen lokal | |
| Peluang KI | Ketentuan KI belum disebut — tanyakan |

## Checklist selesai

- [x] HMW, competitive audit (draf), kandidat ide, goal statement (draf)
- [x] Rincian ide, paket solusi, pertanyaan pemandu brainstorming
- [ ] Crazy 8s; ide dinilai dan dipilih

<!-- nav-bottom:start -->

---

◂ [2 Define](02-define.md) · [▴ Atas](#) · [4 Prototype](04-prototype.md) ▸  
3 Ideate di proyek lain: [RS-01](../rs-01/03-ideate.md) · [ARB-02](../arb-02/03-ideate.md) · [LKPI-01](../lkpi-01/03-ideate.md) · [LKPI-02](../lkpi-02/03-ideate.md) · [UMS-01](../ums-01/03-ideate.md) · [Template](../_template/03-ideate.md)
<!-- nav-bottom:end -->
