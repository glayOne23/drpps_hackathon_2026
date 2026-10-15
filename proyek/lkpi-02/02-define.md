# 2 · Define — LKPI-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **LKPI-02** · [README](README.md) · [1 Empathize](01-empathize.md) · **2 Define** · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/pt-lkpi.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Understand** · sebelum 20 Okt · Proposal: Bag. 3, Bag. 4 butir 1 · PJ: ketua + koordinator validasi pengguna
> Panduan metode: [_template/02-define.md](../_template/02-define.md). Semua isian di bawah adalah draf dari riset sekunder.

## 1. User stories

| No | Persona | User story | Prioritas |
|---|---|---|---|
| US1 | Petugas CSSD (P-A) | Sebagai petugas CSSD, saya ingin mengeluarkan tepat 20 ml dari jeriken 5 L dengan satu gerakan, agar takaran benar tanpa gelas takar. | Tinggi |
| US2 | Petugas CSSD (P-A) | Sebagai petugas, saya ingin alat tidak bocor atau menetes, agar cairan tidak mengenai kulit dan tidak terbuang. | Tinggi |
| US3 | Petugas CSSD (P-A) | Sebagai petugas yang memakai sarung tangan, saya ingin alat mudah ditekan/dioperasikan, agar tidak repot. | Tinggi |
| US4 | Packaging (P-B) | Sebagai pengembang kemasan, saya ingin alat pas dengan jeriken yang ada dan tahan BAYzime serta BAYcide, agar satu desain untuk dua produk. | Tinggi |
| US5 | Packaging (P-B) | Sebagai pengembang kemasan, saya ingin biaya produksi alat rendah, agar layak dibundel atau dijual. | Sedang |
| US6 | Kepala CSSD | Sebagai kepala CSSD, saya ingin takaran konsisten antarpetugas, agar mutu reprosesing instrumen terjaga. | Sedang |

## 2. User journey map — petugas CSSD, kondisi saat ini (draf)

| Tahap | Tindakan | Perasaan | Pain point | Peluang |
|---|---|---|---|---|
| 1. Siapkan wadah | Isi 2,5 L air `[sumber: W]` | Rutin | — | Penanda volume air |
| 2. Ambil produk | Angkat/miringkan jeriken 5 L `[asumsi]` | Berat | Jeriken berat, sulit dikontrol | Pompa di jeriken, tanpa mengangkat |
| 3. Takar | Tuang ke gelas takar `[sumber: S]` | Hati-hati | Tumpah, tidak akurat `[sumber: W]` | 20 ml sekali tekan |
| 4. Campur | Tuang ke wadah perendaman | — | Sisa di gelas takar `[asumsi]` | Langsung ke wadah |
| 5. Bersihkan | Cuci gelas takar `[asumsi]` | Repot | Langkah tambahan | Tanpa gelas takar |

## 3. 5W + H

| Pertanyaan | Jawaban (draf) |
|---|---|
| Who | Petugas CSSD/kamar operasi pengguna BAYzime (dan BAYcide) |
| What | Menakar 20 ml dari jeriken 5 L secara akurat tanpa tumpah |
| Where | Area dekontaminasi CSSD/kamar operasi |
| When | Setiap menyiapkan larutan pembersihan/disinfeksi instrumen |
| Why | Takaran tidak akurat dan tumpahan memengaruhi mutu, keselamatan, dan biaya |
| How (sekarang) | Gelas takar manual `[sumber: S]` |

## 4. Problem statement (draf)

> **Mas Dwi** adalah **petugas CSSD yang menyiapkan larutan detergen enzimatik beberapa kali per shift dengan sarung tangan** yang membutuhkan **cara mengeluarkan tepat 20 ml dari jeriken 5 L tanpa tumpah** karena **menuang ke gelas takar dari jeriken berat tidak akurat, berantakan, dan menambah langkah kerja.**

## 5. Need statement (draf)

> Cara untuk **menakar konsentrat pembersih dan disinfektan instrumen secara tepat dari kemasan 5 liter** pada **petugas CSSD dan kamar operasi**, yang **menurunkan deviasi takaran di bawah 5% dan menghilangkan tumpahan**.

## 6. Kriteria keberhasilan

| No | Kriteria | Ukuran | Sekarang | Target | Sumber |
|---|---|---|---|---|---|
| K1 | Akurasi | Deviasi volume terhadap 20 ml | [ukur baseline manual] | < 5% `[target]` | Indikator mitra `[sumber: W]` |
| K2 | Kebocoran | Tetesan/kebocoran per [n] siklus | Tumpah `[sumber: W]` | 0 `[target]` | Batasan mitra `[sumber: W]` |
| K3 | Kemudahan | Petugas berhasil menakar tanpa alat ukur terpisah dan tanpa bantuan | Butuh gelas takar | 100% `[target]` | Indikator mitra `[sumber: W]` |
| K4 | Ketahanan material | Tidak rusak/berubah setelah paparan BAYzime dan BAYcide | — | Tahan `[target]` | Batasan mitra `[sumber: W]` |
| K5 | Biaya | Biaya produksi per unit | — | ≤ [target LKPI] | Batasan mitra `[sumber: W]` |

## 7. Hypothesis statements

| No | Hipotesis | Kriteria | Cara menguji |
|---|---|---|---|
| H1 | Jika pompa memakai mekanisme volume tetap 20 ml, maka deviasi < 5% tanpa elektronik. | K1, K5 | Uji repeatability ≥ 30 siklus |
| H2 | Kami yakin bahwa pompa yang terpasang di jeriken dengan katup anti-tetes akan menghilangkan tumpahan. | K2 | Uji kebocoran dan tetesan |
| H3 | Jika tuas/tombol dirancang untuk tangan bersarung, maka petugas bisa menakar tanpa bantuan. | K3 | Uji formatif dengan petugas |
| H4 | Jika material bagian basah dipilih tahan enzim dan H₂O₂, maka satu desain cocok untuk BAYzime dan BAYcide. | K4 | Uji rendam/paparan |

## 8. Value proposition (draf)

| Pertanyaan | Jawaban |
|---|---|
| Apa yang dilakukan? | Alat takar yang terpasang di jeriken 5 L dan mengeluarkan tepat 20 ml per tekan |
| Mengapa peduli? | Takaran akurat, tanpa tumpah, tanpa gelas takar; mutu reprosesing lebih konsisten |
| Pembeda | Satu desain untuk BAYzime dan BAYcide; komponen lokal; KI milik tim dengan peluang royalti `[asumsi]` |

## 9. Pertanyaan terbuka untuk mitra

- Dimensi dan ukuran ulir tutup jeriken 5 L; ada beberapa jenis jeriken?
- Viskositas BAYzime dan BAYcide; data kompatibilitas material?
- Pompa dijual bersama kemasan, dipinjamkan, atau terpisah? Target harga per unit?
- Opsi 1: proses produksi mana yang paling lambat, dan berapa volume per hari?

## Checklist selesai

- [x] Semua bagian Define (draf)
- [ ] Dikonfirmasi dengan petugas CSSD dan tim packaging LKPI

<!-- nav-bottom:start -->

---

◂ [1 Empathize](01-empathize.md) · [▴ Atas](#) · [3 Ideate](03-ideate.md) ▸  
2 Define di proyek lain: [RS-01](../rs-01/02-define.md) · [ARB-01](../arb-01/02-define.md) · [ARB-02](../arb-02/02-define.md) · [LKPI-01](../lkpi-01/02-define.md) · [UMS-01](../ums-01/02-define.md) · [Template](../_template/02-define.md)
<!-- nav-bottom:end -->
