# 1 · Empathize — ARB-02

<!-- nav:start -->
[◂ Semua proyek](../README.md) · **ARB-02** · [README](README.md) · **1 Empathize** · [2 Define](02-define.md) · [3 Ideate](03-ideate.md) · [4 Prototype](04-prototype.md) · [5 Test](05-test.md) · [6 Implement](06-implement.md) · [Draf proposal](proposal-draf.md)  
Referensi: [Mitra](../../docs/mitra/cv-arbain.md) · [Peran tim](../../docs/04-peran-tim.md) · [Template proposal](../../docs/03-template-proposal.md) · [Dokumen](../../docs/README.md)
<!-- nav:end -->

> **Understand** · s.d. pembekalan · Proposal: Bag. 4 butir 1 · PJ: koordinator validasi pengguna
> Panduan metode lengkap: [_template/01-empathize.md](../_template/01-empathize.md)

## 1. Ringkasan riset sekunder

Sumber utama: [docs/mitra/cv-arbain.md](../../docs/mitra/cv-arbain.md).

**Kondisi saat ini**
- Data pelanggan, aktivitas sales, dan stok tersebar di buku catatan dan pesan singkat; semuanya manual, sering tercecer dan tidak sinkron `[sumber: S]`.
- Penjualan B2B ke apotek, toko obat, minimarket `[sumber: S]`.
- Belum ada sistem terpusat; manajemen sulit memantau produktivitas sales, melacak riwayat pesanan per outlet, dan menjaga akurasi stok `[sumber: W]`.

**Data situs** `[sumber: A]`
- Semua jalur prospek (formulir konsultasi, tombol produk, tombol kategori) berakhir di **satu nomor WhatsApp** tanpa basis data; pesan templat sudah memuat jenis kebutuhan (mis. "saya ingin maklon Haircare").
- **Dua segmen pelanggan B2B:** klien maklon (siklus panjang: konsultasi → sampel → formula → desain → legalitas → produksi) dan outlet (siklus pendek: kunjungan → pesanan → *repeat order*). Laman tantangan hanya menyebut outlet.
- 16 produk grosir dan 12 kategori maklon (bahan katalog SKU awal).

**Dampak:** riwayat pelanggan sulit ditelusuri; kinerja dan kunjungan sales tidak terpantau; stok tidak sesuai gudang; layanan terlambat; peluang terlewat; risiko kehabisan atau kelebihan stok `[sumber: S, W]`.

**Yang diinginkan mitra** `[sumber: S]`: satu platform untuk tiga fungsi — aktivitas sales (jadwal kunjungan, progres prospek, target), data pelanggan (profil, riwayat transaksi, catatan interaksi), stok (berkurang otomatis, peringatan stok menipis).

## 2. Asumsi awal tim

| No | Asumsi | Hasil setelah riset |
|---|---|---|
| A1 | Jumlah sales lapangan kecil (2–5 orang) `[asumsi]` | |
| A2 | Sales lebih banyak memakai HP daripada laptop; sinyal di lapangan sering lemah `[sumber: W]` | |
| A3 | Pesanan outlet sering masuk lewat WA, bukan hanya saat kunjungan `[asumsi]` | |
| A4 | Pencatatan stok gudang dilakukan oleh satu admin di buku/spreadsheet `[asumsi]` | |
| A5 | Pelanggan maklon juga perlu dilacak di CRM `[asumsi]` | |
| A6 | Ada pola pemesanan ulang outlet yang bisa diprediksi `[asumsi]` | |

## 3. Rencana riset

### 3.1 Tujuan riset

1. Bagaimana alur dari kunjungan sales sampai barang terkirim dan dibayar?
2. Di mana saja data dicatat (buku, chat, spreadsheet), oleh siapa, dan kapan?
3. Bagaimana stok dihitung dan dicocokkan dengan gudang?
4. Bagaimana manajemen memantau sales sekarang?
5. Apakah alur klien maklon perlu masuk lingkup?

### 3.2 Partisipan

| Kelompok | Konteks | Target | Akses |
|---|---|---|---|
| Sales lapangan | Kunjungan outlet, input pesanan | 2–3 | Lewat mitra |
| Admin penjualan | Menerima pesanan, faktur | 1 | Lewat mitra |
| Admin gudang/stok | Mencatat stok masuk/keluar | 1 | Lewat mitra |
| Direktur/manajemen | Memantau kinerja | 1 | Narasumber sosialisasi |
| Pemilik apotek/toko obat | Pelanggan rutin | 1–2 | Lewat sales |

### 3.3 Metode

