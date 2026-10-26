#!/usr/bin/env node
/*
 * build-database-kci.mjs
 * Menyusun site/index.html dari sumber tampilan Apps Script di
 * database-kci/src/ (salinan file .html proyek "Database KCI - COTP").
 *
 *   node tools/build-database-kci.mjs
 *
 * Yang dilakukan:
 *  1. Mulai dari Index.html, ganti setiap <?!= include('Nama'); ?> dengan
 *     isi Nama.html (berulang, sama seperti include() di Code.gs).
 *  2. Buang <base target="_top"> (khusus sandbox Apps Script).
 *  3. Sisipkan config.js dan gas-shim.js paling awal di <head> supaya
 *     google.script.run sudah tersedia sebelum skrip modul berjalan.
 *
 * Setelah mengubah tampilan di Apps Script, salin ulang file .html-nya ke
 * database-kci/src/ lalu jalankan skrip ini lagi.
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const akar = join(dirname(fileURLToPath(import.meta.url)), '..');
const folderSumber = join(akar, 'database-kci', 'src');
const berkasHasil = join(akar, "site", "index.html");
const POLA_INCLUDE = /<\?!=\s*include\(\s*['"]([\w-]+)['"]\s*\)\s*;?\s*\?>/g;

function baca(nama) {
  const jalur = join(folderSumber, nama + '.html');
  if (!existsSync(jalur)) throw new Error('Berkas tidak ditemukan: ' + nama + '.html');
  return readFileSync(jalur, 'utf8');
}

// Sama seperti Apps Script: hanya scriptlet di Index.html yang dijalankan.
// Isi file yang disisipkan dimasukkan apa adanya (include() di Code.gs memakai
// createHtmlOutputFromFile().getContent(), yang tidak memproses scriptlet).
const induk = baca('Index');
const sisa = induk.replace(POLA_INCLUDE, '').match(/<\?[\s\S]*?\?>/g);
if (sisa) throw new Error('Index.html memuat scriptlet yang belum didukung: ' + sisa.slice(0, 3).join(' | '));

let html = induk.replace(POLA_INCLUDE, (_, anak) => baca(anak));

html = html.replace(/\s*<base\s+target=["']_top["']\s*\/?>/i, '');
html = html.replace(/<head>/i, [
  '<head>',
  '    <!-- Dibangun otomatis oleh tools/build-database-kci.mjs — jangan diedit langsung; edit database-kci/src/ -->',
  '    <script src="config.js"></script>',
  '    <script src="gas-shim.js"></script>'
].join('\n'));

writeFileSync(berkasHasil, html);
console.log('site/index.html dibuat (' + Math.round(html.length / 1024) + ' KB)');
