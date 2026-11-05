# User flow SIGAP (ARB-02)

Disusun dari [proposal v03](Proposal_AntechAsync_v03_SIGAP_2026-11-04.docx) (Tabel C.2, C.3) dan Figma "SIGAP · Hi-fi v2". Kode layar (S1, S2a, …) mengikuti nama frame di Figma. Langkah bertanda **(usulan)** sudah ditambahkan ke Figma sebagai layar S2c, S2d, S4b, S4c (4 Nov 2026), S3e, S7d, S4d, dan S1b (5 Nov 2026), tetapi belum ada di purwarupa; lihat [review-figma-hifi-v2.md](review-figma-hifi-v2.md).

Versi visual (5 diagram, dibuat dari kode di bawah lewat "Convert Mermaid code to diagram"): [FigJam — SIGAP User Flow (ARB-02)](https://www.figma.com/board/Dtii8Pg38TnDXi29melNsM/SIGAP-%E2%80%94-User-Flow--ARB-02-). Diagram Sales ada di paling kanan board (dikonversi ulang 5 Nov 2026 dengan S3e); diagram admin gudang (kedua dari kiri) dikonversi ulang 5 Nov 2026 dengan S7d. Bila alur berubah, ubah kode di sini lalu konversi ulang di FigJam.

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
    M1 -->|diterima| M2[S4a Detail pesanan]
    M1 -->|diterima sebagian| M2
    M1 -->|ditolak: stok kurang| M3{{"S4c Tindak lanjut ditolak<br/>produk pengganti atau kabari outlet (usulan)"}}
    M -->|Kirim sekarang| M4{{"S4d Antrean terkirim<br/>(usulan)"}}
```

## 2. Admin penjualan

```mermaid
flowchart TD
    A([L1 Masuk kantor]) --> B[D1 Dashboard admin penjualan]
    B --> C[S5 Kelola outlet]
    C --> C1[S5b Impor Excel] --> C2[S5c Gabung kemungkinan duplikat]
    C --> C3[S5e Validasi outlet baru dari sales]
    C --> C4[S5a Ubah / S5d Tambah outlet]
    B --> D[S6 Kelola pesanan]
    D --> D1{Perlu tindakan?}
    D1 -->|batal sebelum kirim| D2[S6a Batalkan<br/>alasan wajib, stok dipesan kembali]
    D1 -->|bayar| D3[S6c Catat pembayaran] --> D4[S6e Lihat bukti transfer] --> D5[S6d Pesanan lunas]
    D1 -->|"perlu perhatian: stok fisik kurang dari dipesan"| D6[Putuskan: kirim sebagian atau batal]
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
    B --> D[S8 Pengiriman dan telusur batch]
    D --> D1[S8a Konfirmasi kirim FEFO<br/>stok fisik dan dipesan berkurang]
    D --> D2[Telusur nomor batch<br/>outlet penerima, unduh Excel]
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
```

## 5. Alur lintas peran: satu pesanan

```mermaid
flowchart LR
    subgraph Sales
        S1[Buat pesanan di HP] --> S2[Terkirim ke server<br/>kode unik, tepat sekali]
    end
    subgraph Server
        S2 --> V{Stok tersedia cukup?}
        V -->|ya| R[Stok dipesan +q<br/>tersedia -q]
        V -->|tidak| X[Baris ditolak<br/>sisa stok tersedia X]
    end
    subgraph Admin_penjualan[Admin penjualan]
        R --> P[Pantau di Kelola pesanan]
        P -->|batal| B[Stok dipesan kembali]
    end
    subgraph Admin_gudang[Admin gudang]
        P --> K[Konfirmasi kirim FEFO<br/>stok fisik -q, outlet penerima tercatat]
    end
    subgraph Direktur
        K --> D[Dashboard: performa,<br/>perputaran stok, prediksi]
    end
    X --> S3[Sales lihat status Ditolak]
```
