# STATE.md — Papan Posisi Proyek

> **WAJIB DIPERBARUI AI SETIAP AKHIR SESI.**
> File ini adalah ingatan proyek. Kalau file ini tidak diperbarui,
> sesi berikutnya akan kehilangan arah.
> Yang boleh mengubah status tahap menjadi `[x]` hanyalah Pemilik Proyek.

---

## Posisi Sekarang

- **Tahap aktif administratif:** Tahap 1 — Data Jaringan Lintas
- **Pentahapan:** sementara ditahan atas perintah eksplisit Pemilik Proyek; pekerjaan saat ini memprioritaskan alur UI dan fondasi aplikasi.
- **Diperbarui terakhir:** 14 September 2026
- **Oleh sesi:** ChatGPT, 14 September 2026

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
| Simulasi jadwal | Tampilan diperlebar; program jadwal menjadi garis abu-abu, sedangkan garis aktual muncul progresif mengikuti waktu simulasi. Nomor KA dipindahkan ke badan garis. Koreksi tambahan menyamakan tinggi koordinat label kiri, sumbu waktu, grafik, kursor, dan garis aktual pada **520 px** agar tidak melenceng setelah kanvas diperbesar. | Verifikasi visual dan kenyamanan baca oleh Pemilik Proyek. |
| Simulasi sinyal & rute | Diagram strip lurus kecil diganti dengan visual topologi jaringan yang lebih besar. Rute dasar memakai graf Petak Jalan sehingga percabangan dapat dipilih berdasarkan keterhubungan jaringan. Junction, rute aktif, okupansi petak, sinyal, dan posisi KA divisualkan. | Verifikasi pada jaringan yang benar-benar memiliki cabang dan penyempurnaan penempatan sinyal per cabang bila diperlukan. |

---

## Kondisi Repo Terakhir

- Repo utama dokumen kendali tetap: `shandishantoro-rgb/TrainTrafficSimulator`.
- Repo aplikasi/preview Cloudflare saat ini: `shandishantoro-rgb/TRAIN-TRAFFIC`.
- Paket aplikasi TTC lengkap dari Claude telah dipasang di repo `TRAIN-TRAFFIC` dengan modul terpisah untuk model, dinamika, sinyal, blok, emplasemen, jadwal, konflik, GAPEKA, ekspor, simulasi operasi, dan UI.
- `js/ttc-proyek.js` menyimpan banyak proyek di browser.
- `js/ttc-project-manager.js` membuat halaman **Proyek Saya**, membuka proyek, membuat proyek, impor JSON, duplikat, hapus, dan autosave.
- `js/ttc-sim-visual.js` menambahkan penyempurnaan simulasi tanpa menghapus mesin yang sudah ada: rute berbasis graf, label KA di badan garis, program vs aktual, dan topologi bercabang untuk Simulasi Sinyal.
- `js/ttc-sim-alignment-fix.js` mengoreksi ketidaksamaan ukuran koordinat simulasi setelah kanvas diperlebar; tinggi label kiri, grafik, sumbu waktu, dan overlay diseragamkan.
- `js/ttc-ekspor.js` memuat modul manajemen proyek, modul penyempurnaan simulasi, lalu modul koreksi alignment.
- Tombol global **+ Baru**, **Buka**, dan **Contoh** disembunyikan dari workspace. Pembuatan proyek baru hanya dilakukan dari halaman **Proyek Saya**.
- Di dalam workspace tersedia tombol **← Proyek Saya** dan **Simpan JSON**.

---

## Hasil Uji AI

