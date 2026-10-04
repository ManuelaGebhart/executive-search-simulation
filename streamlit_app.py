import streamlit as st
import streamlit.components.v1 as components
from collections import Counter
import json, uuid, urllib.request, urllib.error

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
/* Readable glossary on dark pages */
div[data-testid="stExpander"] {{
    background:#FFFFFF !important;
    border:1px solid #D6E0E8 !important;
    border-radius:9px !important;
    overflow:hidden;
}}
div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary * {{
    color:#17324D !important;
}}
div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p,
div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] strong {{
    color:#243746 !important;
}}
</style>
""", unsafe_allow_html=True)

# ---------- Anonymisierte Praxisprofile ----------
# Interne Zuordnung (nicht in der Teilnehmeroberfläche sichtbar):
# A=N, B=K, C=R, D=A, E=G, F=I, G=Q, H=L, I=F, J=E.
# Die Reihenfolge wurde bewusst gemischt, damit die interne Rankingreihenfolge nicht erkennbar ist.
CANDIDATES = [
{
"id":"CANDIDATE A","source":"N","role":"Head of Marketing · Digitalbank","role_de":"Leitung Marketing · Digitalbank",
"meta":"Süddeutschland (Bayern) · ca. 9 Jahre Berufserfahrung · offen für neue Positionen",
"career":[("Head of Marketing · Managementteam","Leitung Marketing","ca. 2 Jahre"),("Associate Director Strategy (B2C)","Strategie B2C","ca. 2,5 Jahre"),("Associate Director Pricing","Pricing","ca. 7 Monate"),("Senior Consultant","Markenberatung","ca. 1,5 Jahre"),("Consultant","Markenberatung","ca. 2 Jahre")],
"education":"Studium nicht näher angegeben · berufsbegleitendes CMO-Programm (Weiterbildung für Chief Marketing Officers / Marketingleitungen) an einer US-Business-School",
"facts":"Finanzdienstleistung · Brand & Growth · KPI/ROI · B2C/B2B",
"second":["Disziplinarische Führung von 4 Teams mit 24 Mitarbeitenden, davon 4 Teamleiter:innen.","Premium-Repositionierung mit messbaren Ergebnissen; Social-Media-Kanäle mit Agentur aufgebaut.","CRM und Customer Lifetime Value liegen im eigenen Bereich Marketing Operations.","Gesamtpaket zuletzt ca. 150.000–170.000 EUR; Zielrahmen muss geklärt werden.","Sofort verfügbar, aber mehrere parallele Bewerbungsprozesse in München."],
"blind":["24 Mitarbeitende in 4 Teams, davon 4 Teamleiter:innen.","CRM und Customer Lifetime Value im eigenen Verantwortungsbereich.","Sofort verfügbar; mehrere parallele Bewerbungsprozesse." ]},
{
"id":"CANDIDATE B","source":"K","role":"Senior Brand Marketing Manager · Telekommunikation","role_de":"Senior Markenmarketing · Telekommunikation",
"meta":"Westdeutschland · ca. 11 Jahre Berufserfahrung",
"career":[("Senior Brand Marketing Manager","Senior Markenmarketing","ca. 5 Jahre"),("Marketing & Brand Manager","Marketing & Marke · Fluggesellschaft","ca. 6 Jahre"),("Projektmanager","Medien","ca. 3 Monate")],
"education":"Wirtschaftsstudium an einer Universität in den Niederlanden · einjähriger Aufenthalt in den USA",
"facts":"Branding · Sponsoring · Telekommunikation & Airline · Auszeichnung in einem Wirtschaftsmedium",
"second":["Keine Führungsverantwortung – weder disziplinarisch noch als Teamleitung.","Keine CRM-Erfahrung genannt.","Aktuell sehr zufrieden; offen für Neues, aber nicht aktiv suchend.","Aktuelles Paket ca. 132.000 EUR gesamt.","Lebt in Nordrhein-Westfalen; Umzug nach München grundsätzlich vorstellbar."],
"blind":["Keine Führungsverantwortung – weder disziplinarisch noch als Teamleitung.","Keine CRM-Erfahrung genannt.","Aktuelles Paket ca. 132.000 EUR gesamt." ]},
{
"id":"CANDIDATE C","source":"R","role":"Leitung Marketing & Kommunikation · Versicherung","role_de":"Co-Leadership Marketing & Kommunikation",
"meta":"Süddeutschland (Bayern) · ca. 16 Jahre Berufserfahrung · offen für neue Positionen",
"career":[("Leitung Marketing & Kommunikation","Co-Leadership · Versicherung","ca. 1,5 Jahre"),("Head of Brand, Media & Advertising","Marke, Media & Werbung","ca. 3,5 Jahre"),("Head of Sponsoring","Sponsoring","ca. 2 Jahre"),("Senior Project Manager Innovation","Innovation","ca. 1 Jahr"),("Business Development / Strategy & Communications","Versicherung B2B/B2B2C","mehrere Jahre")],
"education":"Abschluss an einer privaten Hochschule in Deutschland",
"facts":"Versicherung · Brand · Sponsoring · Daten & KI · B2C/B2B/B2B2C",
"second":["Disziplinarische Führung von 26 Mitarbeitenden, davon 3 Teamleitungen als direkte Führungskräfte.","Refresh einer Versicherungsmarke, ca. 40 Mio. EUR Budget und messbare Full-Funnel-Steuerung.","KI-gestützte Kampagnenaussteuerung und Content-Produktion; KI-Leitlinien mitentwickelt.","Wechselmotivation sehr hoch: alleinige Verantwortung und Finanzberatervertrieb reizen besonders.","Gehaltsvorstellung 220.000–240.000 EUR gesamt; kein Spielraum nach unten."],
"blind":["26 Mitarbeitende, davon 3 Teamleitungen als direkte Führungskräfte.","KI-gestützte Kampagnenaussteuerung und interne KI-Leitlinien.","Gehaltsvorstellung 220.000–240.000 EUR – deutlich über dem festen Rahmen." ]},
{
"id":"CANDIDATE D","source":"A","role":"Head of Brand, Marketing & Communication · Automotive","role_de":"Leitung Marke, Marketing & Kommunikation · Premiummarke",
"meta":"Süddeutschland (Bayern) · ca. 13 Jahre Berufserfahrung · offen für neue Positionen",
"career":[("Head of Brand, Marketing & Communication","Premiummarke · Automobil","ca. 5 Jahre"),("Teamleitung International Advertising","Internationale Werbung","ca. 1 Jahr"),("Projektleitung International Advertising","Internationale Werbung","ca. 3 Jahre"),("Consultant Organisationsentwicklung & Prozessmanagement","Sales & Marketing","ca. 3,5 Jahre"),("Konzern-Traineeprogramm","Führungsnachwuchs","ca. 1,5 Jahre")],
"education":"Diplomstudium an einer deutschen Universität · Auslandsstudium USA",
"facts":"Premium-Automobilmarke · internationale Werbung · Organisations- und Prozessmanagement",
"second":["Nur fachliche Führung von Projektteams mit 2–6 Personen; keine disziplinarische Führung.","Positionierung und Markenidentität einer Premium-Submarke mit aufgebaut; globale Filmkampagnen gesteuert.","Beschäftigt sich im aktuellen Projekt mit KI im Marketing.","Wechselmotivation sehr hoch: mehr Gestaltungsspielraum und erstmals mehr Führungsverantwortung.","Aktuelles Paket ca. 140.000 EUR plus Dienstwagen."],
"blind":["Nur fachliche Führung von Projektteams mit 2–6 Personen; keine disziplinarische Führung.","Wechselmotivation sehr hoch – sucht erstmals mehr Führungsverantwortung.","Aktuelles Paket ca. 140.000 EUR plus Dienstwagen." ]},
{
"id":"CANDIDATE E","source":"G","role":"Brand Strategist & Marketing Expert · selbstständig","role_de":"Markenstrategie & Marketing · zuvor Versicherung",
"meta":"Süddeutschland (Bayern) · ca. 19 Jahre Berufserfahrung",
"career":[("Brand Strategist & Marketing Expert","Selbstständig","ca. 3 Jahre"),("Co-Founder","HR-Tech-Start-up B2B","ca. 2 Jahre"),("Director Market Management","Versicherung · Ausland","ca. 1,5 Jahre"),("Senior Global Brand Manager & Global Social Media Lead","Versicherung · Holding","langjährige Station"),("CRM Specialist","Automobilkonzern","frühe Station")],
"education":"Abschluss an einer Business School in Deutschland",
"facts":"Versicherung · globale Marke · CRM · Customer Engagement · Start-up & Beratung",
"second":["Seit rund 5 Jahren selbstständig; davor gut 10 Jahre im Versicherungskonzern.","Früher 5 Teams mit rund 25 Mitarbeitenden geführt; seit 5 Jahren keine Führungsverantwortung.","Im Interview kein Bezug zu KI.","Möchte zurück in eine Vollzeit-Führungsrolle, würde aber gern kleine Beratungsmandate behalten.","Gehaltsvorstellung 130.000–150.000 EUR."],
"blind":["Früher 5 Teams mit rund 25 Mitarbeitenden geführt; seit 5 Jahren keine Führungsverantwortung.","Im Interview kein Bezug zu KI.","Gehaltsvorstellung 130.000–150.000 EUR." ]},
{
"id":"CANDIDATE F","source":"I","role":"Head of Brand & Creative Studio · Versicherung","role_de":"Leitung Marke & Inhouse-Kreation · Versicherung",
"meta":"Westdeutschland · ca. 17 Jahre Berufserfahrung im selben Versicherungskonzern",
"career":[("Head of Brand & Creative Studio","Versicherung","ca. 9 Monate"),("Head of Marketing Creative","Versicherung","ca. 3 Jahre"),("Head of Distribution Partner Activation & Storytelling","Vertriebspartner-Aktivierung","ca. 2 Jahre"),("Head of Distribution Partner Communication","Vertriebspartner-Kommunikation","ca. 1,5 Jahre"),("Employer Branding / HR / CEO-Assistenz","Versicherungskonzern","mehrere frühere Stationen")],
"education":"Duales Studium mit Berufsausbildung · Promotion an einer deutschen Universität",
"facts":"Versicherung · Brand · Makler & Exklusivagenturen · Change · KI in Kreativprozessen",
"second":["Seit 7 Jahren disziplinarische Führung; aktuell 17 Mitarbeitende, aber keine Führungskräfte unter sich.","Laufbahn begann in der Kommunikation für Makler und Exklusivagenturen.","Gehalt ca. 148.500–162.000 EUR gesamt.","Umzug von Nordrhein-Westfalen nach München noch offen, grundsätzlich vorstellbar.","6 Monate Kündigungsfrist."],
"blind":["Seit 7 Jahren disziplinarische Führung; aktuell 17 Mitarbeitende.","Erfahrung mit Kommunikation für Makler und Exklusivagenturen.","Umzug nach München noch offen; 6 Monate Kündigungsfrist." ]},
{
"id":"CANDIDATE G","source":"Q","role":"Senior Director Brand Marketing · Sportartikel","role_de":"Globale Markenführung · Sport & Olympia",
"meta":"Süddeutschland (Bayern) · ca. 22 Jahre Berufserfahrung · offen für neue Positionen",
"career":[("Senior Director Brand Marketing · Multi-Category Sports & Olympia","Sportartikelkonzern","ca. 8 Monate"),("Senior Director / Director Brand Marketing · Outdoor","Sportartikelkonzern","ca. 5 Jahre"),("Senior Manager / Manager Brand Marketing","Sportartikelkonzern","mehrere Jahre"),("Global Head of Marketing","Outdoor-Marke","ca. 2 Jahre"),("Private Banking / Vorstandassistenz","Großbank","ca. 5 Jahre")],
"education":"Duales BWL-Studium · Master Marketing Management · Executive Education an einer US-Business-School",
"facts":"Globale Markenführung · Olympia & Sponsoring · internationale Partner · frühere Banking-Erfahrung",
"second":["Disziplinarische Führung von 22 Mitarbeitenden, davon 3 Teamleitungen.","Co-Branding mit globalen Markenpartnern und Sportverbänden; kennt aus der Bankzeit die Perspektive von Finanzberater:innen.","Bisher schnelle Konsumgüterkultur; kaum regulatorische Freigaben. Lange Gremienwege werden kritisch gesehen.","Sucht Gesamtverantwortung für eine Marke und findet die Transformation einer Versicherungsmarke spannend.","Aktuelles Paket 159.500 EUR; erwartet mindestens dasselbe."],
"blind":["22 Mitarbeitende, davon 3 Teamleitungen.","Co-Branding mit globalen Partnern; frühere Perspektive als Finanzberater:in.","Kaum Erfahrung mit langen regulatorischen Freigaben; solche Prozesse werden kritisch gesehen." ]},
{
"id":"CANDIDATE H","source":"L","role":"Head of Marketing · Pharma","role_de":"Leitung Marketing · Pharma / Consumer Health",
"meta":"Süddeutschland (Bayern) · ca. 14 Jahre Brand Management · offen für neue Positionen",
"career":[("Head of Marketing","Pharmaunternehmen","ca. 4,5 Jahre"),("Brand Director","FMCG","ca. 3 Jahre"),("Head of Brand Teams DACH","FMCG","ca. 1 Jahr"),("Head of Brand Teams DACH","Pharma/Chemie","ca. 1,5 Jahre"),("Senior Brand Manager","Konsumgüter / Consumer Health","ca. 5 Jahre")],
"education":"Im Profil nicht angegeben",
"facts":"FMCG-Schule · Pharma / Consumer Health · Brand Management · Profil enthält kaum Tätigkeitsdetails",
"second":["Führung bis zu 8 Mitarbeitenden, davon 4 direkt und 1 Teamleitung.","Keine CRM-Erfahrung.","Im Interview kein Bezug zu KI.","Zuletzt ca. 194.000 EUR; würde 160.000 EUR gesamt akzeptieren.","Wohnt in München; 3–4 Bürotage grundsätzlich vereinbar."],
"blind":["Keine CRM-Erfahrung.","Im Interview kein Bezug zu KI.","Zuletzt ca. 194.000 EUR; würde für die Rolle 160.000 EUR gesamt akzeptieren." ]},
{
"id":"CANDIDATE I","source":"F","role":"Principal AI & Brand Marketing Communications Operations · Telekommunikation","role_de":"KI-Transformation & Marken-/Kommunikationssteuerung",
"meta":"Süddeutschland (Bayern) · ca. 17 Jahre im selben Konzern · offen für neue Positionen",
"career":[("Principal AI & BMC Operations","KI & Brand/MarCom Operations","ca. 1,5 Jahre"),("Head of Communications and Campaigns","Kommunikation & Kampagnen","ca. 6 Monate parallel"),("Director Brand & Marketing Communications · kommissarisch","Bereichsleitung","ca. 1 Jahr"),("Head of Brand Strategy & Brand Management","Markenstrategie","ca. 1,5 Jahre"),("Teamleitung Digital Marketing","Social, Content, Community","ca. 2,5 Jahre")],
"education":"Duales Studium an einer Hochschule in Baden-Württemberg",
"facts":"Telekommunikation · Markenrepositionierung · Kampagnen · digitale Customer Journey · starker KI-Schwerpunkt",
"second":["Als Acting Director rund 70 Mitarbeitende geführt, davon 3 Abteilungsleitungen; aktuell 10 Mitarbeitende.","Markenrepositionierung, 360°-Kampagnen und Budget über 90 Mio. EUR.","Klarer KI-Schwerpunkt: generative KI, Marken in Sprachmodellen und verändertes Suchverhalten.","Paket ca. 150.000 EUR plus Dienstwagen/Altersvorsorge; ca. 50.000 EUR Aktien würden beim Wechsel verfallen.","6 Monate Kündigungsfrist, voraussichtlich auf 2–3 Monate verkürzbar."],
"blind":["Als Acting Director rund 70 Mitarbeitende geführt, davon 3 Abteilungsleitungen.","Klarer Schwerpunkt auf generativer KI und Sichtbarkeit von Marken in Sprachmodellen.","Paket ca. 150.000 EUR; beim Wechsel würden Aktien im Wert von ca. 50.000 EUR verfallen." ]},
{
"id":"CANDIDATE J","source":"E","role":"Head of B2B Brand & Marketing Communications · Telekommunikation","role_de":"Leitung B2B-Marke & Marketingkommunikation",
"meta":"Süddeutschland (Bayern) · ca. 18 Jahre Berufserfahrung",
"career":[("Head of B2B Brand & Marketing Communications","Telekommunikation","ca. 9 Monate"),("Head of B2B Marketing","Telekommunikation","ca. 1,5 Jahre"),("Manager Proposition & Go-to-Market","B2B","ca. 5 Jahre"),("Teamleiter Offer Management","B2B","ca. 9 Monate"),("Senior Marketing / Acquisition Manager","B2B/B2C","mehrere Jahre")],
"education":"Universitätsstudium in Deutschland · Fachrichtung nicht angegeben",
"facts":"B2B-Marke · Kampagnen · Events & Messen · Agentursteuerung · Telekommunikation",
"second":["Seit 14 Jahren im selben Konzern; nicht aktiv auf der Suche.","2 Teams mit gut 20 Mitarbeitenden; Bericht direkt an ein Vorstandsmitglied.","Die Zielrolle wäre eher Seitwärts- oder Rückschritt; Motivation im Gespräch gering.","Gehalt über 175.000 EUR inklusive Bonus, zuzüglich Zusatzleistungen.","Wohnt in München und ist an den Standort gebunden."],
"blind":["2 Teams mit gut 20 Mitarbeitenden; Bericht direkt an ein Vorstandsmitglied.","Die Rolle wäre eher Seitwärts- oder Rückschritt; geringe Wechselmotivation.","Gehalt über 175.000 EUR inklusive Bonus – oberhalb des Rahmens." ]},
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
    "Berufserfahrung / Dauer",
    "Branchenkenntnis",
    "Position / Seniorität",
    "Internationale Erfahrung",
    "Unternehmens- / Konzernerfahrung",
    "Ausbildung",
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
defaults=dict(participant_id=str(uuid.uuid4()),submitted=False,phase=0,max_phase=0,shortlist=[],screening_index=0,screening_draft=[],criteria=[],criteria_other="",confidence1=60,assessments={},second_ranking=[],final_candidate=None,final_reasons=[],final_other="",final_confidence=70,reveal={},counter_change="Nein",counter_candidate=None)
for k,v in defaults.items():
    if k not in st.session_state: st.session_state[k]=v

PHASES=["Suchauftrag","First Screening","Theorie & Praxis","Second Look","Finale Entscheidung","Übergang","Blind-Spot Check","Fertig"]


def submit_result():
    """Speichert anonym aggregierbare Ergebnisse zentral, wenn Supabase-Secrets gesetzt sind.
    Ohne Secrets bleibt die App vollständig als Demo nutzbar."""
    if st.session_state.submitted:
        return True, "bereits gespeichert"
    try:
        url=st.secrets.get("SUPABASE_URL", "").rstrip("/")
        key=st.secrets.get("SUPABASE_KEY", "")
    except Exception:
        url=key=""
    if not url or not key:
        return False, "Demo-Modus: zentrale Live-Speicherung ist noch nicht verbunden."
    payload={
        "participant_id":st.session_state.participant_id,
        "shortlist":st.session_state.shortlist,
        "criteria":st.session_state.criteria,
        "criteria_other":st.session_state.criteria_other,
        "confidence_first":st.session_state.confidence1,
        "assessments":st.session_state.assessments,
        "second_ranking":st.session_state.second_ranking,
        "final_candidate":st.session_state.final_candidate,
        "final_reasons":st.session_state.final_reasons,
        "final_other":st.session_state.final_other,
        "confidence_final":st.session_state.final_confidence,
        "blindspot":st.session_state.reveal
    }
    req=urllib.request.Request(
        url+"/rest/v1/executive_search_results",
        data=json.dumps(payload).encode("utf-8"), method="POST",
        headers={"apikey":key,"Authorization":"Bearer "+key,"Content-Type":"application/json"}
    )
    try:
        urllib.request.urlopen(req,timeout=8).read()
        st.session_state.submitted=True
        return True, "Ergebnis anonym für die Live-Auswertung gespeichert."
    except Exception as e:
        return False, "Live-Speicherung derzeit nicht erreichbar; deine lokale Session bleibt erhalten."

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
    <div style="display:grid;grid-template-columns:minmax(220px,290px) 1fr;gap:6px 16px;line-height:1.45">
      <div>✓ <b>Marke & Kundenmanagement</b></div><div>langjährige Erfahrung in Brand und/oder CRM</div>
      <div>✓ <b>Führung</b></div><div>Teams und idealerweise auch Führungskräfte leiten</div>
      <div>✓ <b>Komplexes / reguliertes Umfeld</b></div><div>z. B. Versicherung, Banking oder ähnlich</div>
      <div>✓ <b>Vertriebs- & Markenpartner</b></div><div>mehrere Unternehmen/Marken spielen zusammen (B2B2C / Co-Branding)</div>
      <div>✓ <b>Digitales Kundenmanagement / CRM</b></div><div>digitale Kommunikation, Kundendaten, personalisierte Kontakte</div>
      <div>✓ <b>Marketingsteuerung</b></div><div>Kampagnen, Agenturen, Medien, Sponsoring und Erfolgsmessung</div>
    </div>
    <div class="newinfo"><b>Zusätzlich ausdrücklich gefordert:</b> KI-Kompetenz (AI-Literacy) – also ein Grundverständnis dafür, wie KI in Marketing und Kundenmanagement sinnvoll eingesetzt werden kann.</div>
    <div class="newinfo"><b>Rahmenbedingungen:</b> max. 160.000 EUR Gesamtvergütung inkl. Bonus (Fixum ca. 130–135 Tsd. EUR) · München · mindestens 3, gewünscht 3–4 Bürotage/Woche · Start möglichst früh.</div>
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
    .recruiter-brand{background:#FFFFFF;border:1px solid #B9D5EE;border-top:6px solid #0A66C2;border-radius:8px;padding:11px 15px;margin-bottom:12px;display:flex;align-items:center;gap:13px;box-shadow:0 1px 2px rgba(0,0,0,.05)}
    .recruiter-mark{width:34px;height:34px;border-radius:4px;background:#0A66C2;color:white;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:18px}
    .recruiter-search{flex:1;background:#EEF3F8;border:1px solid #C9D6E2;border-radius:4px;padding:9px 12px;color:#425466;font-size:13px}
    .profile-card{background:#FFFFFF;border:1px solid #D5DCE2;border-left:5px solid #0A66C2;border-radius:8px;padding:22px 25px;box-shadow:0 1px 3px rgba(0,0,0,.06);margin-bottom:10px}
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
        components.html("""
        <style>
          #warn{display:none;margin-top:5px;font-family:Arial;font-size:12px;font-weight:800;color:#C94E55}
          .blink{animation:blink 0.8s step-end infinite}@keyframes blink{50%{opacity:.25}}
        </style>
        <div id="t" style="font-family:Arial;font-weight:800;font-size:18px;color:#0A66C2">04:00</div>
        <div id="warn">NOCH 30 SEKUNDEN · Bitte Auswahl abschließen.</div>
        <script>let s=240,e=document.getElementById('t'),w=document.getElementById('warn');let x=setInterval(()=>{s--;let m=Math.floor(s/60),r=s%60;e.innerText=String(m).padStart(2,'0')+':'+String(r).padStart(2,'0');if(s<=30&&s>0){e.style.color='#C94E55';e.classList.add('blink');w.style.display='block';}if(s<=0){clearInterval(x);e.classList.remove('blink');e.innerText='ZEIT ABGELAUFEN · Bitte Auswahl bestätigen';w.innerText='Die Auswahl bleibt offen – bitte jetzt abschließen.';}},1000);</script>""",height=58)

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
        st.markdown("### Deine persönliche Top 3 · bitte auf Rang 1–3 bringen")
        rank1=st.selectbox("Rang 1",draft,index=0,key="rank1")
        remaining2=[x for x in draft if x!=rank1]
        rank2=st.selectbox("Rang 2",remaining2,index=0,key="rank2")
        rank3=[x for x in remaining2 if x!=rank2][0]
        st.markdown(f"**Rang 3:** {rank3}")
        ranked=[rank1,rank2,rank3]

        st.markdown("### Was hat deine Auswahl tatsächlich beeinflusst?")
        selected_criteria=st.multiselect(
            "Mehrfachauswahl möglich",
            CRITERIA,default=st.session_state.criteria
        )
        criteria_other=st.text_input(
            "Sonstiges – welches Kriterium?",
            value=st.session_state.criteria_other,
            placeholder="z. B. Gesamteindruck oder ein anderer eigener Grund …"
        ) if "Sonstiges" in selected_criteria else ""
        confidence=st.slider("Wie sicher bist du dir bei deiner Shortlist?",0,100,st.session_state.confidence1,5)

        if st.button("SHORTLIST BESTÄTIGEN →",use_container_width=True):
            st.session_state.shortlist=ranked
            st.session_state.criteria=selected_criteria
            st.session_state.criteria_other=criteria_other
            st.session_state.confidence1=confidence
            goto(2)

# ---------- 2 THEORY HANDOVER ----------
elif st.session_state.phase==2:
    hero("SHORTLIST GESPEICHERT","Jetzt zurück zur Präsentation.","Nach Theorie-Check und Praxis-Check mit Marc geht es hier mit dem Second Look weiter.")
    st.markdown("""<div class="lock" style="font-size:15px;padding:14px 16px">
    ✓ Deine Auswahl ist gespeichert. In der App müsst ihr jetzt nichts tun.
    </div>""",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← FIRST SCREENING ANSEHEN",use_container_width=True): goto(1)
    with c2:
        if st.button("SECOND LOOK ÖFFNEN →",use_container_width=True): goto(3)

# ---------- 3 SECOND LOOK ----------
elif st.session_state.phase==3:
    hero("SECOND LOOK","Gleiche drei. Neue Informationen.","Prüfe die priorisierten Informationen aus dem Erstinterview – und ordne deine Top 3 danach erneut.")
    for cid in st.session_state.shortlist:
        c=BYID[cid]
        st.markdown(f"""<div class="internal"><div class="internal-head"><div><div class="cid">{cid}</div><b>{c['role']}</b></div><span class="status">SHORTLISTED</span></div>
        <div class="small">WAS DU BEREITS WUSSTEST</div><p>{c['meta']}<br>{c['facts']}</p>
        <div class="newinfo"><b>PRIORISIERTE INFORMATIONEN AUS DEM ERSTINTERVIEW</b><br>{''.join(f'• {x}<br>' for x in c['second'])}</div></div>""",unsafe_allow_html=True)

    st.markdown("### Hat sich deine Reihenfolge verändert?")
    st.caption("Es bleiben dieselben drei Personen. Ordne nur Rang 1–3 nach den neuen Informationen neu.")
    base=list(st.session_state.second_ranking or st.session_state.shortlist)
    r1=st.selectbox("Neuer Rang 1",st.session_state.shortlist,index=st.session_state.shortlist.index(base[0]) if base and base[0] in st.session_state.shortlist else 0,key="second_rank1")
    rem=[x for x in st.session_state.shortlist if x!=r1]
    preferred2=base[1] if len(base)>1 and base[1] in rem else rem[0]
    r2=st.selectbox("Neuer Rang 2",rem,index=rem.index(preferred2),key="second_rank2")
    r3=[x for x in rem if x!=r2][0]
    st.markdown(f"**Neuer Rang 3:** {r3}")
    newrank=[r1,r2,r3]
    st.session_state.second_ranking=newrank
    st.session_state.assessments={cid:{"vorher":st.session_state.shortlist.index(cid)+1,"nachher":newrank.index(cid)+1} for cid in st.session_state.shortlist}
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(2)
    with c2:
        if st.button("ZUR FINALEN ENTSCHEIDUNG →",use_container_width=True): goto(4)

# ---------- 4 FINAL ----------
elif st.session_state.phase==4:
    hero("FINALE ENTSCHEIDUNG","Eine Person. Eine Empfehlung.","Wähle genau eine Person aus deiner ursprünglichen Top 3.")
    cols=st.columns(3)
    for i,cid in enumerate(st.session_state.second_ranking or st.session_state.shortlist):
        c=BYID[cid]
        with cols[i]:
            st.markdown(f"""<div class="metricbox"><div class="cid">{cid}</div><h3>{c['role']}</h3><p>{c['meta']}</p><p><b>Ranking:</b> vorher Rang {st.session_state.shortlist.index(cid)+1} · nach Second Look Rang {(st.session_state.second_ranking or st.session_state.shortlist).index(cid)+1}</p></div>""",unsafe_allow_html=True)
    idx=0
    final_pool=st.session_state.second_ranking or st.session_state.shortlist
    if st.session_state.final_candidate in final_pool: idx=final_pool.index(st.session_state.final_candidate)
    final=st.selectbox("Wen empfiehlst du final?",final_pool,index=idx)
    fc=BYID[final]
    st.markdown(f"""<div class="final-choice"><div class="cid">FINALE EMPFEHLUNG</div><b>{final} · {fc['role']}</b></div>""",unsafe_allow_html=True)
    reasons=st.multiselect("Welche Kriterien tragen deine finale Empfehlung?",CRITERIA,default=st.session_state.final_reasons)
    final_other=st.text_input("Sonstiges – welches Kriterium?",value=st.session_state.final_other,placeholder="z. B. Ausbildung, Unternehmensgröße, Gesamteindruck …",key="final_other_input") if "Sonstiges" in reasons else ""
    conf=st.slider("Wie sicher bist du dir jetzt?",0,100,st.session_state.final_confidence,5)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(3)
    with c2:
        if st.button("ENTSCHEIDUNG BESTÄTIGEN",use_container_width=True):
            st.session_state.final_candidate=final; st.session_state.final_reasons=reasons; st.session_state.final_other=final_other; st.session_state.final_confidence=conf; goto(5)

# ---------- 5 PAUSE BEFORE BLIND SPOT ----------
elif st.session_state.phase==5:
    hero("ENTSCHEIDUNG GESPEICHERT","Bitte kurz Blick nach vorne.","Deine finale Empfehlung steht. Der nächste Schritt wird gemeinsam eingeführt.")
    st.markdown("""<div class="main-card"><span class="status">STOPP</span><h2 style="margin-top:14px">Noch nicht weiterklicken.</h2><p>Wir erklären jetzt gemeinsam, warum wir noch einmal auf die sieben bereits ausgeschiedenen Profile schauen.</p></div>""",unsafe_allow_html=True)
    if st.button("BLIND-SPOT CHECK ÖFFNEN →",use_container_width=True): goto(6)

# ---------- 6 REVEAL ----------
elif st.session_state.phase==6:
    hero("ENTSCHEIDUNG STEHT","BLIND-SPOT CHECK","Alle sieben ausgeschiedenen Profile. Je 2–3 Informationen, die im First Screening noch nicht sichtbar waren.")
    excluded=[c["id"] for c in CANDIDATES if c["id"] not in st.session_state.shortlist]
    for cid in excluded:
        c=BYID[cid]
        reveal_html="".join(f"• {x}<br>" for x in c["blind"])
        st.markdown(f"""<div class="internal"><div class="internal-head"><div><div class="cid">{cid}</div><b>{c['role']}</b></div>
        <span style="color:#667788;font-weight:800">IM FIRST SCREENING AUSGESCHIEDEN</span></div>
        <div class="reflection-box"><b>WAS IM ERSTEN SCREENING NICHT SICHTBAR WAR</b><br>{reveal_html}</div></div>""",unsafe_allow_html=True)
        st.session_state.reveal[cid]=st.checkbox(
            "Mit diesen Informationen hätte ich diese Person im First Screening näher geprüft.",
            value=st.session_state.reveal.get(cid,False),key=f"rev_{cid}"
        )
    st.markdown("""<div style="color:#DDE8F1;font-size:13px;margin:14px 0 12px"><b>Wichtig:</b> Keine zweite Auswahlrunde. Die ausgeschiedenen Profile bleiben ausgeschieden. Es geht nur um die Reflexion deiner frühen Vorauswahl.</div>""",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← ZURÜCK",use_container_width=True): goto(5)
    with c2:
        if st.button("BLIND-SPOT CHECK ABSCHLIESSEN →",use_container_width=True): goto(7)

# ---------- 7 LIVE HANDOVER ----------
elif st.session_state.phase==7:
    hero("LIVE-AUSWERTUNG","Deine Auswahl ist abgeschlossen.","Die gemeinsame Auswertung gehört jetzt wieder auf die große Leinwand – nicht auf dein Gerät.")
    ok,msg=submit_result()
    if ok:
        st.success(msg)
    else:
        st.info(msg)
    st.markdown("### Dein Ergebnis auf einen Blick")
    first_rank="  ·  ".join(f"{i+1}. {cid.replace('CANDIDATE ','C')}" for i,cid in enumerate(st.session_state.shortlist))
    second_rank="  ·  ".join(f"{i+1}. {cid.replace('CANDIDATE ','C')}" for i,cid in enumerate(st.session_state.second_ranking or st.session_state.shortlist))
    st.markdown(f"""<div class="main-card">
      <span class="status">ERGEBNIS VOLLSTÄNDIG</span>
      <h3 style="margin-top:14px">Deine erste Top 3</h3><p style="font-size:20px;font-weight:850">{first_rank}</p>
      <h3>Deine Top 3 nach dem Second Look</h3><p style="font-size:20px;font-weight:850">{second_rank}</p>
      <h3>Finale Empfehlung</h3><p style="font-size:24px;font-weight:900">{(st.session_state.final_candidate or '—').replace('CANDIDATE ','C')}</p>
    </div>""",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    c1.metric("Sicherheit First Screening",f"{st.session_state.confidence1}%")
    c2.metric("Sicherheit final",f"{st.session_state.final_confidence}%")

    if st.button("← ZUM BLIND-SPOT CHECK",use_container_width=True):
        goto(6)
