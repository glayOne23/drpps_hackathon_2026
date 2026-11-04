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

## Langkah yang hilang di alur (belum diperbaiki)

1. **Hasil kunjungan tidak bisa dicatat.** Sesudah check-in, sales tidak punya cara mencatat "tidak order + alasan" atau check-out, padahal tabel `kunjungan` memuat kolom "hasil kunjungan" dan kinerja sales harus terpantau. Usul: tambah tombol "Selesai kunjungan" di S2 dengan pilihan hasil (pesan / tidak order + alasan / tutup).
2. **Check-in bisa dilewati.** Tombol "Lewati, buat pesanan" di S2a, dan outlet ke-2 di S1 langsung membuka S3b tanpa check-in. Usul: wajibkan alasan bila check-in dilewati, dan tampilkan di D1.
3. **Tidak ada konfirmasi sesudah "Kirim pesanan".** Prototype langsung pindah ke S4, dan outlet tidak ditandai selesai di S1. Usul: toast/sheet "Pesanan tersimpan", lalu kembali ke S1 dengan outlet bertanda ✓.
4. **Pesanan ditolak buntu.** Kartu "Ditolak" di S4 tidak bisa diklik, jadi tidak ada langkah lanjut (pesan ulang sesuai sisa stok, atau kabari outlet via WhatsApp).
5. **"Ulangi pesanan terakhir" tidak tersambung**, padahal ini fitur inti (target ≤15 detik). S3 sudah terisi sejak awal, dan S3b (tanpa sinyal) tidak punya tombol ini. Usul: S3 mulai kosong → tombol Ulangi → S3 terisi.

## Hotspot prototype yang belum tersambung

- S0 "Lupa kata sandi?" (sales), S4 "Kirim sekarang", S3b "Lihat semua 16 produk", D1 baris "Toko Obat Waras".
- Outlet ke-3 sampai ke-5 di S1 membuka S2a milik Apotek Sehat Jebres.
- Dua flow bernama sama, "2 · Admin penjualan". Ganti nama salah satunya (misalnya "2b · Pembayaran").

## Data yang tidak konsisten

- S2: pesanan 19 Okt tertulis Rp1.420.000, tetapi "Ulangi" di S3 menghasilkan Rp915.000. Tempo 30 hari juga tidak cocok dengan jatuh tempo 3 Nov.
- D1: "Pesanan hari ini 14", padahal jumlah per status 13. Budi "1/5 outlet · 2 pesanan", padahal S4 menulis 5 pesanan hari ini dan S1 menunjukkan 2 check-in.
- S9: Direktur berlabel "Hanya baca", tetapi punya tombol "Atur target".

## UI

- Di S1, tombol "Outlet baru" menutupi kartu outlet ke-5.
- Halaman sales tidak punya menu profil/keluar.
