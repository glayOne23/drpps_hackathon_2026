# PT Likuid Pharmalab Indonesia (PT LKPI) — Detail Kebutuhan Mitra

> Bagian dari [Kebutuhan Mitra UMS HI Hackathon 2026](../01-kebutuhan-mitra.md).
> Tantangan: **LKPI-01** dan **LKPI-02**. Kode sumber: [P] Pedoman, [W] laman hackathon, [S] transkrip sosialisasi 7 Okt 2026, [L] situs mitra https://likuid.co.id/ (diakses 14 Okt 2026).
> Folder kerja tim: [proyek/lkpi-01](../../proyek/lkpi-01/README.md) · [proyek/lkpi-02](../../proyek/lkpi-02/README.md)

---

## 1. Profil mitra

| Aspek | Keterangan | Sumber |
|---|---|---|
| Nama | PT Likuid Pharmalab Indonesia (PT LKPI); menyebut diri *"Medical Devices Principal"* | [L] |
| Usia | Merayakan milad ke-8 pada 2026 (berdiri ±2018) | [L] |
| Bidang | Manufaktur antiseptik, disinfektan tingkat tinggi, sterilan, dan bahan medis habis pakai (BMHP) | [L], [S] |
| Skala | >40 produk (47 item di katalog situs); mengklaim 2.000+ pelanggan; melayani RS, klinik, distributor, mitra internasional | [L] |
| Sertifikasi | ISO 13485:2016, CPAKB (Cara Pembuatan Alat Kesehatan yang Baik), Halal, TKDN; izin Kemenkes FK.01.03/VI/008-e/2019 dan FK.01.02/VI/692-e/2018; produk tercantum di LKPP | [L] |
| Merek | bayMEDIKA, BAYMED, MEDIKA, SASKLIN, BAYcide, BAYzime, BAYGEL | [L] |
| Pelanggan (testimoni) | RSUD Haji Makassar, RS PMI Bogor, RSKIA Annisa | [L] |
| Alamat | Kragilan RT 03/RW 09, Jetis, Baki, Sukoharjo, Jawa Tengah | [L] |
| Kontak | (0271) 6006032 · office@likuid.co.id · liquidpharmalab.lpi@gmail.com | [L] |
| Narasumber sosialisasi | Agus Maulana | [S] |

---

## 2. Temuan dari situs mitra (likuid.co.id)

### 2.1 Portofolio produk

Situs berbasis WordPress/WooCommerce. Sebaran 47 produk per kategori: Antiseptic 14, APD 8, BMHP 5, Walking Aid 5, Intensive Care 5, Wound Care 3, Kasa 2, CSSD 1, Sterilization 1, Alat Kesehatan 1, tanpa kategori 2.

Sebagian besar sediaan cair dijual dalam kemasan **500 ml, 1 L, 5 L, dan 20 L** (bahkan 200 L untuk alkohol). Izin edar terbagi dua jalur: **AKD** (alat kesehatan) dan **PKD** (perbekalan kesehatan rumah tangga/PKRT).

### 2.2 Produk yang terkait langsung dengan LKPI-01 (disinfektan H₂O₂ beraroma)

| Produk | Zat aktif | Fungsi | Izin edar |
|---|---|---|---|
| **SASKLIN Disinfectant Spray** | Benzalkonium chloride + **hidrogen peroksida** | Disinfektan permukaan tanpa alkohol, siap pakai, non-korosif, tanpa residu. 500 ml, 5 L, 20 L. **Tidak ada parfum di komposisi yang tercantum** | Kemenkes PKD 20502120681 |
| **BAYMED Plus h2o2** | Alkohol 80% + H₂O₂ 0,125% | Antiseptik tangan | Kemenkes PKD 20501024158 |
| BAYMED Plus Disinfectant Spray | (tidak dirinci) | Dekontaminasi permukaan alat (tempat tidur pasien, meja operasi); 6-log reduction | Kemenkes AKD 20903021869 |
| SASKLIN Plus Handsanitizer, SASKLIN Handsanitizer Spray, MEDIKA Handrub, SASKLIN Handwash | Alkohol 70% / benzalkonium chloride | Antiseptik tangan **dengan parfum** (Handwash beraroma bunga peony) | PKD |

