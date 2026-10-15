# RS UMS A.R. Fachrudin — Detail Kebutuhan Mitra

> Bagian dari [Kebutuhan Mitra UMS HI Hackathon 2026](../01-kebutuhan-mitra.md).
> Tantangan: **RS-01**. Kode sumber: [P] Pedoman, [W] laman hackathon, [S] transkrip sosialisasi 7 Okt 2026, [R] situs RS https://rs.ums.ac.id/ (diakses 14 Okt 2026).
> Folder kerja tim: [proyek/rs-01](../../proyek/rs-01/README.md)

---

## 1. Profil mitra

| Aspek | Keterangan | Sumber |
|---|---|---|
| Nama | Rumah Sakit UMS A.R. Fachrudin (ejaan pedoman: "Fachruddin") | [R], [P] |
| Status | RS milik Universitas Muhammadiyah Surakarta; masih baru | [S] |
| Alamat | Jl. Adi Sucipto No. 167, Karangasem, Kec. Laweyan, Kota Surakarta 57145 (perbatasan Solo–Karanganyar menurut [S]) | [R] |
| Layanan | IGD 24 jam, rawat jalan (poliklinik), rawat inap, laboratorium, instalasi bedah/kamar operasi, rawat intensif, rehabilitasi medik & fisioterapi, radiologi | [R] |
| Kapasitas rawat inap | 37 tempat tidur: VVIP 2, VIP 5, Kelas 1 16, Kelas 2 4, Kelas 3 5, Isolasi 5 | [R] |
| Kontak | IGD 24 jam (WA) 0851-1305-5755 · Pendaftaran (WA) 0851-2997-2996 · Informasi & pengaduan (WA) 0851-6979-9799 · humas@rs.ums.id · Instagram @rsumsarfachrudin | [R] |
| Narasumber sosialisasi | Mas Candra, bagian Humas & Marketing | [S] |

---

## 2. Temuan dari situs RS (rs.ums.ac.id)

### 2.1 Arsitektur situs

- Situs adalah aplikasi web **React (single-page app)** dengan backend API sendiri di `https://rs.ums.ac.id/api`. Ada panel admin (`/api/admin/login`) untuk mengelola konten.
- Menu: Beranda · Profil (Visi & Misi, Struktur Organisasi) · Fasilitas · Dokter · Informasi · Promo.
- Endpoint publik yang terlihat di kode:

| Endpoint | Isi |
|---|---|
| `GET /api/jadwal` | Jadwal praktik dokter (dipakai halaman Dokter) |
| `GET /api/informasi` | 85 artikel/berita (Informasi 49, Kegiatan 30, Kesehatan 6), Maret–Oktober 2026 |
| `GET /api/promo` | 3 promo layanan (cek fungsi ginjal Rp320.000, layanan akta kelahiran/KIA/KK gratis untuk persalinan, spirometri) |
| `POST /api/visitors/track` | Pelacakan pengunjung |

- **Ketersediaan tempat tidur** diambil dari **Google Sheets yang dipublikasikan sebagai CSV** (kolom: nomor, kelas, ruangan, status kosong/terisi, lantai, bangsal, jenis). Artinya status bed masih diperbarui manual di spreadsheet.

### 2.2 Data jadwal dokter (`/api/jadwal`)

**Struktur data:** `id, nama_dokter, spesialis, deskripsi, image, hari, jam`. Satu baris = satu slot mingguan.

| Ringkasan | Nilai |
|---|---|
| Tenaga medis | 32 (termasuk 2 dokter gigi dan 1 psikolog klinis) |
| Spesialisasi | 18 |
| Slot praktik per minggu | 103 (Senin 20, Selasa 19, Rabu 17, Kamis 18, Jumat 20, Sabtu 9) |
| Slot mulai pukul ≥ 13.00 | 54 dari 103 (±52%) |
| Dokter dengan hanya 1–2 slot/minggu | 13 dari 32 |

Sebaran spesialisasi: Kandungan 4, Anak 4, Bedah Umum 3, THT 2, Penyakit Dalam 2, Ortopedi 2, Kulit & Kelamin 2, Gigi 2, Jantung 2, dan masing-masing 1 untuk Mata, Saraf, Patologi Anatomi, Paru, Radiologi, Jiwa, Rehabilitasi Medik, Forensik, Psikologi Klinis.

### 2.3 Pengamatan yang relevan untuk RS-01

