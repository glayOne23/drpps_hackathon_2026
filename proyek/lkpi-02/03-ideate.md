# 3 · Ideate — LKPI-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **LKPI-02** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · **3 Ideate** · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/pt-lkpi.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · s.d. 20 Okt, diulang saat hackathon · Proposal: Bag. 4 butir 2 · PJ: koordinator teknis + seluruh tim
> Panduan metode: [_template/03-ideate.md](../_template/03-ideate.md). Sketsa = mekanisme pompa.

## 1. How Might We

| Sudut | Bagaimana kita bisa ... |
|---|---|
| Perkuat yang baik | ... memakai jeriken yang sudah ada tanpa mengubah kemasan? |
| Jelajahi kebalikannya | ... membuat air yang ditakar ke konsentrat, bukan sebaliknya? |
| Ubah status quo | ... menghilangkan gelas takar dari proses? |
| Pecah masalah | ... (a) volume tepat, (b) tanpa tetes, (c) mudah dengan sarung tangan, (d) murah? |
| Hilangkan yang buruk | ... meniadakan kebutuhan mengangkat jeriken 5 L? |
| Ubah kata sifat | ... membuat menakar terasa sekali gerak, bukan hati-hati? |
| Pertanyakan asumsi | ... menakar 20 ml tanpa listrik sama sekali? |
| Analogi | ... meniru dispenser sabun/saus di restoran yang mengeluarkan volume tetap? |

## 2. Competitive audit (draf)

| Solusi | Langsung/tidak | Kekuatan | Kelemahan | Penilaian |
|---|---|---|---|---|
| Gelas takar manual (saat ini) | — | Murah | Tumpah, tidak akurat `[sumber: W]` | Kurang |
| Pompa dosing jeriken volume tetap di pasar | Langsung | [cek: volume, harga, ketahanan kimia] | [cek: cocok ulir jeriken LKPI?] | [cek] |
| Dispenser peristaltik/elektronik | Langsung | Presisi tinggi `[asumsi]` | Mahal, butuh listrik `[asumsi]` | [cek] |
| Botol dosing "squeeze-and-pour" (ruang takar di leher botol) | Tidak langsung | Tanpa pompa `[asumsi]` | Tidak untuk jeriken 5 L `[asumsi]` | Inspirasi |

## 3. Kandidat konsep

| No | Konsep | Menjawab | Catatan |
|---|---|---|---|
| I1 | **Pompa mekanis volume tetap 20 ml** (piston/langkah terbatas) di tutup jeriken | H1, K1, K5 | Murah, tanpa listrik |
| I2 | **Katup anti-tetes / anti-balik** pada nozzle | H2, K2 | Wajib untuk semua konsep |
| I3 | **Ruang takar gravitasi** (isi ruang 20 ml, lalu buka katup) | K1 | Tanpa piston |
| I4 | **Dispenser elektronik** (pompa peristaltik/diafragma + sensor/counter) | K1 | Presisi tinggi; biaya lebih besar |
| I5 | **Volume bisa diatur** (20 ml BAYzime / 20 ml BAYcide / volume lain) | US4 | Memperluas pasar |
| I6 | **Tuas besar untuk tangan bersarung** | H3, K3 | Ergonomi |
| I7 | **(Opsi 1) Stasiun pengisian semi-otomatis** jeriken 5 L/20 L di lini produksi | Opsi 1 | Butuh data lini produksi |

## 3a. Rincian konsep

Perkiraan upaya: **Rendah** = beberapa jam (komponen siap) · **Sedang** = 1 hari perakitan + kalibrasi · **Tinggi** = butuh fabrikasi khusus atau lebih dari 3 hari. Semua rincian adalah usulan tim `[asumsi]` kecuali bertanda sumber. Material bagian basah wajib tahan detergen enzimatik dan disinfektan H₂O₂ `[sumber: W]`.

### I1 · Pompa mekanis volume tetap 20 ml
- **Apa:** pompa tangan yang terpasang di leher jeriken dan mengeluarkan volume tetap per tekan.
- **Cara kerja:** piston dalam silinder dengan langkah terbatas (penahan) dan pegas balik; katup satu arah di sisi masuk dan keluar; adaptor ulir sesuai tutup jeriken; pipa hisap sampai dasar jeriken. Volume = luas penampang × panjang langkah, dikalibrasi lewat penyetel langkah.
- **Menjawab:** US1, H1, K1, K5.
- **Kelebihan:** murah, tanpa listrik, prinsipnya mirip pompa dispenser sabun berukuran besar.
- **Risiko / pertanyaan:** akurasi turun karena gelembung udara atau pompa belum terisi penuh di awal (*priming*); viskositas cairan; seal harus tahan bahan kimia.
- **Upaya:** Sedang · **Peran:** inti

### I2 · Katup anti-tetes
- **Apa:** mencegah sisa cairan menetes setelah menakar.
- **Cara kerja:** katup paruh bebek (*duckbill*) atau katup bola di ujung nozzle; nozzle mengarah ke bawah.
- **Menjawab:** US2, H2, K2.
- **Risiko / pertanyaan:** bahan katup (silikon/EPDM) harus diuji terhadap H₂O₂ dan enzim.
- **Upaya:** Rendah · **Peran:** wajib untuk semua konsep

### I3 · Ruang takar gravitasi
- **Apa:** jeriken dibalik di dudukan; ruang takar 20 ml terisi oleh gravitasi, lalu dikeluarkan dengan katup dua posisi (isi/keluarkan), seperti dispenser minuman bertakar.
- **Kelebihan:** tanpa piston dan pegas; sederhana.
- **Risiko / pertanyaan:** perlu dudukan khusus; jeriken 5 L berat untuk dibalik; tutup bisa bocor saat terbalik.
- **Upaya:** Sedang · **Peran:** alternatif

