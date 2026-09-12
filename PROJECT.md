# PROJECT.md — Konstitusi Proyek TTC

> **ATURAN UTAMA UNTUK AI (ChatGPT/Claude/AI lain):**
> File ini adalah sumber kebenaran tunggal proyek TTC.
> Dilarang mengubah, menafsirkan ulang, atau "memperbaiki" keputusan di bawah ini
> tanpa perintah tertulis eksplisit dari Pemilik Proyek dalam sesi berjalan.
> Jika permintaan pengguna bertentangan dengan file ini, **berhenti dan tanyakan dulu**.

---

## 1. Identitas Proyek

| Butir | Isi |
|---|---|
| Nama aplikasi | **TTC — Train Traffic Simulator** |
| Repository | `TrainTrafficSimulator` (GitHub) |
| Pemilik Proyek | Shandi — Train Planning and Evaluation, KAI Commuter |
| Peran Pemilik | Menentukan **APA** yang dibuat dan menyatakan **SUDAH BENAR / BELUM** |
| Peran AI | Menentukan **BAGAIMANA** membuatnya, menulis kode, menguji, melapor |
| Bahasa kerja | Bahasa Indonesia |

**Pemilik Proyek bukan programmer.** Semua laporan AI wajib memakai bahasa awam.
Dilarang meminta Pemilik Proyek membaca kode untuk memutuskan sesuatu.

---

## 2. Tujuan Aplikasi (tidak boleh bergeser)

TTC adalah alat bantu perencanaan operasi kereta api yang:

1. Menyimpan data jaringan lintas (stasiun, jarak, jumlah jalur, emplasemen).
2. **Menghasilkan jadwal perjalanan (timetable) secara otomatis** dari parameter
   yang dimasukkan pengguna — bukan diketik satu per satu.
3. **Menggambar GAPEKA** (grafik perjalanan kereta api: sumbu waktu × sumbu jarak)
   dari jadwal tersebut.
4. **Mendeteksi konflik** perjalanan (persilangan, penyusulan, headway, okupansi jalur).
5. Mengekspor hasilnya ke bentuk yang bisa dipakai kerja (gambar, PDF, Excel).

**Di luar lingkup (JANGAN dibuat kecuali diperintahkan):**
sistem login/multi-user, database server, integrasi ke sistem KAI mana pun,
aplikasi mobile, fitur AI/prediksi, penjualan tiket.

---

## 3. Keputusan Teknis Terkunci

Keputusan ini **tidak boleh diubah AI secara sepihak**. Ditandai `[TERKUNCI]`.

| # | Keputusan | Status |
|---|---|---|
| K1 | Bentuk aplikasi: **aplikasi web satu halaman** (HTML + JavaScript murni, tanpa server, tanpa framework berat). Bisa dibuka dengan klik dua kali di komputer mana pun, dan bisa dipublikasikan gratis lewat GitHub Pages. | [TERKUNCI] |
| K2 | Tidak memerlukan instalasi apa pun di komputer pengguna (tidak perlu Python, tidak perlu izin IT). | [TERKUNCI] |
| K3 | File proyek pengguna disimpan sebagai **satu file `.json`** yang bisa dibuka/disimpan sendiri oleh pengguna. | [TERKUNCI] |
| K4 | Gambar GAPEKA digambar dengan **SVG** (bukan gambar bitmap), supaya bisa di-zoom tanpa pecah dan diekspor ke PDF dengan tajam. | [TERKUNCI] |
| K5 | Acuan tampilan: desain UI yang sudah disetujui Pemilik Proyek (bergaya desktop macOS, menu Bahasa Indonesia, panel Proyek / Properti / Peta Jalur / Daftar Kereta). Tidak membuat desain baru. | [TERKUNCI] |
| K6 | Kode Python `src/ttc/...` yang sudah ada di repo **disimpan sebagai referensi logika**, tidak dihapus, tidak dikembangkan lagi. | [TERKUNCI] |
| K7 | Satu sesi kerja = **satu tahap ROADMAP**. Dilarang melompat tahap. | [TERKUNCI] |

> **Catatan alasan K1 (untuk Pemilik Proyek):** versi Python desktop mengharuskan
> instalasi Python di setiap komputer — di lingkungan kantor itu butuh izin IT dan
> sering gagal. Versi web bisa langsung dibuka lewat link oleh atasan/tim, dan
> jauh lebih mudah dites otomatis. Jika Anda tetap ingin versi desktop Python,
> ubah baris K1 ini sendiri dan beri tahu AI bahwa K1 berubah.

---

## 4. Definisi "SELESAI"

Sebuah tahap hanya boleh dinyatakan selesai bila **ketiganya** terpenuhi:

1. **Bukti terlihat** — Pemilik Proyek membuka aplikasi, melakukan langkah yang
   tertulis di ROADMAP, dan melihat hasil yang dijanjikan di layar.
2. **Tidak merusak yang lama** — semua fitur tahap sebelumnya masih jalan.
3. **Tercatat** — `STATE.md` sudah diperbarui dan perubahan sudah masuk GitHub.

Kalimat "sudah saya buatkan" dari AI **tidak dihitung sebagai selesai**.

---

## 5. Aturan Anti-Nyasar untuk AI

1. **Wajib baca dulu.** Di awal setiap sesi, baca `PROJECT.md`, `ROADMAP.md`,
   `STATE.md`, lalu laporkan posisi terakhir sebelum mengerjakan apa pun.
2. **Satu tahap saja.** Kerjakan hanya tahap aktif di `STATE.md`.
   Ide bagus di luar tahap itu ditulis di bagian "Usulan Tertunda" `STATE.md`, bukan dikerjakan.
3. **Tidak ada kerja diam-diam.** Setiap perubahan disebutkan: file apa, untuk apa, akibatnya apa.
4. **Tidak boleh menghapus.** Fitur/file yang sudah jalan tidak dihapus atau ditulis ulang
   total tanpa izin. Kalau perlu dirombak, minta izin dulu dengan alasan.
5. **Wajib tutup sesi.** Sebelum sesi berakhir, perbarui `STATE.md` dan pastikan
   sudah ter-commit ke GitHub. Sesi tanpa pembaruan `STATE.md` dianggap gagal.
6. **Jujur soal kegagalan.** Kalau tidak bisa, katakan tidak bisa dan sebutkan
   sebabnya. Dilarang melapor "sudah berhasil" untuk sesuatu yang belum diuji.
7. **Bahasa awam.** Laporan ke Pemilik Proyek tanpa istilah teknis yang tidak perlu.
