# 2 · Define — LKPI-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **LKPI-01** · [README](README.md) · [1 Empathize](01-empathize.md) · **2 Define** · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/pt-lkpi.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Understand** · sebelum 20 Okt · Proposal: Bag. 3, Bag. 4 butir 1 · PJ: ketua + koordinator validasi pengguna
> Panduan metode: [_template/02-define.md](../_template/02-define.md). Semua isian di bawah adalah draf dari riset sekunder.

## 1. User stories (kebutuhan formula)

| No | Persona | User story | Prioritas |
|---|---|---|---|
| US1 | R&D (P-A) | Sebagai formulator, saya ingin parfum, H₂O₂, dan surfaktan bercampur homogen tanpa pemisahan fase, agar produk bisa diproduksi. | Tinggi |
| US2 | R&D (P-A) | Sebagai formulator, saya ingin kadar H₂O₂ tidak turun drastis selama penyimpanan, agar daya bunuh mikroba terjaga. | Tinggi |
| US3 | Pengguna RS (P-B) | Sebagai petugas, saya ingin aroma tercium jelas setelah aplikasi, agar tahu ruangan sudah didisinfeksi. | Tinggi |
| US4 | Pengguna RS (P-B) | Sebagai orang yang berada di ruangan, saya ingin aroma tidak menyengat dan tidak memicu iritasi, agar nyaman. | Tinggi |
| US5 | R&D (P-A) | Sebagai formulator, saya ingin protokol uji stabilitas yang sesuai untuk zat aktif termolabil, agar hasil uji bermakna. | Sedang |
| US6 | Produksi | Sebagai bagian produksi, saya ingin metode pencampuran yang bisa diulang di skala produksi dengan biaya bahan wajar. | Sedang |

## 2. Alur penggunaan dan pengembangan saat ini (draf)

| Tahap | Tindakan | Pain point | Peluang |
|---|---|---|---|
| 1. Formulasi | R&D mencampur H₂O₂ + surfaktan + parfum `[sumber: S]` | Tidak homogen `[sumber: S]` | Solubilizer/ko-solven/enkapsulasi |
| 2. Uji stabilitas | Penyimpanan suhu tinggi `[sumber: S]` | H₂O₂ terurai; aroma hilang `[sumber: S, W]` | Protokol uji + stabilizer |
| 3. Produksi | Pencampuran skala besar `[asumsi]` | Belum sampai tahap ini | Metode yang bisa diulang |
| 4. Aplikasi di RS | Petugas menyemprot ruangan `[asumsi]` | Tanpa aroma, tidak ada penanda disinfeksi `[sumber: W]` | Aroma penanda yang stabil |

## 3. 5W + H

| Pertanyaan | Jawaban (draf) |
|---|---|
| Who | Tim R&D PT LKPI; pengguna akhir di fasilitas kesehatan |
| What | Parfum tidak kompatibel dengan sistem H₂O₂ + surfaktan |
| Where | Laboratorium R&D LKPI; ruangan RS/klinik |
| When | Saat pencampuran dan selama penyimpanan/uji stabilitas |
| Why | Produk tidak bisa diluncurkan; pengguna butuh penanda sensorik disinfeksi |
| How (sekarang) | Percobaan kombinasi parfum–surfaktan yang belum berhasil `[sumber: S]` |

## 4. Problem statement (draf)

> **Mas Agus** adalah **formulator R&D di produsen disinfektan rumah sakit** yang membutuhkan **formula disinfektan ruangan berbasis H₂O₂ dengan parfum yang homogen dan stabil** karena **parfum, oksidator, dan surfaktan yang dipakai saat ini memisah atau saling merusak, sehingga produk tidak bisa lolos uji stabilitas.**

## 5. Need statement (draf)

> Cara untuk **menggabungkan parfum yang tahan oksidasi ke dalam disinfektan ruangan berbasis hidrogen peroksida secara homogen dan stabil** pada **produk disinfektan untuk fasilitas kesehatan**, yang **mempertahankan kadar zat aktif dan efikasi antimikroba sekaligus memberi penanda aroma yang jelas**.

