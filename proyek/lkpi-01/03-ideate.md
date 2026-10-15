# 3 · Ideate — LKPI-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **LKPI-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · **3 Ideate** · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/pt-lkpi.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · s.d. 20 Okt, diulang saat hackathon · Proposal: Bag. 4 butir 2 · PJ: koordinator teknis + seluruh tim
> Panduan metode: [_template/03-ideate.md](../_template/03-ideate.md). Untuk formulasi, "sketsa" berupa daftar pendekatan kimia.

## 1. How Might We

| Sudut | Bagaimana kita bisa ... |
|---|---|
| Perkuat yang baik | ... memanfaatkan pengalaman LKPI memformulasi parfum pada produk berbasis alkohol/BKC? |
| Jelajahi kebalikannya | ... membuat aroma muncul justru karena reaksi dengan H₂O₂, bukan dirusak olehnya? |
| Ubah status quo | ... memisahkan parfum dari zat aktif sampai saat aplikasi? |
| Pecah masalah | ... (a) membuat homogen, (b) melindungi parfum dari oksidasi, (c) menjaga kadar H₂O₂, (d) menguji stabilitas dengan benar? |
| Hilangkan yang buruk | ... meniadakan kontak langsung parfum–oksidator selama penyimpanan? |
| Ubah kata sifat | ... membuat aroma tahan lama, bukan cepat hilang? |
| Pertanyakan asumsi | ... memberi penanda disinfeksi tanpa parfum (mis. indikator lain)? |
| Analogi | ... melindungi parfum seperti kapsul melindungi obat dari asam lambung? |

## 2. Competitive audit (draf)

| Solusi | Langsung/tidak | Kekuatan | Kelemahan | Penilaian |
|---|---|---|---|---|
| SASKLIN Disinfectant Spray (LKPI) | Basis internal | Sistem BKC + H₂O₂ sudah berizin edar `[sumber: L]` | Tanpa parfum `[sumber: L]` | Basis |
| Disinfektan ruangan H₂O₂ beraroma di pasar | Langsung | [cek: produk dan komposisi yang beredar] | [cek] | [cek] |
| Disinfektan beraroma berbasis alkohol/quat | Tidak langsung | Aroma mudah ditambahkan `[asumsi]` | Zat aktif berbeda | [cek] |

## 3. Kandidat pendekatan

| No | Pendekatan | Menjawab | Asal |
|---|---|---|---|
| I1 | **Solubilizer/surfaktan pelindung** (nonionik yang tahan oksidasi) untuk melarutkan parfum | H1, K1 | Arah solusi `[sumber: W]` |
| I2 | **Enkapsulasi/mikroenkapsulasi** aroma | H3, K2–K3 | Arah solusi `[sumber: W]` |
| I3 | **Ko-solven atau stabilizer** yang kompatibel dengan H₂O₂ | K1, K2 | Arah solusi `[sumber: W]` |
| I4 | **Pemilihan senyawa fragrance tahan oksidasi** | H2, K3 | Arah solusi `[sumber: W]` |
| I5 | **Basis SASKLIN Disinfectant** + parfum, mempersempit masalah | K1–K5 | Temuan situs `[sumber: L]` |
| I6 | **Protokol uji stabilitas yang disesuaikan** untuk zat termolabil | H4 | Kendala mitra `[sumber: S]` |
| I7 | **Sistem dua kompartemen** (parfum dan zat aktif bercampur saat semprot) | HMW "ubah status quo" | `[asumsi]` — cek kelayakan biaya kemasan |

## 3a. Rincian pendekatan

Perkiraan upaya: **Rendah** = hasil terlihat dalam hitungan jam (mis. homogenitas) · **Sedang** = 1–3 hari percobaan · **Tinggi** = butuh bahan/alat khusus atau berminggu-minggu. Contoh golongan bahan di bawah adalah arahan awal yang **harus dicek dengan literatur dan data LKPI** `[asumsi]`. Bahan yang dipilih wajib aman untuk ruang medis `[sumber: W]`.

