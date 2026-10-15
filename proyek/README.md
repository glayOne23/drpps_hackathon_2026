# Proyek per Tantangan

> Folder kerja tim, satu per tantangan, mengikuti design thinking 6 fase (Empathize, Define, Ideate, Prototype, Test, Implement).
> Referensi mitra dan aturan program ada di [docs/](../docs/README.md). Kerangka kosong ada di [_template/](_template/README.md).

Semua folder **sudah diisi awal dari riset sekunder** (pedoman, laman tantangan, transkrip sosialisasi, situs mitra, iHub). Isian bertanda `[sumber: X]` atau `[asumsi]` dan harus dikonfirmasi lewat wawancara/observasi sebelum dipakai sebagai fakta di proposal.

| Kode | Mitra | Jenis solusi | Folder | Catatan |
|---|---|---|---|---|
| RS-01 | RS UMS A.R. Fachrudin | Perangkat lunak | [rs-01/](rs-01/README.md) | Data jadwal publik `/api/jadwal` bisa dipakai purwarupa |
| ARB-01 | CV Arbain Jaya Mandiri | Perangkat lunak (AI agent) | [arb-01/](arb-01/README.md) | Audit visibilitas AI bisa dikerjakan sebelum 20 Okt |
| ARB-02 | CV Arbain Jaya Mandiri | Perangkat lunak (web/mobile) | [arb-02/](arb-02/README.md) | Perlu pembeda *deeptech* agar bukan CRUD biasa |
| LKPI-01 | PT Likuid Pharmalab Indonesia | Formulasi | [lkpi-01/](lkpi-01/README.md) | KI formula milik penuh LKPI; fase 4–5 pakai desain eksperimen |
| LKPI-02 | PT Likuid Pharmalab Indonesia | Perangkat keras | [lkpi-02/](lkpi-02/README.md) | Fokus awal pompa 20 ml; KI milik tim + royalti |
| UMS-01 | DPM DRPPS UMS | Perangkat lunak (AI/data) | [ums-01/](ums-01/README.md) | Data katalog iHub sudah tersedia untuk demo |

## Navigasi cepat

