# 5 · Test — ARB-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · **5 Test** · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Materialize** · hackathon, demo day, pendampingan · Proposal: Bag. 4 butir 4 · PJ: koordinator validasi pengguna + koordinator teknis
> Panduan metode: [_template/05-test.md](../_template/05-test.md)

## 1. Rencana uji (draf)

| Pertanyaan | Isian |
|---|---|
| Siapa | Admin/marketing CV Arba'in, pemilik, 3–5 calon klien maklon/pembeli outlet |
| Apa | Akurasi dan kecepatan agen; kualitas dan kepatuhan konten; kegunaan dashboard |
| Di mana / kapan | Uji internal saat hackathon dengan skenario dari mitra `[sumber: W]`; uji di WA nyata saat pendampingan |
| Mengapa | Validasi H1–H4 ([02-define.md](02-define.md#7-hypothesis-statements)) |
| Bagaimana | Set pertanyaan uji berlabel; penilaian konten oleh mitra; audit visibilitas sebelum/sesudah |

## 2. Metrik

| Metrik | Cara ukur | Target |
|---|---|---|
| Akurasi jawaban | % benar dari 30–50 pertanyaan berlabel | ≥ [ ]% |
| Waktu respons | Detik sampai jawaban pertama | < 1 menit, 24 jam |
| Ketepatan eskalasi | % prospek serius yang diteruskan ke admin | [ ]% |
| Kepatuhan klaim | Klaim berlebihan yang lolos | 0 |
| Visibilitas AI | % pertanyaan tetap yang menyebut merek | Naik dari baseline |
| Biaya | Rupiah per bulan pada volume perkiraan | ≤ batas mitra |
| Waktu produksi konten | Menit per materi, manual vs agen | Turun |

## 3. Skenario uji (draf)

| No | Skenario | Persona | Hipotesis | Kriteria lulus |
|---|---|---|---|---|
| S1 | Calon klien bertanya MOQ dan legalitas maklon hair care pukul 22.00 | P-C | H1 | Jawaban benar < 1 menit |
| S2 | Calon klien minta harga khusus | P-C | H1 | Agen meneruskan ke admin, tidak menjanjikan harga |
| S3 | Agen membuat draf artikel tentang produk yang klaimnya berisiko | P-B | H3 | Klaim ditandai dan diperbaiki |
| S4 | Admin meninjau dan menerbitkan draf konten | P-B | H4 | Lebih cepat dari manual |
| S5 | Pemilik membaca dashboard mingguan | P-A | — | Memahami tanpa penjelasan |

## 4–8. Hasil, temuan, status hipotesis, bukti demo, retrospektif

*(Diisi tim saat uji — format di [template](../_template/05-test.md#4-hasil-uji).)*

Catatan: kenaikan visibilitas di mesin AI butuh waktu berminggu-minggu; saat demo day, tunjukkan baseline dan mekanisme pengukurannya, lalu hasilnya di pendampingan.

<!-- nav-bottom:start -->

---

◂ [4 Prototype](04-prototype.md) · [▴ Atas](#) · [6 Implement](06-implement.md) ▸  
5 Test di proyek lain: [RS-01](../rs-01/05-test.md) · [ARB-02](../arb-02/05-test.md) · [LKPI-01](../lkpi-01/05-test.md) · [LKPI-02](../lkpi-02/05-test.md) · [UMS-01](../ums-01/05-test.md) · [Template](../_template/05-test.md)
<!-- nav-bottom:end -->
