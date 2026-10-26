# Database KCI — COTP di traintrafficcontrol.site

Aplikasi **Database KCI – COTP Department** (sebelumnya hanya berjalan sebagai
Web App Apps Script) kini juga tayang di situs ini:

- Menu **Database KCI** di sidebar TTC
- Langsung: `https://traintrafficcontrol.site/database/`

Datanya tetap **Google Sheet `DATABASE_KCI_Master`**, dan logika server tetap
di proyek Apps Script **"Database KCI - COTP"**. Yang dipindahkan ke GitHub dan
Cloudflare hanya tampilannya.

## Cara kerja

```
Browser (traintrafficcontrol.site/database/)
   │  google.script.run.namaFungsi(...)   ← kode modul asli, tidak diubah
   ▼
app/database/gas-shim.js   → POST {fn, args} ke URL /exec
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
   ✎ Edit → Versi: *Versi baru* → Terapkan. Akses harus tetap **Siapa saja**.
   URL `/exec` tidak berubah.
3. **URL API**: isi `apiUrl` di `app/database/config.js` dengan URL `/exec` tersebut
   (disarankan, supaya semua pengguna langsung tersambung). Bila dikosongkan,
   halaman akan meminta URL saat pertama dibuka dan menyimpannya di browser
   pengguna itu saja.

## Memperbarui tampilan

Sumber tampilan ada di `database-kci/src/` (salinan file `.html` dari Apps
Script). Setelah mengubah tampilan di Apps Script:

1. Salin ulang file `.html` yang berubah ke `database-kci/src/`.
2. Jalankan `node tools/build-database-kci.mjs` → menghasilkan `app/database/index.html`.
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
