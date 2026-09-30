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
div[data-baseweb="select"] > div {{
    background:#FFFFFF !important;
    border:1px solid #CBD7E1 !important;
    color:#142536 !important;
}}
div[data-baseweb="select"] span {{color:#142536 !important;}}
div[role="listbox"] {{background:#FFFFFF !important;}}
div[role="option"] {{color:#142536 !important;}}
div[data-testid="stMultiSelect"] span[data-baseweb="tag"] {{
    background:#E7F4ED !important;
    color:#247653 !important;
}}
div[data-testid="stMultiSelect"] span[data-baseweb="tag"] * {{color:#247653 !important;}}
div[data-testid="stCheckbox"] label p {{color:#F4F8FB !important;font-weight:700 !important;}}
div[data-testid="stRadio"] label p {{color:#F4F8FB !important;font-weight:700 !important;}}
div[data-testid="stSlider"] p {{color:#F4F8FB !important;}}
div[data-testid="stTextInput"] label p {{color:#F4F8FB !important;}}
div[data-testid="stSelectbox"] label p {{color:#F4F8FB !important;}}
div[data-testid="stMultiSelect"] label p {{color:#F4F8FB !important;}}
.final-choice {{
    background:#F3FAF6;border:1px solid #86C5A6;border-left:5px solid #2F8F67;
    border-radius:10px;padding:14px 16px;margin:8px 0;
}}
.reflection-box {{
    background:#F5F8FA;border-left:4px solid #6E879B;padding:15px;border-radius:7px;
}}
</style>
""", unsafe_allow_html=True)

# ---------- Praxisfall von Marc + Demo-Platzhalter ----------
# Candidate A basiert auf dem anonymisierten Profil von Marc.
# B–J sind bewusst nur sparsame Platzhalter und werden später durch die realen Profile ersetzt.
CANDIDATES = [
{
"id":"CANDIDATE A",
"role":"Head of Brand, Marketing & Communication",
"role_de":"Leitung Marke, Marketing & Kommunikation",
"meta":"Süddeutschland · ca. 13 Jahre Berufserfahrung · offen für neue Positionen",
"career":[
    ("Head of Brand, Marketing & Communication","Leitung Marke, Marketing & Kommunikation","ca. 5 Jahre"),
    ("Teamleitung International Advertising","Leitung internationale Werbung","ca. 1 Jahr"),
    ("Projektleitung International Advertising","Projektleitung internationale Werbung","ca. 3 Jahre"),
    ("Consultant Organisationsentwicklung & Prozessmanagement","Beratung Organisationsentwicklung & Geschäftsprozesse","mehrjährige Erfahrung"),
    ("Traineeprogramm","Berufseinstiegsprogramm","frühere Station"),
],
"education":"Diplomstudium · Auslandsstudium in den USA",
"facts":"Automobilkonzern · internationale Marken-/Werbeerfahrung · Organisations- und Prozessmanagement",
"new":"Im Gespräch wird genauer geklärt, welche Führungsverantwortung, CRM-Nähe und Erfahrung mit komplexen Vertriebsstrukturen tatsächlich vorhanden ist.",
"reveal":"—"
},
{
"id":"CANDIDATE B","role":"Senior Brand Manager","role_de":"Senior Markenmanager:in",
"meta":"Süddeutschland · Profil-Platzhalter","career":[("Senior Brand Manager","Senior Markenmanagement","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Brand Management · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"—"
},
{
"id":"CANDIDATE C","role":"Head of CRM","role_de":"Leitung Kundenmanagement / CRM",
"meta":"Deutschland · Profil-Platzhalter","career":[("Head of CRM","Leitung Kundenmanagement / CRM","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"CRM · digitale Kundenkommunikation · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"—"
},
{
"id":"CANDIDATE D","role":"Marketing Director","role_de":"Marketingleitung",
"meta":"Deutschland · Profil-Platzhalter","career":[("Marketing Director","Marketingleitung","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Marketing · Führung · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"—"
},
{
"id":"CANDIDATE E","role":"Brand & Customer Lead","role_de":"Leitung Marke & Kund:innen",
"meta":"Deutschland · Profil-Platzhalter","career":[("Brand & Customer Lead","Leitung Marke & Kund:innen","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Marke · Kund:innenmanagement · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"—"
},
{
"id":"CANDIDATE F","role":"Head of Marketing","role_de":"Leitung Marketing",
"meta":"Deutschland · Profil-Platzhalter","career":[("Head of Marketing","Leitung Marketing","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Marketing · Agentursteuerung · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"Zusatzinformation für den Blind-Spot-Check folgt."},
{
"id":"CANDIDATE G","role":"CRM & Digital Lead","role_de":"Leitung CRM & Digital",
"meta":"Deutschland · Profil-Platzhalter","career":[("CRM & Digital Lead","Leitung CRM & Digital","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"CRM · Digital · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"Zusatzinformation für den Blind-Spot-Check folgt."},
{
"id":"CANDIDATE H","role":"Brand Director","role_de":"Leitung Markenführung",
"meta":"Deutschland · Profil-Platzhalter","career":[("Brand Director","Leitung Markenführung","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Markenführung · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"—"
},
{
"id":"CANDIDATE I","role":"Customer Engagement Lead","role_de":"Leitung Kundenaktivierung & -bindung",
"meta":"Deutschland · Profil-Platzhalter","career":[("Customer Engagement Lead","Leitung Kundenaktivierung & -bindung","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Kundenkommunikation · Loyalty · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"Zusatzinformation für den Blind-Spot-Check folgt."},
{
"id":"CANDIDATE J","role":"Marketing & Sponsoring Lead","role_de":"Leitung Marketing & Sponsoring",
"meta":"Deutschland · Profil-Platzhalter","career":[("Marketing & Sponsoring Lead","Leitung Marketing & Sponsoring","mehrjährige Erfahrung")],
"education":"Ausbildung / Studium folgt","facts":"Marketing · Sponsoring · weitere Angaben folgen","new":"Zusatzinformation folgt nach Marcs Profil.","reveal":"—"
},
]
BYID={c["id"]:c for c in CANDIDATES}

# Verständlich formulierte Verdichtung des ausführlichen Anforderungsprofils.
CRITERIA=[
    "Marke & Kundenmanagement (Brand / CRM)",
    "Führungserfahrung",
    "Komplexes oder reguliertes Umfeld",
    "Vertriebs- & Markenpartner (B2B2C / Co-Branding)",
    "Digitales Kundenmanagement / CRM",
    "Marketingsteuerung",
    "KI-Kompetenz (AI-Literacy)",
    "Sonstiges"
]

GLOSSARY = {
    "CRM – Customer Relationship Management":"Systematische Gestaltung und Steuerung von Kundenbeziehungen und Kundenkommunikation.",
    "B2B2C – Business to Business to Consumer":"Das Unternehmen erreicht Endkund:innen über einen Geschäftspartner – hier über Finanzberater:innen.",
    "Co-Branding":"Zwei Marken treten gemeinsam gegenüber Kund:innen auf.",
    "Brand Management":"Strategische Führung und Weiterentwicklung einer Marke.",
    "Customer Engagement":"Wie ein Unternehmen Kund:innen gezielt anspricht, aktiviert und langfristig bindet.",
    "Loyalty-Programm":"Kundenbindungsprogramm.",
    "Marketing Performance Management":"Messung und Steuerung des Erfolgs von Marketingmaßnahmen.",
    "AI-Literacy":"Grundverständnis dafür, wie KI im Arbeitsbereich sinnvoll eingesetzt und beurteilt werden kann."
}

# ---------- state ----------
defaults=dict(phase=0,max_phase=0,shortlist=[],screening_index=0,screening_draft=[],criteria=[],criteria_other="",confidence1=60,assessments={},final_candidate=None,final_reasons=[],final_other="",final_confidence=70,reveal={},counter_change="Nein",counter_candidate=None)
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
    hero("CONFIDENTIAL EXECUTIVE SEARCH","DER SUCHAUFTRAG","Praxisfall · Head of Brand Marketing & CRM")
    st.markdown("""<div class="main-card">
    <span class="tag">SEARCH BRIEF</span><span class="status">ACTIVE</span>
    <h2>Head of Brand Marketing & CRM</h2>
    <p><b>Auf Deutsch:</b> Leitung Marke, Marketing & Kundenmanagement</p>
    <p><b>Unternehmen:</b> große Versicherung in Süddeutschland · <b>Führung:</b> ca. 20 Mitarbeitende, darunter 3 Führungskräfte.</p>
    <p><b>Besonderheit:</b> Die Versicherung verkauft überwiegend über selbstständige Finanzberater:innen. Die neue Führungskraft muss daher Versicherung, Vertriebspartner und Kund:innen gleichzeitig im Blick behalten.</p>
    <hr>
    <h3>Für das erste Screening achten wir besonders auf:</h3>
    <p>
    ✓ <b>Marke & Kundenmanagement</b> – langjährige Erfahrung in Brand und/oder CRM<br>
    ✓ <b>Führung</b> – Teams und idealerweise auch Führungskräfte leiten<br>
    ✓ <b>Komplexes / reguliertes Umfeld</b> – z. B. Versicherung, Banking oder ähnlich<br>
    ✓ <b>Vertriebs- & Markenpartner</b> – mehrere Unternehmen/Marken spielen zusammen (B2B2C / Co-Branding)<br>
    ✓ <b>Digitales Kundenmanagement / CRM</b> – digitale Kommunikation, Kundendaten, personalisierte Kontakte<br>
    ✓ <b>Marketingsteuerung</b> – Kampagnen, Agenturen, Medien, Sponsoring und Erfolgsmessung
    </p>
    <div class="newinfo"><b>Zusätzlich ausdrücklich gefordert:</b> KI-Kompetenz (AI-Literacy) – also ein Grundverständnis dafür, wie KI in Marketing und Kundenmanagement sinnvoll eingesetzt werden kann.</div>
    <p class="small">Diese Kurzfassung ist bewusst einfacher als das vollständige Anforderungsprofil. Die finalen 4–6 Screening-Kriterien stimmen wir noch mit Marc ab.</p>
    </div>""",unsafe_allow_html=True)

    with st.expander("BEGRIFFE KURZ ERKLÄRT · Was bedeutet was?"):
        for term, expl in GLOSSARY.items():
            st.markdown(f"**{term}**  \n{expl}")

    if st.button("FIRST SCREENING · ERSTE SICHTUNG STARTEN →",use_container_width=True): goto(1)

# ---------- 1 SCREENING ----------
elif st.session_state.phase==1:
    st.markdown("""
    <style>
    .stApp {background:#F3F2EF !important;}
    [data-testid="stWidgetLabel"] p,
    div[data-testid="stSlider"] p,
    div[data-testid="stTextInput"] label p,
    div[data-testid="stMultiSelect"] label p {color:#243746 !important;}
    .recruiter-brand{background:#FFFFFF;border:1px solid #D5DCE2;border-radius:8px;padding:11px 15px;margin-bottom:12px;display:flex;align-items:center;gap:13px;box-shadow:0 1px 2px rgba(0,0,0,.05)}
    .recruiter-mark{width:34px;height:34px;border-radius:4px;background:#0A66C2;color:white;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:18px}
    .recruiter-search{flex:1;background:#EEF3F8;border:1px solid #C9D6E2;border-radius:4px;padding:9px 12px;color:#425466;font-size:13px}
    .profile-card{background:#FFFFFF;border:1px solid #D5DCE2;border-radius:8px;padding:22px 25px;box-shadow:0 1px 3px rgba(0,0,0,.06);margin-bottom:10px}
    .profile-top{display:flex;gap:17px;align-items:flex-start;border-bottom:1px solid #E3E8EC;padding-bottom:17px;margin-bottom:16px}
    .avatar{width:70px;height:70px;border-radius:50%;background:#DDE6ED;color:#52616D;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}
    .profile-card h2{color:#1B1F23 !important;margin:0 0 3px;font-size:24px}
    .profile-card h3{color:#1B1F23 !important;margin:15px 0 8px;font-size:15px}
    .profile-card p{color:#52616D !important;font-size:13px;line-height:1.45;margin:3px 0}
    .role-de{color:#667788;font-size:13px;font-weight:650;margin-bottom:5px}
    .exp-row{border-left:2px solid #D7E0E7;padding:2px 0 10px 14px;margin-left:6px}
    .exp-title{color:#1B1F23;font-weight:800;font-size:13px}
    .exp-de{color:#667788;font-size:12px}
    .placeholder-note{background:#FFF7E8;border-left:4px solid #D79B32;padding:10px 12px;border-radius:5px;color:#6B552B;font-size:12px;margin-top:12px}
    .shortlist-open{background:#E8F2FB;border:1px solid #B7D4EF;color:#075AAB;border-radius:7px;padding:11px 14px;font-weight:850}
    .shortlist-complete{background:#E6F4EC;border:1px solid #8CC7A9;color:#216C4C;border-radius:7px;padding:11px 14px;font-weight:900}
    </style>
    """,unsafe_allow_html=True)

    st.markdown("""<div class="recruiter-brand">
      <div class="recruiter-mark">R</div>
      <div><b style="color:#1B1F23">Recruiter Search</b><div style="font-size:10px;color:#667788;font-weight:800">EXECUTIVE SEARCH WORKSPACE</div></div>
      <div class="recruiter-search">Head of Brand Marketing & CRM · Deutschland</div>
      <div style="font-size:11px;color:#667788;font-weight:800">10 RESULTS</div>
    </div>""",unsafe_allow_html=True)

    if not st.session_state.shortlist:
        components.html("""<div id="t" style="font-family:Arial;font-weight:800;font-size:18px;color:#0A66C2">01:30</div>
        <script>let s=90,e=document.getElementById('t');let x=setInterval(()=>{s--;let m=Math.floor(s/60),r=s%60;e.innerText=String(m).padStart(2,'0')+':'+String(r).padStart(2,'0');if(s<=20)e.style.color='#C94E55';if(s<=0){clearInterval(x);e.innerText='ZEIT ABGELAUFEN · Bitte Auswahl bestätigen';}},1000);</script>""",height=38)

    # Compact A–J result navigation. Green = currently on shortlist.
    nav_cols=st.columns(10)
    for i,c in enumerate(CANDIDATES):
        letter=c["id"].split()[-1]
        on_shortlist=c["id"] in st.session_state.screening_draft
        label=("✓ " if on_shortlist else "")+letter
        with nav_cols[i]:
            if st.button(label,key=f"candnav_{i}",use_container_width=True):
                st.session_state.screening_index=i
                st.rerun()

    idx=st.session_state.screening_index
    c=CANDIDATES[idx]
    letter=c["id"].split()[-1]

    exp_html=""
    for title,de,dur in c["career"]:
        exp_html += f'<div class="exp-row"><div class="exp-title">{title}</div><div class="exp-de">{de}</div><p>{dur}</p></div>'

    placeholder = "" if c["id"]=="CANDIDATE A" else '<div class="placeholder-note"><b>DEMO-PLATZHALTER</b> · Dieses Profil wird durch Marcs anonymisiertes Originalprofil ersetzt.</div>'

    st.markdown(f"""<div class="profile-card">
      <div class="profile-top">
        <div class="avatar">{letter}</div>
        <div>
          <div style="font-size:10px;color:#0A66C2;font-weight:850;letter-spacing:.8px">{c['id']} · {idx+1} / 10</div>
          <h2>{c['role']}</h2>
          <div class="role-de">{c['role_de']}</div>
          <p><b>{c['meta']}</b></p>
        </div>
      </div>
      <h3>EXPERIENCE · BERUFSERFAHRUNG</h3>
      {exp_html}
      <h3>EDUCATION · AUSBILDUNG</h3>
      <p>{c['education']}</p>
      <h3>PROFILE HIGHLIGHTS · AUF EINEN BLICK</h3>
      <p>{c['facts']}</p>
      {placeholder}
    </div>""",unsafe_allow_html=True)

    draft=list(st.session_state.screening_draft)
    is_selected=c["id"] in draft
    a,b,cnav=st.columns([1,1.5,1])
    with a:
        if st.button("← VORHERIGES PROFIL",disabled=idx==0,use_container_width=True):
            st.session_state.screening_index=max(0,idx-1); st.rerun()
    with b:
        if is_selected:
            if st.button("✓ AUF SHORTLIST · ENTFERNEN",use_container_width=True):
                draft.remove(c["id"]); st.session_state.screening_draft=draft; st.rerun()
        else:
            if st.button("＋ AUF DIE SHORTLIST",disabled=len(draft)>=3,use_container_width=True):
                draft.append(c["id"]); st.session_state.screening_draft=draft; st.rerun()
    with cnav:
        if st.button("NÄCHSTES PROFIL →",disabled=idx==9,use_container_width=True):
            st.session_state.screening_index=min(9,idx+1); st.rerun()

    draft=st.session_state.screening_draft
    status_cls="shortlist-complete" if len(draft)==3 else "shortlist-open"
    chosen=" · ".join(x.split()[-1] for x in draft) if draft else "noch niemand"
    status_text=f"SHORTLIST KOMPLETT · 3 / 3 ✓ · {chosen}" if len(draft)==3 else f"SHORTLIST · {len(draft)} / 3 · {chosen}"
    st.markdown(f'<div class="{status_cls}">{status_text}</div>',unsafe_allow_html=True)

    with st.expander("SEARCH BRIEF & BEGRIFFE NOCHMAL ANSEHEN"):
        st.markdown("**Wichtig im First Screening:** Marke & Kundenmanagement · Führung · komplexes/reguliertes Umfeld · Vertriebs-/Markenpartner · digitales Kundenmanagement/CRM · Marketingsteuerung · zusätzlich KI-Kompetenz.")
        for term, expl in GLOSSARY.items():
            st.markdown(f"**{term}:** {expl}")

    if len(draft)==3:
        st.markdown("### Was hat eure Auswahl tatsächlich beeinflusst?")
        selected_criteria=st.multiselect(
            "Mehrfachauswahl möglich",
            CRITERIA,default=st.session_state.criteria
        )
        criteria_other=st.text_input(
            "Sonstiges – welches Kriterium?",
            value=st.session_state.criteria_other,
            placeholder="z. B. Ausbildung, Unternehmensgröße, Gesamteindruck …"
        ) if "Sonstiges" in selected_criteria else ""
        confidence=st.slider("Wie sicher seid ihr euch bei eurer Shortlist?",0,100,st.session_state.confidence1,5)

        if st.button("SHORTLIST BESTÄTIGEN →",use_container_width=True):
            st.session_state.shortlist=list(draft)
            st.session_state.criteria=selected_criteria
            st.session_state.criteria_other=criteria_other
            st.session_state.confidence1=confidence
            goto(2)

# ---------- 2 THEORY HANDOVER ----------
elif st.session_state.phase==2:
    hero("SHORTLIST GESPEICHERT","Jetzt zurück zur Präsentation.","Nach Theorie-Check und Praxis-Check mit Marc geht es hier mit dem Second Look weiter.")
    st.markdown("""<div class="lock" style="font-size:15px;padding:14px 16px">
    ✓ Eure Auswahl ist gespeichert. In der App müsst ihr jetzt nichts tun.
    </div>""",unsafe_allow_html=True)
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
    final_other=st.text_input("Sonstiges – welches Kriterium?",value=st.session_state.final_other,placeholder="z. B. Ausbildung, Unternehmensgröße, Gesamteindruck …",key="final_other_input") if "Sonstiges" in reasons else ""
    conf=st.slider("Wie sicher seid ihr euch jetzt?",0,100,st.session_state.final_confidence,5)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(3)
    with c2:
        if st.button("ENTSCHEIDUNG BESTÄTIGEN",use_container_width=True):
            st.session_state.final_candidate=final; st.session_state.final_reasons=reasons; st.session_state.final_other=final_other; st.session_state.final_confidence=conf; goto(5)

# ---------- 5 REVEAL ----------
elif st.session_state.phase==5:
    hero("ENTSCHEIDUNG STEHT","BLIND-SPOT CHECK","Der simulierte Search-Prozess ist abgeschlossen. Jetzt beginnt die Reflexion.")
    excluded=[c["id"] for c in CANDIDATES if c["id"] not in st.session_state.shortlist]
    reveal_ids=[x for x in ["CANDIDATE F","CANDIDATE G","CANDIDATE I"] if x in excluded][:2]
    if len(reveal_ids)<2: reveal_ids=excluded[:2]

    for cid in reveal_ids:
        c=BYID[cid]
        st.markdown(f"""<div class="internal"><div class="internal-head"><div><div class="cid">{cid}</div><b>{c['role']}</b></div>
        <span style="color:#667788;font-weight:800">IM FIRST SCREENING AUSGESCHIEDEN</span></div>
        <p>{c['meta']}<br>{c['facts']}</p>
        <div class="reflection-box"><b>WAS IM ERSTEN SCREENING NICHT SICHTBAR WAR</b><br>
        {c['reveal'] if c['reveal']!='—' else c['new']}</div></div>""",unsafe_allow_html=True)
        st.session_state.reveal[cid]=st.checkbox(
            "Mit dieser Information hätten wir diese Person im First Screening näher geprüft.",
            value=st.session_state.reveal.get(cid,False),key=f"rev_{cid}"
        )

    st.markdown("""<div style="color:#FFFFFF;font-size:25px;font-weight:850;margin-top:24px">REFLEXIONSFRAGE</div>
    <div style="color:#DDE8F1;font-size:13px;margin:4px 0 12px">Keine zweite reale Auswahlrunde – nur Reflexion.</div>""",unsafe_allow_html=True)

    change=st.selectbox(
        "Würdet ihr eure finale Entscheidung ändern, wenn ihr diese zusätzlichen Informationen vorher gekannt hättet?",
        ["Nein","Ja"],
        index=0 if st.session_state.counter_change=="Nein" else 1,
        key="counter_change_select"
    )
    st.session_state.counter_change=change

    if change=="Ja":
        # Only people who were actually in the decision story:
        # original Top 3 + the excluded candidates shown in the Blind-Spot reveal.
        eligible=[]
        for cid in list(st.session_state.shortlist)+list(reveal_ids):
            if cid not in eligible and cid != st.session_state.final_candidate:
                eligible.append(cid)
        old=st.session_state.counter_candidate
        idx=eligible.index(old) if old in eligible else 0
        st.session_state.counter_candidate=st.selectbox(
            "Welche Person würdet ihr stattdessen wählen?",
            eligible,index=idx,key="counter_candidate_select"
        )
    else:
        st.session_state.counter_candidate=None

    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(4)
    with c2:
        if st.button("REFLEXION ABSCHLIESSEN →",use_container_width=True): goto(6)

# ---------- 6 LIVE HANDOVER ----------
elif st.session_state.phase==6:
    hero("LIVE-AUSWERTUNG","Euer Team ist fertig.","Die gemeinsame Auswertung gehört jetzt wieder auf die große Leinwand – nicht auf jedes einzelne Gerät.")
    st.markdown("""<div class="main-card">
        <span class="status">TEAM-ERGEBNIS VOLLSTÄNDIG</span>
        <h2 style="margin-top:14px">Zurück zur gemeinsamen Präsentation.</h2>
        <p>Wir vergleichen gleich die Ergebnisse aller Search Teams: Shortlists, Auswahlkriterien,
        Second-Look-Veränderungen, finale Empfehlungen und Blind-Spot-Reaktionen.</p>
        <div class="lock">Die gemeinsame Auswertung wird von der Moderation gezeigt.</div>
    </div>""",unsafe_allow_html=True)

    st.markdown("### Euer Ergebnis auf einen Blick")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Top 3",", ".join(x.split()[-1] for x in st.session_state.shortlist))
    c2.metric("Finale Empfehlung",(st.session_state.final_candidate or "—").replace("CANDIDATE ","C"))
    c3.metric("Sicherheit vorher",f"{st.session_state.confidence1}%")
    c4.metric("Sicherheit final",f"{st.session_state.final_confidence}%")

    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZUR REFLEXION",use_container_width=True): goto(5)
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
