# STATE.md — Papan Posisi Proyek

> **WAJIB DIPERBARUI AI SETIAP AKHIR SESI.**
> File ini adalah ingatan proyek. Kalau file ini tidak diperbarui,
> sesi berikutnya akan kehilangan arah.
> Yang boleh mengubah status tahap menjadi `[x]` hanyalah Pemilik Proyek.

---

## Posisi Sekarang

- **Tahap aktif administratif:** Tahap 1 — Data Jaringan Lintas
- **Pentahapan:** sementara ditahan atas perintah eksplisit Pemilik Proyek; pekerjaan saat ini memprioritaskan alur UI dan fondasi aplikasi.
- **Diperbarui terakhir:** 13 September 2026
- **Oleh sesi:** ChatGPT, 13 September 2026

---

## Sudah Selesai & Diverifikasi Pemilik Proyek

| Tahap | Nama | Tanggal diverifikasi |
|---|---|---|
| Tahap 0 | Fondasi Kendali | 12 September 2026 |

---

## Sedang Dikerjakan

| Butir | Keterangan | Sisa pekerjaan |
|---|---|---|
| Alur Proyek | Pemilik Proyek memerintahkan agar TTC selalu masuk ke **Proyek Saya** terlebih dahulu, baru setelah memilih/membuat proyek masuk ke menu prasarana, sarana, jadwal, GAPEKA, simulasi, dan lainnya. | Verifikasi langsung oleh Pemilik Proyek pada preview Cloudflare. |
| Penyimpanan browser | Beberapa proyek kini disimpan di browser melalui **IndexedDB** dengan fallback `localStorage`. Perubahan proyek aktif disalin otomatis ke penyimpanan browser. | Verifikasi persistensi setelah refresh/tutup-buka browser pada perangkat Pemilik Proyek. |
| Backup proyek | Tombol **Simpan JSON** tetap dipertahankan sebagai backup dan sarana pindah perangkat. Impor JSON tersedia dari halaman Proyek Saya. | Uji impor/ekspor oleh Pemilik Proyek. |

---

## Kondisi Repo Terakhir

- Repo utama dokumen kendali tetap: `shandishantoro-rgb/TrainTrafficSimulator`.
- Repo aplikasi/preview Cloudflare saat ini: `shandishantoro-rgb/TRAIN-TRAFFIC`.
- Paket aplikasi TTC lengkap dari Claude telah dipasang di repo `TRAIN-TRAFFIC` dengan modul terpisah untuk model, dinamika, sinyal, blok, emplasemen, jadwal, konflik, GAPEKA, ekspor, simulasi operasi, dan UI.
- Modul baru `js/ttc-proyek.js` menyimpan banyak proyek di browser.
- Modul baru `js/ttc-project-manager.js` membuat halaman **Proyek Saya**, membuka proyek, membuat proyek, impor JSON, duplikat, hapus, dan autosave.
- `js/ttc-ekspor.js` memuat modul manajemen proyek tersebut tanpa mengubah struktur utama aplikasi TTC.
- Tombol global **+ Baru**, **Buka**, dan **Contoh** disembunyikan dari workspace. Pembuatan proyek baru hanya dilakukan dari halaman **Proyek Saya**.
- Di dalam workspace tersedia tombol **← Proyek Saya** dan **Simpan JSON**.

---

## Hasil Uji AI

- Semua JavaScript paket TTC yang dipakai: **lulus pemeriksaan sintaks**.
- Penyimpanan proyek fallback telah diuji: **buat → daftar → buka → ubah → duplikat → hapus** berjalan.
- Uji browser terisolasi alur baru: **Proyek Saya → buka/buat proyek → workspace → ubah nama → autosave → kembali ke Proyek Saya** berjalan tanpa runtime error.
- Uji dengan proyek contoh: 24 stasiun tetap dapat dirender setelah manajemen proyek ditambahkan.
- GitHub sudah berisi `js/ttc-proyek.js` dan `js/ttc-project-manager.js` serta loader pada `js/ttc-ekspor.js`.
- Deployment Cloudflare terbaru belum diverifikasi langsung oleh AI pada sesi ini; verifikasi visual tetap dilakukan oleh Pemilik Proyek melalui `traintrafficcontrol.site`.

---

## Keputusan Baru yang Diambil dalam Sesi

- Pemilik Proyek memerintahkan: **jangan tampilkan tombol + Baru di seluruh workspace**.
- Alur resmi UI yang dipilih Pemilik Proyek: **Buka TTC → Proyek Saya → pilih/buat proyek → masuk workspace TTC**.
- Menu prasarana, sarana, jadwal, GAPEKA, dan simulasi baru dipakai setelah proyek aktif dipilih.
- Proyek disimpan otomatis di browser, tetapi file `.json` tetap dipertahankan sebagai backup utama dan untuk memindahkan proyek antar perangkat.
- Daftar proyek menampilkan nama proyek, waktu terakhir diubah, ringkasan stasiun/petak/sarana/KA, serta aksi Buka, Duplikat, dan Hapus.
- Pemilik Proyek sebelumnya memerintahkan pentahapan ditahan sementara untuk membangun UI dan alur aplikasi terlebih dahulu. Status ROADMAP belum diubah pada sesi ini.

---

## Masalah / Macet

- Tidak ada error sintaks yang ditemukan pada implementasi manajemen proyek.
- Perlu bukti langsung bahwa Cloudflare telah mengambil commit terbaru dan IndexedDB berjalan normal pada browser/perangkat Pemilik Proyek.
- Penyimpanan browser bersifat lokal pada browser/perangkat. Menghapus data situs/browser dapat menghapus proyek lokal; karena itu **Simpan JSON** tetap diperlukan sebagai backup.

---

## Usulan Tertunda

- Sinkronisasi proyek antar perangkat/server belum dibuat dan tetap di luar lingkup saat ini.
- Fitur login/multi-user tetap di luar lingkup sesuai PROJECT.md.
- Pentahapan ROADMAP akan dilanjutkan kembali setelah Pemilik Proyek memerintahkan melanjutkan tahapan.
