import json
import urllib.request
from collections import Counter

import streamlit as st

st.set_page_config(
    page_title="Executive Search · Live-Auswertung",
    page_icon="◼",
    layout="wide",
)

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg,#0E2033 0%,#17324D 55%,#1D405D 100%); }
h1, h2, h3, h4, h5, h6, p, [data-testid="stCaptionContainer"], [data-testid="stMarkdownContainer"] { color:#fff !important; }
[data-testid="stMarkdownContainer"] strong, [data-testid="stMarkdownContainer"] span { color:inherit !important; }
.block-container { max-width: 1400px; padding-top: 2rem; }
[data-testid="stMetric"] { background:#fff; border-radius:14px; padding:16px 18px; }
[data-testid="stMetric"] * { color:#14283B !important; }
[data-testid="stDataFrame"] { background:#fff; border-radius:14px; padding:8px; }
/* All presentation text on the navy canvas stays white. */
.stApp > header { background: transparent; }
.live-chart { background:#fff; border-radius:16px; padding:20px 22px; margin:8px 0 18px; }
.live-bar-row { display:grid; grid-template-columns:minmax(120px, 220px) 1fr 48px; gap:14px; align-items:center; margin:12px 0; }
.live-bar-label, .live-bar-value { color:#14283B !important; font-weight:700; }
.live-bar-value { text-align:right; font-size:1.05rem; }
.live-bar-track { height:22px; background:#E8EEF4; border-radius:6px; overflow:hidden; }
.live-bar-fill { height:100%; background:#0A66C2; border-radius:6px; }
.live-table-wrap { background:#fff; border-radius:16px; padding:12px 18px; overflow-x:auto; }
.live-table { width:100%; border-collapse:collapse; }
.live-table th, .live-table td { color:#14283B !important; padding:12px 10px; border-bottom:1px solid #E4EAF0; text-align:left; }
.live-table th { font-weight:800; }
@media (max-width: 800px) { .live-bar-row { grid-template-columns:90px 1fr 38px; gap:8px; } }
</style>
""", unsafe_allow_html=True)

st.title("LIVE-AUSWERTUNG · EXECUTIVE SEARCH")
st.caption("Anonym aggregierte Einzelentscheidungen · Moderatoransicht")

try:
    SUPABASE_URL = st.secrets.get("SUPABASE_URL", "").rstrip("/")
    SERVICE_KEY = st.secrets.get("SUPABASE_SERVICE_KEY", "")
except Exception:
    SUPABASE_URL = ""
    SERVICE_KEY = ""

if not SUPABASE_URL or not SERVICE_KEY:
    st.error("Supabase ist noch nicht vollständig verbunden. Für dieses Dashboard müssen SUPABASE_URL und SUPABASE_SERVICE_KEY in den Streamlit-Secrets hinterlegt sein.")
    st.stop()


def load_rows():
    endpoint = (
        SUPABASE_URL
        + "/rest/v1/executive_search_results"
        + "?select=*&completed=eq.true&order=created_at.asc"
    )
    req = urllib.request.Request(
        endpoint,
        headers={
            "apikey": SERVICE_KEY,
            "Authorization": "Bearer " + SERVICE_KEY,
        },
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


try:
    rows = load_rows()
except Exception as exc:
    st.error("Die Live-Daten konnten nicht aus Supabase geladen werden.")
    st.caption(str(exc))
    st.stop()

if st.button("↻ Live-Daten aktualisieren", type="primary"):
    st.rerun()

st.metric("Abgeschlossene Einzelentscheidungen", len(rows))

if not rows:
    st.info("Noch keine abgeschlossenen Durchläufe vorhanden.")
    st.stop()


def short_candidate(value):
    if not value:
        return None
    return str(value).replace("KANDIDAT ", "").replace("CANDIDATE ", "").strip()


def show_counter(title, counter, x_label="Kandidat:in"):
    st.subheader(title)
    if not counter:
        st.caption("Noch keine Daten vorhanden.")
        return

    items = counter.most_common()
    max_value = max(value for _, value in items) or 1
    bars = []
    for label, value in items:
        width = max(4, round(value / max_value * 100))
        bars.append(f"""
        <div class="live-bar-row">
          <div class="live-bar-label">{label}</div>
          <div class="live-bar-track"><div class="live-bar-fill" style="width:{width}%"></div></div>
          <div class="live-bar-value">{value}</div>
        </div>
        """)
    st.markdown('<div class="live-chart">' + ''.join(bars) + '</div>', unsafe_allow_html=True)


# 1) First Screening: Häufigkeit + gewichtete Rangpunkte
first_frequency = Counter()
first_points = Counter()
for row in rows:
    for rank, field in enumerate(("first_rank_1", "first_rank_2", "first_rank_3"), start=1):
        cand = short_candidate(row.get(field))
        if cand:
            first_frequency[cand] += 1
            first_points[cand] += {1: 3, 2: 2, 3: 1}[rank]

# 2) Auswahlkriterien
criteria = Counter()
for row in rows:
    obj = row.get("first_criteria") or {}
    if isinstance(obj, str):
        try:
            obj = json.loads(obj)
        except Exception:
            obj = {}
    selected = obj.get("selected", []) if isinstance(obj, dict) else []
    for item in selected or []:
        if item:
            criteria[str(item)] += 1

# 3) Rankingbewegung nach Second Look
moved = 0
unchanged = 0
movement_by_candidate = Counter()
for row in rows:
    first = [short_candidate(row.get(f"first_rank_{i}")) for i in (1, 2, 3)]
    second = [short_candidate(row.get(f"second_rank_{i}")) for i in (1, 2, 3)]
    if all(first) and all(second):
        if first == second:
            unchanged += 1
        else:
            moved += 1
        for cand in set(first) & set(second):
            delta = first.index(cand) - second.index(cand)
            if delta != 0:
                movement_by_candidate[cand] += 1

# 4) Finale Empfehlungen
finals = Counter(
    short_candidate(row.get("final_candidate"))
    for row in rows
    if row.get("final_candidate")
)

# 5) Blind Spot
blind_yes = Counter()
blind_total = Counter()
for row in rows:
    obj = row.get("blind_spot") or {}
    if isinstance(obj, str):
        try:
            obj = json.loads(obj)
        except Exception:
            obj = {}
    if isinstance(obj, dict):
        for cand_raw, answer in obj.items():
            cand = short_candidate(cand_raw)
            blind_total[cand] += 1
            # App speichert bool oder textähnliche Werte; beides robust auswerten.
            yes = answer is True or str(answer).strip().lower() in {
                "ja", "yes", "true", "1", "würde ich näher prüfen"
            }
            if yes:
                blind_yes[cand] += 1

# 6) Sicherheit
conf_first = [r.get("confidence_first") for r in rows if isinstance(r.get("confidence_first"), (int, float))]
conf_final = [r.get("confidence_final") for r in rows if isinstance(r.get("confidence_final"), (int, float))]

st.markdown("---")
st.header("1 · First Screening")
c1, c2 = st.columns(2)
with c1:
    show_counter("Wie oft war ein Profil in der ersten Top 3?", first_frequency)
with c2:
    show_counter("Ranggewichtete Shortlist-Punkte", first_points)

st.markdown("---")
st.header("2 · Welche Kriterien haben die Auswahl geprägt?")
show_counter("Auswahlkriterien im First Screening", criteria, "Kriterium")

st.markdown("---")
st.header("3 · Was hat der Second Look verändert?")
a, b, c = st.columns(3)
a.metric("Rangfolge verändert", moved)
b.metric("Rangfolge unverändert", unchanged)
c.metric("Ausgewertete Second Looks", moved + unchanged)
if movement_by_candidate:
    show_counter("Bei welchen Profilen änderte sich die Position?", movement_by_candidate)

st.markdown("---")
st.header("4 · Finale Empfehlungen")
show_counter("Welche Kandidat:innen wurden final empfohlen?", finals)

st.markdown("---")
st.header("5 · Blind-Spot Check")
if blind_total:
    rows_html = []
    for cand, total in sorted(blind_total.items()):
        yes_count = blind_yes.get(cand, 0)
        yes_share = f"{(yes_count / total * 100):.0f}%" if total else "—"
        rows_html.append(
            f"<tr><td>{cand}</td><td>{yes_count}</td><td>{total}</td><td><strong>{yes_share}</strong></td></tr>"
        )
    st.markdown(
        """<div class="live-table-wrap"><table class="live-table">
        <thead><tr><th>Kandidat:in</th><th>Ja – hätte ich näher geprüft</th><th>Antworten gesamt</th><th>Ja-Anteil</th></tr></thead>
        <tbody>""" + "".join(rows_html) + "</tbody></table></div>",
        unsafe_allow_html=True,
    )
else:
    st.caption("Noch keine Blind-Spot-Antworten vorhanden.")

st.markdown("---")
st.header("6 · Sicherheit der Entscheidungen")
m1, m2 = st.columns(2)
m1.metric(
    "Ø Sicherheit First Screening",
    f"{sum(conf_first) / len(conf_first):.0f}%" if conf_first else "—",
)
m2.metric(
    "Ø Sicherheit final",
    f"{sum(conf_final) / len(conf_final):.0f}%" if conf_final else "—",
)

st.markdown("---")
st.caption(
    "Moderationsprinzip: Ergebnisse beschreiben, nicht als richtig oder falsch bewerten. "
    "Fokus: Information → Interpretation → Anforderungsbezug → Eignungsprognose."
)
