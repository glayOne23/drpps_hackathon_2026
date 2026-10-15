# 1 · Empathize — RS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **RS-01** · [README](README.md) · **1 Empathize** · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/rs-ums-ar-fachrudin.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Understand** · s.d. pembekalan · Proposal: Bag. 4 butir 1 · PJ: koordinator validasi pengguna
> Panduan metode lengkap: [_template/01-empathize.md](../_template/01-empathize.md)

## 1. Ringkasan riset sekunder

Sumber utama: [docs/mitra/rs-ums-ar-fachrudin.md](../../docs/mitra/rs-ums-ar-fachrudin.md).

**Kondisi saat ini**
- Jadwal praktik dokter spesialis berubah mendadak "hampir setiap hari" `[sumber: W]`.
- Penyebab: dokter spesialis terbatas dan praktik di 2–3 tempat (SIP berlaku hingga 3 tempat); sering tertahan kasus *cito* di RS/klinik lain `[sumber: S]`.
- Pemberitahuan perubahan dan *reschedule* dilakukan manual oleh petugas lewat WhatsApp `[sumber: W]`.
- RS sudah punya alur informasi ke pasien, tetapi sebagian pasien tidak membuka HP seharian; pasien yang reservasi H-1 tetap tidak terinfo `[sumber: S]`.
- Komunikasi antarpoli/unit perlu diperbaiki `[sumber: W]`.
- RS masih baru; sistemnya belum sekompleks SIMRS RS besar `[sumber: S]`.

**Data situs RS** `[sumber: R]`
- 32 tenaga medis, 18 spesialisasi, 103 slot praktik per minggu; 54 slot mulai pukul ≥ 13.00; 13 dokter hanya 1–2 slot per minggu.
- Jadwal di API `/api/jadwal` hanya pola mingguan (hari + jam), **tanpa tanggal, status, atau dokter pengganti**.
- "Pendaftaran Online" = tautan WhatsApp; belum ada booking, nomor antrean, atau akun pasien.
- Tiga nomor WhatsApp terpisah: IGD, pendaftaran, informasi/pengaduan.
- Catatan di halaman Dokter: *"Jadwal dapat berubah sewaktu-waktu..."*

**Dampak:** pasien datang lalu menunggu lama, kepuasan turun, ulasan negatif di ruang publik `[sumber: W, S]`.

## 2. Asumsi awal tim

| No | Asumsi | Hasil setelah riset |
|---|---|---|
| A1 | Sebagian besar perubahan jadwal baru diketahui RS < 1 jam sebelum praktik `[asumsi]` | |
| A2 | Masalah terbesar adalah pasien tidak membaca pesan, bukan RS terlambat mengirim `[asumsi]` | |
| A3 | Data pasien per slot tercatat di SIMRS/buku pendaftaran, bukan hanya di chat `[asumsi]` | |
| A4 | Pasien lansia lebih sering tidak terjangkau notifikasi WhatsApp `[asumsi]` | |
| A5 | Dokter bersedia memperbarui status sendiri jika caranya cukup cepat `[asumsi]` | |
| A6 | Sebagian besar pasien rawat jalan adalah pasien BPJS `[asumsi]` | |

## 3. Rencana riset

### 3.1 Tujuan riset

1. Bagaimana perubahan jadwal diketahui RS (dari siapa, lewat apa, berapa menit sebelum praktik)?
2. Bagaimana petugas mengabari pasien sekarang, berapa lama, dan di mana macetnya?
3. Bagaimana pasien mendaftar dan menerima informasi; mengapa notifikasi tidak terbaca?
4. Bagaimana koordinasi antara dokter, perawat poli, admisi, dan humas saat jadwal berubah?
5. Sistem apa yang sudah ada (SIMRS, backend situs, WhatsApp Business) dan bisa diintegrasikan?

### 3.2 Partisipan

| Kelompok | Konteks | Target | Akses |
|---|---|---|---|
| Petugas admisi/pendaftaran | Menerima pendaftaran via WA, mengabari perubahan | 2–3 | Lewat Humas (Mas Candra) |
| Perawat poliklinik | Mengetahui kedatangan dokter, menangani pasien menunggu | 2 | Lewat manajemen RS |
| Humas & marketing | Menangani komplain dan ulasan | 1–2 | Narasumber sosialisasi |
| Dokter spesialis | Sumber perubahan jadwal | 1–2 | Lewat manajemen |
| Tim IT/SIMRS | Sistem yang ada, peluang integrasi | 1 | Lewat manajemen |
| Pasien/keluarga | Penerima informasi; variasi usia dan kemampuan teknologi | 3–5 | Di ruang tunggu poli, dengan izin RS |

### 3.3 Metode

| Metode | Untuk | Catatan |
|---|---|---|
| Wawancara | Semua kelompok | Video/telepon sebelum 20 Okt; tatap muka saat pembekalan |
| Observasi kontekstual | Admisi saat jadwal berubah; ruang tunggu poli | Catat waktu dari kabar perubahan → pesan terkirim → pasien tahu |
| Analisis artefak | Contoh pesan WA ke pasien, log perubahan jadwal, data komplain/ulasan | Minta versi tanpa data pribadi |
| Survei singkat pasien (opsional) | Pasien rawat jalan | Kanal yang paling sering dibuka, kebiasaan cek HP |

## 4. Pertanyaan wawancara khusus

**Admisi/pendaftaran**
- Ceritakan terakhir kali jadwal dokter berubah mendadak. Dari siapa Anda tahu, dan apa yang Anda lakukan?
- Berapa pasien yang harus dihubungi, dan berapa lama?
- Bagaimana Anda tahu siapa saja pasien di slot itu?
- Apa yang terjadi jika pasien tidak membalas?

