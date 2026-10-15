# 5 · Test — ARB-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-02** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · **5 Test** · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Materialize** · hackathon, demo day, pendampingan · Proposal: Bag. 4 butir 4 · PJ: koordinator validasi pengguna + koordinator teknis
> Panduan metode: [_template/05-test.md](../_template/05-test.md)

## 1. Rencana uji (draf)

| Pertanyaan | Isian |
|---|---|
| Siapa | 2–3 sales, admin gudang, admin penjualan, direktur |
| Apa | Kecepatan input, keandalan offline, akurasi stok, kegunaan dashboard |
| Di mana / kapan | Simulasi dengan dummy data saat hackathon; uji lapangan (ride-along) saat pendampingan |
| Mengapa | Validasi H1–H4 ([02-define.md](02-define.md#7-hypothesis-statements)) |
| Bagaimana | Uji tugas berwaktu; simulasi mode pesawat; stock opname simulasi |

## 2. Metrik

| Metrik | Cara ukur | Target |
|---|---|---|
| Waktu input pesanan | Detik dari buka aplikasi sampai tersimpan | [ ] detik |
| Keandalan offline | % input offline yang tersinkron benar | 100% |
| Selisih stok | Sistem vs fisik setelah simulasi transaksi | Turun dari baseline |
| Input berulang | Jumlah tempat input untuk satu pesanan | 1 |
| Keberhasilan tugas dashboard | % tugas direktur selesai tanpa bantuan | [ ]% |

## 3. Skenario uji (draf)

| No | Skenario | Persona | Hipotesis | Kriteria lulus |
|---|---|---|---|---|
| S1 | Sales mencatat pesanan 5 SKU di outlet tanpa sinyal | P-A | H1 | < [ ] detik; tersinkron setelah online |
| S2 | Sales mengecek stok sebelum menjanjikan | P-A | H2 | Stok terbaru tampil |
| S3 | Stok produk X turun di bawah ambang | P-B | H2 | Peringatan muncul |
| S4 | Direktur mencari sales terbaik bulan ini dan outlet paling aktif | P-C | H4 | Ditemukan < 1 menit tanpa bantuan |
| S5 | Sistem menyarankan outlet yang waktunya pesan ulang | P-A | H3 | Sales menilai saran relevan |

## 4–8. Hasil, temuan, status hipotesis, bukti demo, retrospektif

*(Diisi tim saat uji — format di [template](../_template/05-test.md#4-hasil-uji).)*

<!-- nav-bottom:start -->

---

◂ [4 Prototype](04-prototype.md) · [▴ Atas](#) · [6 Implement](06-implement.md) ▸  
5 Test di proyek lain: [RS-01](../rs-01/05-test.md) · [ARB-01](../arb-01/05-test.md) · [LKPI-01](../lkpi-01/05-test.md) · [LKPI-02](../lkpi-02/05-test.md) · [UMS-01](../ums-01/05-test.md) · [Template](../_template/05-test.md)
<!-- nav-bottom:end -->