- Semua JavaScript paket TTC yang dipakai sebelumnya: **lulus pemeriksaan sintaks**.
- `js/ttc-sim-visual.js`: **lulus `node --check`**.
- `js/ttc-sim-alignment-fix.js`: **lulus `node --check`**.
- Logika pencarian lintasan berbasis graf diuji pada jaringan bercabang sederhana dan menghasilkan lintasan terhubung yang benar.
- Penyimpanan proyek fallback telah diuji: **buat → daftar → buka → ubah → duplikat → hapus** berjalan.
- Uji browser terisolasi alur proyek: **Proyek Saya → buka/buat proyek → workspace → ubah nama → autosave → kembali ke Proyek Saya** berjalan tanpa runtime error.
- Uji dengan proyek contoh: 24 stasiun tetap dapat dirender setelah manajemen proyek ditambahkan.
- Deployment Cloudflare terbaru untuk koreksi alignment simulasi belum diverifikasi langsung oleh AI pada sesi ini; verifikasi visual tetap dilakukan oleh Pemilik Proyek melalui `traintrafficcontrol.site`.

---

## Referensi Desain / Logika yang Dipakai

- OpenTrack memodelkan jaringan sebagai **graf topologi** yang berisi edge/vertex, signal, switch, station, dan route; pendekatan ini dijadikan rujukan untuk mengubah TTC dari asumsi lintas lurus menjadi jaringan bercabang.
- OpenTrack juga menampilkan **reserved route, occupied track, signal aspect**, serta perbandingan timetable/actual pada visual simulasi. Prinsip tersebut dipakai sebagai acuan penyempurnaan Simulasi TTC.
- Contoh interlocking UIC menggunakan penyorotan warna pada route dan kondisi wesel; prinsip kontras route/okupansi dipakai untuk topologi Simulasi Sinyal TTC.

---

## Keputusan Baru yang Diambil dalam Sesi

- Pemilik Proyek meminta area **Simulasi lebih lebar**.
- Pada Simulasi, **garis program/jadwal berwarna abu-abu** sebagai referensi.
- Garis aktual **tidak tampil penuh sejak awal**; garis muncul mengikuti waktu simulasi.
- Identitas **nomor KA ditempatkan di badan garis**, bukan di ujung garis.
- Simulasi Sinyal dan Rute harus mampu menampilkan **percabangan**, bukan hanya strip lintas lurus.
- Tampilan Simulasi Sinyal dibuat lebih informatif dan lebih besar, dengan pembeda jaringan, rute aktif, okupansi, sinyal, junction, dan KA.
- Pemilik Proyek menemukan frame kiri dan sumbu atas simulasi melenceng setelah kanvas diperlebar. Koreksi dilakukan dengan menyamakan ukuran koordinat internal dan ukuran tampil SVG, bukan sekadar memperbesar CSS.
- Pemilik Proyek sebelumnya memerintahkan pentahapan ditahan sementara untuk membangun UI dan alur aplikasi terlebih dahulu. Status ROADMAP tidak diubah pada sesi ini.

---

## Masalah / Macet

- Model sinyal lama masih menyimpan banyak sinyal terutama berdasarkan **Km**. Pada jaringan bercabang kompleks, sinyal idealnya nanti juga memiliki identitas Petak Jalan/rute agar penempatan dan logika blok cabang sepenuhnya tidak ambigu.
- Mesin simulasi operasi lama masih memakai posisi Km sebagai salah satu acuan gerak; dukungan cabang dasar sudah ditambahkan pada pemilihan lintasan, tetapi jaringan bercabang kompleks perlu diuji dengan data nyata sebelum dianggap final.
- Penyimpanan browser bersifat lokal pada browser/perangkat. Menghapus data situs/browser dapat menghapus proyek lokal; karena itu **Simpan JSON** tetap diperlukan sebagai backup.

---

## Usulan Tertunda

- Tambahkan atribut eksplisit **petak/rute** pada objek sinyal untuk jaringan bercabang kompleks.
- Tambahkan pilihan **via stasiun** pada Pola Operasi bila terdapat lebih dari satu rute valid antara asal–tujuan, agar pengguna tidak selalu bergantung pada rute terpendek otomatis.
- Sinkronisasi proyek antar perangkat/server belum dibuat dan tetap di luar lingkup saat ini.
- Fitur login/multi-user tetap di luar lingkup sesuai PROJECT.md.
- Pentahapan ROADMAP akan dilanjutkan kembali setelah Pemilik Proyek memerintahkan melanjutkan tahapan.
