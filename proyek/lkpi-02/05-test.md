# 5 · Test — LKPI-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **LKPI-02** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · **5 Test** · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/pt-lkpi.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Materialize** · hackathon, demo day, pendampingan · Proposal: Bag. 4 butir 4 · PJ: koordinator validasi pengguna + koordinator teknis
> Panduan metode: [_template/05-test.md](../_template/05-test.md). Pakai konsep **evaluasi formatif** IEC 62366-1 untuk uji pemakaian.

## 1. Rencana uji (draf)

| Pertanyaan | Isian |
|---|---|
| Siapa | Petugas CSSD/kamar operasi (2–5), tim Technical Services/Packaging LKPI |
| Apa | Akurasi volume, kebocoran, ketahanan material, kemudahan pakai |
| Di mana / kapan | Bengkel/lab tim saat hackathon; CSSD RS (mis. RS UMS) dan LKPI saat pendampingan |
| Mengapa | Validasi H1–H4 ([02-define.md](02-define.md#7-hypothesis-statements)) |
| Bagaimana | Uji repeatability terukur; uji rendam material; uji formatif dengan petugas memakai APD |

## 2. Metrik

| Metrik | Cara ukur | Target |
|---|---|---|
| Deviasi volume | Timbang/ukur ≥ 30 siklus; hitung rata-rata, simpangan, deviasi maksimum terhadap 20 ml | < 5% `[sumber: W]` |
| Baseline manual | Ukur 10–20 takaran dengan gelas takar | Pembanding |
| Kebocoran | Tetesan setelah siklus; posisi diam 24 jam | 0 |
| Ketahanan material | Perubahan fisik setelah rendam BAYzime/BAYcide [n] hari | Tidak berubah |
| Kemudahan | % petugas berhasil tanpa bantuan; waktu per takaran | 100%; lebih cepat dari manual |

## 3. Skenario uji (draf)

| No | Skenario | Persona | Hipotesis | Kriteria lulus |
|---|---|---|---|---|
| S1 | 30 siklus berturut-turut dengan BAYzime (atau air bila produk belum tersedia) | — | H1 | Deviasi < 5% |
| S2 | Pompa dibiarkan terpasang 24 jam | — | H2 | Tidak menetes |
| S3 | Petugas dengan sarung tangan menyiapkan larutan 2,5 L | P-A | H3 | Berhasil tanpa bantuan |
| S4 | Skenario berisiko: pompa ditekan sebagian/berulang cepat, jeriken hampir habis | P-A | H1, H2 | Volume tetap dalam toleransi; tidak menyemprot |
| S5 | Rendam komponen basah dalam BAYzime dan BAYcide | — | H4 | Tidak ada degradasi |

## 4–8. Hasil, temuan, status hipotesis, bukti demo, retrospektif

*(Diisi tim saat uji — format di [template](../_template/05-test.md#4-hasil-uji).)*

<!-- nav-bottom:start -->

---

◂ [4 Prototype](04-prototype.md) · [▴ Atas](#) · [6 Implement](06-implement.md) ▸  
5 Test di proyek lain: [RS-01](../rs-01/05-test.md) · [ARB-01](../arb-01/05-test.md) · [ARB-02](../arb-02/05-test.md) · [LKPI-01](../lkpi-01/05-test.md) · [UMS-01](../ums-01/05-test.md) · [Template](../_template/05-test.md)
<!-- nav-bottom:end -->
