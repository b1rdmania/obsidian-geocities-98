import json, pathlib
d = json.loads(pathlib.Path("promo_assets.json").read_text())
html = pathlib.Path("promo.src.html").read_text()
for k,v in d.items():
    html = html.replace("__%s__"%k, v)
pathlib.Path("_promo.html").write_text(html)
print("promo html built")
