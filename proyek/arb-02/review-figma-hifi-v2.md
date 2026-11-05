# Review Figma "SIGAP · Hi-fi v2" (4 Nov 2026)

Sumber: [Figma ARB-02](https://www.figma.com/design/cvBD4wgdf2jIGWW8NGOJZ7/SIGAP-%E2%80%94-Hi-fi-Prototype--ARB-02-?node-id=31-304), dibandingkan dengan [proposal v03](Proposal_AntechAsync_v03_SIGAP_2026-11-04.docx) (memakai PWA). Diperiksa lewat browser, karena kuota Figma MCP (paket Starter) habis.

## Kesesuaian dengan proposal

- Kesembilan layar di Tabel C.3 ada: S1–S4 (sales), S5–S8 (kantor), S9 (direktur). Ada juga layar turunan (S2a, S3b–d, S4a, S5a–e, S6a–e, S7a–c, S8a–b, S9a), login (S0, L1, L1a), dan dashboard admin (D1, D2).
- Aturan stok konsisten antar-layar: tersedia = fisik − dipesan, FEFO, dan telusur batch PR-2603 (15 masuk, sisa 9, 6 terkirim).
- Rumus saran produksi di S9 cocok (perkiraan + stok minimum − tersedia).
- PWA: S0 "Pasang di layar utama" dan frame "Catatan teknis PWA" sudah sesuai dengan keputusan terbaru.

## Sudah diperbaiki di Figma

| Masalah | Perbaikan |
|---|---|
| Total PS-1104 salah hitung: 4×95rb + 3×45rb + 2×120rb = Rp755.000, tertulis Rp650.000 | Diganti di S4a, S6, S6a, S6c, S6d, S6e (14 teks). Kekurangan bayar Rp400.000 → Rp505.000 (13 teks). PS-1105 (Rp400.000) tidak diubah. |

## Langkah yang hilang di alur

Butir 1–4 sudah ditambahkan ke Figma sebagai layar usulan (dibuat lewat browser dengan menduplikasi layar mirip, ditempatkan di kanan S4a, nama berakhiran "(usulan)") dan sudah tersambung di prototype:

| Usulan | Layar baru | Masuk dari | Keluar ke |
|---|---|---|---|
| 1. Catat hasil kunjungan (pesan / tidak order + alasan / tutup, kunjungan berikutnya, check-out) | S2c · Hasil kunjungan | S2, tombol "Selesai kunjungan" (sebelumnya "Chat WhatsApp outlet") | Simpan → S1; Batal → S2 |
| 2. Alasan wajib saat check-in dilewati, ditandai untuk admin penjualan | S2d · Alasan lewati check-in | S2a, tombol "Lewati check-in" | Lanjut → S3; Kembali → S2a |
| 3. Konfirmasi pesanan tersimpan, outlet ditandai selesai, saran outlet berikutnya | S4b · Pesanan tersimpan | S3, "Kirim pesanan" (sebelumnya langsung ke S4) | Lanjut → S1; Lihat pesanan → S4 |
| 4. Tindak lanjut pesanan ditolak | S4c · Tindak lanjut pesanan ditolak | S4, kartu "Ditolak" | Pesan produk pengganti → S3c; Kabari outlet → WhatsApp |
| 5. "Ulangi pesanan terakhir" tersambung (fitur inti, target ≤15 detik) — 5 Nov 2026 | S3e · Form pesanan kosong (semua jumlah 0, total Rp0) | S2, "Buat pesanan" (sebelumnya langsung ke S3 yang sudah terisi) | "Ulangi pesanan terakhir" → S3 (terisi 21 botol, Rp915.000); tombol Kirim di S3e sengaja tanpa interaksi |

Usulan untuk admin gudang (5 Nov 2026):

| Usulan | Layar baru | Masuk dari | Keluar ke |
|---|---|---|---|
| 6. Tambah produk baru ke master data (kode, nama, kategori, satuan, harga, no. BPOM wajib, stok minimum). Stok awal selalu 0; stok bertambah lewat S7a Barang masuk per batch agar kedaluwarsa tercatat | S7d · Tambah produk baru (duplikat S7c, contoh MDK02 Madu Daun Kelor, Rp60.000, TR-CONTOH-017; kolom kode wajib diisi dan tidak lagi bergaya hanya-baca) | S7, tombol baru "+ Produk baru" di antara "Penyesuaian (opname)" dan "+ Barang masuk" | Simpan produk / Batal → S7 |

Keputusan yang masih terbuka: apakah harga produk baru perlu disetujui direktur sebelum produk muncul di katalog sales (lihat celah "Kelola master data" di bawah). Di purwarupa, produk saat ini hanya bisa ditambah lewat Django admin (`/admin/`).

Tombol kembali (←) di S2c dan S2d sudah diarahkan ke S2 dan S2a (5 Nov 2026).

Masih terbuka:

6. ~~S3b belum punya tombol "Ulangi pesanan terakhir".~~ **Sudah (5 Nov 2026):** instance komponen Button (gaya Secondary, hijau muda) "↻ Ulangi pesanan terakhir (20 Okt)" disisipkan lewat panel Assets di atas kartu produk S3b. Isi form S3b dianggap hasil Ulangi, jadi tombol ini tanpa interaksi. Warnanya sengaja beda dari tombol kuning di S3 agar tidak menyatu dengan banner "Tidak ada sinyal".
7. Outlet ke-2 di S1 masih langsung membuka S3b tanpa check-in (jalan pintas demo mode tanpa sinyal).

## Hotspot prototype

Sudah disambungkan (5 Nov 2026):

- S0 "Lupa kata sandi? Hubungi admin penjualan" → WhatsApp (belum ada layar reset sandi untuk sales).
- S3b "Lihat semua 16 produk" → S3c.
- D1 baris "Toko Obat Waras · Budi" → S6 Kelola pesanan.
- Flow "2 · Admin penjualan" yang kedua (mulai dari L1a) diganti nama menjadi "2b · Lupa kata sandi (kantor)".

Masih terbuka:

- ~~S4 "Kirim sekarang" belum tersambung.~~ **Sudah (5 Nov 2026):** → layar baru **S4d · Antrean terkirim (usulan)**: "Antrean kosong · 1 pesanan terkirim 09.26, tepat sekali", Toko Obat Waras berubah dari "Menunggu sinyal" ke "Diterima".
- Outlet ke-3 dan ke-4 di S1 dulu membuka S2a milik Apotek Sehat Jebres. **5 Nov 2026:** tautannya dilepas agar demo tidak menampilkan outlet yang salah; outlet ke-5 (sudah check-in, pesanan terkirim) kini membuka S4 Pesanan saya. Varian S2a/S2 per outlet tetap belum dibuat.

## Data yang tidak konsisten (sudah diperbaiki 5 Nov 2026)

| Masalah | Perbaikan |
|---|---|
| S2: pesanan 19 Okt Rp1.420.000 "Belum bayar", tetapi "Ulangi" menghasilkan Rp915.000; tempo 30 hari tidak cocok dengan jatuh tempo 3 Nov | Riwayat S2 menjadi: 19 Okt · Rp915.000 · Lunas; 4 Okt · 3 produk · Rp1.420.000 · Belum bayar (4 Okt + 30 hari = 3 Nov); 21 Sep tetap. Selang ±14 hari tetap cocok. |
| D1: "Pesanan hari ini 14", padahal rincian status berjumlah 13 dan memuat status lintas hari | KPI menjadi "Pesanan 7 hari · 13" dan panel "Pesanan 7 hari per status". |
| D1: Budi "1/5 outlet · 2 pesanan · check-in 08.20 Apotek Sehat Jebres" tidak cocok dengan S1/S4 | Menjadi "5/5 outlet · 5 pesanan", check-in terakhir 09.20 Toko Herbal Sumber Waras, progress bar penuh. |
| S4: jam status bar 09.05, padahal ada pesanan PS-1105 pukul 09.20 | Jam diubah ke 09.25. |
| S9 dan S9a: Direktur berlabel "Hanya baca", padahal punya "Atur target" | Label peran menjadi "Laporan & target". |

## UI

- Di S1, tombol mengambang "Outlet baru" menutupi kartu outlet ke-5. **Sudah diperbaiki 5 Nov 2026:** tombol mengambang dihapus; chip "5 outlet" di kepala kartu Kunjungan hari ini diganti chip hijau "+ Outlet baru" yang membuka S1a (jumlah outlet sudah tertulis di sapaan "5 kunjungan hari ini"). Kelima outlet kini terlihat utuh. Saat dibangun, beri area sentuh ≥44 px.
- ~~Halaman sales tidak punya menu profil/keluar.~~ **Sudah (5 Nov 2026):** layar baru **S1b · Profil & keluar (usulan)** (dari duplikat S2d) berisi akun, data tersimpan di HP, jumlah antrean, versi aplikasi, sinkron terakhir, dan tombol "Keluar dari SIGAP" (Danger) → S0. Peringatan: keluar menghapus data di HP, jadi antrean harus terkirim dulu. Dibuka dengan mengetuk sapaan "Halo, Budi" di S1; ← dan "Kembali ke kunjungan" → S1. Sapaan belum punya penanda visual bahwa ia bisa diketuk (mis. avatar).

## Perubahan Figma 5 Nov 2026 (malam)

Dibaca langsung dari file (teks semua layar dan semua sambungan prototype). Semua layar baru sudah punya tautan masuk dan sidebar kantor kini memuat Riwayat pembayaran, Riwayat barang masuk, dan Manajemen akun. Satu-satunya frame tanpa tautan masuk adalah "Catatan teknis PWA" (memang catatan).

### Layar baru

| Peran | Alur | Layar |
|---|---|---|
| Admin penjualan | ACC pesanan dari HP: detail → ubah isi (sebelum ACC) → ACC dengan ketentuan bayar tunai/tempo → siap bayar → catat pembayaran sebagian | S6j, S6q, S6f, S6n, S6o |
| Admin penjualan | Pesanan dengan kekurangan: dikirim sebagian (urgent) → tandai selesai dengan alasan → selesai, tagihan dihitung ulang → buka kembali | S6h, S6g, S6i |
| Admin penjualan | Filter perlu perhatian, ubah pesanan setelah kirim (tempo, sales PJ), riwayat pembayaran | S6k, S6p, S6m |
| Admin gudang | Antrean kirim (hanya pesanan di-ACC) → proses kirim FEFO yang bisa diubah → kirim sebagian dengan karantina → Belum lengkap · urgent | S8, S8a, S8c, S8d |
| Admin gudang | Telusur batch dengan penjelasan dan tombol Hubungi PIC; riwayat barang masuk dan detail penerimaan dengan selisih surat jalan | S8e, S7e, S7f |
| Direktur | Manajemen akun: tambah (undangan WhatsApp), ubah (reset sandi, keluarkan perangkat), nonaktifkan (pindah outlet binaan); role & hak akses per modul | U1, U1a–c, U2, U2a |

Aturan bisnis, model data, dan user flow sudah disesuaikan (5 Nov 2026 malam).

### Tombol tanpa tujuan / alur yang belum ada

| Prioritas | Temuan | Layar |
|---|---|---|
| T | **Sisi sales belum mengikuti alur ACC**: S4/S4a tidak punya status menunggu ACC, di-ACC, dikirim sebagian, selesai; tidak ada notifikasi saat admin mengubah pesanan (S6q menjanjikan "Sales Dewi mendapat notifikasi") | S4, S4a |
| T | **Tolak pesanan** tidak punya layar alasan/kabar ke sales: di S6j tombolnya membuka S6f (modal ACC), di S6f langsung kembali ke S6 | S6j, S6f |
| T | **Kirim susulan** dan **Detail** di daftar Belum lengkap belum tersambung | S8d |
| T | **Mulai penarikan batch ini** (recall) belum punya layar | S8e |
| S | "Kabari outlet" (S6h) dan "Lihat tagihan" (S6i) belum tersambung | S6h, S6i |
| S | Retur disebut di S6p ("gunakan retur dari detail pesanan") tetapi belum dirancang | S6p |
| S | Koreksi pembayaran oleh direktur (S6m) belum punya layar | S6m |
| S | Nasib barang karantina (retur ke pemasok / pemusnahan) belum ada | S8c |
| S | Pencatatan 3 botol susulan pemasok, cetak label batch, dan PO pembelian belum ada | S7f |
| R | U1 "Kirim ulang" dan "Aktifkan", U1b "Kirim tautan reset" dan "Keluarkan", U2 "+ Peran baru", S6m/S7e "Unduh Excel" belum tersambung | U1, U1b, U2, S6m, S7e |
| R | Pembayaran "Tunai via Budi" (S6m) berarti sales menerima uang, tetapi HP sales tidak punya pencatatan penagihan | S6m, S2 |

### Data dan aturan yang bertentangan

| Temuan | Saran |
|---|---|
| Dua aturan stok kurang hidup bersama: PS-1104 baris Sari Kurma "diterima 3 dari 10" otomatis saat tiba di server, sedangkan PS-1095 dengan stok 0 tetap bisa di-ACC dan kekurangannya jadi urgent | Pakai satu aturan: server mencadangkan sebanyak stok tersedia, sisanya jadi kekurangan yang diputuskan saat ACC (sudah ditulis di aturan bisnis sebagai **[pilih]**) |
| S8c: "2 tetap dipesan (urgent)" dan "stok tersedia −2", tetapi S8d menulis "tersedia MHP: 0" | Kekurangan tidak menahan stok dipesan; barang rusak keluar dari fisik dan dipesan sekaligus, tersedia tetap |
| Harga di S6q: MKL01 Rp45.000 dan MHP01 Rp30.000, padahal S7c MKL01 Rp75.000 dan S3 Madu Hitam Pahit Rp15.000 (total Rp480.000 tetap cocok dengan harga lama) | Samakan S6q dengan harga di S3/S7c |
| U2a: "Ubah harga jual" dimatikan untuk admin gudang (harga diatur admin penjualan), tetapi S7c/S7d menaruh kolom harga di layar admin gudang | Pindahkan kolom harga ke layar milik admin penjualan, atau buat read-only di S7c/S7d |
| Sidebar menampilkan semua menu (termasuk Manajemen akun) untuk Sari dan Joko, padahal U2 membatasi akses per peran | Sidebar mengikuti peran |
| Toko Herbal Sumber Waras: di HP sales PS-1105 pukul 09.20 menunggu validasi, di S8 PS-1107 dipesan 09.12 "outlet baru, sudah divalidasi" | Samakan kode dan jam, atau jelaskan bahwa ini pesanan kedua |
| Linimasa kantor: "Hari ini" = 2 Nov di tabel, tetapi PS-1095 "selesai 5 Nov 09.10" (S6i) | Pilih satu tanggal demo untuk semua layar |
| PS-1095 sudah dibayar Rp210.000 (S6o) lalu tagihan menjadi Rp210.000 (S6i), tetapi S6i tidak menyebut lunas | Tampilkan "Lunas" di S6i |

## Celah alur (flow hole) per peran

Situasi nyata yang belum punya alur, baik di desain maupun di proposal. Prioritas: **T** = tinggi (mengganggu tujuan utama proposal), **S** = sedang, **R** = rendah / setelah MVP.

### Sales
| Celah | Kenapa penting | Pri |
|---|---|---|
| **Retur / barang kedaluwarsa dari outlet** | Produk herbal punya masa simpan; tanpa alur retur, stok dan riwayat outlet tidak pernah dikoreksi, dan telusur batch (CPOTB) berhenti di pengiriman. Tidak ada di proposal maupun desain. | T |
| **Edit atau batalkan pesanan yang masih di antrean HP** (belum terkirim) | Salah input saat tanpa sinyal tidak bisa diperbaiki sebelum terkirim; satu-satunya jalan adalah admin membatalkan setelah stok terlanjur dipesan. | T |
| **Kunjungan ke outlet di luar daftar hari ini** | S1 hanya berisi 5 outlet terjadwal; tidak ada pencarian outlet terdaftar lain (selain "Outlet baru"). | S |
| **Pembukaan pertama tanpa sinyal / data belum tersinkron** | PWA bisa terbuka dari nol, tetapi belum ada layar untuk "katalog belum pernah diunduh" atau "data stok sudah >24 jam". | S |
| **GPS ditolak / izin lokasi dimatikan** | S2a mengandaikan GPS selalu ada; perlu state izin ditolak (berbeda dari "GPS lemah" di S2d). | S |
| **Penagihan oleh sales** | S2 menampilkan tagihan jatuh tempo besok, tetapi sales tidak bisa mencatat "uang diterima / janji bayar"; pencatatan hanya di S6c oleh admin. | S |
| **HP hilang / ganti HP dengan antrean belum terkirim**, logout | Antrean IndexedDB hilang tanpa jejak; tidak ada menu keluar. | R |

### Admin penjualan
| Celah | Kenapa penting | Pri |
|---|---|---|
| **Outlet baru ditolak** (S5e punya tombol "Tolak") | Tidak jelas nasib pesanan PS-1105 yang tertahan dan bagaimana sales diberi tahu. | T |
| ~~Kelola akun pengguna & penugasan outlet ke sales~~ | **Sudah dirancang 5 Nov 2026 (U1–U2a)**: tambah, ubah, nonaktifkan dengan pindah outlet binaan, hak akses per peran. | — |
| **Reset kata sandi** | L1a menyebut "kata sandi sementara dibuat direktur", tetapi direktur tidak punya layar untuk itu. | S |
| **Pesanan via telepon/WA langsung dari outlet** (tanpa sales) | Pesanan masuk kantor tidak punya form; akan dicatat di luar sistem lagi. | S |
| ~~Ubah jumlah pesanan sebelum kirim~~ | **Sudah dirancang 5 Nov 2026**: S6q (sebelum ACC) dan S6p (setelah kirim, tanpa ubah item). | — |
| **Piutang menunggak → tahan pesanan baru** | Tidak ada aturan/alur blokir outlet yang lewat jatuh tempo. | R |

### Admin gudang
| Celah | Kenapa penting | Pri |
|---|---|---|
| **Recall batch setelah telusur** | S8 menampilkan outlet penerima, tetapi tidak ada tindak lanjut: tandai batch "ditarik", blokir dari FEFO, catat barang kembali. Ini inti klaim CPOTB di proposal. | T |
| **Barang rusak / kedaluwarsa di gudang (pemusnahan)** | Opname S7b hanya "penyesuaian"; perlu jenis mutasi pemusnahan dengan alasan dan batch. | S |
| **Gagal kirim** (outlet tutup, ditolak di tempat) | Kirim sebagian karena barang di gudang kurang/rusak sudah dirancang (S8c, S8d); barang yang kembali dari outlet belum. | S |
| **Bukti serah terima / surat jalan** | Tidak ada cetak surat jalan atau tanda terima outlet sebagai bukti kirim. | R |

### Direktur
| Celah | Kenapa penting | Pri |
|---|---|---|
| **Tindak lanjut saran produksi** | S9 memberi angka saran produksi tetapi tidak bisa disetujui/diteruskan; hasilnya tidak bisa dibandingkan dengan realisasi. | S |
| **Kelola master data (produk baru, harga, stok minimum)** | S7c dipegang admin gudang; tidak jelas siapa yang menyetujui perubahan harga. | S |
| **Ekspor laporan** (bulanan, per sales) | Dashboard hanya tampilan; tidak ada unduh laporan untuk rapat. | R |

### Lintas peran
| Celah | Kenapa penting | Pri |
|---|---|---|
| **Notifikasi antar-peran** | Sales tidak diberi tahu bila pesanan ditolak/diterima sebagian setelah ia pergi; admin tidak diberi tahu outlet baru masuk. Saat ini mengandalkan membuka layar. | T |
| **Log audit yang bisa dilihat** | Proposal menjanjikan "log sesuai UU PDP", tetapi tidak ada layar untuk melihatnya. | S |
| **Dua sales mendaftarkan outlet yang sama saat tanpa sinyal** | Deteksi duplikat hanya untuk impor Excel (S5c), belum untuk outlet baru dari HP. | S |
