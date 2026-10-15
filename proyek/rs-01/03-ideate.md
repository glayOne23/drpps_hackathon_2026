# 3 · Ideate — RS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **RS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · **3 Ideate** · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/rs-ums-ar-fachrudin.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Explore** · s.d. 20 Okt, diulang saat hackathon · Proposal: Bag. 4 butir 2 · PJ: koordinator teknis + seluruh tim
> Panduan metode: [_template/03-ideate.md](../_template/03-ideate.md)

## 1. How Might We

| Sudut | Bagaimana kita bisa ... |
|---|---|
| Perkuat yang baik | ... memanfaatkan alur informasi pasien yang sudah dibuat RS menjadi otomatis? |
| Jelajahi kebalikannya | ... membuat pasien yang mencari tahu status dokter, bukan RS yang mengabari? |
| Ubah status quo | ... membuat perubahan jadwal dicatat sekali oleh dokter dan langsung menyebar ke semua pihak? |
| Pecah masalah | ... (a) mempercepat RS tahu perubahan, (b) mempercepat pasien tahu, (c) memudahkan pasien pindah jadwal? |
| Hilangkan yang buruk | ... meniadakan pengiriman WA manual satu per satu? |
| Ubah kata sifat | ... membuat perubahan jadwal terasa terencana, bukan mendadak? |
| Pertanyakan asumsi | ... menjangkau pasien yang tidak membuka HP sama sekali? |
| Analogi | ... memberi kabar seperti status penerbangan (on-time, delay, batal) dengan pilihan rebooking? |

## 2. Competitive audit (draf)

**Tujuan audit:** membandingkan cara menyampaikan perubahan jadwal dan reschedule.

| Solusi | Langsung/tidak | Kekuatan | Kelemahan | Penilaian |
|---|---|---|---|---|
| Cara manual RS saat ini (WA oleh admisi) | — | Personal, tanpa biaya sistem | Lambat, tidak terlacak, bergantung pasien membuka WA `[sumber: S, W]` | Kurang |
| Situs RS (`/dokter`) | — | Jadwal mingguan publik | Tidak ada status harian; pendaftaran = WA `[sumber: R]` | Kurang |
| Antrean online BPJS (Mobile JKN) | Tidak langsung | Dipakai luas pasien BPJS | Perlu dicek: apakah memberi notifikasi perubahan jadwal `[asumsi]` | [cek] |
| Aplikasi telekonsultasi/booking (mis. Halodoc, disebut mitra sebagai acuan UX) | Tidak langsung | Pengalaman booking & reschedule mandiri `[sumber: W]` | Perlu dicek: integrasi dengan RS kecil, biaya `[asumsi]` | [cek] |
| SIMRS yang dipakai RS | Langsung | — | Belum diketahui | [cek] |
| Pemberitahuan maskapai (delay/rebooking) | Analogi | Status jelas + pilihan tindakan dalam satu pesan | — | Inspirasi |

**Celah (draf):** tidak ada lapisan status harian dokter; tidak ada pelacakan apakah pasien terjangkau; tidak ada kanal cadangan bagi pasien yang tidak membuka HP `[asumsi]`.

## 3. Crazy 8s

*(Diisi tim. Sesi yang disarankan: HMW "pecah masalah" (a), (b), (c) masing-masing satu sesi.)*

## 4. Kandidat ide (dari riset sekunder)

| No | Ide | Menjawab | Asal |
|---|---|---|---|
| I1 | **Lapisan pengecualian jadwal**: status harian per slot (praktik/terlambat/batal/pengganti) di atas `/api/jadwal` | US5, US6, pain point produk | Temuan situs RS |
| I2 | **Lapor status 1 ketukan** untuk dokter (tautan/WA bot/aplikasi web), memicu notifikasi otomatis | US5, H1 | HMW "ubah status quo" |
| I3 | **Notifikasi multi-kanal dengan eskalasi**: WA → SMS → panggilan suara otomatis → kontak keluarga, bila belum dibaca dalam X menit | US1, US7, H2 | HMW "pertanyakan asumsi" |
| I4 | **Dashboard admisi**: daftar pasien terdampak + status terkirim/dibaca/dikonfirmasi; telepon hanya yang belum | US3, US4, H3 | Pain point proses |
| I5 | **Reschedule mandiri** dari tautan di pesan (pilih slot pengganti) | US2, H4 | Acuan UX Halodoc `[sumber: W]` |
| I6 | **Booking sederhana** pengganti pendaftaran via chat, agar daftar pasien per slot tersedia digital | Prasyarat US1–US4 | Temuan situs RS |
| I7 | **Prediksi keterlambatan** dari pola historis per dokter/slot, untuk notifikasi lebih awal | Kedalaman teknologi | Catatan proposal |
| I8 | **Kanal umpan balik** setelah kunjungan, diteruskan ke humas | US8 | Arah solusi mitra `[sumber: W]` |
| I9 | **Desain konektor modular** SIMRS ↔ SATUSEHAT (FHIR) ↔ antrean BPJS | US9 | Arah solusi mitra `[sumber: W]` |
| I10 | **Validasi data jadwal** (jam mustahil, bentrok slot) | Kualitas data | Temuan situs RS (slot "00:00–00:04") |

