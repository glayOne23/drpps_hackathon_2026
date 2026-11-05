# User flow SIGAP (ARB-02)

Disusun dari [proposal v03](Proposal_AntechAsync_v03_SIGAP_2026-11-04.docx) (Tabel C.2, C.3) dan Figma "SIGAP · Hi-fi v2". Kode layar (S1, S2a, …) mengikuti nama frame di Figma. Langkah bertanda **(usulan)** sudah ditambahkan ke Figma sebagai layar S2c, S2d, S4b, S4c (4 Nov 2026), S3e, S7d, S4d, dan S1b (5 Nov 2026), tetapi belum ada di purwarupa; lihat [review-figma-hifi-v2.md](review-figma-hifi-v2.md).

Versi visual (5 diagram, dibuat dari kode di bawah lewat "Convert Mermaid code to diagram"): [FigJam — SIGAP User Flow (ARB-02)](https://www.figma.com/board/Dtii8Pg38TnDXi29melNsM/SIGAP-%E2%80%94-User-Flow--ARB-02-). Semua diagram dikonversi ulang 5 Nov 2026 malam (alur ACC, kirim sebagian, pembayaran, manajemen akun); urutan di board dari kiri: Sales, Admin penjualan, Admin gudang, Direktur, Lintas peran. Bila alur berubah, ubah kode di sini lalu konversi ulang di FigJam.

## 1. Sales (PWA di HP)

```mermaid
flowchart TD
    A([Buka SIGAP dari layar utama]) --> B[S0 Masuk]
    B --> C[S1 Kunjungan hari ini<br/>urut: jatuh tempo, waktunya order, lama tidak dikunjungi]
    C -->|pilih outlet| D[S2a Check-in GPS dan jam]
    C -->|outlet belum terdaftar| N[S1a Outlet baru<br/>status menunggu validasi]
    C -->|ketuk sapaan| P{{"S1b Profil & keluar<br/>(usulan)"}}
    P -->|keluar, antrean kosong| B
    N --> F
    D -->|check-in| E[S2 Halaman outlet<br/>3 pesanan terakhir, tagihan]
    D -->|lewati| D2{{"S2d Alasan lewati check-in<br/>(usulan)"}}
    D2 --> E
    E -->|buat pesanan| F{Ada sinyal?}
    E -->|tidak order| H{{"S2c Hasil kunjungan<br/>tidak order + alasan (usulan)"}}
    F -->|ya| G0{{"S3e Form pesanan kosong<br/>(usulan)"}}
    G0 -->|Ulangi pesanan terakhir| G[S3 Form pesanan terisi<br/>ubah jumlah +/-]
    F -->|tidak| G2[S3b Form tanpa sinyal<br/>simpan di HP]
    G --> K[Kirim pesanan]
    G2 --> K2[Simpan di HP<br/>menunggu sinyal] -->|sinyal kembali, kirim otomatis| K
    K --> L{{"S4b Pesanan tersimpan<br/>outlet ditandai selesai (usulan)"}}
    H -->|simpan hasil| C
    L --> C
    K --> M[S4 Pesanan saya]
    M --> M1{Status dari server}
    M1 -->|"menunggu ACC, dikirim sebagian, selesai (belum ada di desain)"| M2
    M1 -->|diterima| M2[S4a Detail pesanan]
    M1 -->|diterima sebagian| M2
    M1 -->|ditolak: stok kurang| M3{{"S4c Tindak lanjut ditolak<br/>produk pengganti atau kabari outlet (usulan)"}}
    M -->|Kirim sekarang| M4{{"S4d Antrean terkirim<br/>(usulan)"}}
```

## 2. Admin penjualan

Diperbarui 5 Nov 2026 malam mengikuti Figma: pesanan dari HP kini **menunggu ACC** admin penjualan sebelum masuk antrean gudang.

```mermaid
flowchart TD
    A([L1 Masuk kantor]) --> B[D1 Dashboard admin penjualan]
    B --> C[S5 Kelola outlet]
    C --> C1[S5b Impor Excel] --> C2[S5c Gabung kemungkinan duplikat]
    C --> C3[S5e Validasi outlet baru dari sales]
    C --> C4[S5a Ubah / S5d Tambah outlet]
    B --> D[S6 Kelola pesanan]
    B -->|Urgent| K[S6k Filter perlu perhatian]
    D --> K
    D -->|Menunggu ACC| J[S6j Detail pesanan<br/>info stok kurang]
    K --> J
    J -->|ubah sebelum ACC| Q[S6q Ubah isi pesanan<br/>alasan wajib, sales diberi tahu]
    Q --> J
    J --> F[S6f ACC pesanan<br/>ketentuan bayar: tunai / tempo + jatuh tempo]
    F -->|Tolak pesanan| X{{"Tolak: alasan dan kabar ke sales<br/>(belum ada layar)"}}
    F -->|ACC & teruskan ke gudang| N[S6n Di-ACC, siap bayar]
    N --> O[S6o Catat pembayaran<br/>sebagian atau lunas, bukti wajib]
    O --> N
    N -. gudang kirim sebagian .-> H[S6h Dikirim sebagian · urgent]
    H --> G[S6g Tandai selesai<br/>menyusul / batalkan sisa / ganti produk]
    G --> I[S6i Selesai · tagihan dihitung ulang]
    I -->|Buka kembali| H
    D -->|Ubah, setelah kirim| P[S6p Ubah pesanan<br/>status, tempo, sales PJ; item terkunci]
    D -->|Bayar| C6[S6c Catat pembayaran] --> D6[S6d Pesanan lunas] --> E6[S6e Lihat bukti transfer]
    D -->|sebelum kirim| A6[S6a Batalkan pesanan<br/>alasan wajib]
    B --> M[S6m Riwayat pembayaran<br/>tidak bisa diubah, koreksi oleh direktur] --> E6
```

## 3. Admin gudang

```mermaid
flowchart TD
    A([L1 Masuk kantor]) --> B[D2 Dashboard admin gudang]
    B --> C[S7 Produk dan stok<br/>fisik, dipesan, tersedia]
    C --> C1[S7a Barang masuk<br/>batch + kedaluwarsa]
    C --> C2[S7b Penyesuaian stok opname<br/>alasan wajib]
    C --> C3[S7c Ubah data produk]
    C --> C4{{"S7d Tambah produk baru<br/>stok awal 0 (usulan)"}}
    C4 -->|lalu catat stok| C1
    B --> R[S7e Riwayat barang masuk]
    R --> R1[S7f Detail penerimaan<br/>selisih surat jalan, data terkunci]
    R1 -. koreksi jumlah .-> C2
    B --> D[S8 Antrean kirim<br/>pesanan yang sudah di-ACC]
    D -->|Proses| D1[S8a Proses kirim<br/>batch FEFO terisi otomatis, bisa diubah]
    D1 -->|stok cukup| OK[Konfirmasi kirim<br/>stok fisik dan dipesan berkurang]
    D1 -->|barang kurang atau rusak| D2[S8c Kirim sebagian<br/>alasan wajib, rusak ke karantina]
    D2 --> D3[S8d Belum lengkap · urgent]
    B -->|Urgent| D3
    D3 -->|barang masuk dicadangkan| S{{"Kirim susulan<br/>(belum ada layar)"}}
    D --> T[S8e Telusur batch<br/>outlet penerima, hubungi PIC]
    T --> T2{{"Mulai penarikan batch<br/>(belum ada layar)"}}
```

## 4. Direktur

```mermaid
flowchart TD
    A([L1 Masuk kantor]) --> B[S9 Dashboard direktur]
    B --> B1[Performa sales vs target]
    B --> B2[Outlet paling aktif, perputaran stok]
    B --> B3[Stok menipis, mendekati kedaluwarsa]
    B --> B4[Prediksi penjualan 4 minggu<br/>dan saran produksi]
    B1 --> C[S9a Atur target sales]
    B --> U[U1 Manajemen akun]
    U --> U1[U1a Tambah akun<br/>undangan WhatsApp 48 jam]
    U --> U2[U1b Ubah akun<br/>reset sandi, keluarkan perangkat]
    U --> U3[U1c Nonaktifkan akun<br/>pindahkan outlet binaan, alasan wajib]
    U2 --> U3
    U --> R[U2 Role & hak akses] --> R1[U2a Ubah hak akses per modul]
```

## 5. Alur lintas peran: satu pesanan

```mermaid
flowchart LR
    subgraph Sales
        S1[Buat pesanan di HP] --> S2[Terkirim ke server<br/>kode unik, tepat sekali]
    end
    subgraph Server
        S2 --> V[Reservasi stok tersedia<br/>kekurangan dicatat per baris]
    end
    subgraph Admin_penjualan[Admin penjualan]
        V --> P[Menunggu ACC]
        P -->|ubah isi| P
        P -->|tolak| T[Ditolak]
        P -->|ACC + ketentuan bayar| Q[Di-ACC]
        Q --> Y[Catat pembayaran]
        Z[Tandai selesai<br/>tagihan dihitung ulang]
    end
    subgraph Admin_gudang[Admin gudang]
        Q --> K[Proses kirim FEFO]
        K -->|lengkap| L[Dikirim]
        K -->|sebagian| U[Belum lengkap · urgent]
        M[Barang masuk] -->|dicadangkan dulu| U
        U -->|kirim susulan| L
    end
    subgraph Direktur
        L --> D[Dashboard: performa,<br/>perputaran stok, prediksi]
    end
    U --> Z
    T -.-> S3[Sales lihat status]
    U -.-> S3
```

Sisi sales (S4, S4a) belum menampilkan status baru "menunggu ACC", "dikirim sebagian", dan "selesai", serta notifikasi saat admin mengubah pesanan; lihat review.
