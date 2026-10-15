# 2 · Define — ARB-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-02** · [README](README.md) · [1 Empathize](01-empathize.md) · **2 Define** · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Understand** · sebelum 20 Okt · Proposal: Bag. 3, Bag. 4 butir 1 · PJ: ketua + koordinator validasi pengguna
> Panduan metode: [_template/02-define.md](../_template/02-define.md). Semua isian di bawah adalah draf dari riset sekunder.

## 1. User stories

| No | Persona | User story | Prioritas |
|---|---|---|---|
| US1 | Sales (P-A) | Sebagai sales, saya ingin mencatat kunjungan dan pesanan dari HP dalam hitungan detik meski sinyal lemah, agar tidak menghabiskan waktu di outlet. | Tinggi |
| US2 | Sales (P-A) | Sebagai sales, saya ingin melihat stok tersedia sebelum menjanjikan ke outlet, agar tidak mengecewakan pelanggan. | Tinggi |
| US3 | Admin gudang (P-B) | Sebagai admin gudang, saya ingin stok berkurang otomatis saat pesanan dibuat dan mendapat peringatan stok menipis, agar tidak menghitung manual. | Tinggi |
| US4 | Direktur (P-C) | Sebagai direktur, saya ingin melihat kinerja sales harian/bulanan dan outlet paling aktif di satu dashboard, agar tidak mengumpulkan laporan. | Tinggi |
| US5 | Sales (P-A) | Sebagai sales, saya ingin melihat riwayat transaksi dan catatan setiap outlet, agar kunjungan lebih personal. | Sedang |
| US6 | Sales (P-A) | Sebagai sales, saya ingin diingatkan outlet yang sudah waktunya pesan ulang atau jatuh tempo, agar tidak ada peluang terlewat. | Sedang |
| US7 | Admin penjualan | Sebagai admin, saya ingin prospek dari WhatsApp otomatis tercatat di CRM, agar tidak hilang di riwayat chat. | Sedang |
| US8 | Direktur (P-C) | Sebagai direktur, saya ingin data lama dari buku/spreadsheet bisa dipindahkan, agar riwayat tidak hilang. | Sedang |

## 2. User journey map — sales, kondisi saat ini (draf)

| Tahap | Tindakan | Perasaan | Pain point | Peluang |
|---|---|---|---|---|
| 1. Rencana kunjungan | Menentukan outlet dari ingatan/catatan `[asumsi]` | Netral | Tidak tahu outlet yang waktunya pesan ulang | Rekomendasi kunjungan |
| 2. Di outlet | Tanya kebutuhan, cek stok ke admin `[asumsi]` | Tidak yakin | Stok tidak diketahui real-time `[sumber: S]` | Stok terlihat di HP |
| 3. Catat pesanan | Tulis di buku/kirim chat `[sumber: S]` | Terburu-buru | Input berulang, bisa hilang | Input cepat, offline |
| 4. Serah ke admin | Admin menyalin ke catatan lain `[asumsi]` | — | Data tidak sinkron `[sumber: S]` | Satu sumber data |
| 5. Laporan | Direktur mengumpulkan dari beberapa sumber `[asumsi]` | — | Kinerja tidak terpantau `[sumber: S]` | Dashboard otomatis |

## 3. 5W + H

| Pertanyaan | Jawaban (draf) |
|---|---|
| Who | Sales lapangan, admin gudang/penjualan, direktur CV Arba'in |
| What | Data pelanggan, aktivitas sales, dan stok tidak terintegrasi |
| Where | Di outlet (sinyal lemah), gudang, kantor |
| When | Setiap kunjungan, setiap pesanan, setiap laporan |
| Why | Stok kosong/berlebih, peluang terlewat, kinerja tidak terpantau |
| How (sekarang) | Buku catatan, chat, pencatatan manual `[sumber: S]` |

## 4. Problem statement (draf)

> **Mas Budi** adalah **sales lapangan yang mengunjungi banyak outlet per hari dengan sinyal tidak stabil** yang membutuhkan **cara mencatat kunjungan dan pesanan secepat mungkin sambil mengetahui stok yang benar** karena **pencatatan di buku dan chat memakan waktu, sering tidak sinkron dengan gudang, dan membuatnya menjanjikan barang yang ternyata kosong.**