## 4a. Rincian ide

Perkiraan upaya: **Rendah** = bisa dibuat dalam beberapa jam saat hackathon · **Sedang** = 1 hari · **Tinggi** = butuh data/akses yang belum ada atau lebih dari 3 hari. Semua rincian adalah usulan tim berbasis riset sekunder `[asumsi]` kecuali bertanda sumber.

### I1 · Lapisan pengecualian jadwal
- **Apa:** status harian per slot (praktik / terlambat X menit / batal / diganti dokter lain) yang disimpan di atas pola jadwal mingguan.
- **Cara kerja:** jadwal mingguan di `/api/jadwal` tetap menjadi pola `[sumber: R]`. Setiap perubahan dicatat sebagai pengecualian bertanggal. Situs dan dashboard menampilkan status hari ini, dan setiap pengecualian baru memicu notifikasi (I3).
- **Teknologi:** basis data + API REST; antrean event.
- **Menjawab:** US5, US6; pain point produk (jadwal tidak bisa menyatakan perubahan harian).
- **Kelebihan:** tidak mengganti sistem yang ada; fondasi semua ide lain.
- **Risiko / pertanyaan:** perlu akses ke backend situs/SIMRS; siapa yang berwenang mengubah status?
- **Butuh dari mitra:** akses API/admin, aturan wewenang.
- **Upaya:** Rendah · **Peran:** inti (fondasi)

### I2 · Lapor status satu ketukan untuk dokter
- **Apa:** dokter (atau perawat poli atas nama dokter) melaporkan status tanpa menelepon banyak pihak.
- **Cara kerja:** sebelum jam praktik, dokter menerima pesan "Praktik 13.00 hari ini?" dengan tombol *Tepat waktu / Terlambat 30 / Terlambat 60 / Batal*. Jawaban langsung masuk ke I1. Bila dokter tidak menjawab, perawat poli bisa mengisi.
- **Teknologi:** tombol interaktif WhatsApp Business API atau formulir web tanpa login (tautan sekali pakai).
- **Menjawab:** US5, H1, K1.
- **Kelebihan:** memindahkan informasi ke sumbernya; dokter tidak perlu memasang aplikasi.
- **Risiko / pertanyaan:** dokter lupa/enggan menjawab; ketentuan templat pesan WhatsApp; verifikasi identitas pengirim.
- **Butuh dari mitra:** kesediaan dokter, nomor kontak dokter/perawat poli.
- **Upaya:** Rendah–Sedang · **Peran:** inti

### I3 · Notifikasi multi-kanal dengan eskalasi
- **Apa:** kabar perubahan dikirim lewat kanal bertingkat sampai pasien terjangkau.
- **Cara kerja:** WhatsApp → bila belum dibaca dalam X menit, SMS → bila masih belum, panggilan suara otomatis (teks-ke-suara bahasa Indonesia) → kontak keluarga (bila pasien setuju). Aturan berbeda untuk "batal" dan "terlambat", dan memperhitungkan sisa waktu sebelum jam praktik.
- **Teknologi:** WhatsApp Business API (status terkirim/dibaca), SMS gateway, layanan panggilan suara/IVR, mesin aturan eskalasi.
- **Menjawab:** US1, US7, H2, K3.
- **Kelebihan:** menjawab akar masalah: pasien yang tidak membuka HP `[sumber: S]`.
- **Risiko / pertanyaan:** biaya per pesan/panggilan; tanda dibaca bisa dimatikan pengguna; persetujuan menghubungi keluarga (UU PDP).
- **Butuh dari mitra:** data kontak pasien dan keluarga, anggaran komunikasi.
- **Upaya:** Sedang (saat demo, kanal SMS/suara bisa disimulasikan) · **Peran:** inti

