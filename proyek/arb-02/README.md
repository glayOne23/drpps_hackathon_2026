# ARB-02 — Sistem CRM Terpadu: Integrasi Data Pelanggan B2B, Aktivitas Sales, dan Manajemen Stok

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-02** · **README** · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> Folder kerja tim untuk ARB-02, mengikuti design thinking 6 fase. Diisi awal dari riset sekunder (14 Okt 2026); semua isian masih perlu dikonfirmasi lewat riset primer.
> Panduan metode tiap fase: [_template/](../_template/README.md) · Detail mitra: [docs/mitra/cv-arbain.md](../../docs/mitra/cv-arbain.md)

## Identitas

| Field | Isian |
|---|---|
| Kode dan nama tantangan | ARB-02 — Sistem CRM Terpadu: Integrasi Data Pelanggan B2B, Aktivitas Sales, dan Manajemen Stok |
| Mitra | CV Arbain (CV Arbain Jaya Mandiri, Mojosongo, Jebres, Surakarta) |
| Nama tim | |
| Kategori | Awal / Lanjutan — [tentukan] |
| Jenis solusi | Perangkat lunak (aplikasi web/mobile) |
| TKT awal → target | [ ] → [ ] |
| Indikator utama mitra | Data pelanggan, sales, dan stok terhubung real-time tanpa input berulang; kinerja sales terpantau; akurasi stok naik `[sumber: W]` |
| Ketentuan KI | Tidak disebut di laman tantangan — tanyakan |

## Alur kerja

| Kelompok | Fase | File | Tahap program | Masuk ke proposal | Status |
|---|---|---|---|---|---|
| **Understand** | 1 Empathize | [01-empathize.md](01-empathize.md) | Sekarang s.d. 20 Okt | Bag. 4 butir 1 | ◐ riset sekunder terisi |
| | 2 Define | [02-define.md](02-define.md) | Sekarang s.d. 20 Okt | Bag. 3, Bag. 4 butir 1 | ◐ draf awal |
| **Explore** | 3 Ideate | [03-ideate.md](03-ideate.md) | s.d. 20 Okt | Bag. 4 butir 2 | ◐ kandidat ide |
| | 4 Prototype | [04-prototype.md](04-prototype.md) | Bukti awal s.d. 20 Okt; hackathon | Bag. 4 butir 3, Lampiran C | ☐ |
| **Materialize** | 5 Test | [05-test.md](05-test.md) | Hackathon, demo day, pendampingan | Bag. 4 butir 4 | ◐ metrik terisi |
| | 6 Implement | [06-implement.md](06-implement.md) | s.d. April 2027 | Bag. 4 butir 4 & 6 | ◐ |
| — | Draf proposal | [proposal-draf.md](proposal-draf.md) | s.d. 20 Okt 2026, 23.59 WIB | Semua bagian | ◐ |

☐ belum · ◐ terisi sebagian · ☑ selesai

## Konvensi penandaan

`[sumber: X]` dari sumber sekunder (kode di [docs/README](../../docs/README.md#sumber)) · `[asumsi]` dugaan tim · `[tervalidasi: sumber, tanggal]` sudah dikonfirmasi · `[target]` hasil yang ingin dicapai.

## Log keputusan

| Tanggal | Keputusan | Alasan | Fase |
|---|---|---|---|
| 14 Okt 2026 | Folder dibuat dan diisi dari riset sekunder | Persiapan proposal | — |
| 19 Okt 2026 | Proposal pembanding disusun di template resmi: tim Antech Async, kategori Awal, konsep ArbaSync (PWA offline-first + buku besar stok ber-batch + jatah stok prediktif) — lihat [Proposal_AntechAsync_ArbaSync.docx](Proposal_AntechAsync_ArbaSync.docx) | Dibandingkan dengan proposal RS-01 sebelum memilih satu untuk diajukan | Proposal |
| 19 Okt 2026 | Rancangan solusi gabungan v0.4 — fondasi SIGAP (P3), ditambah stok fisik vs dipesan, 4 peran, dan uji konkurensi (P1), serta batch/kedaluwarsa/FEFO, telusur batch, dan kunjungan berprioritas (P2); jatah stok prediktif ditunda — lihat [draf-solusi-gabungan.md](draf-solusi-gabungan.md) | Fondasi paling layak dibangun dan sudah teruji; tambahan dipilih yang murah (≤ 2 tabel, ≤ 1 layar, tanpa teknologi baru) | Ideate |
| 19 Okt 2026 | **Tanpa PWA**; stack **Django + PostgreSQL** (monolit). Proposal disusun: [Proposal_AntechAsync_SIGAP.docx](Proposal_AntechAsync_SIGAP.docx) (+ [pratinjau PDF](PRATINJAU_Proposal_AntechAsync_SIGAP.pdf), diagram di [lampiran/](lampiran/)), kategori Awal, tim Antech Async | Keputusan pengguna. Mode tanpa sinyal cukup dengan halaman sales satu halaman + IndexedDB | Proposal |
| 19 Okt 2026 | Purwarupa dipindahkan ke **Django + PostgreSQL** ([purwarupa/](purwarupa/)): stok fisik/dipesan, batch + FEFO, batal, opname, telusur batch; uji otomatis **19/19 lulus**. Lampiran C proposal diperbarui (C.5 tiga gambar + 19 uji, C.6 tinggal rencana) dan informasi yang bertentangan/berulang di docx dikoreksi | Uji coba harus memakai stack yang sama dengan proposal; klaim di Lampiran C harus sesuai uji nyata | Prototype |

<!-- nav-bottom:start -->

---

[▴ Atas](#) · [1 Empathize](01-empathize.md) ▸  
README di proyek lain: [RS-01](../rs-01/README.md) · [ARB-01](../arb-01/README.md) · [LKPI-01](../lkpi-01/README.md) · [LKPI-02](../lkpi-02/README.md) · [UMS-01](../ums-01/README.md) · [Template](../_template/README.md)
<!-- nav-bottom:end -->
