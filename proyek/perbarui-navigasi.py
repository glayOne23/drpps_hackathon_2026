"""Perbarui bilah navigasi di semua file proyek/. Jalankan: python3 proyek/perbarui-navigasi.py
Aman dijalankan berulang (memakai penanda <!-- nav:... -->). Tambahkan proyek baru ke daftar PROJECTS."""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))  # default: folder proyek/
PROJECTS = [  # (folder, label, file mitra di docs/mitra)
    ("rs-01", "RS-01", "rs-ums-ar-fachrudin.md"),
    ("arb-01", "ARB-01", "cv-arbain.md"),
    ("arb-02", "ARB-02", "cv-arbain.md"),
    ("lkpi-01", "LKPI-01", "pt-lkpi.md"),
    ("lkpi-02", "LKPI-02", "pt-lkpi.md"),
    ("ums-01", "UMS-01", "dpm-drpps-ums.md"),
]
TEMPLATE = ("_template", "Template", None)
FILES = [  # (nama file, label)
    ("README.md", "README"),
    ("01-empathize.md", "1 Empathize"),
    ("02-define.md", "2 Define"),
    ("03-ideate.md", "3 Ideate"),
    ("04-prototype.md", "4 Prototype"),
    ("05-test.md", "5 Test"),
    ("06-implement.md", "6 Implement"),
    ("proposal-draf.md", "Draf proposal"),
]
TOP = re.compile(r"\n?<!-- nav:start -->.*?<!-- nav:end -->\n?", re.S)
BOTTOM = re.compile(r"\n?<!-- nav-bottom:start -->.*?<!-- nav-bottom:end -->\n?", re.S)


def top_bar(proj, cur):
    folder, label, mitra = proj
    items = []
    for fn, fl in FILES:
        items.append(f"**{fl}**" if fn == cur else f"[{fl}]({fn})")
    line1 = f"[◂ Semua proyek](../README.md) · **{label}** · " + " · ".join(items)
    extra = []
    if mitra:
        extra.append(f"[Mitra](../../docs/mitra/{mitra})")
    else:
        extra.append("[Mitra](../../docs/mitra/)")
    extra.append("[Peran tim](../../docs/04-peran-tim.md)")
    extra.append("[Template proposal](../../docs/03-template-proposal.md)")
    extra.append("[Dokumen](../../docs/README.md)")
    line2 = "Referensi: " + " · ".join(extra)
    return f"<!-- nav:start -->\n{line1}  \n{line2}\n<!-- nav:end -->\n"


def bottom_bar(proj, cur):
    names = [f for f, _ in FILES]
    labels = dict(FILES)
    i = names.index(cur)
    parts = []
    if i > 0:
        parts.append(f"◂ [{labels[names[i-1]]}]({names[i-1]})")
    parts.append("[▴ Atas](#)")
    if i < len(names) - 1:
        parts.append(f"[{labels[names[i+1]]}]({names[i+1]}) ▸")
    line1 = " · ".join(parts)
    others = []
    for f, l, _ in PROJECTS + [TEMPLATE]:
        if f == proj[0]:
            continue
        others.append(f"[{l}](../{f}/{cur})")
    line2 = f"{labels[cur]} di proyek lain: " + " · ".join(others)
    return f"<!-- nav-bottom:start -->\n\n---\n\n{line1}  \n{line2}\n<!-- nav-bottom:end -->\n"


def apply(path, proj, cur):
    s = open(path, encoding="utf8").read()
    s = TOP.sub("\n", s, count=1)
    s = BOTTOM.sub("", s).rstrip() + "\n"
    lines = s.split("\n")
    # sisipkan bilah atas tepat setelah judul H1
    h1 = next(k for k, l in enumerate(lines) if l.startswith("# "))
    rest = "\n".join(lines[h1 + 1:]).lstrip("\n")
    s = "\n".join(lines[: h1 + 1]) + "\n\n" + top_bar(proj, cur) + "\n" + rest
    s = s.rstrip() + "\n\n" + bottom_bar(proj, cur)
    open(path, "w", encoding="utf8").write(s)


n = 0
for proj in PROJECTS + [TEMPLATE]:
    for fn, _ in FILES:
        p = os.path.join(ROOT, proj[0], fn)
        if os.path.exists(p):
            apply(p, proj, fn)
            n += 1
print("updated", n)