**Pengamatan:** LKPI sudah berpengalaman memakai parfum pada sistem alkohol dan benzalkonium chloride, dan sudah punya disinfektan permukaan berbasis H₂O₂ tanpa parfum. Produk baru di LKPI-01 tampaknya menggabungkan keduanya: disinfektan **ruangan** berbasis H₂O₂ yang diberi parfum. Ini dugaan dari katalog dan perlu dikonfirmasi ke mitra (apakah ini varian SASKLIN Disinfectant atau produk baru).

### 2.3 Produk yang terkait langsung dengan LKPI-02 (precision dosing)

| Produk | Fungsi | Kemasan | Rasio pengenceran | Izin edar |
|---|---|---|---|---|
| **BAYzime** Detergen Alkali Enzimatik | Pembersih instrumen (enzim protease + amilase, surfaktan, agen disinfektan), memecah biofilm; 6-log reduction | 1 L, 5 L | **20 ml per 2,5 L air (1:125)** | Kemenkes AKD 20903021330 |
| **BAYcide** High Level Disinfectant | Disinfeksi tingkat tinggi instrumen dengan perendaman setelah pembersihan | 1 L, 5 L | **20 ml per 1 L air (1:50)** | Kemenkes AKD 20903021178 |
| BAYcide Ready to Use | HLD siap pakai (DDAC) | 5 L, 20 L | Tanpa pengenceran | Kemenkes AKD 20903321709 |

**Pengamatan:**
- **BAYzime dan BAYcide sama-sama memakai takaran 20 ml** dan sama-sama dijual dalam jeriken 5 L, serta dipakai berurutan di alur reprosesing instrumen CSSD (pembersihan enzimatik → disinfeksi tingkat tinggi). Satu desain pompa 20 ml berpotensi dipakai untuk kedua produk, dan materialnya harus tahan terhadap keduanya.
- Banyak produk lain dijual dalam jeriken 5 L dan 20 L (Povidine, Handrub, Alkohol, Chlorhexidine scrub, SASKLIN Disinfectant). Ini relevan untuk fokus "otomasi lini produksi" (pengisian/filling cair).

---

## 3. Tantangan LKPI-01 — Formulasi Disinfektan Beraroma

**Judul:** Inovasi Formulasi Disinfektan dengan Karakteristik Aroma yang Sesuai Kebutuhan Pengguna
**Detail resmi:** https://ihub.ums.ac.id/hackathon/tantangan/lkpi-01-inovasi-formulasi-disinfektan-dengan-karakteristik-aroma-yang-sesuai-kebutuhan-pengguna

### 3.1 Masalah inti

PT LKPI sedang mengembangkan **disinfektan ruangan berbasis hidrogen peroksida (H₂O₂)** dengan tambahan parfum. Parfum, H₂O₂, dan surfaktan **tidak kompatibel (tidak bisa homogen)**, dan formula yang menstabilkan keduanya belum ditemukan [S].

### 3.2 Mengapa perlu parfum [S, W]

- Aroma menjadi **penanda sensorik bahwa ruangan sudah didisinfeksi**.
- Aroma juga menutupi bau khas zat aktif.

### 3.3 Empat kendala teknis yang disebut mitra [S]

1. **H₂O₂ termolabil** — tidak tahan suhu tinggi, padahal uji stabilitas memerlukan suhu tinggi.
2. **Parfum** — terdegradasi oleh oksidator; wangi tidak keluar, atau parfum justru mengganggu stabilitas zat aktif [W].
3. **Surfaktan** — tidak kompatibel dengan sistem.
4. **Homogenitas** — campuran tidak menyatu/terjadi pemisahan fase.

### 3.4 Arah solusi awal [W] (contoh, belum final)

- Pemilihan agen *solubilizer* atau surfaktan pelindung.
- Enkapsulasi/mikroenkapsulasi aroma.
- Ko-solven atau stabilizer yang kompatibel.
- Senyawa *fragrance* yang tahan oksidasi.

Tujuannya: aroma keluar optimal dan bertahan sebagai penanda disinfeksi, zat aktif tetap stabil, daya bunuh mikroba tidak turun.

### 3.5 Pengguna [W]

- Tim R&D dan Produksi PT LKPI.
- Fasilitas pelayanan kesehatan (RS/klinik) sebagai pengguna akhir.

### 3.6 Keluaran yang diharapkan [W]

- Prototipe/sampel formula disinfektan beraroma yang stabil dan homogen.
- Dokumen rasionalisasi ilmiah: komposisi, metode pencampuran, spesifikasi bahan tambahan.
- Data uji awal:
  - organoleptik (intensitas dan ketahanan aroma)
  - stabilitas fisikokimia (pH, kejernihan, ketahanan suhu)
  - potensi efikasi antimikroba