| Metode | Untuk | Catatan |
|---|---|---|
| Wawancara | Semua kelompok | |
| Observasi kontekstual (*ride-along*) | Ikut 1 sales berkunjung ke 2–3 outlet | Catat apa yang dicatat, di mana, berapa lama |
| Observasi gudang | Proses stok masuk/keluar | Bandingkan catatan vs fisik |
| Analisis artefak | Buku catatan, contoh nota, spreadsheet, chat pesanan (anonim) | Bahan desain data dan migrasi |

## 4. Pertanyaan wawancara khusus

**Sales**
- Ceritakan kunjungan terakhir Anda dari berangkat sampai pesanan tercatat.
- Di mana Anda mencatat pesanan dan catatan pelanggan? Pernah ada yang hilang?
- Bagaimana Anda tahu stok tersedia sebelum menjanjikan ke outlet?

**Admin gudang**
- Bagaimana Anda mencatat barang keluar? Seberapa sering hitungan tidak cocok?
- Kapan Anda tahu stok menipis?

**Manajemen**
- Bagaimana Anda tahu sales mana yang berprestasi?
- Laporan apa yang paling Anda butuhkan setiap minggu?

**Outlet**
- Bagaimana Anda memesan ulang? Apa yang sering bermasalah?

## 5. Catatan wawancara dan observasi

*(Diisi tim — format di [template](../_template/01-empathize.md#5-catatan-wawancara-dan-observasi).)*

## 6. Empathy map awal

**Sales lapangan**

| Says | Thinks |
|---|---|
| *(dari wawancara)* | "Mencatat itu memakan waktu kunjungan." `[asumsi]` |
| **Does** | **Feels** |
| Mencatat di buku/chat, menyampaikan pesanan ke admin `[sumber: S]` | Kesal bila stok ternyata kosong setelah dijanjikan `[asumsi]` |

**Manajemen**

| Says | Thinks |
|---|---|
| "Data tidak terintegrasi, kadang tidak sinkron." (parafrase) `[sumber: S]` | Tidak tahu peluang yang terlewat `[asumsi]` |
| **Does** | **Feels** |
| Mengumpulkan laporan dari beberapa sumber `[asumsi]` | Tidak yakin dengan angka yang ada `[asumsi]` |

## 7. Pain points awal

| Kategori | Pain point | Bukti | Keparahan |
|---|---|---|---|
| Finansial | Stok berlebih/kosong; peluang penjualan terlewat | `[sumber: S]` | Tinggi |
| Produk | Tidak ada sistem terpusat | `[sumber: W]` | Tinggi |
| Proses | Input berulang di buku, chat, dan catatan gudang; data tidak sinkron | `[sumber: S]` | Tinggi |
| Dukungan | Layanan pelanggan terlambat; riwayat pelanggan sulit ditelusuri | `[sumber: S]` | Sedang |

## 8. Proto-persona (untuk divalidasi)

**P-A · "Mas Budi", sales lapangan** `[asumsi]`
- Mengunjungi 8–15 outlet per hari dengan motor; HP Android kelas menengah; sinyal sering hilang.
- Kebutuhan: catat kunjungan dan pesanan dalam hitungan detik, cek stok sebelum menjanjikan.

**P-B · "Mbak Wati", admin gudang** `[asumsi]`
- Mencatat barang masuk/keluar; menghitung stok berkala.
- Kebutuhan: stok berkurang otomatis saat pesanan dibuat; peringatan stok menipis.

**P-C · "Pak Karno", direktur** `[asumsi]`
- Kebutuhan: dashboard kinerja sales, outlet paling aktif, perputaran stok — tanpa mengumpulkan laporan manual.

**P-D · "Bu Lina", pemilik apotek** `[asumsi]`
- Kebutuhan: pesanan ulang tercatat benar dan dikirim tepat waktu.

## Checklist selesai

- [x] Riset sekunder dirangkum; asumsi ditulis
- [ ] Wawancara, ride-along sales, observasi gudang
- [ ] Empathy map dan persona divalidasi

<!-- nav-bottom:start -->

---

◂ [README](README.md) · [▴ Atas](#) · [2 Define](02-define.md) ▸  
1 Empathize di proyek lain: [RS-01](../rs-01/01-empathize.md) · [ARB-01](../arb-01/01-empathize.md) · [LKPI-01](../lkpi-01/01-empathize.md) · [LKPI-02](../lkpi-02/01-empathize.md) · [UMS-01](../ums-01/01-empathize.md) · [Template](../_template/01-empathize.md)
<!-- nav-bottom:end -->
