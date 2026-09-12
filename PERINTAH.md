# PERINTAH.md — Perintah Baku untuk Pemilik Proyek

File ini untuk **Anda**, bukan untuk AI.
Isinya kalimat siap salin-tempel. Anda tidak perlu mengarang perintah sendiri.

**Aturan emas:** setiap sesi chat baru **selalu** dimulai dengan Perintah 1.
Jangan pernah langsung bilang "lanjut" di chat yang baru dibuka.

---

## PERINTAH 1 — Pembuka Sesi (WAJIB, selalu yang pertama)

```
Ini proyek TTC — Train Traffic Simulator, repo GitHub: TrainTrafficSimulator.

Sebelum mengerjakan apa pun, baca tiga file ini di repo:
1. PROJECT.md   (konstitusi proyek & keputusan terkunci)
2. ROADMAP.md   (urutan tahap)
3. STATE.md     (posisi terakhir)

Lalu laporkan ke saya dengan bahasa awam, maksimal 10 baris:
- Tahap berapa yang aktif sekarang
- Apa yang sudah selesai
- Apa persisnya yang akan Anda kerjakan di sesi ini
- Apa "Bukti Selesai" yang harus saya lihat di layar nanti

JANGAN menulis kode apa pun sebelum saya menjawab "setuju".
```

---

## PERINTAH 2 — Mulai Kerja

```
Setuju. Kerjakan tahap itu saja, jangan melompat ke tahap lain.
Kalau ada ide di luar tahap ini, tulis di bagian "Usulan Tertunda" STATE.md,
jangan dikerjakan.
```

---

## PERINTAH 3 — Minta Laporan Kemajuan

```
Berhenti sebentar. Laporkan dengan bahasa awam:
- Sudah berapa persen tahap ini
- File apa saja yang Anda ubah dan untuk apa
- Apa yang masih kurang
Tanpa menampilkan kode.
```

---

## PERINTAH 4 — Verifikasi (menagih bukti)

```
Sekarang beri saya langkah persis untuk membuktikan sendiri bahwa ini berhasil:
1. Saya harus buka apa
2. Saya harus klik apa
3. Apa yang harus muncul di layar

Kalau ada yang belum bisa dibuktikan, katakan terus terang bagian mana.
```

---

## PERINTAH 5 — Kalau Hasilnya Salah

```
Belum benar. Yang saya lihat: [tulis apa yang Anda lihat di layar].
Yang seharusnya menurut ROADMAP: [tulis Bukti Selesai dari ROADMAP].

Perbaiki. Jangan menulis ulang seluruh aplikasi — perbaiki bagian yang salah saja.
Kalau memang harus dirombak, minta izin saya dulu dan sebutkan alasannya.
```

---

## PERINTAH 6 — Penutup Sesi (WAJIB, jangan pernah dilewat)

```
Kita tutup sesi.

Sebelum berhenti, lakukan ini:
1. Perbarui STATE.md: tahap aktif, apa yang selesai, apa yang belum,
   masalah yang muncul, dan usulan tertunda.
2. Commit & push semua perubahan ke GitHub.
3. Tulis untuk saya: satu paragraf ringkas kondisi proyek saat ini,
   dan satu kalimat "pekerjaan berikutnya adalah ...".

Tampilkan isi STATE.md yang sudah diperbarui supaya saya bisa periksa.
```

---

## PERINTAH 7 — Kalau AI Mulai Ngawur / Keluar Jalur

```
Berhenti. Anda keluar dari jalur proyek.

Buka lagi PROJECT.md dan STATE.md. Jawab tiga hal ini saja:
1. Tahap aktif menurut STATE.md: ...
2. Apakah yang Anda kerjakan barusan termasuk tahap itu? (ya/tidak)
3. Keputusan terkunci mana yang Anda langgar?

Setelah itu kembalikan pekerjaan ke tahap aktif. Jangan meneruskan yang tadi.
```

---

## PERINTAH 8 — Menutup Tahap (hanya Anda yang boleh)

```
Saya sudah membuktikan sendiri, hasilnya sesuai.
Tandai Tahap [nomor] menjadi [x] di ROADMAP.md, catat tanggalnya di STATE.md,
lalu commit. Jangan mulai tahap berikutnya sekarang.
```

---

## PERINTAH 9 — Mengubah Keputusan Terkunci

```
Saya ingin mengubah keputusan [K1/K2/...] menjadi: [tulis perubahannya].

Sebelum mengerjakan, jelaskan dulu ke saya:
- Apa akibatnya ke pekerjaan yang sudah jadi
- Berapa tahap yang harus diulang
Setelah saya setuju, ubah PROJECT.md dan catat di STATE.md.
```

---

## PERINTAH 10 — Pindah AI (dari ChatGPT ke Claude atau sebaliknya)

Tidak perlu perintah khusus. Cukup pakai **PERINTAH 1**.
Selama `PROJECT.md`, `ROADMAP.md`, dan `STATE.md` ada di repo dan mutakhir,
AI mana pun bisa melanjutkan dari titik yang sama.

---

## Kebiasaan yang Menyelamatkan Proyek

1. **Jangan pernah bilang cuma "lanjut" di chat baru.** Selalu PERINTAH 1 dulu.
2. **Jangan percaya kata "sudah selesai".** Selalu PERINTAH 4 dan buktikan sendiri.
3. **Jangan tutup chat tanpa PERINTAH 6.** Sesi tanpa STATE.md diperbarui = pekerjaan hilang.
4. **Satu sesi satu tahap.** Kalau AI menawarkan mengerjakan tiga tahap sekaligus, tolak.
5. **Kalau ragu, buka STATE.md di GitHub.** Itu ingatan proyek Anda, bukan ingatan AI.