### 3.7 Batasan [W]

- Formula harus memperhitungkan sifat zat aktif yang reaktif dan sensitif suhu.
- Eksipien, stabilizer, dan parfum harus aman untuk ruang medis: tidak meninggalkan residu berbahaya, tidak memicu iritasi pernapasan.
- **HKI atas formula sepenuhnya milik PT LKPI, tanpa skema royalti.**

### 3.8 Indikator keberhasilan [W]

- Formula tetap homogen, tanpa pemisahan fase, tanpa penurunan kadar zat aktif yang drastis.
- Aroma stabil dan jelas tercium saat diaplikasikan di ruangan.
- Lulus **uji stabilitas dipercepat** dan **uji efektivitas antimikroba** sesuai standar PT LKPI.

### 3.9 Dukungan mitra [W]

- Pendampingan teknis dan diskusi terarah bersama Tim R&D.
- Parameter standar mutu dan fasilitasi evaluasi kelayakan formula di laboratorium mitra.

### 3.10 Catatan untuk penyusun proposal

- **Perhatikan ketentuan HKI.** Formula menjadi milik penuh PT LKPI tanpa royalti, berbeda dengan LKPI-02. Ini memengaruhi aspek "kekayaan intelektual" di penilaian (10%) dan perlu disepakati sejak awal oleh tim.
- **Titik awal formula sudah ada.** SASKLIN Disinfectant Spray (benzalkonium chloride + H₂O₂) menunjukkan sistem H₂O₂ + surfaktan kationik yang sudah lolos izin edar. Tanyakan apakah formula ini bisa menjadi basis, sehingga masalahnya menyempit menjadi "menambahkan parfum tanpa merusak stabilitas".
- Hackathon hanya 3 hari, sedangkan uji stabilitas dipercepat biasanya butuh berminggu-minggu. Pisahkan apa yang bisa ditunjukkan saat demo day (homogenitas, organoleptik, pH awal, stres termal singkat) dan apa yang dilanjutkan pada pendampingan hingga April 2027.
- Kendala termolabil vs uji stabilitas suhu tinggi bisa dijawab dengan desain protokol uji yang sesuai, bukan hanya formula.
- Panitia sendiri mengaku kurang memahami istilah teknis tantangan ini [S], jadi proposal perlu menjelaskan mekanisme kimianya dengan bahasa yang jelas bagi juri lintas disiplin.
- Jalur regulasi kemungkinan **PKRT (PKD)** seperti SASKLIN Disinfectant Spray, karena untuk ruangan/permukaan, bukan instrumen.
- Disiplin yang relevan: farmasi (teknologi farmasi/formulasi), kimia, mikrobiologi; teknik kimia untuk *scale-up*.

---

## 4. Tantangan LKPI-02 — Otomasi Produksi dan Precision Dosing

**Judul:** Inovasi Peralatan Otomatisasi Produksi dan Sistem Penakaran Presisi (Precision Dosing) Sediaan Cair Medis
**Detail resmi:** https://ihub.ums.ac.id/hackathon/tantangan/lkpi-02-otomatisasi-peralatan-produksi-disinfektan

### 4.1 Masalah inti

Ada dua sisi masalah [W]:

1. **Manufaktur:** PT LKPI butuh peralatan otomasi untuk mempercepat produksi dan menjaga konsistensi mutu sediaan cair.
2. **Aplikasi di rumah sakit:** Detergen enzimatik **BAYzime kemasan jeriken 5 liter** dipakai untuk membersihkan instrumen bedah di kamar operasi atau **CSSD** (*Central Sterile Supply Department*). Pengguna harus mengencerkan **20 ml cairan ke 2,5 liter air**. Penuangan manual sering tumpah dan takarannya tidak akurat.

### 4.2 Kondisi saat ini [S]

- Penakaran masih manual dengan **gelas takar**.
- Mitra kesulitan menuangkan dari jeriken ke takaran yang diinginkan, dan **belum ada dispenser** untuk mengalirkan cairan dari jeriken ke takaran 20 ml.
- Panitia merangkum kebutuhannya sebagai "pompa mini otomatis" untuk kapasitas sangat kecil [S].

### 4.3 Arah solusi awal [W] — peserta memilih salah satu fokus

