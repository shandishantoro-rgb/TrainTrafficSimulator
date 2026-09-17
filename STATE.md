# STATE.md — Papan Posisi Proyek

> **WAJIB DIPERBARUI AI SETIAP AKHIR SESI.**
> File ini adalah ingatan proyek. Kalau file ini tidak diperbarui,
> sesi berikutnya akan kehilangan arah.
> Yang boleh mengubah status tahap menjadi `[x]` hanyalah Pemilik Proyek.

---

## Posisi Sekarang

- **Tahap aktif administratif:** Tahap 1 — Data Jaringan Lintas
- **Pentahapan:** sementara ditahan atas perintah eksplisit Pemilik Proyek; pekerjaan saat ini memprioritaskan alur UI dan fondasi aplikasi.
- **Diperbarui terakhir:** 17 September 2026
- **Oleh sesi:** ChatGPT, 17 September 2026

---

## Sudah Selesai & Diverifikasi Pemilik Proyek

| Tahap | Nama | Tanggal diverifikasi |
|---|---|---|
| Tahap 0 | Fondasi Kendali | 12 September 2026 |

---

## Sedang Dikerjakan

| Butir | Keterangan | Sisa pekerjaan |
|---|---|---|
| Alur Proyek | TTC masuk ke **Proyek Saya** terlebih dahulu, baru setelah memilih/membuat proyek masuk ke menu prasarana, sarana, jadwal, GAPEKA, simulasi, dan lainnya. | Verifikasi langsung oleh Pemilik Proyek pada preview Cloudflare. |
| Penyimpanan browser | Beberapa proyek disimpan di browser melalui **IndexedDB** dengan fallback `localStorage`. Perubahan proyek aktif disalin otomatis ke penyimpanan browser. | Verifikasi persistensi setelah refresh/tutup-buka browser pada perangkat Pemilik Proyek. |
| Backup proyek | Tombol **Simpan JSON** tetap dipertahankan sebagai backup dan sarana pindah perangkat. Impor JSON tersedia dari halaman Proyek Saya. | Uji impor/ekspor oleh Pemilik Proyek. |
| Perjalanan KA / Course-Service | Menu Jadwal memperoleh fungsi perjalanan individual: **Tambah KA, Edit, Duplikat, Nonaktif/Aktifkan, Hapus, Hitung Ulang, dan Simpan Daftar Waktu**. KA dibedakan `manual` dan `generator`; KA manual dipertahankan saat generator dijalankan ulang. | Verifikasi langsung seluruh alur oleh Pemilik Proyek, terutama regenerasi jadwal setelah ada KA manual dan penghapusan KA generator. |
| Daftar Waktu editable | Daftar Waktu per stasiun dapat mengubah program datang/berangkat, realisasi datang/berangkat, jalur, berhenti/langsung, dan WT. Program dan realisasi disimpan terpisah; waktu di atas 24 jam seperti `25:14` didukung. | Verifikasi kenyamanan editor, validasi urutan waktu, dan persistensi setelah tutup-buka proyek. |
| Simulasi jadwal | Tampilan diperlebar; program jadwal menjadi garis abu-abu, sedangkan garis aktual muncul progresif mengikuti waktu simulasi. Nomor KA dipindahkan ke badan garis. Koreksi tambahan menyamakan tinggi koordinat label kiri, sumbu waktu, grafik, kursor, dan garis aktual pada **520 px** agar tidak melenceng setelah kanvas diperbesar. Ditambahkan kontrol zoom **− / 100% / + / Pas** serta Ctrl/Cmd + scroll. | Verifikasi visual, alignment, dan kenyamanan zoom oleh Pemilik Proyek. |
| Simulasi sinyal & rute | Diagram strip lurus kecil diganti dengan visual topologi jaringan yang lebih besar. Rute dasar memakai graf Petak Jalan sehingga percabangan dapat dipilih berdasarkan keterhubungan jaringan. Junction, rute aktif, okupansi petak, sinyal, dan posisi KA divisualkan. Diagram topologi juga memiliki kontrol zoom **− / 100% / + / Pas** dan Ctrl/Cmd + scroll. | Verifikasi pada jaringan yang benar-benar memiliki cabang dan penyempurnaan penempatan sinyal per cabang bila diperlukan. |

---

## Kondisi Repo Terakhir

