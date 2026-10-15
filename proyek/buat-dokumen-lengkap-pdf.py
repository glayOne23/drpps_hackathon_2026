"""Buat PDF dokumen lengkap per proyek dari file .md (tanpa batas halaman).

Jalankan:  python3 proyek/buat-dokumen-lengkap-pdf.py [kode ...]   mis. rs-01 arb-01
Hasil:     proyek/<kode>/dokumen-lengkap-<kode>.pdf
Butuh:     python3-markdown, weasyprint (CLI), font Noto Sans.

Isi selalu diambil dari file .md terbaru, jadi cukup jalankan ulang bila file berubah.
Urutan: sampul + daftar isi → profil mitra & temuan situs (docs/mitra) → README proyek
→ 01–06 → draf proposal.
"""
import datetime, html, os, re, subprocess, sys
import markdown

PROYEK_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(os.path.dirname(PROYEK_DIR), "docs")
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus",
         "September", "Oktober", "November", "Desember"]

PROYEK = {  # kode: (label, file mitra, judul bab mitra yang diambil)
    "rs-01": ("RS-01", "rs-ums-ar-fachrudin.md", ["1. Profil mitra", "2. Temuan dari situs RS"]),
    "arb-01": ("ARB-01", "cv-arbain.md", ["1. Profil mitra", "2. Temuan dari situs mitra"]),
    "arb-02": ("ARB-02", "cv-arbain.md", ["1. Profil mitra", "2. Temuan dari situs mitra"]),
    "lkpi-01": ("LKPI-01", "pt-lkpi.md", ["1. Profil mitra", "2. Temuan dari situs mitra"]),
    "lkpi-02": ("LKPI-02", "pt-lkpi.md", ["1. Profil mitra", "2. Temuan dari situs mitra"]),
    "ums-01": ("UMS-01", "dpm-drpps-ums.md", ["1. Profil mitra", "2.11 Referensi tambahan"]),
}
BAB = [  # file proyek, judul bab di PDF
    ("README.md", "Identitas dan status proyek"),
    ("01-empathize.md", "Fase 1 · Empathize"),
    ("02-define.md", "Fase 2 · Define"),
    ("03-ideate.md", "Fase 3 · Ideate"),
    ("04-prototype.md", "Fase 4 · Prototype"),
    ("05-test.md", "Fase 5 · Test"),
    ("06-implement.md", "Fase 6 · Implement"),
    ("proposal-draf.md", "Draf proposal"),
]

CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm;
  @top-left { content: string(proj); font: 7pt 'Noto Sans'; color:#7a8794 }
  @top-right { content: string(bab); font: 7pt 'Noto Sans'; color:#7a8794 }
  @bottom-left { content: "UMS HI Hackathon 2026 · Dokumen lengkap · " string(proj); font: 7pt 'Noto Sans'; color:#7a8794 }
  @bottom-right { content: "hlm. " counter(page) " / " counter(pages); font: 7pt 'Noto Sans'; color:#7a8794 } }
@page sampul { @top-left { content: none } @top-right { content: none } }
body { font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; font-size: 9pt; line-height: 1.4; color:#1d232a }
.sampul { page: sampul; break-after: page }
.sampul .kode { string-set: proj content(); font-size: 11pt; font-weight:700; color:#1f5f99; letter-spacing:.04em; margin-top: 18mm }
.sampul h1 { font-size: 20pt; line-height:1.2; margin: 4mm 0 3mm; color:#14324f; bookmark-level: none }
.sampul .meta { font-size: 9.5pt; color:#444; margin-bottom: 8mm }
.sampul .ket { border-left:3px solid #1f5f99; background:#f4f7fa; padding:6px 9px; font-size:8.5pt; margin: 4mm 0 }
.toc h2 { bookmark-level: none; font-size: 11pt; color:#14324f; border:none; margin-top: 6mm }
.toc ol { list-style:none; padding:0; margin:0 } .toc li { padding: 2px 0; border-bottom: 1px dotted #c9d6e3 }
.toc a { color:#1d232a; text-decoration:none }
.toc a::after { content: target-counter(attr(href), page); float:right; color:#1f5f99 }
.bab { break-before: page }
h1.bab-judul { string-set: bab content(); font-size: 15pt; color:#fff; background:#1f5f99; padding: 5px 9px; border-radius:3px; margin: 0 0 3mm; bookmark-level: 1 }
.bab h1, .bab h2 { font-size: 12pt; color:#14324f; border-bottom: 1.5px solid #1f5f99; padding-bottom:2px; margin: 5mm 0 2mm; bookmark-level: 2 }
.bab h3 { font-size: 10pt; color:#1f5f99; margin: 4mm 0 1.5mm; bookmark-level: 3 }
.bab h4 { font-size: 9.3pt; color:#1f5f99; margin: 3mm 0 1mm; bookmark-level: none }
h2, h3, h4 { break-after: avoid }
p { margin: 1mm 0 2mm }
ul, ol { margin: 1mm 0 2mm; padding-left: 5mm } li { margin: 0 0 .6mm }
blockquote { margin: 1mm 0 3mm; padding: 3px 8px; border-left: 3px solid #9fb3c8; background:#f4f7fa; color:#33404d; font-size: 8.5pt }
blockquote p { margin: .5mm 0 }
table { width:100%; border-collapse: collapse; margin: 1.5mm 0 3mm; font-size: 8.2pt; break-inside: auto }
tr { break-inside: avoid }
th { background:#e6eef6; text-align:left; padding:3px 5px; border:1px solid #c9d6e3 }
td { padding:3px 5px; border:1px solid #d9e1e9; vertical-align: top }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8pt; background:#eef2f6; padding: 0 2px; border-radius:2px }
pre { background:#f4f7fa; padding: 5px 8px; font-size: 7.8pt; white-space: pre-wrap; border-radius:3px }
pre code { background:none; padding:0 }
hr { border:none; border-top: 1px solid #d9e1e9; margin: 3mm 0 }
.src { display:inline-block; font-size:6.8pt; font-weight:700; color:#1f5f99; background:#e6eef6; border-radius:2px; padding:0 3px; line-height:1.2 }
.asm { color:#8a5a00; background:#fbefd7 }
.tgt { color:#2b6b2b; background:#e3f2e1 }
.val { color:#fff; background:#2b6b2b }
.cek { font-family: 'DejaVu Sans'; }
"""


def potong_bab(teks, judul_awal):
    """Ambil bab '## <judul_awal>...' (atau ### untuk sub-bab) sampai heading setingkat berikutnya."""
    for lv in ("## ", "### "):
        m = re.search(rf"^{lv}{re.escape(judul_awal)}.*$", teks, re.M)
        if m:
            sisa = teks[m.end():]
            n = re.search(rf"^#{{1,{len(lv) - 1}}} ", sisa, re.M)
            return teks[m.start(): m.end() + (n.start() if n else len(sisa))].strip()
    return ""


def bersihkan(md):
    md = re.sub(r"<!-- nav(-bottom)?:start -->.*?<!-- nav(-bottom)?:end -->", "", md, flags=re.S)
    md = re.sub(r"^# .*\n", "", md, count=1)  # judul file diganti judul bab
    # tautan relatif → teks saja; tautan http tetap
    md = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\)", r"\1", md)
    md = md.replace("H₂O₂", "H<sub>2</sub>O<sub>2</sub>")
    return md


def label(htm):
    htm = re.sub(r"<code>\[sumber: ([^\]]+)\]</code>", r'<span class="src">\1</span>', htm)
    htm = re.sub(r"\[([PWSRALH](?:, [PWSRALH])*)\]", r'<span class="src">\1</span>', htm)
    htm = htm.replace("<code>[asumsi]</code>", '<span class="src asm">asumsi</span>')
    htm = htm.replace("<code>[target]</code>", '<span class="src tgt">target</span>')
    htm = re.sub(r"<code>\[tervalidasi: ([^\]]*)\]</code>", r'<span class="src val">tervalidasi: \1</span>', htm)
    htm = htm.replace("<li>[ ] ", '<li><span class="cek">☐</span> ').replace("<li>[x] ", '<li><span class="cek">☑</span> ')
    return htm


def md2html(md):
    return label(markdown.markdown(md, extensions=["tables", "sane_lists", "fenced_code"]))


def judul_proyek(p):
    t = open(os.path.join(PROYEK_DIR, p, "README.md"), encoding="utf8").readline()
    return t.lstrip("# ").split("—", 1)[-1].strip()


def buat(p):
    label_kode, file_mitra, bab_mitra = PROYEK[p]
    judul = judul_proyek(p)
    hari = datetime.date.today()
    tgl = f"{hari.day} {BULAN[hari.month - 1]} {hari.year}"

    bagian = []
    mitra_md = open(os.path.join(DOCS, "mitra", file_mitra), encoding="utf8").read()
    isi_mitra = "\n\n".join(potong_bab(mitra_md, b) for b in bab_mitra)
    bagian.append(("mitra", "Profil mitra dan temuan situs", bersihkan("# x\n" + isi_mitra)))
    for fn, jb in BAB:
        md = open(os.path.join(PROYEK_DIR, p, fn), encoding="utf8").read()
        bagian.append((fn.split(".")[0], jb, bersihkan(md)))

    toc = "".join(f'<li><a href="#b-{i}">{html.escape(j)}</a></li>' for i, (_, j, _) in enumerate(bagian))
    badan = "".join(
        f'<section class="bab"><h1 class="bab-judul" id="b-{i}">{html.escape(j)}</h1>{md2html(md)}</section>'
        for i, (_, j, md) in enumerate(bagian))
    doc = f"""<!doctype html><html lang="id"><head><meta charset="utf-8">
<title>{label_kode} · Dokumen lengkap</title><style>{CSS}</style></head><body>
<div class="sampul"><div class="kode">{label_kode}</div><h1>{html.escape(judul)}</h1>
<div class="meta">Dokumen lengkap proyek · UMS Health Innovation Hackathon 2026 · dibuat {tgl}</div>
<div class="ket"><b>Isi:</b> semua data yang sudah dikumpulkan dan diolah untuk tantangan ini — profil mitra dan temuan situs, identitas proyek, fase Empathize sampai Implement, dan draf proposal. Sebagian besar isi adalah <b>draf dari riset sekunder</b> yang harus dikonfirmasi lewat wawancara/observasi.</div>
<div class="ket"><b>Tanda:</b> <span class="src">W</span> laman tantangan · <span class="src">S</span> sosialisasi 7 Okt · <span class="src">P</span> pedoman · <span class="src">R</span> situs RS · <span class="src">A</span> situs CV Arbain · <span class="src">L</span> situs PT LKPI · <span class="src">H</span> UMS Innovation Hub · <span class="src asm">asumsi</span> dugaan tim · <span class="src tgt">target</span> hasil yang ingin dicapai · ☐/☑ checklist.</div>
<div class="toc"><h2>Daftar isi</h2><ol>{toc}</ol></div></div>
{badan}</body></html>"""

    build = os.path.join(PROYEK_DIR, ".pdf-build")
    os.makedirs(build, exist_ok=True)
    src = os.path.join(build, f"lengkap-{p}.html")
    out = os.path.join(PROYEK_DIR, p, f"dokumen-lengkap-{p}.pdf")
    open(src, "w", encoding="utf8").write(doc)
    subprocess.run(["weasyprint", "-q", src, out], check=True)
    return out


if __name__ == "__main__":
    for p in sys.argv[1:] or PROYEK:
        print(buat(p))
