# 4 · Prototype — UMS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **UMS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · **4 Prototype** · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/dpm-drpps-ums.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · bukti awal s.d. 20 Okt; dibangun saat hackathon · Proposal: Bag. 4 butir 3, Lampiran C · PJ: koordinator teknis
> Panduan metode: [_template/04-prototype.md](../_template/04-prototype.md)

## 1. Kondisi awal dan TKT

| Field | Isian |
|---|---|
| Kategori | Awal / Lanjutan — [tentukan] |
| Yang sudah dicapai | |
| Yang belum diuji | |
| TKT awal + alasan | |
| TKT target + alasan | |

## 2. Bukti awal untuk Lampiran C

| No | Bukti | Bentuk | Berkas/tautan | Menunjukkan apa |
|---|---|---|---|---|
| C1 | Diagram arsitektur (data iHub → normalisasi → pencocokan/kalkulator/generator → pipeline → iHub) | Diagram | | Rancangan sistem |
| C2 | Contoh hasil pencocokan awal pada 1–2 produk nyata | Tabel/tangkapan layar | | Kelayakan |
| C3 | Contoh *product brief* otomatis | Dokumen | | Cara kerja |

## 3. Data uji yang sudah tersedia

Data katalog iHub sudah diambil dan dianalisis (lihat [docs/mitra/dpm-drpps-ums.md](../../docs/mitra/dpm-drpps-ums.md#2113-halaman-katalog-inovasi-katalog)) `[sumber: H]`. Kandidat 3–5 studi kasus dengan jalur regulasi berbeda:

| Produk | Jalur regulasi | Status | Alasan dipilih |
|---|---|---|---|
| Channa Peria | Obat herbal (sudah BPOM, Halal) | Sudah diadopsi | Pembanding kasus berhasil |
| Personal Feedback Balance | Alat kesehatan (AKD Kemenkes) | Sudah diadopsi; rencana izin edar | Jalur alkes |
| ENSIKOL | Pangan olahan keperluan medis khusus (PKMK) | Belum diadopsi | Butuh mitra industri |
| Clovena | Aromaterapi (OHT/kosmetik) | Belum diadopsi | Butuh mitra industri |
| Sampo Herbal 4H | Kosmetik (notifikasi BPOM) | Sudah diadopsi (mitra CV Arbain) | Kaitan dengan mitra hackathon |

Konfirmasi pilihan ini dengan DPM DRPPS.

## 4. Fungsi inti (draf)

| No | Fungsi inti | User story | Kriteria "berfungsi" |
|---|---|---|---|
| F1 | Rekomendasi mitra per produk dengan alasan | US1 | Rekomendasi tampil untuk 3–5 produk uji (K1) |
| F2 | Kalkulator kesiapan: TKT, KI, checklist izin edar | US3 | Celah teridentifikasi per produk (K3) |
| F3 | Generator *product brief* | US2 | Brief dihasilkan dari data katalog (K2) |
| F4 | *Pipeline* kemitraan | US4 | Status prospek bisa diperbarui dan dilihat |

## 5. Rancangan purwarupa (perangkat lunak)

| Artefak | Isian / tautan |
|---|---|
| Arsitektur sistem | |
| Alur pengguna (tim hilirisasi, inovator, industri) | |
| Wireframe | |
| Repositori kode | |
| Sumber data | Katalog iHub (35 inovasi), produk (6), inovator (32) `[sumber: H]`; akses resmi dari taskforce hilirisasi `[sumber: W]` |
| Integrasi | iHub kemungkinan Laravel; data saat ini disematkan di HTML, belum ada API publik `[sumber: H]` + `[asumsi]` — koordinasi dengan pengelola |

## 6. Rencana 3 hari hackathon

Ikuti [template](../_template/04-prototype.md#5-rencana-3-hari-hackathon). Prioritas: F1 → F3 → F2 → F4.

## 7. Iterasi

| Versi | Tanggal | Perubahan | Alasan |
|---|---|---|---|
| v0.1 | | Bukti awal untuk proposal | |

<!-- nav-bottom:start -->

---

◂ [3 Ideate](03-ideate.md) · [▴ Atas](#) · [5 Test](05-test.md) ▸  
4 Prototype di proyek lain: [RS-01](../rs-01/04-prototype.md) · [ARB-01](../arb-01/04-prototype.md) · [ARB-02](../arb-02/04-prototype.md) · [LKPI-01](../lkpi-01/04-prototype.md) · [LKPI-02](../lkpi-02/04-prototype.md) · [Template](../_template/04-prototype.md)
<!-- nav-bottom:end -->