- Repo utama dokumen kendali tetap: `shandishantoro-rgb/TrainTrafficSimulator`.
- Repo aplikasi/preview Cloudflare saat ini: `shandishantoro-rgb/TRAIN-TRAFFIC`.
- Paket aplikasi TTC lengkap dari Claude telah dipasang di repo `TRAIN-TRAFFIC` dengan modul terpisah untuk model, dinamika, sinyal, blok, emplasemen, jadwal, konflik, GAPEKA, ekspor, simulasi operasi, dan UI.
- `js/ttc-proyek.js` menyimpan banyak proyek di browser.
- `js/ttc-project-manager.js` membuat halaman **Proyek Saya**, membuka proyek, membuat proyek, impor JSON, duplikat, hapus, dan autosave.
- `js/ttc-course-service.js` menambahkan editor **Perjalanan KA / Course-Service** dan Daftar Waktu editable tanpa menghapus generator Pola Operasi.
- `COURSE-SERVICE.md` di repo aplikasi mendokumentasikan sumber perjalanan, status aktif/nonaktif, Daftar Waktu program/realisasi, Hitung Ulang, serta perilaku Hapus KA.
- `js/ttc-sim-visual.js` menambahkan penyempurnaan simulasi tanpa menghapus mesin yang sudah ada: rute berbasis graf, label KA di badan garis, program vs aktual, dan topologi bercabang untuk Simulasi Sinyal.
- `js/ttc-sim-alignment-fix.js` mengoreksi ketidaksamaan ukuran koordinat simulasi setelah kanvas diperlebar; tinggi label kiri, grafik, sumbu waktu, dan overlay diseragamkan. Modul ini sekarang memuat modul zoom setelah alignment siap.
- `js/ttc-sim-zoom.js` menambahkan zoom pada Simulasi dan Simulasi Sinyal tanpa mengubah koordinat dasar SVG, sehingga label/sumbu tetap sejajar.
- `js/ttc-ekspor.js` saat ini masih menjadi pemuat beberapa modul tambahan, termasuk Course-Service. Ini masih merupakan utang arsitektur yang sudah ditandai pada audit Claude dan belum dibersihkan pada sesi ini.
- Tombol global **+ Baru**, **Buka**, dan **Contoh** disembunyikan dari workspace. Pembuatan proyek baru hanya dilakukan dari halaman **Proyek Saya**.
- Di dalam workspace masih terdapat toolbar lama; rencana menghilangkan header besar sudah disepakati tetapi belum dieksekusi pada sesi Course-Service ini.

---

## Model Data Perjalanan KA yang Disepakati

Setiap KA memiliki identitas tetap `id` yang terpisah dari `nomor` KA.

Atribut penting:

- `id`
- `nomor`
- `nama`
- `sumber`: `manual` atau `generator`
- `polaId`: ID pola pembentuk bila berasal dari generator
- `diubahManual`: penanda KA generator yang sudah dikoreksi pengguna
- `aktif`
- `hariOperasi`
- `saranaId`
- `arah`
- `relasi`
- `perjalanan[]`

Setiap titik `perjalanan[]` menyimpan program dan realisasi secara terpisah:

- `datang`
- `berangkat`
- `datangAktual`
- `berangkatAktual`
- `berhenti`
- `jalur`
- `wt`

KA nonaktif disimpan di `jadwal.kaNonaktif` agar tidak dipakai oleh GAPEKA, konflik, simulasi, dan ekspor tetapi masih dapat diaktifkan kembali.

KA generator yang sengaja dihapus dicatat pada `jadwal.pengecualianGenerator` agar tidak langsung muncul kembali pada regenerasi berikutnya.

---

## Hasil Uji AI

