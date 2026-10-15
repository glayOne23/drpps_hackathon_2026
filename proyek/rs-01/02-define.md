# 2 · Define — RS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **RS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · **2 Define** · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/rs-ums-ar-fachrudin.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Understand** · sebelum 20 Okt · Proposal: Bag. 3, Bag. 4 butir 1 · PJ: ketua + koordinator validasi pengguna
> Panduan metode: [_template/02-define.md](../_template/02-define.md). Semua isian di bawah adalah draf dari riset sekunder.

## 1. User stories

| No | Persona | User story | Prioritas |
|---|---|---|---|
| US1 | Pasien (P-B, P-C) | Sebagai pasien yang sudah mendaftar, saya ingin tahu perubahan jadwal dokter sebelum berangkat, agar tidak datang sia-sia. | Tinggi |
| US2 | Pasien (P-C) | Sebagai pasien, saya ingin memilih jadwal pengganti sendiri dari pesan pemberitahuan, agar tidak perlu menelepon RS. | Tinggi |
| US3 | Admisi (P-A) | Sebagai petugas admisi, saya ingin mengabari semua pasien di slot terdampak sekaligus, agar tidak menghubungi satu per satu. | Tinggi |
| US4 | Admisi (P-A) | Sebagai petugas admisi, saya ingin melihat pasien mana yang belum menerima/membaca kabar, agar bisa menelepon mereka. | Tinggi |
| US5 | Dokter | Sebagai dokter, saya ingin memberi tahu RS bahwa saya terlambat/batal dengan satu langkah cepat, agar tidak perlu menelepon banyak pihak. | Tinggi |
| US6 | Perawat poli | Sebagai perawat poli, saya ingin melihat status kedatangan dokter secara real-time, agar bisa memberi informasi akurat ke pasien yang menunggu. | Sedang |
| US7 | Pasien lansia (P-B) | Sebagai pasien yang jarang membuka HP, saya ingin kabar juga dikirim ke anggota keluarga, agar tetap tahu. | Sedang |
| US8 | Humas | Sebagai humas, saya ingin menerima umpan balik pasien sebelum mereka menulis ulasan publik, agar keluhan tertangani lebih awal. | Sedang |
| US9 | Tim IT | Sebagai tim IT, saya ingin solusi terhubung lewat API ke SIMRS dan siap SATUSEHAT/BPJS, agar tidak membuat sistem baru yang terpisah. | Sedang |

## 2. User journey map — kondisi saat ini (draf)

**Persona:** P-B/P-C (pasien) · **Tujuan:** periksa ke dokter spesialis sesuai jadwal

| Tahap | Tindakan | Perasaan | Pain point | Peluang |
|---|---|---|---|---|
| 1. Cari jadwal | Lihat situs/IG atau tanya via WA | Netral | Jadwal di situs hanya pola mingguan `[sumber: R]` | Tampilkan status harian |
| 2. Daftar | Chat WA ke nomor pendaftaran, H-1 `[sumber: S]` | Lega | Tidak ada konfirmasi/nomor antrean terstruktur `[sumber: R]` | Booking dengan data kontak lengkap |
| 3. Jadwal berubah | Dokter tertahan *cito*; RS tahu mendadak `[sumber: S]` | — (pasien belum tahu) | Informasi lambat dari dokter ke RS `[asumsi]` | Dokter lapor status 1 ketukan |
| 4. RS mengabari | Admisi WA pasien satu per satu `[sumber: W]` | — | Pasien tidak membuka HP `[sumber: S]` | Multi-kanal + eskalasi |
| 5. Berangkat & menunggu | Pasien datang, menunggu lama `[sumber: W]` | Kesal | Waktu dan biaya terbuang | Kabar sebelum berangkat |
| 6. Setelah kejadian | Komplain/ulasan negatif `[sumber: W]` | Kecewa | Keluhan langsung ke ruang publik | Kanal umpan balik |

*Edge case:* dokter batal setelah pasien sudah tiba; pasien tanpa HP; nomor HP salah/tidak aktif.

## 3. 5W + H

| Pertanyaan | Jawaban (draf) |
|---|---|
| Who | Pasien rawat jalan spesialis dan petugas admisi RS UMS A.R. Fachrudin |
| What | Perubahan jadwal dokter tidak sampai ke pasien tepat waktu |
| Where | Pasien: di rumah/perjalanan; petugas: meja pendaftaran |
| When | Saat dokter tertahan di fasilitas lain, hampir setiap hari `[sumber: W]` |
| Why | Pasien kehilangan waktu dan biaya; kepuasan dan reputasi RS turun |
| How (sekarang) | Admisi mengirim WA manual; tidak ada pelacakan apakah pesan sampai |

## 4. Problem statement (draf)

> **Pak Harjo** adalah **pasien lansia yang kontrol rutin ke dokter spesialis dan jarang membuka HP** yang membutuhkan **kabar perubahan jadwal dokter yang pasti sampai sebelum ia berangkat** karena **pemberitahuan WhatsApp manual sering tidak terbaca, sehingga ia datang dan menunggu sia-sia.**

