# 6 · Implement — RS-01

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **RS-01** · [README](README.md) · [1 Empathize](01-empathize.md) · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · **6 Implement** · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/rs-ums-ar-fachrudin.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Materialize** · rencana di proposal; dijalankan s.d. April 2027 · Proposal: Bag. 4 butir 4 & 6 · PJ: koordinator bisnis & hilirisasi + operasional/regulasi
> Panduan metode: [_template/06-implement.md](../_template/06-implement.md)

## 1. Dukungan mitra

| Dukungan | Nyata / Rencana | Bukti |
|---|---|---|
| Diskusi kebutuhan dan alur layanan dengan Kepala Humas & Marketing serta manajemen RS | Diumumkan mitra di laman resmi `[sumber: W]` | Laman tantangan RS-01 |
| Skenario kasus nyata: alur penjadwalan poli, alur komplain, kebutuhan komunikasi pasien | Diumumkan `[sumber: W]` | Laman tantangan |
| Fasilitasi uji purwarupa dan evaluasi kelayakan di lingkungan RS | Diumumkan `[sumber: W]` | Laman tantangan |
| Akses data jadwal | API publik `/api/jadwal` tersedia `[sumber: R]`; akses data pasien/SIMRS: **rencana**, perlu izin | — |
| Kesediaan pilot setelah hackathon | Rencana — perlu dikonfirmasi | |

## 2. Regulasi dan standar

| Aspek | Berlaku? | Ketentuan | Langkah |
|---|---|---|---|
| Pelindungan data pribadi | **Ya** | UU PDP; data pasien termasuk data kesehatan `[sumber: W]` | Minimalkan data (nama, nomor HP, slot); persetujuan pasien; enkripsi; jangan kirim info medis di notifikasi |
| Etika komunikasi RS | **Ya** | KODERSI untuk komunikasi, informasi, dan promosi `[sumber: W]` | Tinjau isi pesan dan fitur promosi bersama humas |
| Interoperabilitas | **Ya** | SATUSEHAT (FHIR/API), antrean BPJS Kesehatan `[sumber: W]` | Desain konektor modular; cek resource FHIR yang relevan (mis. jadwal/appointment) `[asumsi]` |
| Arsitektur | **Ya** | Terbuka, modular, tidak terkunci satu vendor `[sumber: W]` | API terdokumentasi; pertimbangkan komponen open source |
| Komunikasi massal | Mungkin | Kebijakan WhatsApp Business API, SMS gateway `[asumsi]` | Cek ketentuan template pesan dan biaya |

## 3. Kekayaan intelektual

| Field | Isian |
|---|---|
| Ketentuan KI tantangan | **Tidak disebut** di laman tantangan — tanyakan ke mitra/panitia |
| Potensi KI | Hak cipta perangkat lunak; [algoritma eskalasi/prediksi bila baru] `[asumsi]` |
| Komponen pihak lain | [daftar library/layanan + lisensi] |

## 4. Model bisnis (draf)

| Elemen | Isian |
|---|---|
| Pengguna | Admisi, perawat poli, dokter, humas, pasien |
| Pembayar | RS UMS A.R. Fachrudin |
| Nilai bagi mitra | Lebih sedikit kedatangan sia-sia dan komplain; hemat waktu admisi; reputasi |
| Skema penerapan | Adopsi internal RS; peluang replikasi ke RS lain (mis. jaringan RS Muhammadiyah) `[asumsi]` |
| Biaya operasional | Server + biaya per pesan WA/SMS/IVR — [hitung] |
| Komponen lokal | Pengembangan oleh tim lokal; integrasi standar nasional SATUSEHAT |

## 5. Rencana kegiatan

Gunakan tabel di [template](../_template/06-implement.md#5-rencana-kegiatan-dan-milestone-612-bulan-sd-april-2027). Usulan *milestone* `[asumsi]`:
- Des 2026: integrasi dengan sumber jadwal RS dan data pendaftaran nyata.
- Jan–Feb 2027: pilot di 2–3 poli dengan perubahan jadwal paling sering.
- Mar 2027: evaluasi K1–K4; desain konektor SATUSEHAT divalidasi Tim IT.
- Apr 2027: laporan dan rencana adopsi penuh.

## 6–7. Hipotesis pendampingan dan dampak

*(Diisi setelah hackathon — format di [template](../_template/06-implement.md#6-hipotesis-untuk-siklus-pendampingan).)*

<!-- nav-bottom:start -->

---

◂ [5 Test](05-test.md) · [▴ Atas](#) · [Draf proposal](proposal-draf.md) ▸  
6 Implement di proyek lain: [ARB-01](../arb-01/06-implement.md) · [ARB-02](../arb-02/06-implement.md) · [LKPI-01](../lkpi-01/06-implement.md) · [LKPI-02](../lkpi-02/06-implement.md) · [UMS-01](../ums-01/06-implement.md) · [Template](../_template/06-implement.md)
<!-- nav-bottom:end -->
