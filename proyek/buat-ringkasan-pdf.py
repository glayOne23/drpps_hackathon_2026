"""Buat PDF ringkasan brainstorming (maks. 2 halaman A4) untuk tiap proyek.

Jalankan:  python3 proyek/buat-ringkasan-pdf.py
Hasil:     proyek/<kode>/ringkasan-brainstorming-<kode>.pdf
Butuh:     weasyprint (CLI), font Noto Sans.

Isi diringkas dari file 01–03 tiap proyek (per 15 Okt 2026). Bila file fase berubah,
perbarui data di bawah lalu jalankan ulang.
"""
import html, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TANGGAL = "15 Oktober 2026"


def e(s):
    """Escape HTML, lalu ubah tanda sumber [X] menjadi label kecil dan H2O2 menjadi subskrip."""
    s = html.escape(s.replace("`", ""))
    s = re.sub(r"\[([PWSRALH](?:, [PWSRALH])*)\]", r'<span class="src">\1</span>', s)
    s = s.replace("[asumsi]", '<span class="src asm">asumsi</span>')
    s = s.replace("H2O2", "H<sub>2</sub>O<sub>2</sub>")
    s = s.replace("**", "\x00")
    parts = s.split("\x00")
    return "".join(f"<b>{p}</b>" if i % 2 else p for i, p in enumerate(parts))


def ul(items):
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ol>"