### I1 · Solubilizer / surfaktan pelindung
- **Apa:** melarutkan parfum (umumnya berminyak) ke dalam sistem berair H₂O₂ agar homogen.
- **Cara kerja:** campurkan dulu parfum dengan solubilizer/surfaktan nonionik (mis. golongan etoksilat) pada beberapa rasio, lalu masukkan ke fase air. Pilih yang tidak mempercepat penguraian H₂O₂ dan cocok dengan benzalkonium klorida (kationik) bila basisnya SASKLIN.
- **Menjawab:** H1, K1 (homogenitas).
- **Kelebihan:** paling cepat diuji; homogenitas terlihat dalam hitungan jam.
- **Risiko / pertanyaan:** surfaktan bisa ikut teroksidasi; busa berlebih; ketidakcocokan dengan surfaktan kationik.
- **Upaya:** Rendah · **Peran:** inti

### I2 · Enkapsulasi aroma
- **Apa:** melindungi molekul parfum dari kontak dengan H₂O₂ selama penyimpanan.
- **Cara kerja:** parfum dibungkus, mis. dengan kompleks inklusi siklodekstrin (lebih sederhana) atau mikrokapsul polimer. Aroma dilepas saat larutan disemprotkan dan mengering.
- **Menjawab:** H3, K2, K3.
- **Kelebihan:** menyasar penyebab degradasi aroma secara langsung.
- **Risiko / pertanyaan:** proses lebih rumit dan mahal; larutan bisa keruh; aroma bisa kurang keluar saat dipakai.
- **Upaya:** Tinggi (siklodekstrin: Sedang) · **Peran:** alternatif/pembanding

### I3 · Ko-solven, stabilizer, dan pengaturan pH
- **Apa:** menjaga kelarutan parfum dan kestabilan H₂O₂.
- **Cara kerja:** ko-solven (mis. glikol) membantu kelarutan; stabilizer H₂O₂ (mis. pengikat logam yang lazim dipakai untuk peroksida) dan pH sedikit asam menekan penguraian.
- **Menjawab:** K1, K2.
- **Risiko / pertanyaan:** bila memakai alkohol, klaim "tanpa alkohol" pada SASKLIN `[sumber: L]` bisa berubah; potensi iritasi; kompatibilitas dengan bahan lain.
- **Upaya:** Rendah–Sedang · **Peran:** inti pendukung

### I4 · Fragrance tahan oksidasi
- **Apa:** memilih parfum yang tidak mudah dirusak oksidator.
- **Cara kerja:** hindari komponen yang mudah teroksidasi (mis. banyak ikatan rangkap atau aldehida). Minta sampel parfum yang memang dirancang untuk produk pembersih berbahan oksidator dari pemasok parfum industri.
- **Menjawab:** H2, K2, K3.
- **Kelebihan:** jalan paling langsung; pemasok parfum industri biasanya punya lini khusus ini `[asumsi]`.
- **Risiko / pertanyaan:** pilihan aroma terbatas; harga; perlu sampel dari pemasok.
- **Upaya:** Rendah (bila sampel tersedia) · **Peran:** inti

### I5 · Mulai dari basis SASKLIN Disinfectant Spray
- **Apa:** memakai formula BKC + H₂O₂ yang sudah berizin edar (PKD 20502120681) sebagai titik awal `[sumber: L]`.
- **Cara kerja:** masalahnya menyempit dari "membuat formula baru" menjadi "menambahkan sistem aroma tanpa merusak formula yang sudah lolos".
- **Kelebihan:** variabel lebih sedikit; jalur izin edar lebih jelas.
- **Risiko / pertanyaan:** produk baru mungkin berbeda konsentrasi atau cara aplikasi. Harus dikonfirmasi ke LKPI.
- **Upaya:** Rendah · **Peran:** titik awal

### I6 · Protokol uji stabilitas yang disesuaikan
- **Apa:** cara uji yang adil untuk zat aktif yang tidak tahan panas.
- **Cara kerja:** uji dipercepat pada suhu tinggi bisa melebih-lebihkan penguraian H₂O₂ `[sumber: S]`. Usulan: kombinasi suhu sedang dan uji suhu ruang secara paralel; ukur kadar H₂O₂ (mis. titrasi) dan intensitas aroma di setiap titik waktu; kriteria lulus disepakati dengan QC LKPI.
- **Menjawab:** US5, H4; kendala nomor 1 dari mitra.
- **Kelebihan:** nilai ilmiah; menjawab masalah metodologi yang disebut mitra.
- **Risiko / pertanyaan:** perlu persetujuan standar internal LKPI.
- **Upaya:** Sedang · **Peran:** inti (metodologi)

