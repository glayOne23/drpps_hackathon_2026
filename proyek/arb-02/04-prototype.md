# 4 · Prototype — ARB-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-02** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · **4 Prototype** · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · bukti awal s.d. 20 Okt; dibangun saat hackathon · Proposal: Bag. 4 butir 3, Lampiran C · PJ: koordinator teknis
> Panduan metode: [_template/04-prototype.md](../_template/04-prototype.md)

## 1. Kondisi awal dan TKT

| Field | Isian |
|---|---|
| Kategori | Awal / Lanjutan — [tentukan; sistem inventori/CRM yang pernah dibuat tim bisa menjadi dasar kategori Lanjutan] |
| Yang sudah dicapai | |
| Yang belum diuji | |
| TKT awal + alasan | |
| TKT target + alasan | |

## 2. Bukti awal untuk Lampiran C

| No | Bukti | Bentuk | Berkas/tautan | Menunjukkan apa |
|---|---|---|---|---|
| C1 | Model data (pelanggan, kunjungan, pesanan, produk, stok) | Diagram ERD | | Rancangan sistem |
| C2 | Wireframe aplikasi sales (HP) dan dashboard (desktop) | Wireframe | | Alur pengguna |
| C3 | [Purwarupa/kode yang sudah ada] | | | |

## 3. Fungsi inti (draf)

| No | Fungsi inti | User story | Kriteria "berfungsi" |
|---|---|---|---|
| F1 | Sales check-in kunjungan dan input pesanan dari HP, termasuk offline | US1 | Tersimpan offline, tersinkron saat online (K5) |
| F2 | Stok berkurang otomatis + peringatan stok menipis | US2, US3 | Stok terbarui setelah pesanan (K3) |
| F3 | Profil outlet dengan riwayat transaksi | US5 | Riwayat tampil per outlet |
| F4 | Dashboard kinerja sales dan outlet aktif | US4 | Data dari F1–F3 tanpa input ulang (K1) |

## 4. Rancangan purwarupa (perangkat lunak)

| Artefak | Isian / tautan |
|---|---|
| Arsitektur sistem | |
| Alur pengguna (sales, admin gudang, direktur) | |
| Wireframe | |
| Repositori kode | |
| Sumber data | Dummy data dari mitra `[sumber: W]`; katalog awal dari 16 produk grosir di situs `[sumber: A]` |

Uji di HP Android kelas menengah dan koneksi lambat.

## 5. Rencana 3 hari hackathon

Ikuti [template](../_template/04-prototype.md#5-rencana-3-hari-hackathon). Prioritas: F1 → F2 → F4 → F3.

## 6. Iterasi

| Versi | Tanggal | Perubahan | Alasan |
|---|---|---|---|
| v0.1 | | Bukti awal untuk proposal | |

<!-- nav-bottom:start -->

---

◂ [3 Ideate](03-ideate.md) · [▴ Atas](#) · [5 Test](05-test.md) ▸  
4 Prototype di proyek lain: [RS-01](../rs-01/04-prototype.md) · [ARB-01](../arb-01/04-prototype.md) · [LKPI-01](../lkpi-01/04-prototype.md) · [LKPI-02](../lkpi-02/04-prototype.md) · [UMS-01](../ums-01/04-prototype.md) · [Template](../_template/04-prototype.md)
<!-- nav-bottom:end -->