def table(head, rows, cls=""):
    h = "".join(f"<th>{e(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


CSS = """
@page { size: A4; margin: 11mm 12mm 12mm 12mm;
  @bottom-left { content: "UMS HI Hackathon 2026 · Bahan brainstorming · " string(kode); font: 7pt 'Noto Sans'; color:#777 }
  @bottom-right { content: "hlm. " counter(page) " / " counter(pages); font: 7pt 'Noto Sans'; color:#777 } }
* { box-sizing: border-box }
body { font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; font-size: 8.1pt; line-height: 1.28; color:#1d232a; margin:0 }
.kode { string-set: kode content() }
header { border-bottom: 2px solid #1f5f99; padding-bottom: 4px; margin-bottom: 6px }
header .top { display:flex; justify-content:space-between; font-size:7.5pt; color:#1f5f99; font-weight:700; letter-spacing:.02em }
header h1 { font-size: 12.5pt; margin: 2px 0 2px; line-height:1.2 }
header .meta { font-size: 7.6pt; color:#444 }
h2 { font-size: 9pt; color:#fff; background:#1f5f99; padding:2px 6px; margin: 7px 0 4px; border-radius:2px }
h3 { font-size: 8.4pt; margin: 4px 0 2px; color:#1f5f99 }
ul, ol { margin: 0 0 2px 0; padding-left: 13px } li { margin: 0 0 1.3px }
table { width:100%; border-collapse: collapse; margin: 1px 0 3px; font-size: 7.7pt }
th { background:#e6eef6; text-align:left; padding:2px 4px; border:1px solid #c9d6e3; font-weight:700 }
td { padding:2px 4px; border:1px solid #d9e1e9; vertical-align: top }
.src { display:inline-block; font-size:6pt; font-weight:700; color:#1f5f99; background:#e6eef6; border-radius:2px; padding:0 2px; margin-left:1px; line-height:1.15; vertical-align: 1px }
.asm { color:#8a5a00; background:#fbefd7 }
.cols { display:flex; gap: 10px } .cols > div { flex:1; min-width:0 }
.box { border-left: 3px solid #1f5f99; background:#f4f7fa; padding: 3px 6px; margin: 2px 0 4px }
.persona { border:1px solid #d9e1e9; border-radius:3px; padding:3px 5px; margin-bottom:3px }
.persona b { color:#1f5f99 }
.note { font-size:7pt; color:#555; margin-top:3px }
.ide td:first-child { white-space:nowrap; font-weight:700; color:#1f5f99 }
.ide td:nth-child(4), .ide td:nth-child(5) { white-space:nowrap }
.pb { break-before: page }
.catat { border:1px dashed #9fb3c8; border-radius:3px; padding:3px 6px; color:#7a8794; font-size:7pt; height: var(--h, 40mm) }
.catat .baris { display:flex; gap:10px } .catat .baris div { flex:1 }
"""


def render(p):
    personas = "".join(f'<div class="persona"><b>{e(n)}</b> — {e(d)}</div>' for n, d in p["persona"])
    h = f"""<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{p['kode']} · Ringkasan brainstorming</title><style>{CSS}</style></head><body>
<header><div class="top"><span class="kode">{p['kode']}</span><span>Ringkasan untuk brainstorming · {TANGGAL}</span></div>
<h1>{e(p['judul'])}</h1>
<div class="meta"><b>Mitra:</b> {e(p['mitra'])} · <b>Jenis solusi:</b> {e(p['jenis'])} · <b>KI:</b> {e(p['ki'])}</div></header>

<h2>1. Data awal</h2>
<div class="cols"><div><h3>Profil dan konteks mitra</h3>{ul(p['profil'])}</div>
<div><h3>Kondisi saat ini dan temuan data</h3>{ul(p['data'])}</div></div>

<h2>2. Pengguna dan masalah</h2>
<div class="cols"><div><h3>Pain points</h3>{table(['Kategori','Pain point'], p['pain'])}</div>
<div><h3>Proto-persona (belum divalidasi)</h3>{personas}</div></div>
<h3>Rumusan masalah (draf)</h3>
<div class="box"><b>Problem statement:</b> {e(p['problem'])}</div>
<div class="box"><b>Need statement:</b> {e(p['need'])}</div>

<h2>3. Target dan batasan dari mitra</h2>
<div class="cols"><div>{table(['Kriteria keberhasilan','Target'], p['kriteria'])}</div>
<div><h3>Batasan</h3>{ul(p['batasan'])}<h3>Dukungan mitra</h3>{ul(p['dukungan'])}</div></div>

<h2 class="pb">4. Ide</h2>
{table(['Kode','Ide','Inti cara kerja','Upaya','Peran'], p['ide'], 'ide')}
<h3>Paket solusi untuk dibahas</h3>
{table(['Paket','Isi','Kekuatan','Risiko'], p['paket'])}

<div class="cols"><div><h2>5. Pertanyaan pemandu brainstorming</h2>{ol(p['tanya'])}</div>
<div><h2>6. Pertanyaan untuk mitra</h2>{ul(p['mitra_q'])}</div></div>
<h2>7. Catatan sesi brainstorming</h2>
<div class="catat" style="--h:{p.get('catat','68mm')}"><div class="baris"><div>Ide/paket yang dipilih: ______________________</div><div>Alasan: ______________________</div></div>
<div class="baris" style="margin-top:4px"><div>Ide baru dari diskusi:</div><div>Yang perlu dicek ke mitra minggu ini:</div></div></div>
<div class="note">Sumber: <span class="src">P</span> Pedoman · <span class="src">W</span> laman tantangan · <span class="src">S</span> sosialisasi 7 Okt · <span class="src">R</span>/<span class="src">A</span>/<span class="src">L</span>/<span class="src">H</span> situs RS / CV Arbain / PT LKPI / iHub · <span class="src asm">asumsi</span> dugaan tim. Upaya: Rendah = beberapa jam, Sedang = ±1 hari, Tinggi = butuh data/akses baru atau &gt; 3 hari. Detail lengkap: proyek/{p['folder']}/ (01-empathize, 02-define, 03-ideate).</div>
</body></html>"""
    return h


PROYEK = [
 dict(folder="rs-01", kode="RS-01",
  judul="Sistem Cerdas Manajemen Jadwal Dokter, Otomatisasi Notifikasi Pasien, dan Interoperabilitas Layanan RS",
  mitra="RS UMS A.R. Fachrudin (Laweyan, Surakarta)", jenis="Perangkat lunak", ki="tidak disebut — tanyakan",
  profil=["RS baru milik UMS: IGD 24 jam, rawat jalan, rawat inap (37 tempat tidur), laboratorium, kamar operasi [R]",
          "32 tenaga medis, 18 spesialisasi, 103 slot praktik per minggu [R]",
          "Dokter spesialis terbatas dan praktik di 2–3 tempat (SIP hingga 3 tempat); sering tertahan kasus cito [S]",
          "Narasumber: Humas & Marketing RS [S]"],
  data=["Jadwal berubah mendadak **hampir setiap hari** [W]",
        "Pemberitahuan dan reschedule manual oleh petugas lewat WhatsApp [W]",
        "Pasien reservasi H-1 tetap tidak terinfo karena jarang membuka HP [S]",
        "API jadwal situs (`/api/jadwal`) hanya pola mingguan: **tanpa tanggal, status, atau pengganti** [R]",
        "\"Pendaftaran online\" = tautan WhatsApp; belum ada booking/antrean/akun pasien [R]",
        "54 dari 103 slot mulai ≥ 13.00; 13 dari 32 dokter hanya 1–2 slot/minggu [R]",
        "Data janggal di jadwal (slot \"00:00–00:04\") — belum ada validasi [R]",
        "Dampak: pasien menunggu lama, kepuasan turun, ulasan negatif publik [W, S]"],
  pain=[["Produk","Sistem jadwal tidak bisa menyatakan perubahan harian [R]"],
        ["Proses","Admisi mengabari pasien satu per satu; daftar pasien per slot tidak digital [W, R]"],
        ["Proses","Kabar dari dokter ke unit lain lambat/terputus [W]"],
        ["Dukungan","Pasien tidak terjangkau; 3 nomor WA terpisah [S, R]"],
        ["Finansial","Waktu dan biaya perjalanan pasien terbuang [asumsi]"]],
  persona=[("Bu Sri, petugas admisi","mengelola pendaftaran via WA; butuh mengabari semua pasien terdampak sekaligus dan tahu siapa yang belum terjangkau [asumsi]"),
           ("Pak Harjo, pasien lansia","kontrol rutin, jarang membuka HP; butuh kabar lewat kanal yang pasti sampai (telepon/SMS/anak) [asumsi]"),
           ("Mbak Dina, pasien pekerja","izin kerja untuk periksa; butuh kabar cepat dan bisa pilih jadwal pengganti sendiri [asumsi]")],
  problem="Pak Harjo adalah pasien lansia yang kontrol rutin dan jarang membuka HP, yang membutuhkan kabar perubahan jadwal dokter yang pasti sampai sebelum berangkat, karena pemberitahuan WhatsApp manual sering tidak terbaca sehingga ia datang dan menunggu sia-sia.",
  need="Cara untuk memastikan pasien rawat jalan spesialis mengetahui perubahan jadwal dokter sebelum berangkat, termasuk yang jarang membuka HP, sehingga kedatangan sia-sia dan komplain berkurang.",
  kriteria=[["Notifikasi terkirim sejak status diperbarui","< 1 menit [W]"],
            ["Beban manual admisi","turun signifikan [W]"],
            ["Pasien terjangkau sebelum jam praktik","[ ]% — usulan tim"],
            ["Pasien bisa konfirmasi/reschedule sendiri","mudah [W]"],
            ["Rancangan integrasi","kompatibel SIMRS/SATUSEHAT [W]"]],
  batasan=["Wajib sesuai KODERSI dan perlindungan data pasien (UU PDP) [W]",
           "Arsitektur terbuka, modular, tidak terkunci satu vendor [W]",
           "Kebutuhan RS lebih sederhana dari SIMRS lengkap — fokus notifikasi dulu [S]"],
  dukungan=["Diskusi dengan Humas & manajemen; skenario kasus nyata; uji purwarupa di RS [W]"],
  ide=[["I1","Lapisan pengecualian jadwal","Status harian per slot (terlambat/batal/pengganti) di atas pola mingguan; memicu notifikasi","Rendah","Inti (fondasi)"],
       ["I2","Lapor status 1 ketukan","Dokter/perawat poli menekan tombol di WA/tautan sebelum praktik","Rendah–Sedang","Inti"],
       ["I3","Notifikasi multi-kanal + eskalasi","WA → SMS → panggilan suara otomatis → kontak keluarga bila belum dibaca","Sedang","Inti"],
       ["I4","Dashboard admisi","Status terkirim/dibaca/dikonfirmasi per pasien; telepon hanya yang belum","Rendah–Sedang","Inti"],
       ["I5","Reschedule mandiri","Tautan di pesan: tetap menunggu / pindah slot / dokter pengganti / batal","Sedang","Pendukung"],
       ["I6","Booking sederhana","Formulir/bot pendaftaran yang menyimpan daftar pasien per slot (atau ambil dari SIMRS)","Rendah","Prasyarat"],
       ["I7","Prediksi keterlambatan","Model dari riwayat per dokter/slot; awalnya untuk internal; data simulasi saat demo","Tinggi","Deeptech"],
       ["I8","Umpan balik pasien","Survei singkat; skor rendah diteruskan ke humas sebelum jadi ulasan publik","Rendah","Pendukung"],
       ["I9","Desain konektor SATUSEHAT/BPJS","Arsitektur modular FHIR + antrean BPJS (desain, bukan implementasi)","Sedang","Desain"],
       ["I10","Validasi data jadwal","Cegah jam mustahil/bentrok saat input","Rendah","Pendukung"]],
  paket=[["A · Minimum","I6 + I1 + I2 + I3 + I4","Alur ujung-ke-ujung kuat, realistis 3 hari","Kurang unsur deeptech"],
         ["B · Disarankan","A + I5 + I10 + I9 + I7 (simulasi)","Lengkap sesuai arah mitra; ada pembeda teknologi","Beban kerja tinggi"],
         ["C · Ambisius","B + I8 + integrasi SIMRS nyata","Paling dekat ke penerapan","Bergantung akses SIMRS"]],
  tanya=["Mana masalah lebih besar: RS terlambat tahu, atau pasien tidak terjangkau?",
         "Bisakah daftar pasien per slot didapat dari RS, atau I6 wajib dibangun?",
         "Bagaimana menjangkau pasien lansia tanpa melanggar privasi?",
         "Unsur deeptech apa yang paling meyakinkan juri?",
         "Berapa biaya komunikasi per bulan yang wajar bagi RS?"],
  mitra_q=["SIMRS apa yang dipakai; terhubung dengan /api/jadwal?",
           "Di mana pasien per slot tercatat sekarang?",
           "Berapa kejadian perubahan jadwal per minggu dan berapa menit sebelum praktik diketahui?",
           "Ada WhatsApp Business API resmi? Sudah terhubung Mobile JKN?",
           "Ketentuan KI tantangan ini?"]),

 dict(folder="arb-01", kode="ARB-01",
  judul="Agen AI untuk Otomatisasi Pemasaran, Penjualan B2B, dan Optimasi SEO AI",
  mitra="CV Arbain Jaya Mandiri (Mojosongo, Surakarta)", jenis="Perangkat lunak (agen AI/LLM)", ki="tidak disebut — tanyakan",
  profil=["Produsen dan jasa maklon herbal, madu, kosmetik; standar CPOTB-BPOM; mengurus izin BPOM/Halal/HKI untuk klien [A]",
          "Penjualan B2B ke apotek, toko obat, minimarket [S]; klien maklon dari berbagai kota [A]",
          "12 kategori maklon, 16 produk grosir; semua kontak lewat satu nomor WhatsApp [A]",
          "Sudah mitra inovasi UMS (Sampo Herbal 4H) [H]"],
  data=["Branding, marketing, selling masih manual: analisis pesaing, konten, gambar/video, iklan, balas chat [S]",
        "Kalah di Google dan AI; pencari maklon beralih ke AI; respons ke pembeli sering terlambat; penjualan di bawah target [S]",
        "Blog: **6.841 artikel** — 6.216 terbit pada 2025 (±17/hari), judul sangat mirip; terakhir terbit 28 Jul 2026 [A]",
        "Dugaan: masalahnya kualitas/keunikan konten, bukan jumlah [asumsi]",
        "Deskripsi produk grosir memuat klaim kesehatan (mis. \"untuk penderita diabetes & kolesterol\") [A]",
        "Mitra ingin agen AI sebagai \"digital team\" 24 jam; manusia tetap memegang negosiasi; tanpa menambah karyawan [S]"],
  pain=[["Finansial","Penjualan di bawah target; tidak bisa menambah karyawan [S]"],
        ["Produk","Konten banyak tetapi merek tidak tampil di Google/AI [A, S]"],
        ["Proses","Konten, iklan, balasan chat manual dan tidak konsisten [S]"],
        ["Dukungan","Calon pembeli menunggu balasan; satu nomor WA untuk semua [S, A]"]],
  persona=[("Pak Karno, pemilik","ingin penjualan naik tanpa menambah karyawan; tetap memegang negosiasi [asumsi]"),
           ("Mbak Ani, admin marketing & chat","pekerjaan berulang; butuh draf konten siap pakai dan balasan otomatis [asumsi]"),
           ("Mas Rizal, calon pemilik merek","mencari maklon lewat Google/AI; butuh jawaban cepat soal MOQ, legalitas, biaya [asumsi]")],
  problem="Mbak Ani adalah admin marketing tunggal di produsen maklon herbal skala UMKM, yang membutuhkan cara menghasilkan konten yang membuat merek tampil di Google dan AI sekaligus menjawab pertanyaan rutin otomatis, karena ia tidak sempat konsisten dan konten massal yang ada tidak menaikkan visibilitas.",
  need="Cara untuk meningkatkan visibilitas dan kecepatan respons pemasaran B2B pada produsen maklon herbal dengan SDM pemasaran terbatas, sehingga prospek dan konversi naik tanpa menambah karyawan.",
  kriteria=[["Efisiensi waktu membuat konten","turun [W]"],
            ["Akurasi jawaban agen, 24 jam","≥ [ ]% [W]"],
            ["Waktu respons pertama","< 1 menit — usulan tim"],
            ["Penyebutan merek di mesin AI","naik dari baseline [W]"],
            ["Klaim berlebihan yang lolos","0 [W]"]],
  batasan=["Mudah dioperasikan UMKM; perawatan rendah [W]",
           "Patuh regulasi klaim produk kesehatan/herbal [W]",
           "Biaya API/model AI efisien dan terjangkau [W]"],
  dukungan=["Diskusi proses bisnis dengan direksi dan tim pemasaran; katalog produk dan skenario penjualan [W]; materi PDF mitra [S]"],
  ide=[["I1","Agen penjawab B2B","WA bot + RAG atas katalog/MOQ/legalitas; kualifikasi prospek; serah ke admin","Sedang","Inti"],
       ["I2","Agen konten GEO/SEO","Halaman jawaban atas pertanyaan nyata + data terstruktur; ditinjau admin","Sedang","Inti"],
       ["I3","Pemeriksa klaim","Aturan + LLM menandai klaim berisiko dan mengusulkan perbaikan","Rendah–Sedang","Inti"],
       ["I4","Pemantau visibilitas AI","20–50 pertanyaan tetap ke mesin AI; catat penyebutan merek; baseline bisa dibuat sekarang","Rendah–Sedang","Inti (ukur)"],
       ["I5","Dashboard pemasaran","Prospek, eskalasi, waktu respons, konversi, biaya, visibilitas","Rendah","Inti"],
       ["I6","Agen analisis pesaing","Ringkasan mingguan aktivitas pesaing maklon","Sedang","Lanjutan"],
       ["I7","Agen pemetaan prospek","Cari calon B2B dari data publik + draf penawaran","Sedang–Tinggi","Lanjutan"],
       ["I8","Gambar/video + jadwal medsos","Kalender konten → draf → disetujui → terbit","Sedang","Lanjutan"],
       ["I9","Kurasi blog","Kelompokkan 6.841 artikel, tandai duplikat/tipis; bisa jadi bukti awal","Sedang","Pendukung"]],
  paket=[["A · Minimum","I1 + I3 + I5","Respons 24 jam aman; demo jelas","Tidak menyentuh visibilitas AI"],
         ["B · Disarankan","I1 + I2 + I3 + I4 + I5 (+ I9 bukti awal)","Menjawab dua keluhan utama dan terukur","Hasil visibilitas baru terlihat di pendampingan"],
         ["C · Ambisius","B + I6 + I7 + I8","Mendekati \"digital team\" yang diminta","Terlalu luas untuk 3 hari"]],
  tanya=["Mana lebih mendesak: respons cepat atau tampil di Google/AI?",
         "Bagaimana membuktikan kenaikan visibilitas AI dalam waktu singkat?",
         "Agen untuk klien maklon, outlet, atau keduanya?",
         "Apa batas yang tidak boleh dilewati agen (harga, janji, klaim)?",
         "Bagaimana menjaga biaya API terjangkau?"],
  mitra_q=["Apakah artikel 2025 dibuat otomatis? Mengapa berhenti Juli 2026?",
           "Kanal mana yang paling banyak mendatangkan pelanggan?",
           "Akun medsos/iklan aktif dan anggarannya?",
           "Batas biaya bulanan layanan AI?",
           "Boleh minta contoh chat (anonim) dan materi PDF?"]),

 dict(folder="arb-02", kode="ARB-02",
  judul="Sistem CRM Terpadu: Integrasi Data Pelanggan B2B, Aktivitas Sales, dan Manajemen Stok",
  mitra="CV Arbain Jaya Mandiri (Mojosongo, Surakarta)", jenis="Perangkat lunak (web/mobile)", ki="tidak disebut — tanyakan",
  profil=["Distribusi produk herbal/kesehatan B2B ke apotek, toko obat, minimarket [S]",
          "Dua segmen: klien maklon (siklus panjang) dan outlet (kunjungan → pesanan → pesan ulang) [A]",
          "16 produk grosir dan 12 kategori maklon — bahan katalog SKU awal [A]"],
  data=["Data pelanggan, sales, dan stok tersebar di buku catatan dan chat; manual, tercecer, tidak sinkron [S]",
        "Manajemen sulit memantau produktivitas sales, riwayat pesanan per outlet, dan akurasi stok [W]",
        "Semua prospek dari situs masuk ke satu nomor WA tanpa basis data; pesan templat sudah memuat jenis kebutuhan [A]",
        "Dampak: riwayat sulit ditelusuri, kinerja tidak terpantau, stok tidak sesuai gudang, peluang terlewat, stockout/overstock [S, W]",
        "Fitur yang diminta: aktivitas sales, data pelanggan, pengelolaan stok + peringatan stok menipis [S]"],
  pain=[["Finansial","Stok kosong/berlebih; peluang penjualan terlewat [S]"],
        ["Produk","Belum ada sistem terpusat [W]"],
        ["Proses","Input berulang di buku, chat, catatan gudang [S]"],
        ["Dukungan","Layanan pelanggan terlambat; riwayat sulit dicari [S]"]],
  persona=[("Mas Budi, sales lapangan","8–15 outlet/hari, sinyal sering hilang; butuh catat pesanan dalam detik dan cek stok [asumsi]"),
           ("Mbak Wati, admin gudang","butuh stok berkurang otomatis dan peringatan stok menipis [asumsi]"),
           ("Pak Karno, direktur","butuh dashboard kinerja tanpa mengumpulkan laporan manual [asumsi]")],
  problem="Mas Budi adalah sales lapangan yang mengunjungi banyak outlet dengan sinyal tidak stabil, yang membutuhkan cara mencatat kunjungan dan pesanan secepat mungkin sambil mengetahui stok yang benar, karena pencatatan di buku dan chat lambat, tidak sinkron dengan gudang, dan membuatnya menjanjikan barang yang ternyata kosong.",
  need="Cara untuk menyatukan data pelanggan, aktivitas sales, dan stok dalam satu sumber yang selalu mutakhir pada distributor herbal skala UMKM, sehingga selisih stok dan peluang yang terlewat berkurang.",
  kriteria=[["Data terhubung real-time tanpa input berulang","1 kali input [W]"],
            ["Waktu input pesanan di lapangan","hitungan detik [W]"],
            ["Selisih stok sistem vs fisik","turun [W]"],
            ["Kinerja sales harian/bulanan","terpantau tanpa laporan manual [W]"],
            ["Input offline tersinkron","100% — usulan tim"]],
  batasan=["Antarmuka sangat sederhana [W]",
           "Ringan dan andal pada jaringan seluler tidak stabil [W]",
           "Fokus operasional B2B; modul akuntansi rumit tidak termasuk [W]"],
  dukungan=["Konsultasi alur distribusi/penjualan/stok dengan manajemen; contoh format data (dummy) [W]"],
  ide=[["I1","Aplikasi sales offline-first","PWA: check-in kunjungan, pesanan dari SKU favorit outlet, sinkron saat online","Sedang","Inti"],
       ["I2","Stok otomatis + peringatan","Stok = masuk − pesanan dikonfirmasi; ambang per SKU; opsi batch/kedaluwarsa","Rendah–Sedang","Inti"],
       ["I3","Profil outlet","Kontak, lokasi, riwayat transaksi, catatan, jatuh tempo","Rendah","Inti"],
       ["I4","Dashboard manajemen","Kunjungan, pesanan, target, outlet aktif, perputaran stok","Rendah–Sedang","Inti"],
       ["I5","Rekomendasi pesan ulang","Perkiraan jarak pembelian per outlet/SKU → daftar outlet yang waktunya dikunjungi","Sedang","Deeptech"],
       ["I6","Tangkap prospek WA","Pesan templat dari situs → kartu prospek otomatis","Sedang","Pendukung"],
       ["I7","Input cepat","Pesan ulang 1 ketukan (Rendah); barcode (Sedang); suara (Tinggi)","Rendah–Tinggi","Pendukung"],
       ["I8","Migrasi data","Templat spreadsheet impor outlet/produk/stok","Rendah","Pendukung"],
       ["I9","Prediksi restock","Peramalan permintaan per SKU + waktu produksi","Sedang","Lanjutan"]],
  paket=[["A · Minimum","I1 + I2 + I3 + I4","Persis tiga fitur yang diminta mitra","Mudah dinilai \"aplikasi CRUD biasa\""],
         ["B · Disarankan","A + I5 + I7 (pesan ulang) + I8","Ada unsur cerdas; siap dipakai","I5 lemah tanpa data riwayat"],
         ["C · Ambisius","B + I6 + I9","Terhubung ke prospek WA dan produksi","Lingkup melebar"]],
  tanya=["Apa yang membuat solusi ini lebih dari aplikasi pencatatan di mata juri deeptech?",
         "Alur klien maklon ikut, atau cukup outlet?",
         "Seberapa parah sinyal di lapangan — offline wajib?",
         "Data apa yang bisa diminta minggu ini untuk demo?",
         "Bagaimana membuat sales mau memakai aplikasi?"],
  mitra_q=["Jumlah sales, outlet aktif, SKU, gudang?",
           "CRM juga untuk alur klien maklon?",
           "Ada sistem kasir/akuntansi yang harus disambungkan?",
           "Siapa yang menindaklanjuti chat WA dari situs?",
           "Boleh minta dummy data dan contoh nota?"]),

 dict(folder="lkpi-01", kode="LKPI-01",
  judul="Inovasi Formulasi Disinfektan dengan Karakteristik Aroma yang Sesuai Kebutuhan Pengguna",
  mitra="PT Likuid Pharmalab Indonesia (Baki, Sukoharjo)", jenis="Formulasi kimia/farmasi", ki="**formula milik penuh PT LKPI, tanpa royalti** [W]",
  profil=["Manufaktur antiseptik, disinfektan, BMHP; >40 produk; ISO 13485, CPAKB, Halal [L]",
          "Sudah punya **SASKLIN Disinfectant Spray**: benzalkonium klorida + H2O2, tanpa alkohol, **tanpa parfum**; izin PKD 20502120681 [L]",
          "Berpengalaman memberi parfum pada produk berbasis alkohol/benzalkonium klorida (SASKLIN Handwash, hand sanitizer) [L]"],
  data=["Sedang mengembangkan disinfektan **ruangan** berbasis H2O2 dengan parfum [S]",
        "Parfum = penanda sensorik bahwa ruangan sudah didisinfeksi + penutup bau zat aktif [S, W]",
        "Parfum, H2O2, dan surfaktan tidak kompatibel — tidak homogen; formula belum ditemukan [S]",
        "4 kendala: H2O2 termolabil (padahal uji stabilitas pakai suhu tinggi), parfum, surfaktan, homogenitas [S]",
        "Aroma cepat hilang atau justru mengganggu stabilitas zat aktif [W]",
        "Dugaan: produk baru dikembangkan dari basis SASKLIN Disinfectant [asumsi]"],
  pain=[["Produk","Formula tidak homogen; aroma hilang; zat aktif terganggu [S, W]"],
        ["Proses","Uji stabilitas suhu tinggi bertentangan dengan sifat termolabil H2O2 [S]"],
        ["Dukungan","Pengguna RS tidak punya penanda bahwa disinfeksi sudah dilakukan [W]"],
        ["Finansial","Waktu dan bahan R&D terbuang pada percobaan gagal [asumsi]"]],
  persona=[("Mas Agus, formulator R&D LKPI","butuh formula homogen dan stabil dengan dasar ilmiah, bahan ekonomis, lolos mutu internal [asumsi]"),
           ("Bu Ratna, petugas PPI/sanitasi RS","butuh disinfektan efektif dengan aroma penanda yang tidak menyengat dan tidak memicu iritasi [asumsi]")],
  problem="Mas Agus adalah formulator R&D produsen disinfektan rumah sakit, yang membutuhkan formula disinfektan ruangan berbasis H2O2 dengan parfum yang homogen dan stabil, karena parfum, oksidator, dan surfaktan yang dipakai memisah atau saling merusak sehingga tidak lolos uji stabilitas.",
  need="Cara untuk menggabungkan parfum yang tahan oksidasi ke dalam disinfektan ruangan berbasis H2O2 secara homogen dan stabil, sehingga kadar zat aktif dan efikasi terjaga sekaligus ada penanda aroma yang jelas.",
  kriteria=[["Homogenitas","tanpa pemisahan fase [W]"],
            ["Kadar H2O2 setelah uji stabilitas","tidak turun drastis — batas tanyakan [W]"],
            ["Aroma","stabil, jelas saat aplikasi [W]"],
            ["Uji stabilitas dipercepat + antimikroba","lulus standar LKPI [W]"],
            ["Data awal","organoleptik, pH, kejernihan, suhu [W]"]],
  batasan=["Perhitungkan zat aktif reaktif dan sensitif suhu [W]",
           "Aman untuk ruang medis: tanpa residu berbahaya, tidak iritasi pernapasan [W]"],
  dukungan=["Pendampingan R&D; parameter standar mutu; evaluasi formula di lab mitra [W]"],
  ide=[["I1","Solubilizer / surfaktan pelindung","Larutkan parfum dengan surfaktan nonionik pada beberapa rasio; cek kecocokan dengan BKC","Rendah","Inti"],
       ["I2","Enkapsulasi aroma","Kompleks siklodekstrin atau mikrokapsul; aroma lepas saat disemprot","Tinggi (siklodekstrin: Sedang)","Alternatif"],
       ["I3","Ko-solven, stabilizer, pH","Ko-solven untuk kelarutan; stabilizer peroksida + pH sedikit asam","Rendah–Sedang","Inti pendukung"],
       ["I4","Fragrance tahan oksidasi","Hindari komponen mudah teroksidasi; minta sampel parfum untuk produk berbahan oksidator","Rendah","Inti"],
       ["I5","Basis SASKLIN Disinfectant","Mulai dari formula BKC + H2O2 berizin; tinggal tambah sistem aroma","Rendah","Titik awal"],
       ["I6","Protokol uji stabilitas","Suhu sedang + suhu ruang paralel; ukur kadar H2O2 (titrasi) dan aroma per titik waktu","Sedang","Inti (metode)"],
       ["I7","Dua kompartemen","Parfum dan zat aktif terpisah sampai disemprot","Tinggi","Cadangan"],
       ["I8","Penanda non-aroma","Indikator warna yang memudar (eksplorasi)","Sedang","Diskusi"]],
  paket=[["A · Minimum","I5 + I4 + I1, diuji dengan I6","Cepat, fokus, realistis 3 hari","Bisa gagal bila semua parfum tetap terdegradasi"],
         ["B · Disarankan","A + I3, rancangan percobaan faktorial","Menyerang homogenitas dan stabilitas sekaligus","Jumlah batch bertambah"],
         ["C · Ambisius","B + I2 (siklodekstrin) pembanding","Ada rencana cadangan","Butuh bahan dan waktu lebih"]],
  tanya=["Boleh SASKLIN dijadikan basis? Apa beda produk baru?",
         "Apa yang realistis dibuktikan saat demo day: homogenitas + aroma, atau kadar H2O2?",
         "Ada akses lab (pH, titrasi, inkubator) sebelum hackathon?",
         "Tim menerima KI formula sepenuhnya milik LKPI?",
         "Aroma apa yang cocok untuk RS, dan bagaimana mengujinya?"],
  mitra_q=["Konsentrasi H2O2 target dan batas penurunan kadar?",
           "Metode aplikasi: semprot, fogging, atau lap?",
           "Surfaktan dan parfum yang sudah dicoba + hasilnya?",
           "Standar uji efikasi dan stabilitas; target masa simpan?",
           "Jalur izin edar: PKD/PKRT atau AKD?"]),

 dict(folder="lkpi-02", kode="LKPI-02",
  judul="Inovasi Peralatan Otomatisasi Produksi dan Sistem Penakaran Presisi (Precision Dosing) Sediaan Cair Medis",
  mitra="PT Likuid Pharmalab Indonesia (Baki, Sukoharjo)", jenis="Perangkat keras (mekanik/mekatronika)", ki="**milik tim inovator; royalti bila diadopsi LKPI** [W]",
  profil=["Manufaktur antiseptik, disinfektan, BMHP; ISO 13485, CPAKB; pelanggan RS di berbagai kota [L]",
          "**BAYzime** (detergen enzimatik): 1 L & 5 L; **20 ml per 2,5 L air**; izin AKD [L, W]",
          "**BAYcide HLD**: 1 L & 5 L; **20 ml per 1 L air** — takaran dan kemasan sama dengan BAYzime [L]",
          "Banyak produk lain dalam jeriken 5 L dan 20 L (relevan untuk opsi otomasi lini produksi) [L]"],
  data=["BAYzime dipakai di kamar operasi/CSSD untuk membersihkan instrumen bedah [W]",
        "Penakaran manual dengan gelas takar dari jeriken 5 L: sering tumpah, takaran tidak akurat [S, W]",
        "Belum ada dispenser dari jeriken ke takaran 20 ml [S]",
        "Opsi lain dari mitra: alat otomasi lini produksi sediaan cair [W]",
        "Fokus yang diusulkan: pompa/dispenser 20 ml di jeriken 5 L (lingkup paling jelas) [asumsi]",
        "RS UMS punya kamar operasi — calon lokasi uji [R]"],
  pain=[["Produk","Kemasan 5 L tanpa alat penakar [S]"],
        ["Proses","Menakar 20 ml dari jeriken berat dengan gelas takar sulit dan tidak akurat [S, W]"],
        ["Dukungan","Takaran tidak tepat bisa memengaruhi hasil reprosesing instrumen [asumsi]"],
        ["Finansial","Produk terbuang karena tumpah/berlebih [asumsi]"]],
  persona=[("Mas Dwi, petugas CSSD","menyiapkan larutan beberapa kali per shift dengan sarung tangan; butuh 20 ml satu gerakan tanpa tumpah [asumsi]"),
           ("Pak Hendro, packaging development LKPI","butuh alat yang pas jeriken yang ada, tahan kimia, murah diproduksi [asumsi]")],
  problem="Mas Dwi adalah petugas CSSD yang menyiapkan larutan detergen enzimatik beberapa kali per shift dengan sarung tangan, yang membutuhkan cara mengeluarkan tepat 20 ml dari jeriken 5 L tanpa tumpah, karena menuang ke gelas takar dari jeriken berat tidak akurat, berantakan, dan menambah langkah kerja.",
  need="Cara untuk menakar konsentrat pembersih dan disinfektan instrumen secara tepat dari kemasan 5 liter bagi petugas CSSD dan kamar operasi, sehingga deviasi takaran di bawah 5% dan tidak ada tumpahan.",
  kriteria=[["Deviasi volume terhadap 20 ml","< 5% [W]"],
            ["Tanpa alat ukur terpisah","mudah di lapangan [W]"],
            ["Kebocoran/tetesan","0 — usulan tim"],
            ["Tahan BAYzime dan BAYcide","tidak berubah — usulan tim"],
            ["Keluaran","purwarupa, CAD/3D, BoM, biaya, uji repeatability [W]"]],
  batasan=["Material tahan detergen enzimatik dan disinfektan H2O2 [W]",
           "Ergonomis, tidak bocor, 20 ml konsisten, ekonomis diproduksi [W]"],
  dukungan=["Pendampingan R&D, Technical Services, Packaging; sampel kemasan/spesifikasi; peluang lisensi/royalti [W]"],
  ide=[["I1","Pompa mekanis volume tetap","Piston dengan langkah terbatas + pegas + katup satu arah; adaptor ulir jeriken","Sedang","Inti"],
       ["I2","Katup anti-tetes","Katup duckbill/bola di nozzle; bahan diuji terhadap H2O2/enzim","Rendah","Wajib"],
       ["I3","Ruang takar gravitasi","Jeriken dibalik di dudukan; ruang 20 ml + katup isi/keluar","Sedang","Alternatif"],
       ["I4","Dispenser elektronik","Pompa peristaltik + mikrokontroler; volume terprogram","Sedang–Tinggi","Pembanding"],
       ["I5","Volume bisa diatur","Penyetel langkah 10/20/40 ml; satu desain untuk beberapa produk","Sedang","Pendukung"],
       ["I6","Tuas besar / pedal kaki","Mudah dengan sarung tangan; pedal membuat tangan bebas","Rendah–Sedang","Pendukung"],
       ["I7","Stasiun pengisian (opsi 1)","Sensor berat/aliran untuk mengisi jeriken sampai target","Tinggi","Alternatif fokus"]],
  paket=[["A · Minimum","I1 + I2 + adaptor jeriken","Fokus pada deviasi < 5%","Ergonomi belum teruji"],
         ["B · Disarankan","A + I6 + I5","Menjawab pengguna CSSD dan dua produk sekaligus","Desain lebih rumit"],
         ["C · Ambisius","B + I4 pembanding","Dua pilihan harga untuk LKPI","Dua purwarupa dalam 3 hari"]],
  tanya=["Piston atau ruang takar gravitasi — mana lebih mungkin < 5% dengan biaya rendah?",
         "Pompa dijual bersama jeriken atau dipakai ulang di RS?",
         "Bahan lokal apa yang tahan BAYzime dan BAYcide?",
         "Bisakah dapat sampel jeriken dan produk minggu ini?",
         "Apakah pedal kaki benar-benar dibutuhkan petugas CSSD?"],
  mitra_q=["Dimensi dan ukuran ulir tutup jeriken 5 L?",
           "Viskositas BAYzime dan BAYcide; data kompatibilitas material?",
           "Model distribusi dan target harga per unit?",
           "Untuk opsi 1: proses produksi paling lambat dan volume per hari?"]),

 dict(folder="ums-01", kode="UMS-01",
  judul="Solusi Pendukung Komersialisasi Produk Kesehatan Hasil Riset UMS",
  mitra="DPM DRPPS UMS — Tim Hilirisasi / UMS Innovation Hub (tantangan internal)", jenis="Perangkat lunak (AI/data)", ki="tidak disebut — tanyakan",
  profil=["DPM DRPPS mengelola UMS Innovation Hub (ihub.ums.ac.id): katalog inovasi, produk, inovator, mitra [H]",
          "Katalog: 35 inovasi dengan ±40 field (TKT, KI, legalitas, tahap, mitra); 8 bidang kesehatan [H]",
          "6 produk komersial; 32 inovator; profil menautkan inovator ↔ inovasi ↔ produk [H]",
          "Database mitra: 103 kegiatan; nama mitra sering \"tidak disebutkan\" [H]"],
  data=["Serapan produk riset kesehatan oleh masyarakat dan industri masih rendah [S]",
        "Sulit menghubungkan produk kampus dengan industri dan faskes secara cepat dan akurat [W]",
        "**20 dari 35** inovasi belum diadopsi; hanya **3** yang punya legalitas edar [H]",
        "Kasus belum diadopsi: Clovena (TKT 7), ENSIKOL (TKT 6), media edukasi (TKT 4) [H]",
        "iHub belum punya pencocokan, profil kebutuhan industri, checklist izin edar, product brief, pipeline [H]",
        "Masalah data: nama fakultas tidak seragam, field mitra teks bebas, sektor kosong pada 10 inovasi [H]"],
  pain=[["Produk","iHub masih katalog statis [H]"],
        ["Proses","Pencocokan dan penyusunan dokumen penawaran manual [W]"],
        ["Dukungan","Inovator kurang panduan jalur izin edar; 32/35 tanpa legalitas [H]"],
        ["Finansial","Investasi riset tidak kembali karena tidak diserap [asumsi]"]],
  persona=[("Pak Agus, staf Tim Hilirisasi","butuh daftar mitra cocok per produk + alasan, product brief siap pakai, pelacakan tindak lanjut [asumsi]"),
           ("Bu Setya, dosen inovator","produk TKT 6, KI granted, belum diadopsi; butuh tahu jalur izin edar dan industri yang tertarik [asumsi]"),
           ("Pak Rudi, manajer produk industri","butuh ringkasan jelas (bukti, KI, regulasi, pasar) sebelum bertemu [asumsi]")],
  problem="Pak Agus adalah staf hilirisasi kampus yang mengelola puluhan inovasi dengan tenaga terbatas, yang membutuhkan cara cepat menemukan mitra industri yang cocok dan menyiapkan penawaran tiap produk, karena pencocokan dan dokumen masih manual dan katalog yang ada tidak membantu menghubungkan produk dengan kebutuhan industri.",
  need="Cara untuk mencocokkan produk riset kesehatan kampus dengan kebutuhan industri dan memetakan celah kesiapan komersialisasinya, sehingga lebih banyak produk mencapai tahap kerja sama.",
  kriteria=[["Rekomendasi relevan dengan kebutuhan mitra","≥ [ ]% dinilai relevan [W]"],
            ["Penyusunan product brief","lebih cepat [W]"],
            ["Pemetaan celah teknis/regulasi","untuk 3–5 produk uji [W]"],
            ["Kemudahan bagi tim hilirisasi","tugas selesai tanpa bantuan [W]"],
            ["Integrasi","dokumentasi siap untuk iHub [W]"]],
  batasan=["Bukan direktori e-commerce/katalog statis [W]",
           "Diuji dengan minimal 3–5 produk nyata UMS [W]",
           "Kompatibel dan mudah diintegrasikan dengan iHub [W]"],
  dukungan=["Akses data katalog dan profil TKT dari taskforce hilirisasi; pendampingan proses hilirisasi, kerja sama satu pintu, business matching [W]"],
  ide=[["I1","Mesin pencocokan","Embedding produk vs profil industri + aturan (sektor, regulasi, TKT) → 5 teratas dengan alasan","Sedang","Inti"],
       ["I2","Formulir kebutuhan industri","5–8 isian + teks bebas diolah AI","Rendah","Pendukung"],
       ["I3","Kalkulator kesiapan","Pohon keputusan jalur izin edar + checklist + status iHub → skor dan celah","Sedang","Inti"],
       ["I4","Generator product brief","Data katalog → 1 halaman untuk industri/investor/RS; ditinjau inovator","Rendah–Sedang","Inti"],
       ["I5","Pipeline kemitraan","Status prospek sampai MoU/lisensi + pengingat","Rendah","Inti"],
       ["I6","Normalisasi data","Seragamkan fakultas, isi sektor, ekstrak nama mitra; bisa jadi bukti awal","Rendah","Fondasi"],
       ["I7","Demo dengan mitra hackathon","Profil CV Arba'in dan PT LKPI sebagai contoh industri","Rendah","Demo"],
       ["I8","Konektor iHub","API baca katalog + widget \"mitra yang cocok\"","Sedang","Integrasi"]],
  paket=[["A · Minimum","I6 + I1 + I4","Cepat terlihat; data nyata","Belum menyentuh regulasi dan tindak lanjut"],
         ["B · Disarankan","A + I3 + I5 + I7","Keempat keluaran yang diminta mitra","I3 butuh validasi pakar regulasi"],
         ["C · Ambisius","B + I2 + I8 berjalan di iHub","Langsung dipakai DPM","Bergantung akses teknis iHub"]],
  tanya=["Dari mana profil kebutuhan industri saat demo?",
         "Seberapa dalam kalkulator regulasi bisa dibuat secara bertanggung jawab; siapa validatornya?",
         "Produk mana untuk 3–5 studi kasus; bisa bicara dengan inovatornya minggu ini?",
         "Bagaimana membuktikan ini bukan katalog statis?",
         "Integrasi iHub: desain + API, atau berjalan langsung?"],
  mitra_q=["Stack teknis iHub; ada API/akses basis data?",
           "Produk pilihan untuk studi kasus?",
           "Industri yang pernah ikut business matching — bisa diwawancarai?",
           "Prosedur kerja sama industri satu pintu?",
           "Ketentuan KI tantangan ini?"]),
]


def main():
    only = sys.argv[1:]
    tmp = os.path.join(ROOT, ".pdf-build")
    os.makedirs(tmp, exist_ok=True)
    for p in PROYEK:
        if only and p["folder"] not in only:
            continue
        src = os.path.join(tmp, p["folder"] + ".html")
        out = os.path.join(ROOT, p["folder"], f"ringkasan-brainstorming-{p['folder']}.pdf")
        open(src, "w", encoding="utf8").write(render(p))
        subprocess.run(["weasyprint", "-q", src, out], check=True)
        print(out)


if __name__ == "__main__":
    main()