## 6. Kriteria keberhasilan

| No | Kriteria | Ukuran | Target | Sumber |
|---|---|---|---|---|
| K1 | Homogenitas | Tidak ada pemisahan fase/kekeruhan setelah [waktu] pada [suhu] | Homogen `[target]` | Indikator mitra `[sumber: W]` |
| K2 | Stabilitas zat aktif | % kadar H₂O₂ tersisa setelah uji stabilitas dipercepat | ≥ [ ]% — **tanyakan batas LKPI** | Indikator mitra `[sumber: W]` |
| K3 | Aroma | Intensitas dan ketahanan aroma (organoleptik) setelah penyimpanan dan saat aplikasi | Tercium jelas `[target]` | Indikator mitra `[sumber: W]` |
| K4 | Fisikokimia | pH, kejernihan, ketahanan suhu | Dalam rentang spesifikasi LKPI `[target]` | Keluaran mitra `[sumber: W]` |
| K5 | Efikasi | Uji antimikroba sesuai standar LKPI | Lulus `[target]` | Indikator mitra `[sumber: W]` |
| K6 | Keamanan | Tanpa residu berbahaya; tidak iritatif bagi saluran napas | Memenuhi `[target]` | Batasan mitra `[sumber: W]` |

## 7. Hypothesis statements

| No | Hipotesis | Kriteria | Cara menguji |
|---|---|---|---|
| H1 | Jika parfum dilarutkan dengan solubilizer/surfaktan nonionik yang tahan oksidasi, maka campuran tetap homogen. | K1 | Variasi jenis dan rasio solubilizer |
| H2 | Jika komponen parfum dipilih yang minim gugus mudah teroksidasi, maka aroma lebih stabil dan kadar H₂O₂ lebih terjaga. | K2, K3 | Bandingkan beberapa kandidat fragrance |
| H3 | Jika parfum dienkapsulasi, maka kontak dengan H₂O₂ berkurang dan aroma bertahan lebih lama. | K2, K3 | Bandingkan bebas vs terenkapsulasi |
| H4 | Jika protokol uji stabilitas dipercepat disesuaikan untuk zat termolabil, maka hasil uji mencerminkan kondisi penyimpanan nyata. | US5 | Diskusikan dengan QC LKPI |

Semua hipotesis adalah dugaan berbasis literatur umum dan perlu dicek dengan data percobaan LKPI `[asumsi]`.

## 8. Value proposition (draf)

| Pertanyaan | Jawaban |
|---|---|
| Apa yang dilakukan? | Formula disinfektan ruangan H₂O₂ beraroma yang homogen dan stabil, lengkap dengan rasionalisasi ilmiah dan data uji awal |
| Mengapa peduli? | LKPI bisa meluncurkan produk baru; pengguna RS mendapat penanda bahwa ruangan sudah didisinfeksi |
| Pembeda | [diisi setelah pendekatan dipilih] |

## 9. Pertanyaan terbuka untuk mitra

- Konsentrasi H₂O₂ target dan penurunan kadar yang diterima?
- Apakah formula SASKLIN Disinfectant Spray bisa menjadi basis?
- Metode aplikasi (semprot, fogging, lap)?
- Surfaktan dan parfum yang sudah dicoba beserta hasilnya?
- Standar uji efikasi (mis. EN/AOAC) dan stabilitas yang dipakai; target masa simpan?
- Jalur izin edar: PKRT (PKD) atau AKD?
- Batas biaya bahan per liter?

## Checklist selesai

- [x] Semua bagian Define (draf)
- [ ] Dikonfirmasi dengan R&D LKPI

<!-- nav-bottom:start -->

---

◂ [1 Empathize](01-empathize.md) · [▴ Atas](#) · [3 Ideate](03-ideate.md) ▸  
2 Define di proyek lain: [RS-01](../rs-01/02-define.md) · [ARB-01](../arb-01/02-define.md) · [ARB-02](../arb-02/02-define.md) · [LKPI-02](../lkpi-02/02-define.md) · [UMS-01](../ums-01/02-define.md) · [Template](../_template/02-define.md)
<!-- nav-bottom:end -->
