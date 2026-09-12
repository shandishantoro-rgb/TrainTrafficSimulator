# Cara Pakai Dokumen Kendali Ini

Lima file ini gunanya satu: **supaya proyek TTC tidak hilang arah**, walaupun
chat AI berganti-ganti dan Anda bukan programmer.

| File | Untuk siapa | Gunanya |
|---|---|---|
| `PROJECT.md` | AI | Aturan & keputusan yang tidak boleh diubah AI |
| `ROADMAP.md` | AI + Anda | Urutan tahap, dan bukti apa yang harus Anda lihat tiap tahap |
| `STATE.md` | AI | Ingatan proyek. Diperbarui tiap akhir sesi |
| `PERINTAH.md` | **Anda** | Kalimat siap salin-tempel untuk memerintah AI |
| `GLOSARIUM.md` | AI | Istilah perkeretaapian supaya AI tidak salah paham |

## Langkah pemasangan (sekali saja)

1. Buka repo `TrainTrafficSimulator` di GitHub.
2. Klik **Add file → Upload files**.
3. Seret kelima file ini ke sana.
4. Klik **Commit changes**.

Setelah itu, di chat GPT Anda cukup tempel **PERINTAH 1** dari `PERINTAH.md`.

## Siklus kerja sehari-hari

```
Buka chat baru
   ↓
PERINTAH 1  → AI baca repo & lapor posisi
   ↓
PERINTAH 2  → AI kerja satu tahap
   ↓
PERINTAH 4  → Anda buktikan sendiri di layar
   ↓
belum benar? → PERINTAH 5 (perbaiki)
sudah benar? → PERINTAH 8 (tutup tahap)
   ↓
PERINTAH 6  → AI perbarui STATE.md & push
   ↓
Tutup chat. Besok ulangi dari PERINTAH 1.
```

Selama siklus ini dijalankan, proyek **tidak bisa** hilang arah — karena arahnya
tidak disimpan di ingatan AI, tapi di repo Anda sendiri.