**Perawat poli**
- Bagaimana Anda tahu dokter terlambat atau batal?
- Apa yang Anda katakan ke pasien yang sudah menunggu?

**Dokter**
- Kapan biasanya Anda tahu tidak bisa tepat waktu? Kepada siapa Anda mengabari?
- Cara tercepat apa yang masih masuk akal untuk memberi tahu RS?

**Pasien/keluarga**
- Bagaimana Anda mendaftar untuk periksa hari ini?
- Pernah datang tetapi dokter tidak ada? Apa yang terjadi, bagaimana perasaan Anda?
- Lewat apa Anda paling cepat menerima kabar (WA, SMS, telepon, keluarga)?

**IT/SIMRS**
- SIMRS apa yang dipakai? Apakah terhubung dengan `/api/jadwal` dan panel admin situs?
- Apakah RS sudah terhubung SATUSEHAT dan antrean online BPJS (Mobile JKN)?

## 5. Catatan wawancara dan observasi

*(Diisi tim. Satu blok per partisipan — format di [template](../_template/01-empathize.md#5-catatan-wawancara-dan-observasi). Jangan mencatat data pribadi pasien.)*

## 6. Empathy map awal (dari riset sekunder)

Hipotesis awal untuk dibandingkan dengan hasil wawancara. Semua `[asumsi]` kecuali bertanda sumber.

**Petugas admisi**

| Says | Thinks |
|---|---|
| "Pasien sudah dikabari tetapi tidak membuka HP." (parafrase dari mitra) `[sumber: S]` | Sudah berusaha, tetapi tetap disalahkan pasien `[asumsi]` |
| **Does** | **Feels** |
| Menghubungi pasien satu per satu via WA `[sumber: W]` | Terburu-buru dan tertekan saat perubahan mendadak `[asumsi]` |

**Pasien**

| Says | Thinks |
|---|---|
| *(dari wawancara)* | "Sudah daftar dan datang jauh-jauh, kenapa tidak dikabari?" `[asumsi]` |
| **Does** | **Feels** |
| Daftar H-1 lewat WA, datang, menunggu lama `[sumber: S, W]` | Kecewa, merasa tidak dihargai `[sumber: S]` |

## 7. Pain points awal

| Kategori | Pain point | Bukti | Keparahan |
|---|---|---|---|
| Finansial | Biaya dan waktu perjalanan pasien terbuang | `[asumsi]` | Sedang |
| Produk | Jadwal di situs/sistem tidak bisa menyatakan perubahan harian | `[sumber: R]` | Tinggi |
| Proses | Admisi mengabari pasien manual satu per satu; daftar pasien per slot tidak digital | `[sumber: W, R]` | Tinggi |
| Proses | Informasi perubahan dari dokter ke unit lain lambat/terputus | `[sumber: W]` | Tinggi |
| Dukungan | Pasien tidak terjangkau karena jarang membuka HP; kanal WA terpisah-pisah | `[sumber: S, R]` | Tinggi |

## 8. Proto-persona (untuk divalidasi)

Persona sementara dari riset sekunder. Ganti setelah ada data wawancara.

**P-A · "Bu Sri", petugas admisi** `[asumsi]`
- Mengelola pendaftaran via WhatsApp dan telepon; juga melayani pasien datang langsung.
- Tujuan: semua pasien terlayani tanpa komplain.
- Pain point: kabar perubahan dari dokter datang mendadak; harus menghubungi banyak pasien sekaligus.
- Kebutuhan: satu tombol untuk mengabari semua pasien di slot terdampak, dan tahu siapa yang sudah membaca.

**P-B · "Pak Harjo", pasien lansia kontrol rutin** `[asumsi]`
- 65 tahun, kontrol bulanan ke spesialis penyakit dalam, diantar anak; jarang membuka HP.
- Tujuan: kontrol tepat waktu tanpa bolak-balik.
- Pain point: tidak membaca pesan WA; tahu dokter batal setelah sampai.
- Kebutuhan: kabar lewat kanal yang pasti sampai (telepon/SMS, atau ke anak).

**P-C · "Mbak Dina", pasien pekerja** `[asumsi]`
- 30 tahun, izin kerja setengah hari untuk periksa; aktif di HP.
- Tujuan: waktu tunggu singkat.
- Pain point: sudah izin kerja tetapi dokter terlambat/batal.
- Kebutuhan: kabar secepatnya dan bisa langsung pilih jadwal pengganti sendiri.

**Aksesibilitas:** pasien lansia, gangguan penglihatan, atau tidak terbiasa teknologi — pertimbangkan teks besar, bahasa sederhana, dan kanal suara.

## Checklist selesai

- [x] Riset sekunder dirangkum
- [x] Asumsi awal tim ditulis
- [ ] Wawancara (target: admisi 2, perawat 2, humas 1, dokter 1, IT 1, pasien 3–5)
- [ ] Observasi kontekstual di admisi dan ruang tunggu
- [ ] Empathy map diperbarui dari data primer
- [ ] Persona divalidasi

<!-- nav-bottom:start -->

---

◂ [README](README.md) · [▴ Atas](#) · [2 Define](02-define.md) ▸  
1 Empathize di proyek lain: [ARB-01](../arb-01/01-empathize.md) · [ARB-02](../arb-02/01-empathize.md) · [LKPI-01](../lkpi-01/01-empathize.md) · [LKPI-02](../lkpi-02/01-empathize.md) · [UMS-01](../ums-01/01-empathize.md) · [Template](../_template/01-empathize.md)
<!-- nav-bottom:end -->
