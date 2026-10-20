'use strict';
/**
 * Uji otomatis purwarupa SIGAP (ARB-02): Django + PostgreSQL, halaman sales di Chrome tampilan HP.
 * Menjalankan migrasi, menyalakan server Django, lalu memeriksa mode tanpa sinyal, aturan stok, FEFO,
 * konkurensi, dan telusur batch. Hasil dan tangkapan layar ditulis ke ../bukti/.
 * Jalankan: npm run uji   (variabel SIGAP_DB_* dan SIGAP_PYTHON mengikuti README)
 */
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const ROOT = path.join(__dirname, '..');
const BUKTI = path.join(ROOT, 'bukti');
fs.mkdirSync(BUKTI, { recursive: true });
const PY = process.env.SIGAP_PYTHON || 'python3';
const PORT = 8099;
const BASE = `http://127.0.0.1:${PORT}`;
const hasil = [];
const gambar = [];
const tidur = (ms) => new Promise((r) => setTimeout(r, ms));

function cek(nama, lulus, detail = '') {
  hasil.push({ nama, lulus, detail });
  console.log(`${lulus ? 'LULUS' : 'GAGAL'}  ${nama}${detail ? ` — ${detail}` : ''}`);
}

function cariBrowser() {
  return [
    process.env.BROWSER_PATH,
    '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ].filter(Boolean).find((p) => fs.existsSync(p));
}

async function api(p, opsi = {}) {
  const r = await fetch(BASE + p, { headers: { 'Content-Type': 'application/json' }, ...opsi });
  return { kode: r.status, ...(await r.json()) };
}
const kirimJson = (p, body) => api(p, { method: 'POST', body: JSON.stringify(body) });

async function tungguServer() {
  for (let i = 0; i < 75; i += 1) {
    try { await api('/api/versi'); return; } catch (_) { await tidur(200); }
  }
  throw new Error('Server Django tidak menyala');
}

async function offline(page, aktif) {
  if (typeof page.setOfflineMode === 'function') return page.setOfflineMode(aktif);
  const cdp = await page.createCDPSession();
  await cdp.send('Network.enable');
  return cdp.send('Network.emulateNetworkConditions', { offline: aktif, latency: 0, downloadThroughput: -1, uploadThroughput: -1 });
}

async function foto(page, nama, penuh = true) {
  await page.screenshot({ path: path.join(BUKTI, nama), fullPage: penuh });
  gambar.push(nama);
}

async function bukaHp(browser) {
  const page = await browser.newPage();
  await page.setViewport({ width: 400, height: 860, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  await page.goto(`${BASE}/`, { waitUntil: 'networkidle0' });
  await page.waitForSelector('#daftar-produk .produk');
  return page;
}

async function tambah(page, produkId, kali) {
  for (let i = 0; i < kali; i += 1) await page.click(`.tambah[data-id="${produkId}"]`);
}

const statusTerakhir = (page) => page.evaluate(() => (document.querySelector('.ps') || {}).dataset?.status);
const uuid = () => require('crypto').randomUUID();
const waktuWIB = () => new Intl.DateTimeFormat('id-ID', {
  timeZone: 'Asia/Jakarta', day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false,
}).format(new Date()).replace(/\//g, '-').replace(',', '').replace(':', '.');

(async () => {
  const exe = cariBrowser();
  execFileSync(PY, ['manage.py', 'migrate', '--noinput'], { cwd: ROOT, stdio: 'ignore' });
  const server = spawn(PY, ['manage.py', 'runserver', `127.0.0.1:${PORT}`, '--noreload'], { cwd: ROOT, stdio: 'ignore' });
  let browser;
  let versi = {};
  try {
    await tungguServer();
    versi = await api('/api/versi');
    await kirimJson('/api/reset', {});
    const kat = await api('/api/katalog');
    const P = Object.fromEntries(kat.produk.map((p) => [p.kode, p.id]));
    const O = Object.fromEntries(kat.outlet.map((o) => [o.kode, o.id]));
    const srvProduk = async (kode) => (await api('/api/ringkasan')).produk.find((p) => p.kode === kode);

    browser = await puppeteer.launch({ executablePath: exe, headless: true, args: ['--no-first-run', '--no-sandbox'] });
    const page = await bukaHp(browser);
    cek('Katalog produk dan outlet dimuat dari server Django', (await page.$$eval('#daftar-produk .produk', (e) => e.length)) === 5);
    await foto(page, '01_online_katalog_dimuat.png', false);

    // 1) Tanpa sinyal: pesanan disimpan di HP
    await offline(page, true);
    await page.waitForFunction(() => document.getElementById('status-koneksi').textContent === 'Tanpa sinyal', { timeout: 5000 }).catch(() => {});
    await page.select('#outlet', String(O.OT001));
    await tambah(page, P.KHB060, 3);
    await tambah(page, P.MDP250, 2);
    await page.click('#btn-kirim');
    await page.waitForFunction(() => document.getElementById('pesan').textContent.includes('Tersimpan di HP'), { timeout: 15000 });
    const menunggu = await page.evaluate(() => window.sigap.db.outbox.where('status').equals('menunggu').count());
    cek('Saat tanpa sinyal, pesanan tersimpan di HP (IndexedDB) dengan status "menunggu"', menunggu === 1, `${menunggu} pesanan menunggu`);
    cek('Server belum menerima pesanan selama tanpa sinyal', (await api('/api/ringkasan')).pesanan.length === 0);
    await foto(page, '02_tanpa_sinyal_pesanan_tersimpan_di_hp.png');
    await tidur(10000); // sales berada di area tanpa sinyal selama ±10 detik
    cek('Selama 10 detik tanpa sinyal, pesanan tetap aman di HP', (await page.evaluate(() => window.sigap.db.outbox.count())) === 1);

    // 2) Sinyal kembali: terkirim otomatis
    const mulai = Date.now();
    await offline(page, false);
    await page.waitForFunction(() => document.getElementById('jumlah-menunggu').textContent === '0', { timeout: 25000, polling: 200 });
    const durasi = (Date.now() - mulai) / 1000;
    cek('Saat sinyal kembali, pesanan terkirim otomatis tanpa input ulang', true, `${durasi.toFixed(1)} detik setelah sinyal kembali`);
    await page.waitForFunction(() => (document.querySelector('.ps') || {}).dataset?.status === 'diterima', { timeout: 10000 });
    await tidur(800);
    await foto(page, '03_sinyal_kembali_terkirim_otomatis.png');

    // 3) Tidak tercatat ganda
    const p1 = await page.evaluate(() => window.sigap.db.outbox.toCollection().first());
    const body = { client_uuid: p1.client_uuid, outlet_id: p1.outlet_id, item: p1.item, dibuat_di_hp: p1.dibuat_di_hp };
    const ulang = [(await kirimJson('/api/pesanan', body)).status, (await kirimJson('/api/pesanan', body)).status];
    await page.click('#btn-sinkron');
    await tidur(1000);
    let srv = await api('/api/ringkasan');
    cek('Pengiriman ulang dengan kode unik yang sama dijawab "duplikat"', ulang.every((s) => s === 'duplikat'), `jawaban server: ${ulang.join(', ')}`);
    cek('Server mencatat tepat 1 pesanan (tidak ganda)', srv.pesanan.length === 1, `${srv.pesanan.length} pesanan di server`);
    const pesanan1 = srv.pesanan[0].id;
    const kap = srv.produk.find((p) => p.kode === 'KHB060');
    const madu = srv.produk.find((p) => p.kode === 'MDP250');
    cek('Pesanan diterima: stok tersedia berkurang tepat sekali, stok fisik tetap',
      kap.stok_tersedia === 9 && kap.stok_fisik === 12 && madu.stok_tersedia === 38 && madu.stok_fisik === 40,
      `Kapsul tersedia 12 → ${kap.stok_tersedia} (fisik ${kap.stok_fisik}); Madu Propolis tersedia 40 → ${madu.stok_tersedia} (fisik ${madu.stok_fisik})`);
    cek('Setiap perubahan stok tercatat di riwayat mutasi', srv.mutasi.filter((m) => m.jenis === 'pesan').length === 2, '2 mutasi "pesan"');
    cek('Peringatan stok menipis muncul', kap.menipis === true, `Kapsul tersedia ${kap.stok_tersedia} ≤ minimum ${kap.stok_min}`);

    // 4) Stok kurang: baris ditolak, stok tidak minus
    await page.select('#outlet', String(O.OT002));
    await tambah(page, P.KHB060, 15);
    await page.click('#btn-kirim');
    await page.waitForFunction(() => (document.querySelector('.ps') || {}).dataset?.status === 'ditolak', { timeout: 10000 });
    srv = await api('/api/ringkasan');
    cek('Pesanan melebihi stok tersedia ditolak dan stok tidak menjadi minus',
      srv.produk.find((p) => p.kode === 'KHB060').stok_tersedia === 9, `keterangan: ${srv.pesanan[0].item[0].keterangan}`);
    await tidur(500);
    await foto(page, '04_stok_kurang_baris_ditolak.png');

    // 5) Konfirmasi kirim dengan FEFO
    const k1 = await kirimJson(`/api/pesanan/${pesanan1}/kirim`, {});
    srv = await api('/api/ringkasan');
    const kap2 = srv.produk.find((p) => p.kode === 'KHB060');
    const madu2 = srv.produk.find((p) => p.kode === 'MDP250');
    const batch = (no) => srv.batch.find((b) => b.no_batch === no);
    cek('Konfirmasi kirim: stok fisik dan stok dipesan berkurang, stok tersedia tetap',
      k1.status === 'dikirim' && kap2.stok_fisik === 9 && kap2.stok_dipesan === 0 && kap2.stok_tersedia === 9 && madu2.stok_fisik === 38,
      `Kapsul fisik 12 → ${kap2.stok_fisik}, dipesan 3 → ${kap2.stok_dipesan}; Madu Propolis fisik 40 → ${madu2.stok_fisik}`);
    cek('FEFO: batch dengan kedaluwarsa terdekat terpakai lebih dulu walau masuk belakangan',
      batch('MP-2603').sisa === 13 && batch('MP-2609').sisa === 25,
      `MP-2603 (kedaluwarsa Mar 2027, masuk 1 Okt) 15 → ${batch('MP-2603').sisa}; MP-2609 (Sep 2027, masuk 10 Sep) tetap ${batch('MP-2609').sisa}`);

    // 6) Batal sebelum kirim
    const ps2 = await kirimJson('/api/pesanan', { client_uuid: uuid(), outlet_id: O.OT003, item: [{ produk_id: P.JKA200, jumlah: 4 }] });
    const jamuSaatDipesan = await srvProduk('JKA200');
    const bt = await kirimJson(`/api/pesanan/${ps2.pesanan_id}/batal`, { alasan: 'Outlet membatalkan lewat telepon' });
    const jamu = await srvProduk('JKA200');
    cek('Pesanan dibatalkan sebelum kirim: stok dipesan kembali, stok fisik tetap',
      bt.status === 'batal' && jamuSaatDipesan.stok_tersedia === 20 && jamu.stok_dipesan === 0 && jamu.stok_tersedia === 24 && jamu.stok_fisik === 24,
      `Jamu tersedia 24 → ${jamuSaatDipesan.stok_tersedia} saat dipesan → ${jamu.stok_tersedia} setelah batal; fisik ${jamu.stok_fisik}`);

    // 7) Opname saat ada pesanan yang belum dikirim
    await kirimJson('/api/pesanan', { client_uuid: uuid(), outlet_id: O.OT004, item: [{ produk_id: P.SKR330, jumlah: 5 }] });
    const op = await kirimJson('/api/penyesuaian', { produk_id: P.SKR330, jumlah_fisik: 18, alasan: 'Stock opname rutin' });
    cek('Opname saat ada pesanan belum dikirim: hitungan rak sama dengan stok fisik, tanpa selisih palsu',
      op.selisih === 0 && op.stok_dipesan === 5 && op.stok_tersedia === 13,
      `Sari Kurma: rak 18 = fisik 18 (selisih ${op.selisih}); dipesan ${op.stok_dipesan}, tersedia ${op.stok_tersedia}`);

    // 8) Penyesuaian barang rusak
    const adj = await kirimJson('/api/penyesuaian', { produk_id: P.JKA200, jumlah_fisik: 22, alasan: 'Hasil stock opname: 2 botol rusak' });
    srv = await api('/api/ringkasan');
    const mAdj = srv.mutasi.find((m) => m.jenis === 'penyesuaian' && m.fisik === -2);
    cek('Penyesuaian stok (opname) mencatat selisih, batch, dan alasan',
      adj.selisih === -2 && batch('JK-2612') && srv.batch.find((b) => b.no_batch === 'JK-2612').sisa === 22 && !!mAdj,
      `Jamu fisik 24 → 22 (selisih −2), batch JK-2612 sisa 22, alasan: ${mAdj ? mAdj.alasan : '-'}`);

    // 9) Konkurensi: dua pesanan tiba bersamaan untuk stok terakhir
    const [a, b] = await Promise.all([
      kirimJson('/api/pesanan', { client_uuid: uuid(), outlet_id: O.OT001, item: [{ produk_id: P.MDH500, jumlah: 30 }] }),
      kirimJson('/api/pesanan', { client_uuid: uuid(), outlet_id: O.OT002, item: [{ produk_id: P.MDH500, jumlah: 30 }] }),
    ]);
    const mh = await srvProduk('MDH500');
    cek('Dua pesanan bersamaan untuk 30 botol terakhir: satu diterima, satu ditolak, stok tidak minus',
      [a.status, b.status].sort().join(',') === 'diterima,ditolak' && mh.stok_dipesan === 30 && mh.stok_tersedia === 0,
      `Madu Hutan: ${a.status} dan ${b.status}; dipesan ${mh.stok_dipesan}, tersedia ${mh.stok_tersedia}`);

    // 10) Dua ponsel tanpa sinyal memesan stok terakhir
    const ctxB = await (browser.createBrowserContext ? browser.createBrowserContext() : browser.createIncognitoBrowserContext());
    const hpA = await bukaHp(ctxB);
    const ctxC = await (browser.createBrowserContext ? browser.createBrowserContext() : browser.createIncognitoBrowserContext());
    const hpB = await bukaHp(ctxC);
    for (const [hp, outlet] of [[hpA, O.OT001], [hpB, O.OT003]]) {
      await offline(hp, true);
      await hp.select('#outlet', String(outlet));
      await tambah(hp, P.SKR330, 10);
      await hp.click('#btn-kirim');
      await hp.waitForFunction(() => document.getElementById('pesan').textContent.includes('Tersimpan di HP'), { timeout: 15000 });
    }
    await Promise.all([offline(hpA, false), offline(hpB, false)]);
    for (const hp of [hpA, hpB]) {
      await hp.waitForFunction(() => document.getElementById('jumlah-menunggu').textContent === '0', { timeout: 25000, polling: 200 });
      await hp.waitForFunction(() => ['diterima', 'ditolak'].includes((document.querySelector('.ps') || {}).dataset?.status), { timeout: 10000 });
    }
    const st = [await statusTerakhir(hpA), await statusTerakhir(hpB)];
    const sk = await srvProduk('SKR330');
    srv = await api('/api/ringkasan');
    const tidakMinus = srv.produk.every((p) => p.stok_tersedia >= 0 && p.stok_fisik >= 0);
    cek('Dua ponsel tanpa sinyal memesan 10 botol saat tersedia 13: satu diterima, satu ditolak, stok tidak minus',
      st.slice().sort().join(',') === 'diterima,ditolak' && sk.stok_dipesan === 15 && sk.stok_tersedia === 3 && tidakMinus,
      `HP 1 ${st[0]}, HP 2 ${st[1]}; Sari Kurma dipesan ${sk.stok_dipesan}, tersedia ${sk.stok_tersedia}`);
    await tidur(500);
    await foto(hpA, '06a_dua_ponsel_hp1.png', false);
    await foto(hpB, '06b_dua_ponsel_hp2.png', false);

    // 11) Telusur batch dan panel admin
    const tl = await api('/api/telusur-batch/MP-2603');
    cek('Telusur batch menampilkan outlet penerima yang benar',
      tl.penerima.length === 1 && tl.penerima[0].outlet === 'Apotek Sehat Jebres' && tl.penerima[0].jumlah === 2,
      `MP-2603: ${tl.penerima.map((x) => `${x.outlet} ${x.jumlah} botol`).join('; ')}`);
    const panel = await browser.newPage();
    await panel.setViewport({ width: 1000, height: 500, deviceScaleFactor: 2 });
    await panel.goto(`${BASE}/panel/`, { waitUntil: 'networkidle0' });
    await panel.type('#no-batch', 'MP-2603');
    await panel.click('#btn-telusur');
    await panel.waitForFunction(() => document.querySelectorAll('#t-telusur tr').length >= 3, { timeout: 10000 });
    await panel.waitForFunction(() => document.querySelectorAll('#t-pesanan tr').length > 2, { timeout: 10000 });
    const bawah = await panel.evaluate(() => Math.ceil(document.querySelector('main > .grid').getBoundingClientRect().bottom) + 12);
    await panel.screenshot({ path: path.join(BUKTI, '05_panel_stok_batch_telusur.png'), clip: { x: 0, y: 0, width: 1000, height: bawah } });
    gambar.push('05_panel_stok_batch_telusur.png');
    await foto(panel, '07_panel_lengkap_pesanan_mutasi.png');
  } catch (e) {
    cek('Uji berjalan tanpa galat', false, e.message);
  } finally {
    if (browser) await browser.close();
    server.kill();
  }

  const lulus = hasil.filter((h) => h.lulus).length;
  let py = '';
  try { py = execFileSync(PY, ['--version']).toString().trim(); } catch (_) { /* opsional */ }
  const laporan = [
    'Hasil uji otomatis purwarupa SIGAP (ARB-02)',
    `Dijalankan: ${waktuWIB()} WIB | ${py} | Django ${versi.django} | PostgreSQL ${versi.postgresql} | Node ${process.version} | Dexie 3.2.7 (IndexedDB)`,
    `Browser: ${exe} (tampilan HP 400 × 860)`,
    'Cara uji: koneksi browser diputus lewat emulasi jaringan (setara mode pesawat), lalu dinyalakan kembali.',
    '================================================================',
    ...hasil.map((h, i) => `${h.lulus ? 'LULUS' : 'GAGAL'}  ${i + 1}. ${h.nama}${h.detail ? ` — ${h.detail}` : ''}`),
    '================================================================',
    `Ringkasan: ${lulus} dari ${hasil.length} pemeriksaan lulus.`,
    '',
    'Tangkapan layar:',
    ...gambar.map((g) => `- ${g}`),
  ].join('\n');
  fs.writeFileSync(path.join(BUKTI, 'hasil_uji.txt'), laporan);
  console.log(`\n${lulus}/${hasil.length} lulus. Laporan: bukti/hasil_uji.txt`);
  process.exitCode = lulus === hasil.length ? 0 : 1;
})();