| Proyek | README | 1 Empathize | 2 Define | 3 Ideate | 4 Prototype | 5 Test | 6 Implement | Proposal | Mitra |
|---|---|---|---|---|---|---|---|---|---|
| RS-01 | [▸](rs-01/README.md) | [▸](rs-01/01-empathize.md) | [▸](rs-01/02-define.md) | [▸](rs-01/03-ideate.md) | [▸](rs-01/04-prototype.md) | [▸](rs-01/05-test.md) | [▸](rs-01/06-implement.md) | [▸](rs-01/proposal-draf.md) | [RS UMS](../docs/mitra/rs-ums-ar-fachrudin.md) |
| ARB-01 | [▸](arb-01/README.md) | [▸](arb-01/01-empathize.md) | [▸](arb-01/02-define.md) | [▸](arb-01/03-ideate.md) | [▸](arb-01/04-prototype.md) | [▸](arb-01/05-test.md) | [▸](arb-01/06-implement.md) | [▸](arb-01/proposal-draf.md) | [CV Arba'in](../docs/mitra/cv-arbain.md) |
| ARB-02 | [▸](arb-02/README.md) | [▸](arb-02/01-empathize.md) | [▸](arb-02/02-define.md) | [▸](arb-02/03-ideate.md) | [▸](arb-02/04-prototype.md) | [▸](arb-02/05-test.md) | [▸](arb-02/06-implement.md) | [▸](arb-02/proposal-draf.md) | [CV Arba'in](../docs/mitra/cv-arbain.md) |
| LKPI-01 | [▸](lkpi-01/README.md) | [▸](lkpi-01/01-empathize.md) | [▸](lkpi-01/02-define.md) | [▸](lkpi-01/03-ideate.md) | [▸](lkpi-01/04-prototype.md) | [▸](lkpi-01/05-test.md) | [▸](lkpi-01/06-implement.md) | [▸](lkpi-01/proposal-draf.md) | [PT LKPI](../docs/mitra/pt-lkpi.md) |
| LKPI-02 | [▸](lkpi-02/README.md) | [▸](lkpi-02/01-empathize.md) | [▸](lkpi-02/02-define.md) | [▸](lkpi-02/03-ideate.md) | [▸](lkpi-02/04-prototype.md) | [▸](lkpi-02/05-test.md) | [▸](lkpi-02/06-implement.md) | [▸](lkpi-02/proposal-draf.md) | [PT LKPI](../docs/mitra/pt-lkpi.md) |
| UMS-01 | [▸](ums-01/README.md) | [▸](ums-01/01-empathize.md) | [▸](ums-01/02-define.md) | [▸](ums-01/03-ideate.md) | [▸](ums-01/04-prototype.md) | [▸](ums-01/05-test.md) | [▸](ums-01/06-implement.md) | [▸](ums-01/proposal-draf.md) | [DPM DRPPS](../docs/mitra/dpm-drpps-ums.md) |
| Template | [▸](_template/README.md) | [▸](_template/01-empathize.md) | [▸](_template/02-define.md) | [▸](_template/03-ideate.md) | [▸](_template/04-prototype.md) | [▸](_template/05-test.md) | [▸](_template/06-implement.md) | [▸](_template/proposal-draf.md) | — |

**Ringkasan PDF untuk brainstorming** (maks. 2 halaman A4, data awal → ide → pertanyaan → kotak catatan sesi): [RS-01](rs-01/ringkasan-brainstorming-rs-01.pdf) · [ARB-01](arb-01/ringkasan-brainstorming-arb-01.pdf) · [ARB-02](arb-02/ringkasan-brainstorming-arb-02.pdf) · [LKPI-01](lkpi-01/ringkasan-brainstorming-lkpi-01.pdf) · [LKPI-02](lkpi-02/ringkasan-brainstorming-lkpi-02.pdf) · [UMS-01](ums-01/ringkasan-brainstorming-ums-01.pdf). Dibuat ulang dengan `python3 proyek/buat-ringkasan-pdf.py`; isinya ada di script itu, jadi perbarui script bila file fase berubah.

**Dokumen lengkap PDF** (tanpa batas halaman: profil mitra & temuan situs → identitas → fase 1–6 → draf proposal): [RS-01](rs-01/dokumen-lengkap-rs-01.pdf) · [ARB-01](arb-01/dokumen-lengkap-arb-01.pdf) · [ARB-02](arb-02/dokumen-lengkap-arb-02.pdf) · [LKPI-01](lkpi-01/dokumen-lengkap-lkpi-01.pdf) · [LKPI-02](lkpi-02/dokumen-lengkap-lkpi-02.pdf) · [UMS-01](ums-01/dokumen-lengkap-ums-01.pdf). Diambil langsung dari file `.md`; perbarui dengan `python3 proyek/buat-dokumen-lengkap-pdf.py` (atau `... rs-01` untuk satu proyek).

Setiap file juga punya bilah navigasi di atas (semua tahap di proyek itu + referensi) dan di bawah (tahap sebelum/sesudah + tahap yang sama di proyek lain).

## Isi setiap folder

| File | Sudah terisi | Diisi tim |
|---|---|---|
| `README.md` | Identitas, indikator mitra, ketentuan KI, status fase | Nama tim, kategori, TKT, log keputusan |
| `01-empathize.md` | Ringkasan riset sekunder, asumsi awal, rencana riset, pertanyaan wawancara, empathy map & proto-persona awal, pain points | Catatan wawancara/observasi, validasi persona |
| `02-define.md` | Draf user stories, journey map, 5W+H, problem/need statement, kriteria keberhasilan, hipotesis, value proposition, pertanyaan untuk mitra | Konfirmasi dengan data primer |
| `03-ideate.md` | HMW, competitive audit awal, kandidat ide, usulan inti, goal statement | Crazy 8s, penilaian dan pemilihan ide, rancangan solusi |
| `04-prototype.md` | Daftar bukti Lampiran C, fungsi inti draf | Kategori, TKT, rancangan, purwarupa |
| `05-test.md` | Rencana uji, metrik, skenario uji | Hasil uji, temuan, retrospektif |
| `06-implement.md` | Dukungan mitra, regulasi, ketentuan KI, model bisnis draf, usulan *milestone* | Biaya, rencana kegiatan final |
| `proposal-draf.md` | Tema, draf bagian 4.1 (masalah) dan 4.6 (dukungan mitra) | Bagian lain setelah fase 1–3 selesai |

Batas pengajuan final proposal: **20 Oktober 2026, 23.59 WIB**.
