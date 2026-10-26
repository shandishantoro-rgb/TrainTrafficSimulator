# Database KCI — COTP di traintrafficcontrol.site

Aplikasi **Database KCI – COTP Department** (sebelumnya hanya berjalan sebagai
Web App Apps Script) kini juga tayang di situs ini:

- Halaman utama `https://traintrafficcontrol.site/` (folder `site/` di repo ini)
- Cadangan: GitHub Pages repo ini (workflow `.github/workflows/pages.yml`)

Simulator TTC (folder `app/`) untuk sementara **tidak ditayangkan** atas perintah Pemilik Proyek (26 Okt 2026); kodenya tetap utuh di repo.

Datanya tetap **Google Sheet `DATABASE_KCI_Master`**, dan logika server tetap
di proyek Apps Script **"Database KCI - COTP"**. Yang dipindahkan ke GitHub dan
Cloudflare hanya tampilannya.

## Cara kerja

```
Browser (traintrafficcontrol.site)
   │  google.script.run.namaFungsi(...)   ← kode modul asli, tidak diubah
   ▼
site/gas-shim.js   → POST {fn, args} ke URL /exec
   ▼
Apps Script: Api.gs → doPost → fungsi modul yang sama (gangguan_*, sap_*, tc_*, …)
   ▼
Google Sheet DATABASE_KCI_Master + folder Drive Database_KCI
```

Login, sesi (token), dan izin per role tetap diperiksa di Apps Script persis
seperti sebelumnya.

## Pemasangan (sekali saja)

1. **Apps Script**: buka proyek "Database KCI - COTP", tambah file skrip `Api`,
   tempel isi `apps-script/Api.gs`.
2. **Terapkan ulang**: Terapkan → Kelola penerapan → pilih penerapan Web App →
   ✎ Edit → Versi: *Versi baru* → Terapkan. Akses **wajib "Siapa saja"** (bukan "Siapa saja yang memiliki Akun Google"): situs tidak bisa memakai login Google pengunjung, sehingga dengan pilihan itu setiap panggilan akan dialihkan ke halaman masuk Google dan gagal. Keamanan tetap dijaga oleh login username/password aplikasi.
   URL `/exec` tidak berubah.
3. **URL API**: sudah diisi di `site/config.js` (Web App s.id/basecotp). Bila URL berubah, ubah `apiUrl` di `site/config.js` dengan URL `/exec` tersebut
   (disarankan, supaya semua pengguna langsung tersambung). Bila dikosongkan,
   halaman akan meminta URL saat pertama dibuka dan menyimpannya di browser
   pengguna itu saja.

## Memperbarui tampilan

Sumber tampilan ada di `database-kci/src/` (salinan file `.html` dari Apps
Script). Setelah mengubah tampilan di Apps Script:

1. Salin ulang file `.html` yang berubah ke `database-kci/src/`.
2. Jalankan `node tools/build-database-kci.mjs` → menghasilkan `site/index.html`.
3. Commit & push ke `main`. Situs menayangkan otomatis.

Fungsi server baru tidak perlu didaftarkan di mana pun, asalkan namanya
memakai awalan modul (`gangguan_`, `sap_`, `tc_`, dst.) dan tidak berakhiran `_`.

## Keamanan

- `Api.gs` hanya menerima fungsi modul berawalan resmi, ditambah `getUrlAplikasi`.
  Fungsi pembantu umum seperti `updateRowById`, `deleteRowById`, `appendRowObject`,
  dan `getMasterSpreadsheet` **tidak** bisa dipanggil dari luar. Aturan ini lebih
  ketat daripada `google.script.run` di Web App lama, yang masih bisa memanggil
  fungsi-fungsi tersebut.
- Kode server (`.gs`) tidak disimpan di repo publik ini, kecuali `Api.gs`.
- Token sesi tetap disimpan di `sessionStorage`, sehingga hilang saat tab ditutup.

## Pengaturan Cloudflare (traintrafficcontrol.site)

Repo lama `TRAIN-TRAFFIC` sudah dihapus. Sambungkan proyek Cloudflare ke repo ini:

| Isian | Nilai |
|---|---|
| Repository | `shandishantoro-rgb/TrainTrafficSimulator` |
| Production branch | `main` |
| Framework preset | None |
| Build command | *(kosong)* |
| Build output directory | `site` |

