/*
 * database-kci-menu.js — menu "Database KCI" di TTC.
 *
 * Menampilkan aplikasi Database KCI – COTP (folder database/) di area kerja
 * TTC. Halaman baru dimuat saat menu pertama kali diklik. Memilih menu lain
 * mengembalikan area kerja TTC seperti semula. Modul ini tidak mengubah data
 * proyek TTC dan tidak menyentuh app.js.
 */
(function () {
  'use strict';

  var area = document.querySelector('.content-area');
  var tombol = document.getElementById('nav-database-kci');
  if (!area || !tombol) return;

  var gaya = document.createElement('style');
  gaya.textContent =
    '#dbkci-panel{flex:1;min-height:0;display:flex;flex-direction:column;padding:12px;gap:8px}' +
    '#dbkci-panel .dbkci-head{display:flex;align-items:center;justify-content:space-between;gap:8px}' +
    '#dbkci-panel h1{margin:2px 0 0;font-size:15px;color:#20324b}' +
    '#dbkci-panel p{margin:3px 0 0;font-size:10px;color:#7e8999}' +
    '#dbkci-panel a.tool-btn{text-decoration:none}' +
    '#dbkci-frame{flex:1;width:100%;min-height:480px;border:1px solid var(--line,#dbe1e8);border-radius:8px;background:#0c1d37}';
  document.head.appendChild(gaya);

  var panel = document.createElement('section');
  panel.id = 'dbkci-panel';
  panel.className = 'hidden';
  panel.innerHTML =
    '<div class="dbkci-head"><div><div class="eyebrow">DATABASE KCI · COTP</div><h1>Database KCI</h1>' +
    '<p>Dashboard, gangguan, sarana &amp; prasarana, train control, dan arsip — data langsung dari Google Sheet DATABASE_KCI_Master.</p></div>' +
    '<a class="tool-btn" href="database/" target="_blank" rel="noopener">⤢ Buka layar penuh</a></div>' +
    '<iframe id="dbkci-frame" title="Database KCI"></iframe>';
  area.insertAdjacentElement('afterend', panel);

  function tampilkan() {
    var frame = document.getElementById('dbkci-frame');
    if (!frame.getAttribute('src')) frame.setAttribute('src', 'database/');
    area.classList.add('hidden');
    panel.classList.remove('hidden');
  }
  function sembunyikan() {
    panel.classList.add('hidden');
    area.classList.remove('hidden');
  }

  tombol.addEventListener('click', tampilkan);
  document.querySelectorAll('.nav-item').forEach(function (b) {
    if (b !== tombol && !b.classList.contains('future')) b.addEventListener('click', sembunyikan);
  });
  if (location.hash === '#database') {
    document.querySelectorAll('.nav-item').forEach(function (b) { b.classList.toggle('active', b === tombol); });
    tampilkan();
  }
})();