- **Jadwal hanya berupa pola mingguan statis.** Tidak ada field tanggal, status (praktik/batal/terlambat), dokter pengganti, kuota, atau alasan perubahan. Perubahan jadwal harian tidak bisa direpresentasikan di sistem yang ada.
- Halaman Dokter hanya memberi catatan: *"Jadwal dapat berubah sewaktu-waktu. Info lebih lanjut silahkan hubungi bagian Pendaftaran."* [R]
- **"Pendaftaran Online" sebenarnya tautan WhatsApp** ke nomor pendaftaran dengan pesan templat. Belum ada sistem booking, nomor antrean, atau akun pasien.
- Situs tidak menyebut BPJS, Mobile JKN, atau antrean online sama sekali.
- Lebih dari separuh slot ada di siang–sore hari dan banyak dokter hanya praktik 1–2 kali seminggu. Ini konsisten dengan penjelasan mitra bahwa dokter spesialis juga bertugas di RS lain dan sering tertahan kasus *cito* [S] (kesimpulan ini dugaan, bukan data RS).
- Ada data yang tampak keliru: slot Forensik "00:34 – 14:36" dan Patologi Anatomi "00:00 – 00:04". Validasi input jadwal belum ada.
- Kanal komunikasi pasien saat ini terpecah ke tiga nomor WhatsApp berbeda (IGD, pendaftaran, informasi/pengaduan).

---

## 3. Tantangan RS-01

**Judul:** Sistem Cerdas Manajemen Jadwal Dokter, Otomatisasi Notifikasi Pasien, dan Interoperabilitas Layanan RS
**Detail resmi:** https://ihub.ums.ac.id/hackathon/tantangan/rs-01-informasi-jadwal-dokter-dan-notifikasi-perubahan-untuk-pasien

### 3.1 Masalah inti

Jadwal praktik dokter spesialis sering berubah mendadak, dan informasi perubahan itu tidak sampai ke pasien tepat waktu.

### 3.2 Latar belakang dan kondisi saat ini

- Dokter spesialis jumlahnya terbatas dan berpraktik di beberapa fasilitas. Satu SIP berlaku untuk hingga 3 tempat, jadi banyak dokter praktik di 2–3 tempat [S].
- Perubahan jadwal sering dipicu kondisi *cito* (darurat) di RS atau klinik lain, sehingga dokter belum selesai di satu tempat ketika jadwal poli di RS UMS sudah dimulai [S].
- Menurut [W], perubahan jadwal terjadi "secara mendadak hampir setiap hari".
- Pemberitahuan perubahan dan *reschedule* masih **manual oleh petugas lewat WhatsApp** [W].
- RS sudah punya alur untuk menginformasikan pasien, tetapi sebagian pasien tidak membuka HP seharian. Pasien yang sudah reservasi H-1 sering tetap tidak menerima informasi [S].
- RS ini masih baru, sehingga sistemnya belum sekompleks SIMRS di RS besar [S, jawaban panitia atas pertanyaan peserta].
- Komunikasi internal antarpoli/unit juga perlu diperbaiki [W].
- RS perlu menyiapkan SIMRS agar bisa terhubung dengan **SATUSEHAT Kemenkes** dan **BPJS Kesehatan**, serta mendukung fungsi humas dan pemasaran [W].

### 3.3 Dampak

- Informasi terlambat; pasien datang lalu menunggu lama [W].
- Kepuasan pasien turun; muncul ulasan negatif di ruang publik [W, S].

### 3.4 Pengguna dan penerima manfaat [W]

- Pasien dan keluarga pasien
- Petugas admisi, perawat poliklinik, dokter spesialis
- Divisi Humas, Marketing, dan Tim IT/SIMRS

### 3.5 Arah solusi awal [W]

Purwarupa **modular** yang mudah diintegrasikan ke SIMRS yang sudah ada melalui API, dengan fokus:

1. **Notifikasi dua arah real-time.** Pasien bisa konfirmasi kehadiran atau *reschedule* sendiri, dengan pengalaman pengguna seperti Halodoc.
2. **Dashboard koordinasi internal** untuk dokter, perawat poli, admisi, dan humas.
3. **Arsitektur pertukaran data** yang siap dengan standar SATUSEHAT (FHIR/API) dan antrean BPJS Kesehatan.
4. **Patient engagement:** informasi layanan, edukasi, promosi yang etis, dan kanal umpan balik pasien untuk mencegah komplain terbuka.

