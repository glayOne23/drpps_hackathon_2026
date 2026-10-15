# UMS Health Innovation Hackathon 2026 — Bahan Tim

Repositori bahan kerja tim untuk **UMS Health Innovation Hackathon 2026**: riset kebutuhan mitra, aturan program, template proposal, dan folder kerja per tantangan yang disusun dengan *design thinking*.

> **Batas pengajuan final proposal: 20 Oktober 2026, 23.59 WIB** · Pendaftaran: https://ihub.ums.ac.id/hackathon/daftar

---

## Mulai dari mana?

| Kalau Anda ingin ... | Buka |
|---|---|
| Memahami keenam tantangan dan memilih satu | [docs/01-kebutuhan-mitra.md](docs/01-kebutuhan-mitra.md) |
| Membaca bahan brainstorming singkat (2 halaman) | PDF ringkasan di [proyek/](proyek/README.md#navigasi-cepat) |
| Membaca semua bahan satu tantangan sekaligus | PDF dokumen lengkap di [proyek/](proyek/README.md#navigasi-cepat) |
| Mengetahui aturan tim, penilaian, jadwal, hadiah | [docs/02-ketentuan-program.md](docs/02-ketentuan-program.md) |
| Menulis proposal | [docs/03-template-proposal.md](docs/03-template-proposal.md) + `proposal-draf.md` di folder proyek |
| Membagi peran dalam tim | [docs/04-peran-tim.md](docs/04-peran-tim.md) |
| Mengerjakan tantangan yang dipilih | Folder proyek, mis. [proyek/rs-01/](proyek/rs-01/README.md) |

## Tantangan

| Kode | Mitra | Tantangan | Folder kerja |
|---|---|---|---|
| RS-01 | RS UMS A.R. Fachrudin | Sistem cerdas jadwal dokter, notifikasi pasien, interoperabilitas RS | [proyek/rs-01](proyek/rs-01/README.md) |
| ARB-01 | CV Arbain Jaya Mandiri | Agen AI pemasaran, penjualan B2B, dan optimasi SEO AI | [proyek/arb-01](proyek/arb-01/README.md) |
| ARB-02 | CV Arbain Jaya Mandiri | CRM terpadu: pelanggan B2B, aktivitas sales, stok | [proyek/arb-02](proyek/arb-02/README.md) |
| LKPI-01 | PT Likuid Pharmalab Indonesia | Formulasi disinfektan H₂O₂ beraroma | [proyek/lkpi-01](proyek/lkpi-01/README.md) |
| LKPI-02 | PT Likuid Pharmalab Indonesia | Otomasi produksi / penakaran presisi sediaan cair | [proyek/lkpi-02](proyek/lkpi-02/README.md) |
| UMS-01 | DPM DRPPS UMS | Pendukung komersialisasi produk kesehatan hasil riset UMS | [proyek/ums-01](proyek/ums-01/README.md) |

## Struktur repositori

```
.
├── README.md                     ← panduan ini
├── docs/                         ← REFERENSI: hasil riset, jarang berubah
│   ├── README.md                 ← indeks dokumen + daftar kode sumber
│   ├── 01-kebutuhan-mitra.md     ← ringkasan 4 mitra & 6 tantangan
│   ├── 02-ketentuan-program.md   ← tim, kategori, rubrik, jadwal, dana
│   ├── 03-template-proposal.md   ← template resmi + petunjuk isian + checklist
│   ├── 04-peran-tim.md           ← tugas 4 koordinator per tahap
│   └── mitra/                    ← detail per mitra (profil, temuan situs, tantangan)
├── proyek/                       ← KERJA TIM: satu folder per tantangan
│   ├── README.md                 ← indeks + tautan cepat + daftar PDF
│   ├── _template/                ← kerangka kosong + panduan metode tiap fase
│   ├── rs-01/ … ums-01/          ← 6 fase design thinking + draf proposal + 2 PDF
│   ├── perbarui-navigasi.py      ← memperbarui bilah navigasi antar-file
│   ├── buat-ringkasan-pdf.py     ← PDF ringkasan 2 halaman
│   └── buat-dokumen-lengkap-pdf.py ← PDF dokumen lengkap
└── referensi/                    ← sumber asli: pedoman, template, transkrip sosialisasi
```

Setiap folder proyek berisi:

| File | Isi |
|---|---|
| `README.md` | Identitas tantangan, indikator mitra, status fase, log keputusan |
| `01-empathize.md` … `06-implement.md` | Enam fase: Empathize → Define → Ideate → Prototype → Test → Implement |
| `proposal-draf.md` | Draf substansi proposal, dipetakan ke file fase |
| `ringkasan-brainstorming-<kode>.pdf` | Ringkasan 2 halaman untuk sesi brainstorming |
| `dokumen-lengkap-<kode>.pdf` | Semua isi proyek + profil mitra dalam satu PDF |

Setiap file proyek punya **bilah navigasi** di atas (semua tahap di proyek itu) dan di bawah (tahap sebelum/sesudah + tahap yang sama di proyek lain).

## Cara membaca isi

Hampir semua isi saat ini adalah **draf dari riset sekunder** (pedoman, laman tantangan, transkrip sosialisasi, situs mitra), dan belum dikonfirmasi langsung ke pengguna. Setiap klaim diberi tanda:

| Tanda | Arti |
|---|---|
| `[sumber: X]` | Dari sumber sekunder. X = kode sumber: **P** pedoman, **W** laman tantangan, **S** sosialisasi 7 Okt, **R** situs RS, **A** situs CV Arbain, **L** situs PT LKPI, **H** UMS Innovation Hub ([daftar lengkap](docs/README.md#sumber)) |
| `[asumsi]` | Dugaan tim; belum dikonfirmasi |
| `[tervalidasi: sumber, tanggal]` | Sudah dikonfirmasi lewat wawancara/observasi/data mitra |
| `[target]` | Hasil yang ingin dicapai |

Sebelum menulis klaim di proposal sebagai fakta, pastikan tandanya sudah `[tervalidasi: ...]` atau `[sumber: ...]`.

## Cara berkontribusi

1. **Edit file `.md` langsung**, baik di GitHub (ikon pensil) maupun di komputer. Satu tahap = satu file, jadi anggota tim bisa bekerja di file berbeda tanpa bentrok.
2. **Ubah tanda klaim** setelah dikonfirmasi, mis. `[asumsi]` → `[tervalidasi: wawancara admisi, 22 Okt]`.
3. **Catat keputusan penting** di tabel *Log keputusan* pada `README.md` proyek, dan perbarui kolom status fase (☐ belum · ◐ sebagian · ☑ selesai).
4. **Jangan mengedit teks di antara penanda** `<!-- nav:start -->` … `<!-- nav:end -->` dan `<!-- nav-bottom:... -->`. Bagian itu dibuat ulang oleh script.
5. **Commit kecil dengan pesan jelas**, mis. `rs-01: catatan wawancara admisi (P1–P2)`.
6. Untuk tantangan baru atau percobaan lain, salin `proyek/_template/` lalu tambahkan foldernya ke daftar di `proyek/perbarui-navigasi.py`.

## Privasi dan data

- **Jangan commit data pribadi:** nama atau nomor pasien, data medis, rekaman wawancara, atau data pelanggan mitra. Di repo cukup catatan yang sudah dianonimkan (mis. "P1 — petugas admisi").
- File audio/video dan folder `proyek/*/data-mentah/` serta `proyek/*/rekaman/` sudah diabaikan oleh `.gitignore`. Simpan bahan mentah di drive tim yang aksesnya terbatas.
- Informasi rahasia dari mitra (formula, data internal) hanya boleh dibagikan sesuai izin mitra (pakta integritas, butir kerahasiaan).
- **Sebaiknya repo ini dibuat *private*.** Folder `referensi/` berisi transkrip sosialisasi yang menyebut nama peserta dan mitra, serta catatan kursus pribadi. Bila repo harus publik, aktifkan baris "Opsional" di `.gitignore` sebelum push pertama.

## Membuat ulang navigasi dan PDF (opsional)

Hanya diperlukan bila ada perubahan struktur atau Anda ingin PDF terbaru. Membaca dan mengedit `.md` tidak memerlukan langkah ini.

**Kebutuhan:** Python 3, paket `markdown`, [WeasyPrint](https://weasyprint.org/), font Noto Sans.

```bash
# Ubuntu/Debian
sudo apt install python3-markdown weasyprint fonts-noto-core

# dari folder utama repositori
python3 proyek/perbarui-navigasi.py              # bilah navigasi semua file proyek
python3 proyek/buat-dokumen-lengkap-pdf.py       # PDF lengkap semua proyek (langsung dari .md)
python3 proyek/buat-dokumen-lengkap-pdf.py rs-01 # PDF lengkap satu proyek
python3 proyek/buat-ringkasan-pdf.py             # PDF ringkasan 2 halaman
```

- **PDF lengkap** selalu mengikuti isi `.md` terbaru.
- **PDF ringkasan** isinya ditulis di dalam script `buat-ringkasan-pdf.py`, jadi perbarui data di script itu bila isi fase berubah.

## Kanal resmi

- Informasi program: https://ihub.ums.ac.id/hackathon
- Pedoman peserta: https://ums.id/PEDOMANUMSHIHACK26
- Template proposal: https://ums.id/PROPOSALUMSHIHACK26
- Email panitia: umsihub.official@gmail.com
