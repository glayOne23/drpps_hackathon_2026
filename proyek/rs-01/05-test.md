# 5 · Test — RS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **RS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · **5 Test** · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/rs-ums-ar-fachrudin.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Materialize** · hackathon, demo day, pendampingan · Proposal: Bag. 4 butir 4 · PJ: koordinator validasi pengguna + koordinator teknis
> Panduan metode: [_template/05-test.md](../_template/05-test.md)

## 1. Rencana uji (draf)

| Pertanyaan | Isian |
|---|---|
| Siapa | Petugas admisi, perawat poli, 1–2 dokter, 3–5 pasien (termasuk lansia) |
| Apa | Fungsi (kecepatan dan keterkiriman notifikasi) dan kegunaan (alur lapor status, dashboard, reschedule) |
| Di mana / kapan | Simulasi saat hackathon; uji di lingkungan RS saat pendampingan (fasilitas uji dari mitra `[sumber: W]`) |
| Mengapa | Validasi H1–H4 ([02-define.md](02-define.md#7-hypothesis-statements)) |
| Bagaimana | Uji fungsi terukur + uji kegunaan berbasis tugas + wawancara singkat setelah uji |

## 2. Metrik

| Metrik | Cara ukur | Target |
|---|---|---|
| Waktu kirim notifikasi | Timestamp status diperbarui → terkirim | < 1 menit `[sumber: W]` |
| Keterkiriman/jangkauan | % pasien uji yang terkonfirmasi menerima sebelum jam praktik | [ ]% |
| Keberhasilan tugas | % partisipan menyelesaikan tugas tanpa bantuan | [ ]% |
| Waktu tugas admisi | Detik untuk mengabari semua pasien satu slot | Turun dibanding manual |
| Kepuasan | Skala singkat setelah uji | [ ] |

## 3. Skenario uji (draf)

| No | Skenario | Persona | Hipotesis | Kriteria lulus |
|---|---|---|---|---|
| S1 | Dokter melaporkan terlambat 60 menit dari HP | Dokter | H1 | Selesai < 30 detik, tanpa bantuan |
| S2 | Sistem mengabari 15 pasien satu slot | — | H2 | Semua terkirim < 1 menit |
| S3 | Admisi menemukan pasien yang belum terjangkau dan menindaklanjuti | P-A | H3 | Ditemukan tanpa membuka chat satu per satu |
| S4 | Pasien memilih slot pengganti dari pesan | P-C | H4 | Selesai tanpa menelepon RS |
| S5 | Pasien lansia tidak membaca WA; eskalasi berjalan | P-B | H2 | Kabar sampai lewat kanal cadangan |

## 4–8. Hasil, temuan, status hipotesis, bukti demo, retrospektif

*(Diisi tim saat uji — format di [template](../_template/05-test.md#4-hasil-uji).)*

<!-- nav-bottom:start -->

---

◂ [4 Prototype](04-prototype.md) · [▴ Atas](#) · [6 Implement](06-implement.md) ▸  
5 Test di proyek lain: [ARB-01](../arb-01/05-test.md) · [ARB-02](../arb-02/05-test.md) · [LKPI-01](../lkpi-01/05-test.md) · [LKPI-02](../lkpi-02/05-test.md) · [UMS-01](../ums-01/05-test.md) · [Template](../_template/05-test.md)
<!-- nav-bottom:end -->
