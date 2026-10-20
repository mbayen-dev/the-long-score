"""Assemble index.html from src/template.html, src/*.js and data/*.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
t = (root/"src/template.html").read_text()
d = json.loads((root/"data/data.json").read_text())
d["audio"] = json.loads((root/"data/audio_meta.json").read_text())
js = (root/"src/content.js").read_text() + "\n" + (root/"src/content2.js").read_text()
t = t.replace("/*DATA*/null", json.dumps(d, ensure_ascii=False).replace("</", "<\\/")).replace("/*CONTENT*/", js)
(root/"index.html").write_text(t)
print("wrote index.html", len(t))