## 5. Need statement (draf)

> Cara untuk **menyatukan data pelanggan, aktivitas sales, dan stok dalam satu sumber yang selalu mutakhir** pada **distributor produk herbal skala UMKM dengan tim sales lapangan**, yang **mengurangi selisih stok dan peluang penjualan yang terlewat**.

## 6. Kriteria keberhasilan

| No | Kriteria | Ukuran | Sekarang | Target | Sumber |
|---|---|---|---|---|---|
| K1 | Integrasi data | Jumlah tempat data yang sama diinput | ≥ 2 (buku + chat + catatan gudang) `[asumsi]` | 1, tanpa input berulang `[target]` | Indikator mitra `[sumber: W]` |
| K2 | Kecepatan input | Detik untuk mencatat satu pesanan di lapangan | Belum diketahui | "Hitungan detik" `[sumber: W]` → [ ] detik `[target]` | Batasan mitra |
| K3 | Akurasi stok | Selisih stok sistem vs fisik | Belum diketahui | Turun `[target]` | Indikator mitra `[sumber: W]` |
| K4 | Pemantauan kinerja | Manajemen melihat kinerja harian/bulanan tanpa laporan manual | Tidak bisa `[sumber: S]` | Bisa `[target]` | Indikator mitra `[sumber: W]` |
| K5 | Keandalan | Input tetap tersimpan saat offline dan tersinkron | — | 100% `[target]` | Batasan mitra `[sumber: W]` |

## 7. Hypothesis statements

| No | Hipotesis | Kriteria | Cara menguji |
|---|---|---|---|
| H1 | Jika sales mencatat pesanan dari aplikasi offline-first dengan pilihan cepat, maka pencatatan selesai dalam hitungan detik dan tidak hilang. | K2, K5 | Uji tugas dengan sales; simulasi offline |
| H2 | Jika stok berkurang otomatis dari setiap pesanan, maka selisih stok sistem vs fisik turun. | K3 | Uji dengan data dummy + stock opname simulasi |
| H3 | Kami yakin bahwa pengingat pesan ulang berbasis riwayat outlet akan mengurangi peluang yang terlewat. | US6 | Uji dengan riwayat dummy; nilai oleh sales |
| H4 | Jika semua data berasal dari satu sumber, maka direktur bisa melihat kinerja tanpa laporan manual. | K1, K4 | Uji tugas dengan direktur |

## 8. Value proposition (draf)

| Pertanyaan | Jawaban |
|---|---|
| Apa yang dilakukan? | Satu aplikasi ringan yang menyatukan pelanggan, kunjungan sales, pesanan, dan stok, bekerja di HP sales meski sinyal lemah |
| Mengapa peduli? | Tidak ada lagi data tercecer; stok tidak salah janji; kinerja sales terlihat |
| Pembeda | Offline-first untuk lapangan, prospek WhatsApp tertangkap otomatis, rekomendasi kunjungan/pesan ulang `[asumsi]` |

## 9. Pertanyaan terbuka untuk mitra

- Berapa sales lapangan, outlet aktif, SKU, dan gudang?
- Apakah CRM juga mencakup alur klien maklon?
- Apakah ada sistem kasir/akuntansi yang harus disambungkan?
- Siapa yang menerima chat WA dari situs, dan bagaimana prospek ditindaklanjuti?
- Bisakah tim mendapat dummy data dan contoh nota/catatan?
- Bagaimana ketentuan KI untuk tantangan ini?

## Checklist selesai

- [x] Semua bagian Define (draf)
- [ ] Dikonfirmasi lewat wawancara dan observasi

<!-- nav-bottom:start -->

---

◂ [1 Empathize](01-empathize.md) · [▴ Atas](#) · [3 Ideate](03-ideate.md) ▸  
2 Define di proyek lain: [RS-01](../rs-01/02-define.md) · [ARB-01](../arb-01/02-define.md) · [LKPI-01](../lkpi-01/02-define.md) · [LKPI-02](../lkpi-02/02-define.md) · [UMS-01](../ums-01/02-define.md) · [Template](../_template/02-define.md)
<!-- nav-bottom:end -->
