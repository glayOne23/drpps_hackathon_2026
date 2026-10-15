# 4 · Prototype — ARB-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · **4 Prototype** · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · bukti awal s.d. 20 Okt; dibangun saat hackathon · Proposal: Bag. 4 butir 3, Lampiran C · PJ: koordinator teknis
> Panduan metode: [_template/04-prototype.md](../_template/04-prototype.md)

## 1. Kondisi awal dan TKT

| Field | Isian |
|---|---|
| Kategori | Awal / Lanjutan — [tentukan] |
| Yang sudah dicapai | [mis. agen/chatbot AI yang pernah dibuat tim untuk konteks lain] |
| Yang belum diuji | |
| TKT awal + alasan | |
| TKT target + alasan | |

## 2. Bukti awal untuk Lampiran C

| No | Bukti | Bentuk | Berkas/tautan | Menunjukkan apa |
|---|---|---|---|---|
| C1 | Diagram arsitektur multi-agen (penjawab, konten, pemeriksa klaim, pemantau visibilitas, dashboard) | Diagram | | Rancangan sistem |
| C2 | Hasil audit visibilitas AI awal (sebelum solusi) | Tabel/tangkapan layar | | Bukti masalah + baseline K4 |
| C3 | Contoh percakapan agen dengan katalog uji | Tangkapan layar/video | | Cara kerja |

## 3. Fungsi inti (draf)

| No | Fungsi inti | User story | Kriteria "berfungsi" |
|---|---|---|---|
| F1 | Agen menjawab pertanyaan katalog, MOQ, legalitas lewat chat | US1 | Akurasi ≥ target pada set uji (K2) |
| F2 | Serah-terima prospek serius ke admin dengan ringkasan | US2 | Admin menerima ringkasan lengkap |
| F3 | Draf konten + pemeriksa klaim | US4 | Klaim berlebihan ditandai (K5) |
| F4 | Pemantau visibilitas AI + dashboard | US3, US5 | Menampilkan % penyebutan dan prospek |

## 4. Rancangan purwarupa (perangkat lunak)

| Artefak | Isian / tautan |
|---|---|
| Arsitektur sistem | |
| Alur percakapan (happy path, eskalasi ke manusia, pertanyaan di luar katalog) | |
| Wireframe dashboard | |
| Repositori kode | |
| Sumber data | Katalog dan skenario penjualan dari mitra `[sumber: W]`; 12 kategori maklon & 16 produk grosir di situs `[sumber: A]` |

Pastikan admin bisa menghentikan/mengambil alih agen kapan saja.

## 5. Rencana 3 hari hackathon

Ikuti [template](../_template/04-prototype.md#5-rencana-3-hari-hackathon). Prioritas: F1 → F2 → F3 → F4.

## 6. Iterasi

| Versi | Tanggal | Perubahan | Alasan |
|---|---|---|---|
| v0.1 | | Bukti awal untuk proposal | |

<!-- nav-bottom:start -->

---

◂ [3 Ideate](03-ideate.md) · [▴ Atas](#) · [5 Test](05-test.md) ▸  
4 Prototype di proyek lain: [RS-01](../rs-01/04-prototype.md) · [ARB-02](../arb-02/04-prototype.md) · [LKPI-01](../lkpi-01/04-prototype.md) · [LKPI-02](../lkpi-02/04-prototype.md) · [UMS-01](../ums-01/04-prototype.md) · [Template](../_template/04-prototype.md)
<!-- nav-bottom:end -->
