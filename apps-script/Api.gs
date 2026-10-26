/**
 * Api.gs
 * Jembatan API untuk tampilan "Database KCI" yang tayang di
 * https://traintrafficcontrol.site/database/ (repo GitHub TRAIN-TRAFFIC,
 * hosting Cloudflare).
 *
 * CARA PASANG (sekali saja):
 *   1. Buka proyek Apps Script "Database KCI - COTP".
 *   2. Tambah file skrip baru bernama  Api  lalu tempel seluruh isi file ini.
 *   3. Terapkan > Kelola penerapan > (penerapan Web App yang ada) > Edit >
 *      Versi: "Versi baru" > Terapkan.  URL /exec TIDAK berubah.
 *
 * CARA KERJA
 * Tampilan di Cloudflare tidak bisa memakai google.script.run (itu hanya ada
 * di dalam halaman Apps Script). Sebagai gantinya tampilan mengirim
 *     POST { fn: "<nama fungsi>", args: [ ... ] }
 * ke URL /exec, dan doPost di bawah memanggil fungsi server yang SAMA persis
 * dengan yang dulu dipanggil lewat google.script.run. Tidak ada logika modul
 * yang diubah atau diduplikasi.
 *
 * KEAMANAN
 * - Hanya fungsi modul (berawalan activity_, auth_, dashboard_, dinasan_,
 *   gangguan_, jadwal_, kalender_, kapasitas_, kinop_, peraturan_,
 *   perlintasan_, peta_, sampah_, sap_, struktur_, tc_, usermgmt_) plus
 *   getUrlAplikasi yang boleh dipanggil. Seluruh fungsi modul ini sudah
 *   memeriksa token sesi login sendiri.
 * - Fungsi pembantu umum (updateRowById, deleteRowById, appendRowObject,
 *   getMasterSpreadsheet, dst.) dan fungsi berakhiran garis bawah TIDAK bisa
 *   dipanggil dari luar. Ini lebih ketat daripada google.script.run, yang
 *   dapat memanggil semua fungsi tanpa garis bawah di akhir namanya.
 */

const API_POLA_FUNGSI_MODUL = /^(activity|auth|dashboard|dinasan|gangguan|jadwal|kalender|kapasitas|kinop|peraturan|perlintasan|peta|sampah|sap|struktur|tc|usermgmt)_[A-Za-z0-9_]*[A-Za-z0-9]$/;
const API_FUNGSI_TAMBAHAN = ['getUrlAplikasi'];
const API_FUNGSI_DITOLAK = ['auth_bersihkanSesiKedaluwarsa'];

function apiBolehDipanggil_(nama) {
  if (typeof nama !== 'string' || !nama) return false;
  if (API_FUNGSI_DITOLAK.indexOf(nama) !== -1) return false;
  const lolos = API_POLA_FUNGSI_MODUL.test(nama) || API_FUNGSI_TAMBAHAN.indexOf(nama) !== -1;
  return lolos && typeof globalThis[nama] === 'function';
}

function apiJson_(objek) {
  return ContentService
    .createTextOutput(JSON.stringify(objek))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Dipanggil otomatis oleh Apps Script untuk setiap HTTP POST ke URL /exec.
 * @param {Object} e
 * @return {TextOutput} JSON { ok: true, result } atau { ok: false, error }
 */
function doPost(e) {
  let nama = '';
  try {
    const isi = (e && e.postData && e.postData.contents) || '{}';
    const permintaan = JSON.parse(isi);
    nama = String(permintaan.fn || '');
    const args = Array.isArray(permintaan.args) ? permintaan.args : [];

    if (nama === '__ping') {
      return apiJson_({ ok: true, result: { siap: true, waktu: new Date().toISOString() } });
    }
    if (!apiBolehDipanggil_(nama)) {
      return apiJson_({ ok: false, error: 'Fungsi tidak diizinkan lewat API: ' + nama });
    }

    const hasil = globalThis[nama].apply(null, args);
    return apiJson_({ ok: true, result: hasil === undefined ? null : hasil });
  } catch (err) {
    return apiJson_({
      ok: false,
      name: (err && err.name) || 'Error',
      error: (err && err.message) || String(err),
      fn: nama
    });
  }
}