### 3.6 Keluaran yang diharapkan [W]

- Purwarupa fungsional notifikasi preventif jadwal dokter dan manajemen antrean/*reschedule*.
- Dashboard internal untuk memperbarui status jadwal secara instan antarunit.
- Desain arsitektur API/konektor modular untuk SIMRS internal, SATUSEHAT, dan BPJS.
- Fitur informasi layanan dan umpan balik pasien.

### 3.7 Batasan [W]

- Seluruh komunikasi, informasi, dan promosi wajib mengikuti **Kode Etik Rumah Sakit Indonesia (KODERSI)**.
- Keamanan dan kerahasiaan data pribadi dan data medis pasien wajib dijamin sesuai regulasi pelindungan data (UU PDP).
- Arsitektur terbuka dan modular, **tidak terkunci pada satu vendor**.

### 3.8 Indikator keberhasilan [W]

- Notifikasi perubahan jadwal terkirim otomatis **< 1 menit** sejak status diperbarui oleh poli/dokter.
- Beban kerja manual admisi untuk menghubungi pasien berkurang signifikan.
- Pasien mudah konfirmasi atau *reschedule*; rancangan integrasi data kompatibel dengan SIMRS/SATUSEHAT.

### 3.9 Dukungan mitra [W]

- Diskusi kebutuhan dan alur layanan bersama Kepala Humas & Marketing serta manajemen RS.
- Skenario kasus nyata: alur penjadwalan poli, alur komplain, kebutuhan komunikasi pasien.
- Fasilitasi uji purwarupa dan evaluasi kelayakan di lingkungan RS.

---

## 4. Catatan untuk penyusun proposal

- **Ada titik integrasi nyata.** Endpoint `/api/jadwal` dan panel admin situs RS bisa menjadi sumber jadwal dasar. Solusi cukup menambahkan lapisan "pengecualian jadwal" (tanggal, status, pengganti, alasan) di atas pola mingguan yang sudah ada, lalu memicu notifikasi dari perubahan itu. Koordinasikan akses dengan Tim IT RS.
- **Masalah yang sebenarnya adalah jangkauan, bukan pengiriman.** Pasien yang jarang membuka HP tetap tidak terjangkau notifikasi WhatsApp. Pertimbangkan kanal cadangan (SMS, panggilan suara otomatis/IVR, notifikasi ke kontak keluarga) dan eskalasi bila pesan tidak dibaca dalam batas waktu.
- **Butuh data pasien terdaftar per slot.** Notifikasi hanya bisa dikirim ke pasien yang sudah mendaftar. Saat ini pendaftaran lewat chat WhatsApp manual, jadi purwarupa perlu modul pendaftaran/booking sederhana agar daftar penerima tersedia.
- **Cegah dari hulu.** Sistem bisa memberi sinyal lebih awal, misalnya dokter memperbarui status dengan satu ketukan, atau prediksi keterlambatan dari pola historis per dokter/slot.
- **Validasi data jadwal** (jam mustahil, bentrok slot) bisa menjadi fitur kecil yang langsung terlihat manfaatnya.
- Dari tanya jawab [S]: kebutuhan RS lebih sederhana daripada SIMRS lengkap berbasis AI yang terintegrasi BPJS. Fokus pada notifikasi perubahan jadwal dulu; integrasi SATUSEHAT/BPJS cukup sampai tahap desain arsitektur.
- Ada potensi sinergi dengan mitra lain: RS punya instalasi bedah/kamar operasi, sehingga bisa menjadi lokasi uji alat takar BAYzime untuk LKPI-02 (lihat [PT LKPI](pt-lkpi.md)).
- Disiplin yang relevan: informatika/sistem informasi, kesehatan masyarakat atau manajemen RS/rekam medis, desain UX, komunikasi/humas.

### Pertanyaan untuk mitra

- SIMRS apa yang dipakai di pendaftaran/poli, dan apakah terhubung dengan backend situs (`/api/jadwal`)?
- Bagaimana pasien saat ini tercatat per slot — di SIMRS, spreadsheet, atau hanya chat WhatsApp?
- Berapa pasien rawat jalan per hari, dan berapa frekuensi perubahan jadwal per minggu? Berapa menit sebelum praktik biasanya perubahan diketahui?
- Apakah RS sudah punya akun WhatsApp Business API resmi, atau masih WhatsApp biasa?
- Apakah RS sudah melayani pasien BPJS dan terdaftar di antrean online Mobile JKN?
