import json
import urllib.request
from collections import Counter
from datetime import datetime, timezone
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Executive Search · Live-Auswertung", page_icon="◼", layout="wide")

NAVY="#0E2033"; NAVY2="#17324D"; BLUE="#0A66C2"; WHITE="#FFFFFF"; SOFT="#D9E5EF"; GREEN="#2F8F67"; AMBER="#D79B32"; RED="#C94E55"

st.markdown(f"""
<style>
.stApp{{background:radial-gradient(circle at 78% 8%,rgba(35,79,112,.55) 0%,rgba(35,79,112,0) 32%),linear-gradient(145deg,#0E2033 0%,#17324D 48%,#1D405D 100%);background-attachment:fixed}}
.block-container{{max-width:1400px;padding-top:1.4rem;padding-bottom:4rem}}
[data-testid="stHeader"]{{background:transparent}}
h1,h2,h3,h4,p,label,div{{font-family:Arial,sans-serif}}
[data-testid="stMarkdownContainer"] h1,[data-testid="stMarkdownContainer"] h2,[data-testid="stMarkdownContainer"] h3,[data-testid="stMarkdownContainer"] h4{{color:#fff!important}}
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] *{{color:#C8D7E4!important}}
.stButton>button{{border-radius:8px;font-weight:800;min-height:44px}}
.hero{{padding:24px 28px;border:1px solid rgba(255,255,255,.18);border-radius:14px;background:rgba(10,32,51,.28);margin-bottom:18px}}
.eyebrow{{font-size:10px;font-weight:850;letter-spacing:1.4px;color:#BFD0E0;text-transform:uppercase}}
.hero h1{{color:white!important;font-size:34px;margin:5px 0 5px}}
.hero p{{color:#D9E5EF!important;margin:0}}
.section{{border-top:1px solid rgba(255,255,255,.18);padding-top:22px;margin-top:28px}}
.outline-card{{border:1px solid rgba(255,255,255,.28);border-radius:11px;padding:15px 17px;background:rgba(255,255,255,.045);height:100%}}
.outline-card,.outline-card *{{color:#fff!important}}
.kicker{{font-size:10px;font-weight:850;letter-spacing:1px;color:#BFD0E0!important;text-transform:uppercase}}
.big-number{{font-size:31px;font-weight:900;margin-top:4px}}
.live-chart{{border:1px solid rgba(255,255,255,.24);border-radius:12px;padding:16px 18px;background:rgba(255,255,255,.035);margin:8px 0 18px}}
.live-bar-row{{display:grid;grid-template-columns:minmax(240px,390px) 1fr 54px;gap:14px;align-items:center;margin:11px 0}}
.live-bar-label{{color:#fff!important;font-weight:750;font-size:13px}}
.live-bar-sub{{color:#BFD0E0!important;font-size:11px;font-weight:500;margin-top:2px}}
.live-bar-value{{color:#fff!important;font-weight:900;text-align:right}}
.live-bar-track{{height:18px;background:rgba(255,255,255,.12);border-radius:5px;overflow:hidden}}
.live-bar-fill{{height:100%;background:#0A66C2;border-radius:5px}}
.live-table-wrap{{border:1px solid rgba(255,255,255,.24);border-radius:12px;overflow-x:auto;background:rgba(255,255,255,.035);margin:8px 0 18px}}
.live-table{{width:100%;border-collapse:collapse}}
.live-table th,.live-table td{{color:#fff!important;padding:11px 12px;border-bottom:1px solid rgba(255,255,255,.12);text-align:left;font-size:13px}}
.live-table th{{color:#BFD0E0!important;font-size:11px;text-transform:uppercase;letter-spacing:.5px}}
.live-table tr:last-child td{{border-bottom:none}}
.control{{border:1px solid rgba(255,255,255,.32);border-left:4px solid #0A66C2;border-radius:12px;padding:18px 20px;background:rgba(10,32,51,.30);margin:14px 0 18px}}
.control,.control *{{color:#fff!important}}
.status-wait{{color:#BFD0E0!important;font-weight:900}} .status-run{{color:#7ED5AA!important;font-weight:900}} .status-end{{color:#F2C56B!important;font-weight:900}}
[data-testid="stMetric"]{{background:transparent!important;border:1px solid rgba(255,255,255,.26);border-radius:10px;padding:12px 14px}}
[data-testid="stMetric"] *{{color:#fff!important}}
@media(max-width:800px){{.live-bar-row{{grid-template-columns:1fr 70px}}.live-bar-track{{grid-column:1/-1}}}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><div class="eyebrow">MODERATORANSICHT · EXECUTIVE SEARCH</div><h1>LIVE-AUSWERTUNG</h1><p>Anonym aggregierte Einzelentscheidungen · Simulation Control & gemeinsame Reflexion</p></div>', unsafe_allow_html=True)

try:
    SUPABASE_URL=st.secrets.get("SUPABASE_URL","").rstrip("/")
    SERVICE_KEY=st.secrets.get("SUPABASE_SERVICE_KEY","")
except Exception:
    SUPABASE_URL=""; SERVICE_KEY=""
if not SUPABASE_URL or not SERVICE_KEY:
    st.error("Supabase ist noch nicht vollständig verbunden. SUPABASE_URL und SUPABASE_SERVICE_KEY müssen in den Streamlit-Secrets hinterlegt sein.")
    st.stop()

HEADERS={"apikey":SERVICE_KEY,"Authorization":"Bearer "+SERVICE_KEY,"Content-Type":"application/json"}

def api_get(path):
    req=urllib.request.Request(SUPABASE_URL+"/rest/v1/"+path,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=10) as r: return json.loads(r.read().decode("utf-8"))

def api_patch(path,payload):
    req=urllib.request.Request(SUPABASE_URL+"/rest/v1/"+path,data=json.dumps(payload).encode(),method="PATCH",headers={**HEADERS,"Prefer":"return=representation"})
    with urllib.request.urlopen(req,timeout=10) as r: return r.read()

def api_delete(path):
    req=urllib.request.Request(SUPABASE_URL+"/rest/v1/"+path,method="DELETE",headers=HEADERS)
    with urllib.request.urlopen(req,timeout=10) as r: return r.read()

def load_control():
    data=api_get("simulation_control?id=eq.1&select=*")
    return data[0] if data else None

def progress_count():
    return len(api_get("screening_progress?select=participant_id"))

def load_rows():
    return api_get("executive_search_results?select=*&completed=eq.true&order=created_at.asc")

def utc_now_iso(): return datetime.now(timezone.utc).isoformat()

def parse_dt(v):
    if not v: return None
    return datetime.fromisoformat(str(v).replace("Z","+00:00")).astimezone(timezone.utc)

# ---------------- SIMULATION CONTROL ----------------
st.markdown('<div class="section"><div class="eyebrow">SIMULATION CONTROL</div><h2 style="color:white;margin-top:6px">Gemeinsamer Start · First Screening</h2></div>', unsafe_allow_html=True)
try: control=load_control()
except Exception as e:
    st.error("Die zentrale Steuerung konnte nicht geladen werden. Wurde das SQL-Setup bereits ausgeführt?")
    st.caption(str(e)); st.stop()

status=control.get("status","waiting")
started=parse_dt(control.get("started_at"))
total=int(control.get("duration_seconds") or 240)+int(control.get("extra_seconds") or 0)
status_label={"waiting":"BEREIT · wartet auf Start","running":"LÄUFT","finished":"BEENDET"}.get(status,status.upper())
status_cls={"waiting":"status-wait","running":"status-run","finished":"status-end"}.get(status,"status-wait")
st.markdown(f'<div class="control"><div class="kicker">FIRST SCREENING</div><div class="{status_cls}" style="font-size:20px;margin-top:5px">{status_label}</div><p style="margin-bottom:0">Gemeinsame Dauer: {total//60}:{total%60:02d} Minuten · Teilnehmergeräte bleiben stumm.</p></div>', unsafe_allow_html=True)

b1,b2,b3=st.columns([1.2,1,1])
with b1:
    if st.button("▶ FIRST SCREENING STARTEN",type="primary",disabled=status=="running",use_container_width=True):
        api_delete("screening_progress?participant_id=not.is.null")
        api_patch("simulation_control?id=eq.1",{"status":"running","started_at":utc_now_iso(),"duration_seconds":240,"extra_seconds":0,"updated_at":utc_now_iso()})
        st.rerun()
with b2:
    if st.button("+ 1 MINUTE",disabled=status!="running",use_container_width=True):
        api_patch("simulation_control?id=eq.1",{"extra_seconds":int(control.get("extra_seconds") or 0)+60,"updated_at":utc_now_iso()})
        st.rerun()
with b3:
    if st.button("↺ SCREENING ZURÜCKSETZEN",use_container_width=True):
        api_patch("simulation_control?id=eq.1",{"status":"waiting","started_at":None,"duration_seconds":240,"extra_seconds":0,"updated_at":utc_now_iso()})
        api_delete("screening_progress?participant_id=not.is.null")
        st.rerun()

if status=="running" and started:
    start_ms=int(started.timestamp()*1000)
    # Der Ton läuft ausschließlich in diesem Moderator-Browser. WebAudio erzeugt die kurzen Signale lokal.
    components.html(f"""
    <style>
    body{{margin:0;background:transparent;font-family:Arial;color:white}}
    #box{{border:1px solid rgba(255,255,255,.28);border-radius:12px;padding:14px 18px;background:rgba(255,255,255,.04);text-align:center}}
    #time{{font-size:54px;font-weight:900;letter-spacing:2px}} #msg{{font-size:13px;color:#cfe0ed;font-weight:700;margin-top:4px}}
    #arm{{margin-top:10px;border:1px solid rgba(255,255,255,.35);background:transparent;color:white;border-radius:7px;padding:7px 11px;font-weight:800;cursor:pointer}}
    </style>
    <div id="box"><div id="time">04:00</div><div id="msg">30-Sekunden-Hinweis · Tick 10–1 · Endsignal nur hier</div><button id="arm">🔊 TON AKTIVIEREN / TESTEN</button></div>
    <script>
    const start={start_ms}, total={total}; let ctx=null, armed=false, last=null;
    function tone(freq,dur,vol=0.035){{
      try{{if(!ctx)ctx=new (window.AudioContext||window.webkitAudioContext)(); if(ctx.state==='suspended')ctx.resume();
      const o=ctx.createOscillator(),g=ctx.createGain();o.frequency.value=freq;o.type='sine';g.gain.value=vol;o.connect(g);g.connect(ctx.destination);o.start();g.gain.exponentialRampToValueAtTime(0.0001,ctx.currentTime+dur);o.stop(ctx.currentTime+dur);}}catch(e){{}}
    }}
    document.getElementById('arm').onclick=()=>{{armed=true;tone(720,.12,.025);document.getElementById('arm').innerText='✓ TON AKTIV';}};
    function tick(){{
      const s=Math.max(0,total-Math.floor((Date.now()-start)/1000));
      const el=document.getElementById('time'); el.innerText=String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');
      if(s<=30)el.style.color='#F2C56B'; if(s<=10){{el.style.fontSize='68px';document.getElementById('msg').innerText='LETZTE '+s+' SEKUNDEN';}}
      if(s!==last && armed){{if(s===30)tone(520,.32,.035); if(s<=10&&s>=1)tone(880,.07,.025); if(s===0){{tone(330,.22,.045);setTimeout(()=>tone(220,.45,.045),220);}}}}
      last=s; if(s>0)setTimeout(tick,150); else document.getElementById('msg').innerText='ZEIT ABGELAUFEN · aktuelle Auswahl bitte abschließen';
    }} tick();
    </script>""",height=145)

    @st.fragment(run_every=2)
    def live_progress():
        try: n=progress_count()
        except Exception: n=0
        st.markdown(f'<div class="outline-card"><div class="kicker">FORTSCHRITT</div><div class="big-number">{n}</div><div>Shortlists bereits bestätigt</div></div>',unsafe_allow_html=True)
    live_progress()
elif status=="waiting":
    st.caption("Die Teilnehmenden können bereits bis zum Wartebildschirm gehen. Erst der Start-Button gibt das Screening frei.")

# ---------------- LIVE DATA ----------------
st.markdown('<div class="section"><div class="eyebrow">LIVE RESULTS</div><h2 style="color:white;margin-top:6px">Gemeinsame Auswertung</h2></div>', unsafe_allow_html=True)
if st.button("↻ LIVE-DATEN AKTUALISIEREN",use_container_width=False): st.rerun()
try: rows=load_rows()
except Exception as e:
    st.error("Die Live-Daten konnten nicht geladen werden."); st.caption(str(e)); st.stop()

st.markdown(f'<div class="outline-card" style="max-width:300px"><div class="kicker">ABGESCHLOSSENE DURCHLÄUFE</div><div class="big-number">{len(rows)}</div></div>',unsafe_allow_html=True)
if not rows:
    st.info("Noch keine vollständig abgeschlossenen Durchläufe vorhanden.")
    st.stop()

CANDIDATE_ROLES={
"A":"Leitung Marketing · Digitalbank","B":"Senior Markenmarketing · Telekommunikation","C":"Leitung Marketing & Kommunikation · Versicherung","D":"Leitung Marke, Marketing & Kommunikation · Automobile","E":"Markenstrategie & Marketing · selbstständig","F":"Leitung Marke & Inhouse-Kreation · Versicherung","G":"Globale Markenführung · Sportartikel","H":"Leitung Marketing · Pharma / Consumer Health","I":"KI-Transformation & Marken-/Kommunikationssteuerung · Telekommunikation","J":"Leitung B2B-Marke & Marketingkommunikation · Telekommunikation"}

def short_candidate(v):
    if not v:return None
    return str(v).replace("KANDIDAT ","").replace("KANDIDATIN ","").replace("CANDIDATE ","").strip()

def label_html(c):
    return f'<div class="live-bar-label">CANDIDATE {c}<div class="live-bar-sub">{CANDIDATE_ROLES.get(c,"")}</div></div>'

def show_counter(title,counter):
    st.markdown(f'<h3 style="color:#FFFFFF !important;margin:8px 0 12px">{title}</h3>', unsafe_allow_html=True)
    if not counter: st.caption("Noch keine Daten vorhanden."); return
    items=counter.most_common(); mx=max(v for _,v in items) or 1
    bars=[]
    for c,v in items:
        w=max(4,round(v/mx*100))
        bars.append(f'<div class="live-bar-row">{label_html(c)}<div class="live-bar-track"><div class="live-bar-fill" style="width:{w}%"></div></div><div class="live-bar-value">{v}</div></div>')
    st.markdown('<div class="live-chart">'+''.join(bars)+'</div>',unsafe_allow_html=True)

first_frequency=Counter(); first_points=Counter(); criteria=Counter(); moved=unchanged=0; finals=Counter(); blind_yes=Counter(); blind_total=Counter(); conf_first=[]; conf_final=[]
net=Counter(); up=Counter(); down=Counter()
for row in rows:
    first=[short_candidate(row.get(f"first_rank_{i}")) for i in (1,2,3)]
    second=[short_candidate(row.get(f"second_rank_{i}")) for i in (1,2,3)]
    for rank,c in enumerate(first,1):
        if c: first_frequency[c]+=1; first_points[c]+={1:3,2:2,3:1}[rank]
    obj=row.get("first_criteria") or {}
    if isinstance(obj,str):
        try: obj=json.loads(obj)
        except: obj={}
    for item in (obj.get("selected",[]) if isinstance(obj,dict) else []):
        if item: criteria[str(item)]+=1
    if all(first) and all(second):
        if first==second: unchanged+=1
        else: moved+=1
        for c in set(first)&set(second):
            change=(first.index(c)+1)-(second.index(c)+1); net[c]+=change
            if change>0: up[c]+=change
            elif change<0: down[c]+=abs(change)
    fc=short_candidate(row.get("final_candidate"));
    if fc: finals[fc]+=1
    b=row.get("blind_spot") or {}
    if isinstance(b,str):
        try:b=json.loads(b)
        except:b={}
    if isinstance(b,dict):
        for raw,ans in b.items():
            c=short_candidate(raw)
            if not c:continue
            blind_total[c]+=1
            yes=ans is True or str(ans).strip().lower() in {"ja","yes","true","1","würde ich näher prüfen"}
            if yes:blind_yes[c]+=1
    if isinstance(row.get("confidence_first"),(int,float)):conf_first.append(row["confidence_first"])
    if isinstance(row.get("confidence_final"),(int,float)):conf_final.append(row["confidence_final"])

st.markdown('<div class="section"><div class="eyebrow">01 · FIRST SCREENING</div></div>',unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1: show_counter("Wie oft war ein Profil in der ersten Top 3?",first_frequency)
with c2: show_counter("Ranggewichtete Shortlist-Punkte",first_points)

st.markdown('<div class="section"><div class="eyebrow">02 · AUSWAHLKRITERIEN</div></div>',unsafe_allow_html=True)
show_counter("Welche Kriterien haben die Auswahl geprägt?",criteria)

st.markdown('<div class="section"><div class="eyebrow">03 · SECOND LOOK</div><h2 style="color:white;margin-top:6px">Was hat sich verändert?</h2></div>',unsafe_allow_html=True)
total_second=moved+unchanged
if total_second:
    c1,c2=st.columns(2)
    with c1: st.markdown(f'<div class="outline-card"><div class="kicker">RANGFOLGE VERÄNDERT</div><div class="big-number">{moved} von {total_second}</div><div>{round(moved/total_second*100)} % haben ihre Top 3 neu gereiht.</div></div>',unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="outline-card"><div class="kicker">RANGFOLGE UNVERÄNDERT</div><div class="big-number">{unchanged} von {total_second}</div><div>{round(unchanged/total_second*100)} % blieben bei ihrer Reihenfolge.</div></div>',unsafe_allow_html=True)
    items=sorted([(c,v) for c,v in net.items() if v],key=lambda x:x[1],reverse=True)
    if items:
        st.markdown('<h3 style="color:#FFFFFF !important;margin:8px 0 12px">Welche Profile bewegten sich nach dem Second Look?</h3>', unsafe_allow_html=True)
        trs=[]
        for c,v in items:
            tendency="häufiger höher gereiht" if v>0 else "häufiger niedriger gereiht"
            trs.append(f'<tr><td><strong>CANDIDATE {c}</strong><br><span style="color:#BFD0E0">{CANDIDATE_ROLES.get(c,"")}</span></td><td>{up.get(c,0)}</td><td>{down.get(c,0)}</td><td>{tendency}</td></tr>')
        st.markdown('<div class="live-table-wrap"><table class="live-table"><thead><tr><th>Profil</th><th>Rangplätze nach oben</th><th>Rangplätze nach unten</th><th>Was ist sichtbar?</th></tr></thead><tbody>'+''.join(trs)+'</tbody></table></div>',unsafe_allow_html=True)
        st.caption("Die Rangplätze werden über alle Entscheidungen summiert. Sie beschreiben Bewegung – nicht richtig oder falsch.")

st.markdown('<div class="section"><div class="eyebrow">04 · FINALE EMPFEHLUNG</div></div>',unsafe_allow_html=True)
show_counter("Wen haben die Teilnehmenden final empfohlen?",finals)

st.markdown('<div class="section"><div class="eyebrow">05 · BLIND-SPOT CHECK</div><h2 style="color:white;margin-top:6px">Welche ausgeschiedenen Profile hätten wir mit mehr Information näher geprüft?</h2></div>',unsafe_allow_html=True)
if blind_total:
    trs=[]
    for c,total in sorted(blind_total.items()):
        yes=blind_yes.get(c,0); share=round(yes/total*100) if total else 0
        trs.append(f'<tr><td><strong>CANDIDATE {c}</strong><br><span style="color:#BFD0E0">{CANDIDATE_ROLES.get(c,"")}</span></td><td>{yes} von {total}</td><td><strong>{share} %</strong></td></tr>')
    st.markdown('<div class="live-table-wrap"><table class="live-table"><thead><tr><th>Profil</th><th>„Hätte ich näher geprüft“</th><th>Anteil</th></tr></thead><tbody>'+''.join(trs)+'</tbody></table></div>',unsafe_allow_html=True)

st.markdown('<div class="section"><div class="eyebrow">06 · SICHERHEIT</div><h2 style="color:white;margin-top:6px">Wie sicher fühlten sich die Entscheidungen an?</h2></div>',unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
    v=f"{sum(conf_first)/len(conf_first):.0f}%" if conf_first else "—"
    st.markdown(f'<div class="outline-card"><div class="kicker">Ø SICHERHEIT · FIRST SCREENING</div><div class="big-number">{v}</div></div>',unsafe_allow_html=True)
with c2:
    v=f"{sum(conf_final)/len(conf_final):.0f}%" if conf_final else "—"
    st.markdown(f'<div class="outline-card"><div class="kicker">Ø SICHERHEIT · FINALE ENTSCHEIDUNG</div><div class="big-number">{v}</div></div>',unsafe_allow_html=True)

st.markdown('<div class="section"></div>',unsafe_allow_html=True)
st.caption("Moderationsprinzip: Ergebnisse beschreiben, nicht als richtig oder falsch bewerten. Fokus: Information → Interpretation → Anforderungsbezug → Eignungsprognose.")
