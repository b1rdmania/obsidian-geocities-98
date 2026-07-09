import base64, os, pathlib
ROOT = pathlib.Path(__file__).parent
A = ROOT / "assets"
def d(fn):
    b = (A / fn).read_bytes()
    mime = "image/png" if fn.endswith(".png") else "image/gif"
    return f"data:{mime};base64,{base64.b64encode(b).decode()}"

VARS = {
 "STARFIELD": d("starfield_tile.png"),
 "CONFETTI":  d("confetti_tile.png"),
 "DIVIDER":   d("divider_bar.gif"),
 "DIVIDER2":  d("divider_grad.gif"),
 "STAR":      d("star.gif"),
 "FLAME":     d("flame.gif"),
 "GLOBE":     d("globe.gif"),
 "CONSTRUCTION": d("construction.gif"),
 "NEWBADGE":  d("newbadge.gif"),
 "COUNTER":   d("counter.gif"),
}
css = (ROOT / "theme.src.css").read_text()
for k,v in VARS.items():
    css = css.replace("__%s__" % k, v)
(ROOT / "theme.css").write_text(css)
print("theme.css written:", len((ROOT/"theme.css").read_text())//1024, "KB")