- Semua JavaScript paket TTC yang dipakai sebelumnya: **lulus pemeriksaan sintaks**.
- `js/ttc-sim-visual.js`: **lulus `node --check`**.
- `js/ttc-sim-alignment-fix.js`: **lulus `node --check`**.
- `js/ttc-sim-zoom.js`: **lulus `node --check`** sebelum dipush ke GitHub.
- `js/ttc-course-service.js`: **lulus `node --check`** sebelum dipush ke GitHub.
- Uji inti Course-Service dengan harness lokal: waktu lebih dari 24 jam (`25:00`) dapat diparsing dan ditulis kembali; pembentukan perjalanan 3 stasiun, dwell, WT persen, dan normalisasi struktur proyek berjalan sesuai hasil yang diharapkan.
- Logika pencarian lintasan berbasis graf sebelumnya diuji pada jaringan bercabang sederhana dan menghasilkan lintasan terhubung yang benar.
- Penyimpanan proyek fallback sebelumnya telah diuji: **buat → daftar → buka → ubah → duplikat → hapus** berjalan.
- Uji browser terisolasi alur proyek sebelumnya: **Proyek Saya → buka/buat proyek → workspace → ubah nama → autosave → kembali ke Proyek Saya** berjalan tanpa runtime error.
- Uji dengan proyek contoh sebelumnya: 24 stasiun tetap dapat dirender setelah manajemen proyek ditambahkan.
- **Belum ada uji browser penuh untuk Course-Service pada deployment Cloudflare** dalam sesi ini. Pemilik Proyek perlu memverifikasi langsung di `traintrafficcontrol.site` setelah deployment menarik commit terbaru.

---

## Referensi Desain / Logika yang Dipakai

- OpenTrack memodelkan jaringan sebagai **graf topologi** yang berisi edge/vertex, signal, switch, station, dan route; pendekatan ini dijadikan rujukan untuk mengubah TTC dari asumsi lintas lurus menjadi jaringan bercabang.
- OpenTrack juga menampilkan **reserved route, occupied track, signal aspect**, serta perbandingan timetable/actual pada visual simulasi. Prinsip tersebut dipakai sebagai acuan penyempurnaan Simulasi TTC.
- Contoh interlocking UIC menggunakan penyorotan warna pada route dan kondisi wesel; prinsip kontras route/okupansi dipakai untuk topologi Simulasi Sinyal TTC.
- PDF GAPEKA eksisting KAI/KCI yang diberikan Pemilik Proyek menjadi referensi visual utama untuk pengembangan renderer GAPEKA selanjutnya: lembar 4 jam, panel lintas utama/cabang, nomor KA di badan garis, angka menit, dwell/turnaround, panel prasarana kiri, dan emplasemen kanan.

---

## Keputusan Baru yang Diambil dalam Sesi

- **Perjalanan KA / Course-Service menjadi prioritas sebelum penyempurnaan simulasi berikutnya**, karena Jadwal dan Daftar Waktu adalah sumber data GAPEKA, konflik, simulasi, dan ekspor.
- Pola Operasi tetap dipertahankan sebagai generator perjalanan massal.
- Pengguna harus dapat membuat **satu KA secara manual**, mengedit, menduplikasi, menonaktifkan/mengaktifkan, menghitung ulang, dan menghapusnya.
- **Hapus KA** harus menghilangkan perjalanan aktif dari Daftar Waktu, GAPEKA, konflik, simulasi, dan ekspor.
- KA manual tidak boleh hilang ketika **Buat Jadwal** dijalankan kembali.
- Nomor KA bukan identitas internal; setiap KA memiliki `id` tetap.
- Program dan realisasi tidak boleh saling menimpa. **Realisasi dicatat per stasiun** melalui datang aktual dan berangkat aktual.
- Daftar Waktu harus dapat mengubah program datang/berangkat, realisasi, jalur, berhenti/langsung, serta WT per stasiun.
- Format waktu harus mendukung perjalanan melewati pukul 24.00.
- Header besar workspace direncanakan dihilangkan dan fungsi penyimpanan dipusatkan pada halaman awal Proyek Saya, tetapi perubahan tersebut belum dikerjakan dalam sesi ini.
- Pemilik Proyek sebelumnya memerintahkan pentahapan ditahan sementara untuk membangun UI dan alur aplikasi terlebih dahulu. Status ROADMAP tidak diubah pada sesi ini.

---

## Masalah / Macet

