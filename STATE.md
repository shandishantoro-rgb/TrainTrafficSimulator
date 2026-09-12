# STATE.md — Papan Posisi Proyek

> **WAJIB DIPERBARUI AI SETIAP AKHIR SESI.**
> File ini adalah ingatan proyek. Kalau file ini tidak diperbarui,
> sesi berikutnya akan kehilangan arah.
> Yang boleh mengubah status tahap menjadi `[x]` hanyalah Pemilik Proyek.

---

## Posisi Sekarang

- **Tahap aktif:** Tahap 1 — Data Jaringan Lintas
- **Diperbarui terakhir:** 12 September 2026
- **Oleh sesi:** ChatGPT, 12 September 2026

---

## Sudah Selesai & Diverifikasi Pemilik Proyek

| Tahap | Nama | Tanggal diverifikasi |
|---|---|---|
| Tahap 0 | Fondasi Kendali | 12 September 2026 |

---

## Sedang Dikerjakan

| Butir | Keterangan | Sisa pekerjaan |
|---|---|---|
| Tahap 1 | Struktur data Stasiun dan Petak Jalan sudah diimplementasikan. Fungsi Simpan/Buka proyek `.json` dan contoh 5 stasiun sudah tersedia di `app/`. | Verifikasi Pemilik Proyek: muat/isi 5 stasiun → Simpan `.json` → buka ulang aplikasi → Buka proyek → pastikan 5 stasiun muncul kembali sama |

---

## Kondisi Repo Terakhir

- Repo: `TrainTrafficSimulator`
- Repo saat ini berstatus **public**.
- Tahap 0 sudah selesai dan diverifikasi langsung oleh Pemilik Proyek.
- `ROADMAP.md` menandai Tahap 1 sebagai `[~]`.
- `app/index.html` sudah menjadi layar Tahap 1.
- `app/app.js` menyimpan data Stasiun, Petak Jalan, Simpan proyek JSON, Buka proyek JSON, dan data contoh untuk pengujian.
- `app/styles.css` memberi tampilan dasar agar data mudah dibaca.
- Workflow preview GitHub Pages sudah ditambahkan di `.github/workflows/pages.yml` dan hanya mempublikasikan isi folder `app/`.
- Isi Python desktop v0.1 tetap berada di `referensi-python/` — **status: referensi saja** (lihat K6).

---

## Hasil Uji AI

- Pemeriksaan sintaks JavaScript dengan Node.js: **lulus**.
- Pemeriksaan hubungan elemen halaman dengan JavaScript: **lulus**; semua 22 elemen yang dipanggil JavaScript tersedia di halaman uji.
- Uji Chromium headless pada lingkungan kerja AI tidak berhasil selesai karena proses browser macet di lingkungan container; ini bukan bukti aplikasi gagal. Verifikasi browser nyata tetap harus dilakukan Pemilik Proyek sesuai ROADMAP.
- Workflow GitHub Pages sudah masuk repo, tetapi GitHub belum menjalankan deployment karena sumber Pages belum diaktifkan dari Settings repo.

---

## Keputusan Baru yang Diambil dalam Sesi (jika ada)

- Pemilik Proyek memerintahkan: **mulai Tahap 1**.
- Pemilik Proyek memberi izin eksplisit: **GitHub Pages boleh dipakai mulai sekarang hanya sebagai preview pengembangan; Tahap 1 tetap aktif**.
- Izin preview ini tidak berarti Tahap 10 dimulai dan tidak mengubah urutan ROADMAP.

---

## Masalah / Macet

- Tidak ada error sintaks atau struktur yang ditemukan pada Tahap 1.
- Bukti Selesai Tahap 1 belum terpenuhi karena belum diverifikasi langsung oleh Pemilik Proyek di browser.
- Agar preview GitHub Pages aktif, Pemilik Proyek perlu satu kali membuka **Settings → Pages → Source → GitHub Actions** karena koneksi GitHub AI saat ini tidak menyediakan aksi untuk mengubah pengaturan Pages tersebut.

---

## Usulan Tertunda (ide bagus di luar tahap aktif — JANGAN dikerjakan sekarang)

- Editor tabel lengkap, ubah/hapus/urutkan data, dan validasi kode stasiun kembar tetap Tahap 2.
- Mesin waktu tempuh dan fitur setelahnya belum dikerjakan.
- Penyempurnaan UI berdasarkan desain acuan K5 tetap ditunda hingga tahap yang relevan.
