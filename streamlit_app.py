import streamlit as st
import streamlit.components.v1 as components
from collections import Counter

st.set_page_config(page_title="Executive Search Simulation", page_icon="◼", layout="wide")

NAVY="#17324D"; NAVY2="#203F5D"; BLUE="#0A66C2"; WHITE="#FFFFFF"; SOFT="#EAF0F5"
TEXT="#142536"; MUTED="#667788"; GREEN="#2F8F67"; AMBER="#D79B32"; RED="#C94E55"

st.markdown(f"""
<style>
.stApp {{
background:
radial-gradient(circle at 78% 8%, rgba(35,79,112,.55) 0%, rgba(35,79,112,0) 32%),
linear-gradient(145deg,#0E2033 0%,#17324D 48%,#1D405D 100%);
background-attachment:fixed;
}}
.block-container {{max-width:1180px;padding-top:1.2rem;padding-bottom:3rem;}}
h1,h2,h3,p,label,div {{font-family:Arial,sans-serif;}}
[data-testid="stMarkdownContainer"] > h1,
[data-testid="stMarkdownContainer"] > h2,
[data-testid="stMarkdownContainer"] > h3 {{color:{WHITE};}}
[data-testid="stWidgetLabel"] p {{color:{SOFT} !important;font-weight:650;}}
.main-card h1,.main-card h2,.main-card h3,.main-card p,
.internal h1,.internal h2,.internal h3,.internal p,
.metricbox h1,.metricbox h2,.metricbox h3,.metricbox p,
.recruiter-shell h1,.recruiter-shell h2,.recruiter-shell h3,.recruiter-shell p {{color:{TEXT};}}

[data-testid="stHeader"] {{background:transparent;}}
.main-card {{background:white;border-radius:14px;padding:26px 28px;color:{TEXT};box-shadow:0 8px 28px rgba(0,0,0,.10);}}
.hero {{padding:28px 30px;border:1px solid rgba(255,255,255,.14);border-radius:14px;background:{NAVY2};color:white;margin-bottom:18px;}}
.eyebrow {{font-size:11px;font-weight:800;letter-spacing:1.6px;color:#BFD0E0;text-transform:uppercase;}}
.hero h1 {{font-size:34px;line-height:1.05;margin:.35rem 0 .45rem;color:white;}}
.hero p {{color:#D9E5EF;font-size:15px;margin:0;}}
.progress-wrap {{margin:0 0 18px;}}
.progress-line {{height:5px;background:#34536F;border-radius:99px;overflow:hidden;}}
.progress-fill {{height:5px;background:{BLUE};}}
.progress-label {{display:flex;justify-content:space-between;color:#C7D5E2;font-size:10px;font-weight:700;margin-top:7px;letter-spacing:.5px;}}
.tag {{display:inline-block;background:#EAF3FC;color:{BLUE};font-size:10px;font-weight:800;letter-spacing:.7px;padding:5px 8px;border-radius:5px;margin-right:5px;}}
.status {{display:inline-block;font-size:10px;font-weight:800;padding:5px 8px;border-radius:5px;background:#E9F5EF;color:{GREEN};}}
.small {{font-size:12px;color:{MUTED};}}
.recruiter-shell {{background:#F3F6F8;border-radius:14px;padding:18px;color:{TEXT};}}
.recruiter-top {{background:{BLUE};color:white;padding:16px 20px;border-radius:10px;margin-bottom:15px;display:flex;justify-content:space-between;align-items:center;}}
.recruiter-title {{font-size:20px;font-weight:800;}}
.candidate {{background:white;border:1px solid #DDE4EA;border-radius:10px;padding:16px 18px;margin:8px 0;}}
.candidate h4 {{margin:0 0 5px;color:{TEXT};font-size:16px;}}
.candidate p {{margin:2px 0;color:#5D6C78;font-size:13px;}}
.internal {{background:white;border-radius:14px;padding:22px 24px;color:{TEXT};margin:10px 0;}}
.internal-head {{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #E3E8EC;padding-bottom:10px;margin-bottom:14px;}}
.cid {{font-size:11px;font-weight:800;letter-spacing:1px;color:{BLUE};}}
.newinfo {{background:#FFF7E8;border-left:4px solid {AMBER};padding:13px 15px;border-radius:6px;margin:12px 0;}}
.lock {{background:#EAF5EF;color:{GREEN};font-weight:800;padding:10px 12px;border-radius:7px;}}
.reveal {{background:#FFF4F1;border-left:4px solid {RED};padding:15px;border-radius:7px;}}
.metricbox {{background:white;border-radius:12px;padding:18px;color:{TEXT};height:100%;}}
.big {{font-size:31px;font-weight:850;color:{TEXT};}}
.stButton>button {{border-radius:8px;font-weight:800;min-height:44px;}}
div[data-testid="stMetric"] {{background:white;padding:12px;border-radius:10px;}}

/* premium controls */
div[data-baseweb="select"] > div {
    background:#FFFFFF !important;
    border:1px solid #CBD7E1 !important;
    color:#142536 !important;
}
div[data-baseweb="select"] span {color:#142536 !important;}
div[role="listbox"] {background:#FFFFFF !important;}
div[role="option"] {color:#142536 !important;}
div[data-testid="stMultiSelect"] span[data-baseweb="tag"] {
    background:#E7F4ED !important;
    color:#247653 !important;
}
div[data-testid="stMultiSelect"] span[data-baseweb="tag"] * {color:#247653 !important;}
div[data-testid="stCheckbox"] label p {color:#EAF0F5 !important;}
.recruiter-shell div[data-testid="stCheckbox"] label p {color:#142536 !important;}
.final-choice {
    background:#F3FAF6;border:1px solid #86C5A6;border-left:5px solid #2F8F67;
    border-radius:10px;padding:14px 16px;margin:8px 0;
}
.reflection-box {
    background:#F5F8FA;border-left:4px solid #6E879B;padding:15px;border-radius:7px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Demo data ----------
CANDIDATES = [
{"id":"CANDIDATE 01","role":"Regional Director","meta":"Finanzdienstleistungen · 16 J. Erfahrung · 9 J. Führung","career":"Regional Director → Sales Director → Key Account Lead","facts":"DACH-Verantwortung · 120 Mitarbeitende · internationale Matrix","new":"Im Gespräch beschreibt die Person den Aufbau einer neuen Einheit von 12 auf 85 Mitarbeitende und konkrete Skalierungsentscheidungen.","reveal":"—"},
{"id":"CANDIDATE 02","role":"Country Manager","meta":"Technologie · 14 J. Erfahrung · 7 J. Führung","career":"Country Manager → Head of Growth → Business Development","facts":"Österreich · Markteintritt · P&L-Verantwortung","new":"Die Person kann die Markteinführung belegen, hatte dabei aber deutlich weniger direkte Personalverantwortung als das Profil vermuten ließ.","reveal":"—"},
{"id":"CANDIDATE 03","role":"Head of Operations","meta":"Industrie · 18 J. Erfahrung · 11 J. Führung","career":"Head of Operations → Plant Manager → Program Lead","facts":"Transformation · 180 Mitarbeitende · Prozessaufbau","new":"Im Gespräch wird sichtbar, dass die Person bereits zwei standortübergreifende Reorganisationen mit hoher Stakeholder-Komplexität geführt hat.","reveal":"—"},
{"id":"CANDIDATE 04","role":"Commercial Director","meta":"FMCG · 15 J. Erfahrung · 8 J. Führung","career":"Commercial Director → Sales Lead → Area Manager","facts":"CEE · Wachstum · Vertrieb & Marketing","new":"Die Expansionsprojekte waren erfolgreich; die Person beschreibt jedoch wenig Erfahrung mit Aufbauorganisation und internen Strukturen.","reveal":"—"},
{"id":"CANDIDATE 05","role":"Managing Director","meta":"Professional Services · 20 J. Erfahrung · 12 J. Führung","career":"Managing Director → Partner → Practice Lead","facts":"P&L · Österreich · Kundenentwicklung","new":"Im Gespräch zeigt sich breite Ergebnisverantwortung, aber der bisherige Kontext war stark partnergeführt und weniger hierarchisch.","reveal":"—"},
{"id":"CANDIDATE 06","role":"Business Unit Lead","meta":"Healthcare · 13 J. Erfahrung · 6 J. Führung","career":"Business Unit Lead → Strategy Manager → Consultant","facts":"Wachstum · 45 Mitarbeitende · Strategie","new":"Die Person hat ein neues Geschäftsfeld von der Planung bis zum operativen Betrieb aufgebaut.","reveal":"Das Profil wirkte zunächst weniger senior. Tatsächlich verantwortete die Person den vollständigen Aufbau eines neuen Geschäftsfelds inklusive Budget, Recruiting und Go-to-Market."},
{"id":"CANDIDATE 07","role":"Operations Director","meta":"Logistik · 17 J. Erfahrung · 10 J. Führung","career":"Operations Director → Site Lead → Project Manager","facts":"Standorte · Effizienz · 220 Mitarbeitende","new":"Die Person hat einen neuen Standort eröffnet und anschließend drei Standorte integriert.","reveal":"Im Kurzprofil war der Standortaufbau kaum sichtbar. Im Projektkontext führte die Person die Eröffnung inklusive Teamaufbau, Behörden und Betriebsstart."},
{"id":"CANDIDATE 08","role":"VP Customer Experience","meta":"Telekommunikation · 15 J. Erfahrung · 7 J. Führung","career":"VP CX → Director Service → Transformation Lead","facts":"Transformation · digital · 95 Mitarbeitende","new":"Die Person verbindet Transformation mit direkter Ergebnis- und Führungsverantwortung.","reveal":"—"},
{"id":"CANDIDATE 09","role":"Head of Market Development","meta":"Energie · 12 J. Erfahrung · 5 J. Führung","career":"Head of Market Development → Expansion Lead → Analyst","facts":"Neue Märkte · Regulierung · Partnerschaften","new":"Die Person hat Markteintritte vorbereitet, aber bisher keine Gesamtverantwortung für eine größere Organisation getragen.","reveal":"Die Person steuerte einen Markteintritt faktisch end-to-end, obwohl der Jobtitel nur 'Head of Market Development' lautete."},
{"id":"CANDIDATE 10","role":"General Manager","meta":"Retail · 19 J. Erfahrung · 13 J. Führung","career":"General Manager → Regional Manager → Store Operations","facts":"P&L · Expansion · 300 Mitarbeitende","new":"Im Gespräch zeigt sich sehr konkrete Skalierungserfahrung, allerdings ausschließlich in stark standardisierten Strukturen.","reveal":"—"},
]
BYID={c["id"]:c for c in CANDIDATES}
CRITERIA=["Führungserfahrung","Aufbau / Expansion","Branchen- / Markterfahrung","Internationale Erfahrung","Funktions- / Rollenerfahrung","Karriereverlauf","Arbeitgeberhintergrund","Stabilität der Stationen"]

# ---------- state ----------
defaults=dict(phase=0,max_phase=0,shortlist=[],criteria=[],confidence1=60,assessments={},final_candidate=None,final_reasons=[],final_confidence=70,reveal={},counter_change="Nein",counter_candidate=None)
for k,v in defaults.items():
    if k not in st.session_state: st.session_state[k]=v

PHASES=["Suchauftrag","First Screening","Theorie & Praxis","Second Look","Finale Entscheidung","Blind-Spot Check","Live-Auswertung","Take-away"]

def progress():
    p=min(st.session_state.phase,7)
    st.markdown(f"""<div class="progress-wrap"><div class="progress-line"><div class="progress-fill" style="width:{(p+1)/8*100}%"></div></div>
    <div class="progress-label"><span>{p+1:02d} / 08</span><span>{PHASES[p].upper()}</span></div></div>""",unsafe_allow_html=True)

def hero(kicker,title,sub):
    st.markdown(f"""<div class="hero"><div class="eyebrow">{kicker}</div><h1>{title}</h1><p>{sub}</p></div>""",unsafe_allow_html=True)

def goto(p):
    st.session_state.phase=p
    st.session_state.max_phase=max(st.session_state.max_phase,p)
    st.rerun()

def nav(back=None, forward=None, forward_label="WEITER →"):
    c1,c2=st.columns([1,1])
    with c1:
        if back is not None and st.button("← ZURÜCK",use_container_width=True,key=f"back_{st.session_state.phase}"): goto(back)
    with c2:
        if forward is not None and forward <= st.session_state.max_phase:
            if st.button(forward_label,use_container_width=True,key=f"fwd_{st.session_state.phase}"): goto(forward)

progress()

# ---------- 0 BRIEFING ----------
if st.session_state.phase==0:
    hero("CONFIDENTIAL EXECUTIVE SEARCH","DER SUCHAUFTRAG","Demo-Case · finale Position und Anforderungen werden nach Marcs Praxisfall ersetzt.")
    st.markdown("""<div class="main-card">
    <span class="tag">DEMO MANDATE</span><span class="status">ACTIVE</span>
    <h2>Managing Director Austria</h2>
    <p><b>Kontext:</b> Ein Unternehmen baut seine Präsenz in Österreich aus und sucht eine Führungspersönlichkeit für Aufbau, Wachstum und Steuerung.</p>
    <hr>
    <h3>Für die Demo arbeiten wir mit drei Kernanforderungen</h3>
    <p>✓ Führung größerer Teams &nbsp;&nbsp; ✓ Aufbau / Expansion &nbsp;&nbsp; ✓ Steuerung komplexer Strukturen</p>
    <p class="small">Hinweis: Diese Anforderungen sind Platzhalter. Sie werden mit dem realen Suchauftrag aus Marcs Praxis ersetzt.</p>
    </div>""",unsafe_allow_html=True)
    if st.button("FIRST SCREENING STARTEN →",use_container_width=True): goto(1)

# ---------- 1 SCREENING ----------
elif st.session_state.phase==1:
    st.markdown('<div class="recruiter-shell">',unsafe_allow_html=True)
    st.markdown("""<div class="recruiter-top"><div><div style="font-size:11px;font-weight:800;opacity:.8">SEARCH WORKSPACE</div>
    <div class="recruiter-title">Recruiter Search · Managing Director Austria</div></div><div><b>10 PROFILE · SHORTLIST 3</b></div></div>""",unsafe_allow_html=True)
    if not st.session_state.shortlist:
        components.html("""<div id="t" style="font-family:Arial;font-weight:800;font-size:20px;color:#0A66C2">01:30</div>
        <script>let s=90;let e=document.getElementById('t');let x=setInterval(()=>{s--;let m=Math.floor(s/60),r=s%60;e.innerText=String(m).padStart(2,'0')+':'+String(r).padStart(2,'0');if(s<=20)e.style.color='#C94E55';if(s<=0){clearInterval(x);e.innerText='ZEIT ABGELAUFEN · Bitte Auswahl bestätigen';}},1000);</script>""",height=42)
    draft=[]
    cols=st.columns(2)
    for i,c in enumerate(CANDIDATES):
        with cols[i%2]:
            st.markdown(f"""<div class="candidate"><div class="cid">{c['id']}</div><h4>{c['role']}</h4><p><b>{c['meta']}</b></p><p>{c['career']}</p><p>{c['facts']}</p></div>""",unsafe_allow_html=True)
            default=c["id"] in st.session_state.shortlist
            if st.checkbox("SHORTLIST",value=default,key=f"sl_{c['id']}"): draft.append(c["id"])
    st.markdown('</div>',unsafe_allow_html=True)
    st.info(f"SHORTLIST · {len(draft)} / 3 ausgewählt")
    selected_criteria=st.multiselect("Welche Kriterien haben eure Auswahl besonders beeinflusst?",CRITERIA,default=st.session_state.criteria)
    confidence=st.slider("Wie sicher seid ihr euch bei eurer Shortlist?",0,100,st.session_state.confidence1,5)
    if st.button("SHORTLIST BESTÄTIGEN",disabled=len(draft)!=3,use_container_width=True):
        st.session_state.shortlist=draft; st.session_state.criteria=selected_criteria; st.session_state.confidence1=confidence; goto(2)
    if st.session_state.shortlist: nav(0,2,"ZUR THEORIE & PRAXIS →")

# ---------- 2 THEORY HANDOVER ----------
elif st.session_state.phase==2:
    hero("SHORTLIST STEHT","10 Profile → 3 auf der Shortlist","Jetzt zurück zur Präsentation: Theorie-Check und Praxis-Check mit Marc.")
    st.markdown("""<div class="main-card">
    <span class="status">SHORTLIST GESPEICHERT</span>
    <h2 style="margin-top:14px">Jetzt zurück zur gemeinsamen Präsentation.</h2>
    <p>Eure Auswahl bleibt gespeichert. Nach Theorie- und Praxis-Check geht es hier mit dem <b>Second Look</b> weiter.</p>
    <div class="lock">Ihr müsst in der App jetzt nichts weiter tun.</div></div>""",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← FIRST SCREENING ANSEHEN",use_container_width=True): goto(1)
    with c2:
        if st.button("SECOND LOOK ÖFFNEN →",use_container_width=True): goto(3)

# ---------- 3 SECOND LOOK ----------
elif st.session_state.phase==3:
    hero("INTERNES ASSESSMENT","SECOND LOOK","Nur eure ursprüngliche Top 3 erhält zusätzliche Information.")
    assessments={}
    for cid in st.session_state.shortlist:
        c=BYID[cid]
        st.markdown(f"""<div class="internal"><div class="internal-head"><div><div class="cid">{cid}</div><b>{c['role']}</b></div><span class="status">SHORTLISTED</span></div>
        <div class="small">WAS IHR BEREITS WUSSTET</div><p>{c['meta']}<br>{c['facts']}</p>
        <div class="newinfo"><b>NEUE INFORMATION AUS DEM GESPRÄCH</b><br>{c['new']}</div></div>""",unsafe_allow_html=True)
        options=["Positiver","Unverändert","Negativer"]
        old=st.session_state.assessments.get(cid,"Unverändert")
        if old.startswith("↑"): old="Positiver"
        elif old.startswith("↓"): old="Negativer"
        elif old.startswith("→"): old="Unverändert"
        assessments[cid]=st.selectbox("Wie verändert diese Information eure Einschätzung?",options,index=options.index(old),key=f"ass_{cid}")
    st.session_state.assessments=assessments
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(2)
    with c2:
        if st.button("ZUR FINALEN ENTSCHEIDUNG →",use_container_width=True): goto(4)

# ---------- 4 FINAL ----------
elif st.session_state.phase==4:
    hero("FINALE ENTSCHEIDUNG","Eine Person. Eine Empfehlung.","Wählt genau eine Person aus eurer ursprünglichen Top 3.")
    cols=st.columns(3)
    for i,cid in enumerate(st.session_state.shortlist):
        c=BYID[cid]
        with cols[i]:
            st.markdown(f"""<div class="metricbox"><div class="cid">{cid}</div><h3>{c['role']}</h3><p>{c['meta']}</p><p><b>Second Look:</b> {st.session_state.assessments.get(cid,'→ unverändert')}</p></div>""",unsafe_allow_html=True)
    idx=0
    if st.session_state.final_candidate in st.session_state.shortlist: idx=st.session_state.shortlist.index(st.session_state.final_candidate)
    final=st.selectbox("Wen empfehlt ihr final?",st.session_state.shortlist,index=idx)
    fc=BYID[final]
    st.markdown(f"""<div class="final-choice"><div class="cid">FINALE EMPFEHLUNG</div><b>{final} · {fc['role']}</b></div>""",unsafe_allow_html=True)
    reasons=st.multiselect("Welche Kriterien tragen eure finale Empfehlung?",CRITERIA,default=st.session_state.final_reasons)
    conf=st.slider("Wie sicher seid ihr euch jetzt?",0,100,st.session_state.final_confidence,5)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(3)
    with c2:
        if st.button("ENTSCHEIDUNG BESTÄTIGEN",use_container_width=True):
            st.session_state.final_candidate=final; st.session_state.final_reasons=reasons; st.session_state.final_confidence=conf; goto(5)

# ---------- 5 REVEAL ----------
elif st.session_state.phase==5:
    hero("ENTSCHEIDUNG STEHT","BLIND-SPOT CHECK","Der simulierte Search-Prozess ist abgeschlossen. Jetzt beginnt die Reflexion.")
    excluded=[c["id"] for c in CANDIDATES if c["id"] not in st.session_state.shortlist]
    reveal_ids=[x for x in ["CANDIDATE 06","CANDIDATE 07","CANDIDATE 09"] if x in excluded][:2]
    if len(reveal_ids)<2: reveal_ids=excluded[:2]
    for cid in reveal_ids:
        c=BYID[cid]
        st.markdown(f"""<div class="internal"><div class="internal-head"><div><div class="cid">{cid}</div><b>{c['role']}</b></div><span style="color:#667788;font-weight:800">IM FIRST SCREENING AUSGESCHIEDEN</span></div>
        <p>{c['meta']}<br>{c['facts']}</p><div class="reflection-box"><b>WAS IM ERSTEN SCREENING NICHT SICHTBAR WAR</b><br>{c['reveal'] if c['reveal']!='—' else c['new']}</div></div>""",unsafe_allow_html=True)
        st.session_state.reveal[cid]=st.checkbox("Mit dieser Information hätten wir diese Person im First Screening näher geprüft.",value=st.session_state.reveal.get(cid,False),key=f"rev_{cid}")
    st.markdown("""<div style="color:#FFFFFF;font-size:25px;font-weight:800;margin-top:22px">REFLEXIONSFRAGE</div>""",unsafe_allow_html=True)
    st.markdown("""<div style="color:#DDE8F1;font-size:13px;margin-bottom:8px">Keine zweite reale Auswahlrunde – nur Reflexion.</div>""",unsafe_allow_html=True)
    change=st.radio("Würdet ihr eure finale Entscheidung ändern, wenn ihr heute alle Informationen gekannt hättet?",["Nein","Ja"],index=0 if st.session_state.counter_change=="Nein" else 1,horizontal=True)
    st.session_state.counter_change=change
    if change=="Ja":
        st.session_state.counter_candidate=st.selectbox("Welche Person würdet ihr dann wählen?",[c["id"] for c in CANDIDATES])
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(4)
    with c2:
        if st.button("REFLEXION ABSCHLIESSEN →",use_container_width=True): goto(6)

# ---------- 6 DASHBOARD ----------
elif st.session_state.phase==6:
    hero("LIVE-AUSWERTUNG","Wie wurde entschieden?","Demo-Ansicht. Später werden hier die Ergebnisse aller Search Teams zentral zusammengeführt.")
    st.warning("DEMO: Aktuell zeigt diese Seite die Struktur der geplanten Auswertung. Die teamübergreifende Live-Speicherung wird nach dem finalen Fall ergänzt.")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Top 3",", ".join(x.split()[-1] for x in st.session_state.shortlist))
    c2.metric("Finale Empfehlung",st.session_state.final_candidate or "—")
    c3.metric("Sicherheit vorher",f"{st.session_state.confidence1}%")
    c4.metric("Sicherheit final",f"{st.session_state.final_confidence}%")
    st.markdown("### Welche Kriterien kamen bei euch zum Zug?")
    counts=Counter(st.session_state.criteria + st.session_state.final_reasons)
    if counts:
        import pandas as pd
        df=pd.DataFrame({"Kriterium":list(counts.keys()),"Nennungen":list(counts.values())}).set_index("Kriterium")
        st.bar_chart(df,horizontal=True)
    else: st.info("Für dieses Demo-Team wurden noch keine Kriterien gewählt.")
    st.markdown("### Geplante gemeinsame Auswertung")
    st.markdown("""<div class="main-card"><b>Über alle Search Teams:</b><br><br>
    ① Welche Kandidat:innen waren am häufigsten in der Top 3?<br>
    ② Welche Auswahlkriterien wurden am häufigsten genannt?<br>
    ③ Was wurde im Second Look positiver / unverändert / negativer?<br>
    ④ Welche Personen wurden final empfohlen?<br>
    ⑤ Wie oft führte der Blind-Spot Check zu „hätte ich näher geprüft“?<br>
    ⑥ Wie viele Teams würden im Gedankenexperiment ihre Entscheidung ändern?</div>""",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(5)
    with c2:
        if st.button("ZUM TAKE-AWAY →",use_container_width=True): goto(7)

# ---------- 7 TAKEAWAY ----------
elif st.session_state.phase==7:
    hero("SEARCH COMPLETED","Biografische Information ≠ Eignung.","Die App endet hier – die gemeinsame Einordnung erfolgt in der Präsentation.")
    st.markdown("""<div class="main-card"><div class="big">Information → Interpretation → Anforderungsbezug → Eignungsprognose</div>
    <br><p>Biografische Informationen können relevant sein. Entscheidend ist, <b>welche konkrete Anforderung</b> sie betreffen und wie belastbar der daraus gezogene Eignungsschluss ist.</p>
    <p class="small">Die theoretische Einordnung und die Quellen bleiben bewusst in der PowerPoint – nicht in der Auswahl-App.</p></div>""",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← LIVE-AUSWERTUNG",use_container_width=True): goto(6)
    with c2:
        if st.button("DEMO NEU STARTEN",use_container_width=True):
            for k,v in defaults.items(): st.session_state[k]=v
            for k in list(st.session_state.keys()):
                if k.startswith(("sl_","ass_","rev_")): del st.session_state[k]
            st.rerun()
