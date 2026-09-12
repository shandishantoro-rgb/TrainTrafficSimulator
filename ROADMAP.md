# ROADMAP.md — Urutan Pembangunan TTC

> **ATURAN:** Tahap dikerjakan **berurutan**. Tidak boleh melompat.
> Sebuah tahap baru boleh dimulai bila tahap sebelumnya sudah dicentang
> oleh **Pemilik Proyek** (bukan oleh AI).
>
> Kolom **Bukti Selesai** ditulis dari sudut pandang orang awam:
> apa yang Pemilik Proyek klik, dan apa yang harus muncul di layar.

Status: `[ ]` belum · `[~]` sedang dikerjakan · `[x]` selesai & diverifikasi Pemilik Proyek

---

## Tahap 0 — Fondasi Kendali `[~]`

Menaruh dokumen kendali di repo dan membersihkan struktur.

**Isi pekerjaan**
- `PROJECT.md`, `ROADMAP.md`, `STATE.md`, `PERINTAH.md`, `GLOSARIUM.md` masuk ke repo.
- Buat folder `app/` untuk aplikasi web; kode Python lama dipindah ke `referensi-python/`.
- Buat `app/index.html` kosong yang sudah bisa dibuka (menampilkan tulisan "TTC v0.1").

**Bukti Selesai**
Saya buka file `app/index.html` di browser → muncul halaman putih bertuliskan **TTC — Train Traffic Simulator**.

---

## Tahap 1 — Data Jaringan Lintas `[ ]`

Aplikasi bisa menyimpan data prasarana.

**Isi pekerjaan**
- Struktur data: Stasiun (kode, nama, km, jumlah jalur, jenis: stasiun/perhentian).
- Struktur data: Petak Jalan antar stasiun (jarak, jalur tunggal/ganda, kecepatan maksimum).
- Simpan & buka file proyek `.json`.

**Bukti Selesai**
Saya isi 5 stasiun contoh (mis. Bogor–Manggarai) → klik **Simpan** → dapat file `.json` →
saya tutup aplikasi, buka lagi, klik **Buka** → 5 stasiun itu muncul kembali persis sama.

---

## Tahap 2 — Tabel Editor Data `[ ]`

Data di Tahap 1 bisa dilihat dan diubah lewat tabel, bukan lewat kode.

**Isi pekerjaan**
- Panel **Peta Jalur**: tabel stasiun bisa tambah / ubah / hapus / urutkan.
- Panel **Properti**: mengubah nilai satu baris terpilih.
- Validasi: km tidak boleh mundur, kode stasiun tidak boleh kembar.

**Bukti Selesai**
Saya tambah stasiun baru di tengah lintas → urutan km otomatis benar.
Saya isi kode stasiun kembar → muncul peringatan merah dan data ditolak.

---

## Tahap 3 — Mesin Waktu Tempuh `[ ]`

Aplikasi bisa menghitung berapa lama KA menempuh tiap petak.

**Isi pekerjaan**
- Hitung waktu tempuh dasar dari jarak & kecepatan.
- Tambahan waktu berhenti di stasiun (dwell time).
- Tambahan waktu untuk berangkat & mengerem (start/stop penalty).
- Waktu Tambahan (WT) per petak yang bisa diisi manual.

**Bukti Selesai**
Saya ubah kecepatan satu petak dari 70 → 50 km/jam →
angka waktu tempuh petak itu bertambah, dan totalnya ikut berubah.

---

## Tahap 4 — Generator Jadwal Otomatis `[ ]`

**Inti aplikasi.** Jadwal dibuat otomatis, tidak diketik satu-satu.

**Isi pekerjaan**
- Masukan: relasi (stasiun awal–akhir), jam operasi, headway/frekuensi, arah.
- Keluaran: daftar KA lengkap dengan jam datang & berangkat di setiap stasiun.
- Penomoran KA otomatis dengan pola yang bisa diatur.

**Bukti Selesai**
Saya isi: relasi Bogor–Jakarta Kota, 05.00–22.00, headway 10 menit →
klik **Buat Jadwal** → muncul daftar puluhan KA beserta jam di tiap stasiun,
dan jam KA pertama = 05.00.

---

## Tahap 5 — Penggambar GAPEKA `[ ]`

Jadwal Tahap 4 digambar menjadi grafik.

**Isi pekerjaan**
- Sumbu mendatar = waktu, sumbu tegak = stasiun berskala jarak (km).
- Garis miring tiap KA; arah hilir/hulu dibedakan warna.
- Garis kisi jam & 10 menit; nomor KA tertulis di ujung garis.
- Zoom dan geser (pan).

**Bukti Selesai**
Setelah Tahap 4, saya klik tab **GAPEKA** → muncul grafik garis-garis kereta
yang bentuknya mirip GAPEKA cetak. Saya zoom → garis tetap tajam, tulisan terbaca.

---

## Tahap 6 — Deteksi Konflik `[ ]`

Aplikasi menandai jadwal yang tidak mungkin dijalankan.

**Isi pekerjaan**
- Persilangan di petak jalur tunggal.
- Penyusulan tanpa jalur yang cukup.
- Pelanggaran headway minimum.
- Okupansi jalur stasiun melebihi jumlah jalur yang tersedia.

**Bukti Selesai**
Saya sengaja buat headway 2 menit di lintas tunggal → muncul daftar konflik
dan titik konfliknya **disorot merah di grafik GAPEKA**.

---

## Tahap 7 — Simulasi Berjalan `[ ]`

**Isi pekerjaan**
- Jam simulasi (play / pause / percepat).
- Posisi tiap KA bergerak di sepanjang lintas mengikuti jam.

**Bukti Selesai**
Saya klik **Play** → penunjuk waktu berjalan di grafik dan titik-titik KA bergerak.

---

## Tahap 8 — Ekspor Hasil Kerja `[ ]`

**Isi pekerjaan**
- Ekspor GAPEKA ke PDF & PNG.
- Ekspor Daftar Waktu ke Excel (`.xlsx`) / CSV.

**Bukti Selesai**
Saya klik **Ekspor PDF** → dapat file PDF yang bisa dicetak dan tulisannya tajam.

---

## Tahap 9 — Sirkulasi Rangkaian (TS) `[ ]`

**Isi pekerjaan**
- Merangkai perjalanan menjadi putaran/dinasan satu rangkaian.
- Hitung kebutuhan jumlah rangkaian (TS) dan waktu putar di ujung.

**Bukti Selesai**
Muncul angka **kebutuhan TS** dan daftar putaran per rangkaian.

---

## Tahap 10 — Perapian & Rilis v1.0 `[ ]`

**Isi pekerjaan**
- Tampilan disamakan dengan desain acuan (K5).
- Buku petunjuk singkat berbahasa Indonesia.
- Publikasi lewat GitHub Pages agar bisa dibuka lewat link.

**Bukti Selesai**
Saya kirim satu link ke rekan kerja → dia bisa membuka TTC di komputernya
tanpa memasang apa pun.