- Audit Claude menemukan arsitektur modul saat ini masih memiliki pemuatan JS berantai dari `ttc-ekspor.js` serta beberapa fungsi simulasi yang ditambal lintas modul. Pembersihan arsitektur tersebut tetap perlu dilakukan; Course-Service pada sesi ini belum menyelesaikan utang itu.
- Proteksi KA manual terhadap regenerasi sudah ditambahkan pada modul Course-Service, tetapi masih perlu uji langsung pada perangkat Pemilik Proyek dengan ratusan KA untuk memastikan tidak ada kondisi lambat yang membuat regenerasi selesai lebih lama daripada jeda penggabungan data.
- Duplikasi perjalanan perlu diverifikasi khusus pada KA yang memiliki pola berhenti manual kompleks.
- Model sinyal lama masih menyimpan banyak sinyal terutama berdasarkan **Km**. Pada jaringan bercabang kompleks, sinyal idealnya nanti juga memiliki identitas Petak Jalan/rute agar penempatan dan logika blok cabang sepenuhnya tidak ambigu.
- Mesin simulasi operasi lama masih memakai posisi Km sebagai salah satu acuan gerak; dukungan cabang dasar sudah ditambahkan pada pemilihan lintasan, tetapi jaringan bercabang kompleks perlu diuji dengan data nyata sebelum dianggap final.
- Penyimpanan browser bersifat lokal pada browser/perangkat. Menghapus data situs/browser dapat menghapus proyek lokal; karena itu **Simpan JSON** tetap diperlukan sebagai backup.

---

## Usulan Tertunda

- Jalankan audit arsitektur Claude: daftarkan seluruh modul secara eksplisit di `index.html`, hilangkan pemuatan JS berantai, satukan tata letak stasiun, dan lipat tambalan simulasi ke modul asal.
- Hilangkan header besar workspace dan pindahkan fungsi proyek/backup ke halaman **Proyek Saya** sesuai keputusan Pemilik Proyek.
- Tambahkan pilihan eksplisit **via stasiun/rute** pada Course-Service dan Pola Operasi untuk lintas yang memiliki lebih dari satu rute valid.
- Tambahkan atribut eksplisit **petak/rute** pada objek sinyal untuk jaringan bercabang kompleks.
- Bangun renderer GAPEKA bergaya KAI/KCI setelah fondasi data dan arsitektur dibersihkan.
- Sinkronisasi proyek antar perangkat/server belum dibuat dan tetap di luar lingkup saat ini.
- Fitur login/multi-user tetap di luar lingkup sesuai PROJECT.md.
- Pentahapan ROADMAP akan dilanjutkan kembali setelah Pemilik Proyek memerintahkan melanjutkan tahapan.

---

## Sesi 17 September 2026 — Peta Jalur interaktif

- Pemilik menyetujui implementasi bertahap Peta Jalur setelah audit: fokus geser/zoom, pilih objek, simpan posisi, Urungkan, dan mode Lihat/Edit.
- Implementasi dipush ke repo aplikasi TRAIN-TRAFFIC, commit 4e1e84fc24e6fb0ef0f7f9386f3066713bb416d3.
- Modul baru `js/ttc-peta.js`: pan latar, zoom scroll/tombol, drag stasiun hanya dalam mode Edit, garis petak mengikuti, properti stasiun/petak, Tampilkan Semua, undo/redo.
- Posisi gambar disimpan dalam `stasiun.petaPos`; tampilan dalam `petaJalur.view`. Km dan jarak petak tidak berubah ketika digeser. Migrasi JSON mempertahankan data peta.
- Editor stasiun mempertahankan layout dan posisi. Pengubahan kode ditolak sementara karena referensi lintas modul belum dimigrasikan otomatis.
- Tombol Gambar ulang dihapus; peta merender otomatis saat dibuka atau data berubah.
- Berkas yang berubah: index.html, js/ttc-model.js, js/ttc-ui.js; ditambahkan js/ttc-peta.js, tests/peta.test.cjs, PETA-JALUR.md.
- Verifikasi: pemeriksaan sintaks lulus; tes DOM tiruan lulus untuk seleksi, pan, mode, drag/garis, properti, undo/redo, pembatalan drag, zoom, fit, simpan/migrasi, invariansi km/jarak, dan reset antar-proyek.
- Batas verifikasi: browser Chromium tidak tersedia dan unduhan timeout; belum uji browser nyata, IndexedDB nyata, atau konfirmasi deployment Cloudflare.
- Belum dibuat: tambah/hubungkan langsung di kanvas dan Rapikan Otomatis. Temuan audit jadwal/konflik/simulasi belum diperbaiki dalam sesi ini.
- Status: implementasi awal Peta Jalur tersedia di repo, menunggu verifikasi pemilik. ROADMAP tidak dicentang; tahap administratif tetap sebagaimana sebelumnya.
- Pekerjaan berikutnya: verifikasi Peta Jalur pada browser pengguna; selesaikan masalah yang ditemukan sebelum memperluas editor jaringan.
