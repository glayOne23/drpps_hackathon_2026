# 4 · Prototype — RS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **RS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · **4 Prototype** · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/rs-ums-ar-fachrudin.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · bukti awal s.d. 20 Okt; dibangun saat hackathon · Proposal: Bag. 4 butir 3, Lampiran C · PJ: koordinator teknis
> Panduan metode: [_template/04-prototype.md](../_template/04-prototype.md)

## 1. Kondisi awal dan TKT

| Field | Isian |
|---|---|
| Kategori | Awal / Lanjutan — [tentukan] |
| Yang sudah dicapai | [mis. purwarupa sistem notifikasi/antrean yang pernah dibuat tim] |
| Yang belum diuji | |
| TKT awal + alasan | |
| TKT target + alasan | |

## 2. Bukti awal untuk Lampiran C

| No | Bukti | Bentuk | Berkas/tautan | Menunjukkan apa |
|---|---|---|---|---|
| C1 | Diagram arsitektur (SIMRS/`/api/jadwal` → layanan status → notifikasi multi-kanal → dashboard) | Diagram | | Rancangan sistem |
| C2 | Wireframe: lapor status dokter, dashboard admisi, pesan + reschedule pasien | Wireframe | | Alur pengguna |
| C3 | [Purwarupa/kode yang sudah ada, bila kategori Lanjutan] | | | |

## 3. Fungsi inti (draf)

| No | Fungsi inti | User story | Kriteria "berfungsi" |
|---|---|---|---|
| F1 | Dokter/poli mengubah status slot (terlambat/batal/pengganti) | US5 | Status tersimpan dan tampil di dashboard |
| F2 | Notifikasi otomatis ke semua pasien terdaftar di slot itu | US1, US3 | Terkirim < 1 menit sejak F1 (K1) |
| F3 | Dashboard admisi: status terkirim/dibaca/dikonfirmasi per pasien | US4 | Admisi bisa melihat siapa yang belum terjangkau |
| F4 | Pasien konfirmasi atau pilih slot pengganti dari pesan | US2 | Pilihan tercatat dan kuota slot diperbarui |

Fitur tambahan: eskalasi ke SMS/IVR/kontak keluarga, prediksi keterlambatan, kanal umpan balik, desain konektor SATUSEHAT.

## 4. Rancangan purwarupa (perangkat lunak)

| Artefak | Isian / tautan |
|---|---|
| Arsitektur sistem | |
| Sitemap / alur pengguna (dokter, admisi, pasien) | |
| Wireframe low-fidelity | |
| Mockup high-fidelity | |
| Repositori kode | |
| Sumber data | Jadwal: `/api/jadwal` situs RS (publik, pola mingguan) `[sumber: R]`; pasien: data dummy; skenario nyata dari mitra `[sumber: W]` |

Aksesibilitas: teks besar dan bahasa sederhana di pesan untuk pasien lansia; jangan hanya mengandalkan warna untuk status.

## 5. Rencana 3 hari hackathon

Ikuti jadwal di [template](../_template/04-prototype.md#5-rencana-3-hari-hackathon). Prioritas: F1 → F2 → F3 → F4.

## 6. Iterasi

| Versi | Tanggal | Perubahan | Alasan |
|---|---|---|---|
| v0.1 | | Bukti awal untuk proposal | |

## Checklist selesai

- [ ] Kategori dan TKT
- [ ] Bukti Lampiran C
- [x] Fungsi inti (draf)
- [ ] Rancangan purwarupa

<!-- nav-bottom:start -->

---

◂ [3 Ideate](03-ideate.md) · [▴ Atas](#) · [5 Test](05-test.md) ▸  
4 Prototype di proyek lain: [ARB-01](../arb-01/04-prototype.md) · [ARB-02](../arb-02/04-prototype.md) · [LKPI-01](../lkpi-01/04-prototype.md) · [LKPI-02](../lkpi-02/04-prototype.md) · [UMS-01](../ums-01/04-prototype.md) · [Template](../_template/04-prototype.md)
<!-- nav-bottom:end -->