> **Bu Sri** adalah **petugas admisi yang menangani pendaftaran lewat WhatsApp** yang membutuhkan **cara mengabari semua pasien terdampak sekaligus dan mengetahui siapa yang belum terjangkau** karena **perubahan jadwal datang mendadak dan menghubungi pasien satu per satu tidak sempat.**

## 5. Need statement (draf)

> Cara untuk **memastikan pasien rawat jalan spesialis mengetahui perubahan jadwal dokter sebelum berangkat** pada **pasien RS UMS A.R. Fachrudin, termasuk yang jarang membuka HP**, yang **mengurangi kedatangan sia-sia dan komplain terkait jadwal**.

## 6. Kriteria keberhasilan

| No | Kriteria | Ukuran | Sekarang | Target | Sumber |
|---|---|---|---|---|---|
| K1 | Kecepatan notifikasi | Waktu dari status diperbarui → notifikasi terkirim | Manual, tidak terukur `[sumber: W]` | < 1 menit `[target]` | Indikator mitra `[sumber: W]` |
| K2 | Beban kerja admisi | Waktu/jumlah kontak manual per kejadian perubahan | Belum diketahui | Turun signifikan `[target]` | Indikator mitra `[sumber: W]` |
| K3 | Jangkauan | % pasien terdampak yang terkonfirmasi tahu sebelum jam praktik | Belum diketahui | [ ]% `[target]` | Usulan tim |
| K4 | Kemudahan pasien | % pasien yang berhasil konfirmasi/reschedule sendiri | 0 (tidak ada fitur) | [ ]% `[target]` | Indikator mitra `[sumber: W]` |
| K5 | Kesiapan integrasi | Rancangan kompatibel SIMRS/SATUSEHAT | — | Desain arsitektur tervalidasi Tim IT `[target]` | Indikator mitra `[sumber: W]` |

## 7. Hypothesis statements

| No | Hipotesis | Kriteria | Cara menguji |
|---|---|---|---|
| H1 | Jika dokter dapat memperbarui status dengan satu langkah, maka RS mengetahui perubahan lebih awal. | K1 | Uji dengan 1–2 dokter; ukur selisih waktu |
| H2 | Jika notifikasi dikirim multi-kanal dengan eskalasi (WA → SMS/telepon otomatis → kontak keluarga), maka lebih banyak pasien tahu sebelum berangkat. | K3 | Simulasi dengan data pasien uji |
| H3 | Kami yakin bahwa dashboard status penerimaan untuk admisi akan mengurangi kontak manual hanya ke pasien yang belum terjangkau. | K2 | Uji tugas dengan petugas admisi |
| H4 | Jika pasien bisa memilih jadwal pengganti dari tautan di pesan, maka reschedule tidak lagi memerlukan telepon ke RS. | K4 | Uji kegunaan dengan 3–5 pasien |

## 8. Value proposition (draf)

| Pertanyaan | Jawaban |
|---|---|
| Apa yang dilakukan? | Menyebarkan perubahan jadwal dokter dari sumbernya ke semua pasien terdampak secara otomatis, lewat kanal yang pasti sampai, dan memungkinkan pasien memilih jadwal pengganti sendiri |
| Mengapa peduli? | Pasien tidak datang sia-sia; admisi tidak mengabari satu per satu; RS terhindar dari komplain publik |
| Pembeda | Lapisan "pengecualian jadwal harian" di atas data yang sudah ada (`/api/jadwal`), eskalasi multi-kanal untuk pasien yang tidak membuka HP, desain modular siap SATUSEHAT `[asumsi]` |

## 9. Pertanyaan terbuka untuk mitra

- SIMRS apa yang dipakai, dan apakah terhubung dengan `/api/jadwal`?
- Di mana pasien per slot tercatat saat ini?
- Berapa pasien rawat jalan per hari, dan berapa kejadian perubahan jadwal per minggu?
- Berapa menit sebelum praktik biasanya perubahan diketahui?
- Apakah RS punya WhatsApp Business API resmi?
- Apakah RS melayani BPJS dan sudah terhubung antrean online Mobile JKN?
- Bagaimana ketentuan KI untuk tantangan ini?

## Checklist selesai

- [x] User stories berprioritas (draf)
- [x] Journey map kondisi saat ini (draf)
- [x] Problem dan need statement (draf)
- [x] Kriteria keberhasilan selaras indikator mitra
- [x] Hipotesis yang bisa diuji
- [ ] Semua draf dikonfirmasi lewat wawancara

<!-- nav-bottom:start -->

---

◂ [1 Empathize](01-empathize.md) · [▴ Atas](#) · [3 Ideate](03-ideate.md) ▸  
2 Define di proyek lain: [ARB-01](../arb-01/02-define.md) · [ARB-02](../arb-02/02-define.md) · [LKPI-01](../lkpi-01/02-define.md) · [LKPI-02](../lkpi-02/02-define.md) · [UMS-01](../ums-01/02-define.md) · [Template](../_template/02-define.md)
<!-- nav-bottom:end -->