### I4 · Dashboard admisi
- **Apa:** daftar pasien terdampak per kejadian, dengan status *terkirim / dibaca / dikonfirmasi / gagal*.
- **Cara kerja:** satu layar per kejadian perubahan; tombol telepon untuk pasien yang belum terjangkau; log tersimpan sebagai bukti bila ada komplain.
- **Teknologi:** aplikasi web dengan pembaruan real-time.
- **Menjawab:** US3, US4, H3, K2.
- **Kelebihan:** kerja admisi berubah dari "mengabari semua" menjadi "menindaklanjuti yang tersisa"; humas punya bukti saat komplain.
- **Risiko / pertanyaan:** membutuhkan daftar pasien per slot dalam bentuk digital (I6).
- **Upaya:** Rendah–Sedang · **Peran:** inti

### I5 · Reschedule mandiri
- **Apa:** pasien memilih tindakan sendiri dari tautan di pesan.
- **Cara kerja:** pilihan *tetap menunggu (perkiraan jam baru) / pindah ke slot lain dokter yang sama / dokter pengganti / batal*. Kuota slot ikut diperbarui.
- **Teknologi:** halaman web mobile, token sekali pakai, aturan kuota.
- **Menjawab:** US2, H4, K4. Pengalaman seperti Halodoc yang disebut mitra `[sumber: W]`.
- **Kelebihan:** mengurangi telepon ke RS.
- **Risiko / pertanyaan:** pasien lansia kesulitan, jadi opsi telepon tetap perlu; aturan rujukan BPJS bila pindah tanggal.
- **Upaya:** Sedang · **Peran:** pendukung (inti bila waktu cukup)

### I6 · Booking sederhana
- **Apa:** pendaftaran yang menyimpan data pasien per slot, pengganti "pendaftaran online" yang sekarang berupa chat WhatsApp `[sumber: R]`.
- **Cara kerja:** formulir web atau bot WhatsApp menyimpan nama, nomor HP, kontak keluarga (opsional), dokter, dan tanggal. Bila SIMRS sudah menyimpan data ini, cukup ambil dari SIMRS.
- **Teknologi:** formulir web/bot + basis data; atau impor dari SIMRS.
- **Menjawab:** prasyarat US1–US4.
- **Kelebihan:** menutup celah "daftar pasien tidak digital".
- **Risiko / pertanyaan:** tumpang tindih dengan SIMRS atau antrean Mobile JKN; perubahan kebiasaan petugas dan pasien.
- **Butuh dari mitra:** penjelasan alur pendaftaran saat ini.
- **Upaya:** Rendah · **Peran:** prasyarat

### I7 · Prediksi keterlambatan dokter
- **Apa:** perkiraan peluang dokter terlambat/batal per slot, agar RS bisa bertindak lebih awal.
- **Cara kerja:** model belajar dari riwayat (dokter, hari, jam, pola keterlambatan). Bila peluang tinggi, sistem menyarankan admisi mengonfirmasi ke dokter lebih dulu. Awalnya hanya untuk internal, tidak dikirim ke pasien.
- **Teknologi:** model klasifikasi sederhana (mis. regresi logistik atau *gradient boosting*).
- **Menjawab:** K1 dan K3 lebih awal; aspek kedalaman teknologi (22%).
- **Kelebihan:** pembeda teknologi.
- **Risiko / pertanyaan:** data riwayat belum ada karena perubahan tidak tercatat sekarang. Mulai mengumpulkan data lewat I1; saat demo pakai data simulasi.
- **Upaya:** Tinggi · **Peran:** komponen *deeptech*, lanjutan

### I8 · Umpan balik pasien
- **Apa:** survei 1–3 pertanyaan via WhatsApp setelah kunjungan atau setelah kejadian perubahan jadwal.
- **Cara kerja:** skor rendah langsung diteruskan ke humas untuk ditindaklanjuti sebelum pasien menulis ulasan publik.
- **Menjawab:** US8; dampak "ulasan negatif" `[sumber: W]`.
- **Risiko / pertanyaan:** harus sesuai KODERSI (tidak memancing ulasan); jangan terlalu sering mengirim survei.
- **Upaya:** Rendah · **Peran:** pendukung

### I9 · Desain konektor SATUSEHAT/BPJS
- **Apa:** desain arsitektur modular, bukan implementasi penuh.
- **Cara kerja:** adaptor SIMRS → pemetaan data jadwal dan janji temu ke standar FHIR SATUSEHAT (cek resource yang tersedia di profil SATUSEHAT) `[asumsi]` → antrean online BPJS. Keluarannya dokumen arsitektur + contoh (*mock*).
- **Menjawab:** US9, K5; diminta mitra `[sumber: W]`.
- **Risiko / pertanyaan:** akses *sandbox* SATUSEHAT memerlukan registrasi faskes; topiknya kompleks.
- **Upaya:** Sedang (desain saja) · **Peran:** desain arsitektur