### I7 · Sistem dua kompartemen
- **Apa:** parfum dan zat aktif disimpan terpisah dan baru bercampur saat disemprot.
- **Risiko / pertanyaan:** biaya kemasan dan kerumitan produksi; tidak cocok untuk jeriken isi ulang.
- **Upaya:** Tinggi · **Peran:** alternatif terakhir

### I8 · Penanda disinfeksi tanpa parfum (eksplorasi)
- **Apa:** penanda visual (mis. indikator warna yang memudar) sebagai pengganti atau pelengkap aroma.
- **Risiko / pertanyaan:** mitra secara eksplisit meminta aroma `[sumber: S]`; risiko noda di permukaan.
- **Upaya:** Sedang · **Peran:** bahan diskusi saja

## 3b. Paket solusi untuk dibahas

| Paket | Isi | Kekuatan | Risiko |
|---|---|---|---|
| **A · Minimum** | I5 + I4 + I1, diuji dengan I6 | Cepat, fokus, realistis untuk 3 hari | Bisa gagal bila semua parfum kandidat tetap terdegradasi |
| **B · Disarankan** | A + I3 (stabilizer/pH), dengan rancangan percobaan faktorial | Menyerang homogenitas dan stabilitas sekaligus | Jumlah batch bertambah |
| **C · Ambisius** | B + I2 (siklodekstrin) sebagai pembanding | Ada rencana cadangan bila A/B gagal | Butuh bahan dan waktu lebih |

## 3c. Pertanyaan pemandu brainstorming

1. Apakah formula SASKLIN boleh dijadikan basis? Kalau tidak, apa yang berbeda dari produk baru ini?
2. Mana yang lebih realistis dibuktikan saat demo day: homogenitas + aroma, atau kestabilan kadar H₂O₂?
3. Apakah tim punya akses laboratorium dan alat ukur (pH, titrasi, inkubator) sebelum hackathon?
4. Apakah tim menerima ketentuan bahwa KI formula sepenuhnya milik LKPI?
5. Aroma seperti apa yang cocok untuk RS, dan bagaimana mengujinya ke pengguna?

## 4. Memilih pendekatan

*(Nilai 1–3 per kriteria, diisi tim. Kriteria tambahan untuk formula: ketersediaan bahan di Indonesia, biaya per liter, kemudahan produksi, keamanan ruang medis.)*

**Usulan inti untuk proposal** `[asumsi]`: kombinasi I4 + I1 (+ I3) di atas basis I5, dengan I2 sebagai alternatif bila tidak stabil; I6 sebagai bagian rencana uji.

## 5. Goal statement (draf)

> Formula kami akan memungkinkan **PT LKPI memproduksi disinfektan ruangan H₂O₂ beraroma yang homogen dan stabil**, yang akan memengaruhi **tim R&D LKPI dan pengguna di fasilitas kesehatan** dengan **produk siap dikembangkan dan aroma penanda disinfeksi yang jelas**. Kami akan mengukur efektivitasnya dengan **homogenitas, kadar H₂O₂ tersisa, intensitas aroma setelah penyimpanan, dan hasil uji antimikroba**.

## 6. Rancangan solusi untuk proposal

| Elemen | Isian |
|---|---|
| Cara kerja (mekanisme kimia) | [diisi setelah pendekatan dipilih — jelaskan dengan bahasa yang bisa dipahami juri lintas disiplin] |
| Dasar ilmiah | |
| Bagian yang dikerjakan tim | |
| Kebaruan | |
| Kelayakan (bahan, biaya, waktu uji) | |
| Komponen lokal | [bahan yang tersedia di dalam negeri] |
| Peluang KI | **KI formula milik penuh PT LKPI, tanpa royalti** `[sumber: W]` |

## Checklist selesai

- [x] HMW, competitive audit (draf), kandidat pendekatan, goal statement (draf)
- [x] Rincian pendekatan, paket solusi, pertanyaan pemandu brainstorming
- [ ] Studi literatur pendukung tiap pendekatan; pendekatan dinilai dan dipilih

<!-- nav-bottom:start -->

---

◂ [2 Define](02-define.md) · [▴ Atas](#) · [4 Prototype](04-prototype.md) ▸  
3 Ideate di proyek lain: [RS-01](../rs-01/03-ideate.md) · [ARB-01](../arb-01/03-ideate.md) · [ARB-02](../arb-02/03-ideate.md) · [LKPI-02](../lkpi-02/03-ideate.md) · [UMS-01](../ums-01/03-ideate.md) · [Template](../_template/03-ideate.md)
<!-- nav-bottom:end -->
