'use strict';
/* SIGAP — halaman sales satu halaman (Django + PostgreSQL; uji mode tanpa sinyal tanpa PWA).
 * Pesanan selalu disimpan dulu ke IndexedDB (outbox) dengan kode unik (client_uuid),
 * lalu dikirim. Bila gagal karena tidak ada sinyal, pesanan tetap di HP dan dikirim ulang
 * otomatis saat sinyal kembali (event "online", setiap 15 detik, atau tombol "Kirim sekarang").
 * Server mengabaikan kode yang sudah pernah diterima, sehingga pesanan tidak tercatat dua kali. */
const db = new Dexie('sigap_sales');
db.version(1).stores({ outbox: 'client_uuid, status, dibuat, outlet_id', cache: 'kunci' });

const $ = (id) => document.getElementById(id);
const rupiah = (n) => 'Rp' + Number(n || 0).toLocaleString('id-ID');
const jam = (d) => 'pukul ' + new Date(d).toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
let katalog = { produk: [], outlet: [], waktu: null };
let jumlah = {};
let sedangSinkron = false;

function uuid() {
  if (window.crypto && crypto.randomUUID) { try { return crypto.randomUUID(); } catch (_) { /* lanjut */ } }
  const b = crypto.getRandomValues(new Uint8Array(16)); // tersedia juga di http (bukan hanya https)
  b[6] = (b[6] & 0x0f) | 0x40; b[8] = (b[8] & 0x3f) | 0x80;
  const h = Array.from(b, (x) => x.toString(16).padStart(2, '0')).join('');
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20)}`;
}

function setKoneksi(online) {
  const el = $('status-koneksi');
  el.textContent = online ? 'Online' : 'Tanpa sinyal';
  el.className = 'lencana ' + (online ? 'online' : 'offline');
}

function tampilPesan(teks, jenis) {
  const el = $('pesan');
  el.textContent = teks;
  el.className = 'pesan ' + jenis;
}

async function muatKatalog() {
  try {
    const r = await fetch('/api/katalog', { cache: 'no-store' });
    if (!r.ok) throw new Error('server');
    const j = await r.json();
    katalog = { produk: j.produk, outlet: j.outlet, waktu: new Date().toISOString() };
    await db.cache.put({ kunci: 'katalog', ...katalog });
    setKoneksi(true);
  } catch (_) {
    const c = await db.cache.get('katalog');
    if (c) katalog = c;
    setKoneksi(false);
  }
  renderForm();
}

function renderForm() {
  const sel = $('outlet');
  const pilih = sel.value;
  sel.innerHTML = katalog.outlet.map((o) => `<option value="${o.id}">${o.nama} (${o.jenis})</option>`).join('');
  if (pilih) sel.value = pilih;
  $('info-stok').textContent = katalog.waktu ? `Stok tersedia per ${jam(katalog.waktu)} (server tetap penentu stok).` : '';
  $('daftar-produk').innerHTML = katalog.produk.map((p) => `
    <div class="produk" data-id="${p.id}">
      <div><div class="nama">${p.nama}</div>
        <span class="stok ${p.stok_tersedia <= p.stok_min ? 'menipis' : ''}">tersedia ${p.stok_tersedia}</span>
        <span class="kecil">${rupiah(p.harga)}</span></div>
      <div class="langkah">
        <button type="button" class="kurang" data-id="${p.id}" aria-label="kurangi">−</button>
        <span id="j-${p.id}">${jumlah[p.id] || 0}</span>
        <button type="button" class="tambah" data-id="${p.id}" aria-label="tambah">+</button>
      </div>
    </div>`).join('');
  hitungTotal();
}

function hitungTotal() {
  const total = katalog.produk.reduce((t, p) => t + (jumlah[p.id] || 0) * p.harga, 0);
  $('total').textContent = rupiah(total);
}

$('daftar-produk').addEventListener('click', (e) => {
  const b = e.target.closest('button');
  if (!b) return;
  const id = b.dataset.id;
  jumlah[id] = Math.max(0, (jumlah[id] || 0) + (b.classList.contains('tambah') ? 1 : -1));
  $(`j-${id}`).textContent = jumlah[id];
  hitungTotal();
});

$('btn-ulang').addEventListener('click', async () => {
  const outlet = Number($('outlet').value);
  const daftar = await db.outbox.where('outlet_id').equals(outlet).sortBy('dibuat');
  const terakhir = daftar[daftar.length - 1];
  if (!terakhir) return tampilPesan('Belum ada pesanan sebelumnya untuk outlet ini.', 'tunggu');
  jumlah = {};
  terakhir.item.forEach((it) => { jumlah[it.produk_id] = it.jumlah; });
  renderForm();
  tampilPesan('Pesanan terakhir dimuat. Ubah jumlah bila perlu, lalu kirim.', 'ok');
});

$('btn-kirim').addEventListener('click', async () => {
  const item = Object.entries(jumlah).filter(([, j]) => j > 0).map(([id, j]) => ({ produk_id: Number(id), jumlah: j }));
  if (!item.length) return tampilPesan('Pilih minimal satu produk.', 'galat');
  const outlet = katalog.outlet.find((o) => o.id === Number($('outlet').value));
  const kode = uuid();
  await db.outbox.put({
    client_uuid: kode, outlet_id: outlet.id, outlet: outlet.nama, item,
    ringkas: item.map((it) => `${katalog.produk.find((p) => p.id === it.produk_id).nama} × ${it.jumlah}`).join(', '),
    dibuat_di_hp: new Date().toISOString(), dibuat: Date.now(), status: 'menunggu',
  });
  jumlah = {};
  renderForm();
  await sinkron();
  const hasil = await db.outbox.get(kode);
  const teks = {
    menunggu: ['Tersimpan di HP. Pesanan akan dikirim otomatis saat sinyal kembali.', 'tunggu'],
    diterima: ['Pesanan diterima kantor; stok tersedia sudah dikurangi.', 'ok'],
    diterima_sebagian: ['Pesanan diterima sebagian: ada item yang stoknya tidak cukup.', 'tunggu'],
    ditolak: ['Pesanan ditolak: stok tersedia tidak mencukupi. Lihat rincian di "Pesanan saya".', 'galat'],
  }[hasil.status] || ['Pesanan gagal dikirim. Coba "Kirim sekarang".', 'galat'];
  tampilPesan(teks[0], teks[1]);
});

async function sinkron() {
  if (sedangSinkron) return false;
  sedangSinkron = true;
  let semua = true;
  let terkirimKali = 0;
  try {
    const daftar = await db.outbox.where('status').equals('menunggu').sortBy('dibuat');
    for (const p of daftar) {
      let r;
      try {
        r = await fetch('/api/pesanan', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Idempotency-Key': p.client_uuid },
          body: JSON.stringify({ client_uuid: p.client_uuid, outlet_id: p.outlet_id, item: p.item, dibuat_di_hp: p.dibuat_di_hp }),
        });
      } catch (_) {
        setKoneksi(false);
        semua = false;
        break; // tidak ada sinyal: coba lagi nanti
      }
      const j = await r.json().catch(() => ({}));
      if (r.ok) {
        await db.outbox.update(p.client_uuid, {
          status: j.status === 'duplikat' ? (j.status_awal || 'diterima') : j.status, server: j, terkirim: Date.now(),
        });
        setKoneksi(true);
        terkirimKali += 1;
      } else {
        await db.outbox.update(p.client_uuid, { status: 'gagal', server: j });
      }
    }
  } finally {
    sedangSinkron = false;
    await renderPesanan();
  }
  if (terkirimKali > 0) tampilPesan(`Sinyal tersedia: ${terkirimKali} pesanan terkirim otomatis ke kantor.`, 'ok');
  if (semua) await muatKatalog();
  return semua;
}

async function renderPesanan() {
  const semua = await db.outbox.orderBy('dibuat').reverse().toArray();
  $('jumlah-menunggu').textContent = semua.filter((p) => p.status === 'menunggu').length;
  const label = { menunggu: 'Menunggu sinyal', diterima: 'Diterima', diterima_sebagian: 'Diterima sebagian', ditolak: 'Ditolak', gagal: 'Gagal' };
  $('daftar-pesanan').innerHTML = semua.length ? semua.map((p) => {
    const tolak = p.server && p.server.baris ? p.server.baris.filter((b) => b.diterima === 0).map((b) => `${b.produk}: ${b.keterangan}`) : [];
    return `<div class="ps" data-uuid="${p.client_uuid}" data-status="${p.status}">
      <span class="chip ${p.status}">${label[p.status] || p.status}</span>
      <b>${p.outlet}</b><br><span class="kecil">dibuat ${jam(p.dibuat)}${p.terkirim ? ` · terkirim ${jam(p.terkirim)}` : ''}${p.server && p.server.pesanan_id ? ` · no. ${p.server.pesanan_id}` : ''}</span>
      <div>${p.ringkas}</div>${tolak.length ? `<div class="merah">${tolak.join('; ')}</div>` : ''}
      <div class="kecil">kode unik: ${p.client_uuid.slice(0, 8)}…</div></div>`;
  }).join('') : '<p class="kecil">Belum ada pesanan.</p>';
}

$('btn-sinkron').addEventListener('click', async () => {
  const ok = await sinkron();
  tampilPesan(ok ? 'Semua pesanan sudah terkirim.' : 'Masih tanpa sinyal; pesanan tetap aman di HP.', ok ? 'ok' : 'tunggu');
});
window.addEventListener('online', () => { setKoneksi(true); sinkron(); });
window.addEventListener('offline', () => setKoneksi(false));
setInterval(sinkron, 15000);

(async () => {
  if (navigator.storage && navigator.storage.persist) { try { await navigator.storage.persist(); } catch (_) { /* opsional */ } }
  await muatKatalog();
  await renderPesanan();
  sinkron();
})();

window.sigap = { db, sinkron }; // dipakai uji otomatis