### I4 · Dispenser elektronik
- **Apa:** pompa peristaltik + mikrokontroler; tombol "20 ml" atau pilih produk; penghitung pemakaian; baterai.
- **Kelebihan:** presisi tinggi; volume bisa diprogram; bisa mencatat data pemakaian.
- **Risiko / pertanyaan:** biaya; perawatan; perangkat listrik di area basah.
- **Upaya:** Sedang–Tinggi · **Peran:** pembanding / versi premium

### I5 · Volume bisa diatur
- **Apa:** penyetel langkah dengan posisi klik (mis. 10 / 20 / 40 ml) atau sisipan yang bisa diganti.
- **Kelebihan:** satu desain untuk BAYzime (20 ml/2,5 L) dan BAYcide (20 ml/1 L) `[sumber: L]` serta produk lain.
- **Risiko / pertanyaan:** salah setel, sehingga perlu penanda warna/skala per produk.
- **Upaya:** Sedang · **Peran:** pendukung

### I6 · Tuas besar atau pedal kaki
- **Apa:** tuas panjang yang mudah ditekan dengan sarung tangan, atau pedal kaki agar tangan tetap bebas.
- **Kelebihan:** pedal kaki menarik untuk area dekontaminasi, karena tangan petugas sering terkontaminasi `[asumsi]`.
- **Menjawab:** US3, H3, K3.
- **Upaya:** Rendah–Sedang · **Peran:** pendukung

### I7 · Stasiun pengisian semi-otomatis (opsi 1, lini produksi)
- **Apa:** pompa + sensor berat atau pengukur aliran untuk mengisi jeriken 5 L/20 L sampai volume target, lalu berhenti otomatis.
- **Risiko / pertanyaan:** butuh data lini produksi yang belum dijelaskan mitra; skala dan keamanan.
- **Upaya:** Tinggi · **Peran:** alternatif fokus (bila tim memilih opsi 1)

## 3b. Paket solusi untuk dibahas

| Paket | Isi | Kekuatan | Risiko |
|---|---|---|---|
| **A · Minimum** | I1 + I2 + adaptor jeriken | Fokus pada indikator mitra (deviasi < 5%) | Ergonomi belum teruji |
| **B · Disarankan** | A + I6 (tuas/pedal) + I5 (volume diatur) | Menjawab kebutuhan pengguna CSSD dan dua produk sekaligus | Desain lebih rumit |
| **C · Ambisius** | B + I4 sebagai pembanding akurasi dan biaya | Memberi LKPI dua pilihan harga | Dua purwarupa dalam 3 hari |

## 3c. Pertanyaan pemandu brainstorming

1. Mekanisme mana yang paling mungkin mencapai deviasi < 5% dengan biaya rendah: piston atau ruang takar gravitasi?
2. Apakah pompa ikut dijual bersama jeriken, atau dipakai ulang di RS? Ini menentukan target harga dan bahan.
3. Bahan apa yang tersedia lokal dan tahan BAYzime serta BAYcide?
4. Bisakah tim mendapat sampel jeriken dan produk minggu ini untuk mengukur ulir dan viskositas?
5. Apakah pedal kaki benar-benar dibutuhkan petugas CSSD? Perlu dicek lewat observasi.

## 4. Memilih konsep

*(Nilai 1–3 per kriteria, diisi tim. Kriteria tambahan: biaya per unit, kemudahan produksi lokal, ketahanan kimia.)*

**Usulan inti untuk proposal** `[asumsi]`: I1 + I2 + I6 sebagai purwarupa utama; I5 bila memungkinkan; I4 sebagai pembanding/versi premium.

## 5. Goal statement (draf)

> Alat kami akan memungkinkan **petugas CSSD menakar tepat 20 ml dari jeriken 5 L dengan satu gerakan tanpa tumpah**, yang akan memengaruhi **petugas CSSD/kamar operasi dan PT LKPI** dengan **takaran konsisten, kerja lebih cepat, dan nilai tambah produk**. Kami akan mengukur efektivitasnya dengan **deviasi volume (< 5%), jumlah tetesan/kebocoran, dan keberhasilan pemakaian tanpa bantuan**.

## 6. Rancangan solusi untuk proposal

| Elemen | Isian |
|---|---|
| Cara kerja (mekanisme) | [diisi setelah konsep dipilih] |
| Dasar ilmiah/teknik | |
| Bagian yang dikerjakan tim | |
| Kebaruan | |
| Kelayakan (manufaktur, biaya) | |
| Komponen lokal | [material dan proses manufaktur dalam negeri] |
| Peluang KI | **KI milik tim; royalti bila diadopsi LKPI** `[sumber: W]` — kandidat paten sederhana/desain industri `[asumsi]` |

## Checklist selesai

- [x] HMW, competitive audit (draf), kandidat konsep, goal statement (draf)
- [x] Rincian ide, paket solusi, pertanyaan pemandu brainstorming
- [ ] Crazy 8s mekanisme; konsep dinilai dan dipilih

<!-- nav-bottom:start -->

---

◂ [2 Define](02-define.md) · [▴ Atas](#) · [4 Prototype](04-prototype.md) ▸  
3 Ideate di proyek lain: [RS-01](../rs-01/03-ideate.md) · [ARB-01](../arb-01/03-ideate.md) · [ARB-02](../arb-02/03-ideate.md) · [LKPI-01](../lkpi-01/03-ideate.md) · [UMS-01](../ums-01/03-ideate.md) · [Template](../_template/03-ideate.md)
<!-- nav-bottom:end -->