1. Alat otomasi untuk lini produksi sediaan cair di pabrik mitra, **atau**
2. Alat bantu takar/pompa dosing (mekanis maupun berbasis sensor/otomatis) yang **terpasang pada jeriken 5 liter** dan mengeluarkan **20 ml per takaran tanpa tumpah**.

### 4.4 Pengguna [W]

- Divisi Produksi, R&D, dan Packaging Development PT LKPI.
- Tenaga kesehatan dan petugas CSSD/kamar operasi di RS pengguna produk PT LKPI.

### 4.5 Keluaran yang diharapkan [W]

- Purwarupa fungsional yang siap diuji coba.
- Desain teknis (CAD/3D), *Bill of Materials* (BoM), dan estimasi biaya produksi.
- Hasil **uji repeatability** untuk akurasi volume dan kinerja alat.

### 4.6 Batasan [W]

- Material **tahan bahan kimia** terhadap detergen enzimatik dan disinfektan berbasis H₂O₂.
- Untuk pompa jeriken 5 L: ergonomis, tidak bocor, mengeluarkan 20 ml secara konsisten, ekonomis diproduksi massal.
- **HKI alat tetap milik tim inovator.** Jika diadopsi PT LKPI, berlaku **skema royalti**.

### 4.7 Indikator keberhasilan [W]

- **Deviasi volume/proses < 5%.**
- Mudah dipakai di lapangan tanpa alat ukur terpisah.
- Siap diintegrasikan ke lini produksi atau kemasan distribusi PT LKPI.

### 4.8 Dukungan mitra [W]

- Pendampingan dari tim R&D, Technical Services, dan Packaging Development.
- Sampel kemasan atau spesifikasi fisik untuk pengujian.
- Peluang kerja sama lisensi/royalti bagi tim pemenang.

### 4.9 Catatan untuk penyusun proposal

- **Rancang untuk dua produk sekaligus.** BAYzime (20 ml/2,5 L) dan BAYcide HLD (20 ml/1 L) memakai takaran yang sama dan jeriken 5 L yang sama. Pompa yang tahan terhadap keduanya memperluas pasar alat tanpa desain tambahan.
- Fokus 2 (pompa 20 ml di jeriken) jauh lebih jelas lingkupnya dan realistis dibuat purwarupanya dalam waktu program. Fokus 1 (otomasi lini produksi) butuh data lini produksi yang belum dijelaskan, meski portofolio jeriken 5 L/20 L menunjukkan kebutuhan pengisian yang besar.
- Dua jalur desain untuk CSSD: **pompa mekanis volume tetap** (murah, tanpa listrik, cocok dibundel dengan kemasan) atau **dispenser elektronik** (pompa peristaltik/diafragma + sensor, lebih presisi tetapi lebih mahal). Pilih berdasarkan target harga per unit.
- Kepemilikan HKI di tangan tim dan skema royalti membuat tantangan ini paling menarik untuk aspek "komponen lokal dan KI" (10% di proposal dan demo).
- **Lokasi uji dekat:** RS UMS A.R. Fachrudin punya instalasi bedah/kamar operasi (lihat [RS UMS](rs-ums-ar-fachrudin.md)), dan laman hackathon menyebut akses uji di RS UMS dan RSGM.
- Dari tanya jawab [S]: panitia menyarankan tim melibatkan dosen teknik mesin dan/atau teknik informatika/elektro yang punya rekam jejak riset terkait.
- Disiplin yang relevan: teknik mesin, teknik elektro/mekatronika, desain produk, farmasi (kompatibilitas material dan penggunaan di CSSD).

---

## 5. Pertanyaan untuk mitra

**LKPI-01**
- Berapa konsentrasi H₂O₂ yang dipakai, dan apakah formula SASKLIN Disinfectant Spray bisa menjadi basis?
- Metode aplikasinya apa: semprot, *fogging*, atau lap?
- Surfaktan dan parfum apa saja yang sudah dicoba, dan bagaimana hasilnya?
- Standar uji efikasi apa yang dipakai (mis. EN/AOAC), dan berapa target masa simpan?
- Apakah jalur izin edarnya PKRT (PKD) atau AKD?

**LKPI-02**
- Berapa dimensi dan ukuran ulir tutup jeriken 5 L, dan berapa viskositas BAYzime dan BAYcide?
- Apakah pompa ikut dijual bersama kemasan, dipinjamkan ke RS, atau dijual terpisah? Berapa target harga per unit?
- Untuk fokus produksi: proses apa yang paling lambat saat ini (pengisian, penutupan, pelabelan), dan berapa volume produksi per hari?
