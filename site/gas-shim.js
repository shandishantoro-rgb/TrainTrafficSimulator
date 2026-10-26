/*
 * gas-shim.js — pengganti google.script.run untuk Database KCI di Cloudflare.
 *
 * Tampilan Database KCI aslinya berjalan di dalam Apps Script dan memanggil
 * server lewat google.script.run. Di luar Apps Script objek itu tidak ada,
 * jadi berkas ini menyediakan objek dengan bentuk yang sama:
 *
 *   google.script.run
 *     .withSuccessHandler(fnSukses)
 *     .withFailureHandler(fnGagal)
 *     .withUserObject(obj)
 *     .namaFungsiServer(arg1, arg2, ...)
 *
 * Setiap panggilan dikirim sebagai POST JSON ke URL /exec Apps Script
 * (lihat apps-script/Api.gs). Kode modul yang ada tidak perlu diubah.
 */
(function () {
  'use strict';

  var KUNCI_SIMPAN = 'dbkci_api_url';

  function ambilUrlApi() {
    var dariConfig = (window.DBKCI_CONFIG && window.DBKCI_CONFIG.apiUrl) || '';
    if (dariConfig) return dariConfig;
    try { return localStorage.getItem(KUNCI_SIMPAN) || ''; } catch (_) { return ''; }
  }

  function buatGalat(pesan, nama) {
    var e = new Error(pesan);
    e.name = nama || 'ScriptError';
    return e;
  }

  function panggil(nama, args) {
    var url = ambilUrlApi();
    if (!url) return Promise.reject(buatGalat('URL API Database KCI belum diatur.'));
    return fetch(url, {
      method: 'POST',
      // text/plain supaya browser tidak mengirim preflight CORS — Apps Script
      // tidak menjawab OPTIONS.
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({ fn: nama, args: args }),
      redirect: 'follow'
    }).then(function (res) {
      return res.text();
    }, function () {
      throw buatGalat('Tidak dapat menghubungi server Database KCI. Periksa koneksi internet.', 'NetworkError');
    }).then(function (teks) {
      var data;
      try { data = JSON.parse(teks); }
      catch (_) {
        throw buatGalat('Server Database KCI tidak menjawab dengan benar. Pastikan Api.gs sudah dipasang dan Web App diterapkan ulang dengan akses "Siapa saja".');
      }
      if (!data || data.ok !== true) throw buatGalat((data && data.error) || 'Galat tidak dikenal', data && data.name);
      return data.result;
    });
  }

  function buatRunner(sukses, gagal, objekPengguna) {
    return new Proxy({}, {
      get: function (_, prop) {
        if (prop === 'withSuccessHandler') return function (h) { return buatRunner(h, gagal, objekPengguna); };
        if (prop === 'withFailureHandler') return function (h) { return buatRunner(sukses, h, objekPengguna); };
        if (prop === 'withUserObject') return function (o) { return buatRunner(sukses, gagal, o); };
        if (typeof prop !== 'string' || prop === 'then' || prop === 'toJSON') return undefined;
        return function () {
          var args = Array.prototype.slice.call(arguments).map(function (a) {
            return a === undefined ? null : a;
          });
          panggil(prop, args).then(function (hasil) {
            if (typeof sukses === 'function') sukses(hasil, objekPengguna);
          }, function (err) {
            if (typeof gagal === 'function') gagal(err, objekPengguna);
            else console.error('[Database KCI] ' + prop + ':', err);
          });
        };
      }
    });
  }

  window.google = window.google || {};
  window.google.script = {
    run: buatRunner(null, null, undefined),
    host: { close: function () {}, setHeight: function () {}, setWidth: function () {}, editor: { focus: function () {} } },
    url: {
      getLocation: function (cb) {
        var p = {}, ps = {};
        new URLSearchParams(location.search).forEach(function (v, k) { p[k] = v; (ps[k] = ps[k] || []).push(v); });
        cb({ hash: location.hash.replace(/^#/, ''), parameter: p, parameters: ps });
      }
    },
    history: { push: function () {}, replace: function () {}, setChangeHandler: function () {} }
  };

  /* Layar pengaturan URL API — hanya muncul bila URL belum diatur. */
  window.DBKCI = {
    panggil: panggil,
    ambilUrlApi: ambilUrlApi,
    simpanUrlApi: function (url) { try { localStorage.setItem(KUNCI_SIMPAN, url); } catch (_) {} },
    hapusUrlApi: function () { try { localStorage.removeItem(KUNCI_SIMPAN); } catch (_) {} }
  };

  function tampilkanPengaturan() {
    var kotak = document.createElement('div');
    kotak.id = 'dbkci-setup';
    kotak.setAttribute('style', 'position:fixed;inset:0;z-index:9999;background:#0c1d37;display:flex;align-items:center;justify-content:center;font-family:"Plus Jakarta Sans",system-ui,sans-serif;padding:16px');
    kotak.innerHTML =
      '<div style="background:#fff;border-radius:18px;max-width:520px;width:100%;padding:28px;color:#1e293b;box-shadow:0 20px 50px rgba(0,0,0,.35)">' +
      '<div style="font-size:11px;font-weight:800;letter-spacing:.12em;color:#b45309">DATABASE KCI · PENGATURAN</div>' +
      '<h1 style="font-size:20px;font-weight:800;margin:6px 0 10px">Sambungkan ke Apps Script</h1>' +
      '<p style="font-size:13px;line-height:1.6;color:#475569;margin:0 0 14px">Tempel URL Web App Apps Script "Database KCI - COTP" (berakhiran <code>/exec</code>). URL disimpan di browser ini saja.</p>' +
      '<input id="dbkci-url" type="url" placeholder="https://script.google.com/macros/s/.../exec" style="width:100%;box-sizing:border-box;padding:10px 12px;border:1px solid #cbd5e1;border-radius:10px;font-size:13px">' +
      '<div id="dbkci-pesan" style="font-size:12px;margin-top:8px;min-height:16px;color:#dc2626"></div>' +
      '<button id="dbkci-simpan" style="margin-top:10px;background:#0c1d37;color:#fff;border:0;border-radius:10px;padding:10px 16px;font-weight:700;font-size:13px;cursor:pointer">Uji &amp; simpan</button>' +
      '</div>';
    document.body.appendChild(kotak);
    var tombol = document.getElementById('dbkci-simpan');
    tombol.onclick = function () {
      var url = document.getElementById('dbkci-url').value.trim();
      var pesan = document.getElementById('dbkci-pesan');
      if (!/^https:\/\/script\.google\.com\/macros\/s\/[\w-]+\/exec$/.test(url)) {
        pesan.textContent = 'Format URL harus https://script.google.com/macros/s/…/exec';
        return;
      }
      tombol.disabled = true; tombol.textContent = 'Menguji…'; pesan.textContent = '';
      window.DBKCI.simpanUrlApi(url);
      panggil('__ping', []).then(function () { location.reload(); }, function (err) {
        window.DBKCI.hapusUrlApi();
        pesan.textContent = err.message;
        tombol.disabled = false; tombol.textContent = 'Uji & simpan';
      });
    };
  }

  if (!ambilUrlApi()) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tampilkanPengaturan);
    else tampilkanPengaturan();
  }
})();