### I10 · Validasi data jadwal
- **Apa:** aturan pemeriksaan saat jadwal diinput (jam tidak masuk akal, bentrok slot, durasi nol) dan laporan data yang mencurigakan.
- **Contoh nyata:** slot "00:00–00:04" dan "00:34–14:36" di data situs `[sumber: R]`.
- **Upaya:** Rendah · **Peran:** pendukung kecil, mudah didemokan

## 4b. Paket solusi untuk dibahas

| Paket | Isi | Kekuatan | Risiko |
|---|---|---|---|
| **A · Minimum** | I6 + I1 + I2 + I3 (WhatsApp + 1 kanal cadangan) + I4 | Demo alur ujung-ke-ujung kuat; realistis 3 hari | Kurang unsur *deeptech* |
| **B · Disarankan** | A + I5 + I10 + I9 (desain) + I7 (data simulasi) | Lengkap sesuai arah mitra; ada pembeda teknologi | Beban kerja tinggi; I7 butuh penjelasan jujur soal data |
| **C · Ambisius** | B + I8 + integrasi SIMRS nyata | Paling dekat ke penerapan | Bergantung akses SIMRS yang belum pasti |

## 4c. Pertanyaan pemandu brainstorming

1. Masalah mana yang lebih besar: RS terlambat tahu perubahan, atau pasien tidak terjangkau kabar? Ide mana yang paling berdampak untuk masing-masing?
2. Apakah tim bisa mendapat daftar pasien per slot dari RS, atau harus membangun I6 dulu?
3. Bagaimana menjangkau pasien lansia yang tidak membuka HP tanpa melanggar privasi?
4. Apa unsur *deeptech* yang paling bisa dipertahankan di depan juri: I7, aturan eskalasi cerdas, atau lainnya?
5. Berapa biaya komunikasi per bulan yang masih masuk akal bagi RS?

## 5. Memilih ide

| Ide | Diinginkan | Layak teknis | Layak bisnis | Kebaruan | Lokal/KI | Total |
|---|---|---|---|---|---|---|
| I1–I10 | *(nilai 1–3, diisi tim setelah riset primer)* | | | | | |

**Usulan inti untuk proposal** `[asumsi]`: I1 + I2 + I3 + I4 sebagai fungsi inti; I5 + I6 sebagai fungsi pendukung; I7 sebagai komponen *deeptech*; I9 sebagai desain arsitektur (bukan implementasi penuh).

## 6. Goal statement (draf)

> Sistem kami akan memungkinkan **RS menyebarkan perubahan jadwal dokter ke semua pasien terdampak dalam hitungan detik lewat kanal yang pasti sampai**, yang akan memengaruhi **pasien rawat jalan dan petugas admisi** dengan **mengurangi kedatangan sia-sia dan kontak manual**. Kami akan mengukur efektivitasnya dengan **waktu kirim notifikasi (< 1 menit), % pasien terjangkau sebelum jam praktik, dan jumlah kontak manual per kejadian**.

## 7. Rancangan solusi untuk proposal

| Elemen | Isian |
|---|---|
| Cara kerja | [diisi setelah ide dipilih] |
| Teknologi inti | [mis. layanan notifikasi berbasis event, WA Business API/SMS gateway/IVR, model prediksi keterlambatan, FHIR] |
| Bagian yang dikerjakan tim | |
| Kebaruan | |
| Kelayakan | |
| Komponen lokal | |
| Peluang KI | Ketentuan KI tantangan belum disebut — tanyakan |

## Checklist selesai

- [x] HMW
- [x] Competitive audit (draf; beberapa baris perlu dicek)
- [x] Rincian ide, paket solusi, pertanyaan pemandu brainstorming
- [ ] Crazy 8s
- [x] Kandidat ide
- [ ] Ide dinilai dan dipilih
- [x] Goal statement (draf)

<!-- nav-bottom:start -->

---

◂ [2 Define](02-define.md) · [▴ Atas](#) · [4 Prototype](04-prototype.md) ▸  
3 Ideate di proyek lain: [ARB-01](../arb-01/03-ideate.md) · [ARB-02](../arb-02/03-ideate.md) · [LKPI-01](../lkpi-01/03-ideate.md) · [LKPI-02](../lkpi-02/03-ideate.md) · [UMS-01](../ums-01/03-ideate.md) · [Template](../_template/03-ideate.md)
<!-- nav-bottom:end -->
