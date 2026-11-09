import json
import re
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent

report = (ROOT / "report.md").read_text(encoding="utf-8")
vocab = (ROOT / "vocabulary.md").read_text(encoding="utf-8")
aliases = json.loads((HERE / "aliases.json").read_text(encoding="utf-8"))

terms = re.findall(r"^##\s+(.+?)\s*$", vocab, flags=re.MULTILINE)

sections = {}
current = None
for line in report.splitlines():
    m = re.match(r"^##\s+(\d+\.\s+.+)$", line)
    if m:
        current = m.group(1)
        sections[current] = []
    elif current:
        sections[current].append(line)
sections = {k: "\n".join(v) for k, v in sections.items()}


def count(phrase, text):
    # whole-phrase match; an optional plural ending is allowed (agent -> agents)
    pattern = r"(?<!\w)" + re.escape(phrase) + r"(?:s|es)?(?!\w)"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


links = []
totals = {t: {"explicit": 0, "implicit": 0} for t in terms}
for term in terms:
    entry = aliases.get(term.lower(), {})
    explicit_forms = [term] + entry.get("variants", [])
    implicit_forms = entry.get("implicit", [])
    for sec, text in sections.items():
        e = sum(count(f, text) for f in explicit_forms)
        i = sum(count(f, text) for f in implicit_forms)
        if e or i:
            links.append({"term": term, "section": sec, "explicit": e, "implicit": i})
        totals[term]["explicit"] += e
        totals[term]["implicit"] += i

data = {"terms": terms, "sections": list(sections), "links": links, "totals": totals}
(HERE / "stats.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
(HERE / "stats.js").write_text("const STATS = " + json.dumps(data) + ";", encoding="utf-8")

print(f"{len(terms)} terms, {len(sections)} sections, {len(links)} links")
for t, v in totals.items():
    print(f"{t}: explicit {v['explicit']}, implicit {v['implicit']}")