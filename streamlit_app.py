import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Executive Search Simulation",
    page_icon="🎯",
    layout="wide"
)


# ============================================================
# DESIGN
# ============================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL
   ========================================================= */

.stApp {
    background-color: #f4f6f8;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    letter-spacing: -0.02em;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 700;
    padding: 0.65rem 1.2rem;
}


/* =========================================================
   EXECUTIVE SEARCH – INTERNAL LOOK
   ========================================================= */

.exec-header {
    background: linear-gradient(120deg, #0b1628 0%, #162943 100%);
    padding: 34px 38px;
    border-radius: 16px;
    margin-bottom: 24px;
    color: white;
}

.exec-eyebrow {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #aebed2;
    margin-bottom: 10px;
}

.exec-title {
    font-size: 38px;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 8px;
}

.exec-subtitle {
    font-size: 16px;
    color: #d7e0eb;
    max-width: 760px;
}

.confidential {
    display: inline-block;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 30px;
    padding: 6px 12px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.3px;
    margin-top: 20px;
}

.mandate-card {
    background: white;
    border: 1px solid #e2e7ed;
    border-radius: 14px;
    padding: 28px 30px;
    margin-bottom: 18px;
    box-shadow: 0 3px 12px rgba(20, 35, 55, 0.05);
}

.card-label {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #68788b;
    margin-bottom: 6px;
}

.position-title {
    font-size: 27px;
    font-weight: 800;
    color: #102239;
    margin-bottom: 5px;
}

.position-meta {
    color: #647386;
    font-size: 14px;
}

.mission-box {
    background: #eaf0f7;
    border-left: 5px solid #183a61;
    border-radius: 8px;
    padding: 20px 24px;
    margin-top: 20px;
    margin-bottom: 22px;
}

.mission-title {
    font-weight: 800;
    color: #102239;
    margin-bottom: 6px;
}

.mission-text {
    color: #34465b;
    line-height: 1.55;
}


/* =========================================================
   PROCESS BAR
   ========================================================= */

.process-row {
    display: flex;
    gap: 8px;
    margin: 24px 0;
}

.process-active {
    flex: 1;
    background: #183a61;
    color: white;
    padding: 11px;
    text-align: center;
    border-radius: 7px;
    font-size: 12px;
    font-weight: 700;
}

.process-inactive {
    flex: 1;
    background: #e5e9ee;
    color: #7b8794;
    padding: 11px;
    text-align: center;
    border-radius: 7px;
    font-size: 12px;
    font-weight: 700;
}


/* =========================================================
   FIRST SCREENING – RECRUITER SEARCH LOOK
   bewusst nur inspiriert, keine LinkedIn-Kopie
   ========================================================= */

.recruiter-shell {
    background: #ffffff;
    border: 1px solid #d8dee5;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 18px;
    box-shadow: 0 2px 8px rgba(20,35,55,0.05);
}

.recruiter-topbar {
    background: #ffffff;
    border-bottom: 1px solid #e2e7ed;
    padding: 16px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.recruiter-brand {
    font-size: 14px;
    font-weight: 800;
    color: #0a66c2;
    letter-spacing: 0.3px;
}

.recruiter-mode {
    font-size: 11px;
    color: #68788b;
    font-weight: 700;
    letter-spacing: 1px;
}

.recruiter-search {
    background: #eef3f8;
    border: 1px solid #d7e0e8;
    border-radius: 6px;
    margin: 16px 22px;
    padding: 12px 16px;
    color: #34465b;
    font-size: 14px;
}

.recruiter-summary {
    display: flex;
    gap: 24px;
    padding: 0 22px 18px 22px;
    color: #5c6f82;
    font-size: 13px;
}

.recruiter-summary strong {
    color: #1f2d3d;
}

.recruiter-section-title {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #68788b;
    margin-bottom: 5px;
}

.recruiter-main-title {
    font-size: 25px;
    font-weight: 800;
    color: #172b3a;
    margin-bottom: 5px;
}

.recruiter-subtitle {
    color: #607386;
    font-size: 14px;
    line-height: 1.5;
}


/* =========================================================
   REQUIREMENTS
   ========================================================= */

.requirement-card {
    background: #ffffff;
    border: 1px solid #e2e7ed;
    border-radius: 10px;
    padding: 18px 20px;
    min-height: 165px;
    box-shadow: 0 2px 7px rgba(20,35,55,0.03);
}

.requirement-label {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.4px;
    color: #68788b;
    margin-bottom: 12px;
}

.requirement-item {
    color: #25384e;
    margin-bottom: 10px;
    line-height: 1.4;
}


/* =========================================================
   CANDIDATE SEARCH RESULT HEADER
   ========================================================= */

.results-header {
    background: white;
    border: 1px solid #dfe4ea;
    border-radius: 10px;
    padding: 18px 20px;
    margin: 22px 0 12px 0;
}

.results-count {
    font-size: 20px;
    font-weight: 800;
    color: #172b3a;
}

.results-caption {
    font-size: 13px;
    color: #68788b;
    margin-top: 3px;
}

.candidate-id {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    color: #0a66c2;
    margin-bottom: 3px;
}

.candidate-role {
    font-size: 19px;
    font-weight: 800;
    color: #172b3a;
    margin-bottom: 3px;
}

.candidate-sector {
    color: #5f7182;
    font-size: 13px;
    margin-bottom: 10px;
}

.profile-chip {
    display: inline-block;
    background: #eef3f8;
    color: #40566c;
    border-radius: 20px;
    padding: 4px 9px;
    margin: 3px 4px 3px 0;
    font-size: 11px;
    font-weight: 600;
}


/* =========================================================
   INTERNAL PROCESS AFTER SOURCING
   ========================================================= */

.internal-header {
    background: linear-gradient(120deg, #0b1628 0%, #1a314e 100%);
    color: white;
    padding: 26px 30px;
    border-radius: 14px;
    margin-bottom: 20px;
}

.internal-label {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.6px;
    color: #aebed2;
    margin-bottom: 6px;
}

.internal-title {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 6px;
}

.internal-text {
    color: #d7e0eb;
    font-size: 14px;
    line-height: 1.5;
}

.internal-card {
    background: white;
    border: 1px solid #e0e5ea;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(20,35,55,0.04);
}

.interview-box {
    background: #eef4f8;
    border-left: 4px solid #183a61;
    border-radius: 7px;
    padding: 15px 17px;
    margin: 12px 0;
    color: #31465a;
}

.change-box {
    background: #fff8e8;
    border: 1px solid #ead7a5;
    border-radius: 10px;
    padding: 18px 20px;
    margin: 14px 0;
}

.complete-box {
    background: linear-gradient(120deg, #0b1628 0%, #183a61 100%);
    color: white;
    padding: 38px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 24px;
}

.complete-small {
    color: #aebed2;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.complete-title {
    font-size: 38px;
    font-weight: 900;
    margin: 8px 0;
}

.complete-text {
    color: #d7e0eb;
    font-size: 15px;
}


/* =========================================================
   SCREENING – DISTINCT BLUE RECRUITER WORKSPACE
   ========================================================= */
.screening-banner {
    background: linear-gradient(120deg, #0A66C2 0%, #07549f 100%);
    color: white;
    padding: 24px 28px;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0 5px 18px rgba(10,102,194,0.18);
}
.screening-banner-label {font-size:11px;font-weight:800;letter-spacing:1.6px;color:#dbeeff;margin-bottom:5px;}
.screening-banner-title {font-size:29px;font-weight:850;margin-bottom:5px;}
.screening-banner-text {font-size:14px;color:#eef7ff;}
.recruiter-shell {border: 1px solid #b9d6f2; box-shadow:0 5px 18px rgba(10,102,194,0.10);}
.recruiter-topbar {background:#0A66C2;border-bottom:none;}
.recruiter-brand {color:white;font-size:17px;}
.recruiter-mode {color:#dbeeff;}
.recruiter-search {background:white;border:2px solid #c8def2;color:#24384b;box-shadow:0 2px 8px rgba(10,102,194,.08);}
.results-header {border-top:4px solid #0A66C2;background:#f8fbff;}
.results-count {color:#0A66C2;}
.screening-help {background:#eaf4ff;border-left:4px solid #0A66C2;border-radius:8px;padding:13px 16px;color:#29465f;margin:14px 0 18px;}
.nav-hint {font-size:12px;color:#728195;text-align:center;margin-top:6px;}

/* =========================================================
   DECISION REVIEW – DIFFERENCES AT A GLANCE
   ========================================================= */

.diff-card {
    background: #ffffff;
    border: 1px solid #dfe5eb;
    border-radius: 12px;
    padding: 18px 20px;
    margin: 10px 0 14px 0;
    box-shadow: 0 2px 8px rgba(20,35,55,0.04);
}
.diff-card-out {border-left: 6px solid #b42318;}
.diff-card-in {border-left: 6px solid #16803c;}
.diff-status {font-size:11px;font-weight:900;letter-spacing:1.3px;margin-bottom:6px;}
.diff-out {color:#b42318;}
.diff-in {color:#16803c;}
.diff-name {font-size:20px;font-weight:850;color:#172b3a;margin-bottom:12px;}
.diff-row {display:grid;grid-template-columns:155px 1fr;gap:12px;padding:8px 0;border-top:1px solid #edf0f3;}
.diff-label {font-size:11px;font-weight:800;letter-spacing:.7px;color:#6a7888;text-transform:uppercase;}
.diff-value {font-size:14px;color:#263b50;line-height:1.45;}
.diff-impact {font-weight:800;color:#102239;}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DEMO-DATEN – ALLES FREI ERFUNDEN
# ============================================================

kandidaten = {

    "Kandidat A – Der Branchenprofi": {
        "id": "CANDIDATE 01",
        "aktuell": "Regional Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "16 Jahre Berufserfahrung",
        "fuehrung": "9 Jahre Führungserfahrung",
        "international": "Deutschland, Österreich, Schweiz",
        "screening_signal": "Starke Branchen- und Führungserfahrung",
        "new_signal": "Führung bisher nur in etablierten Strukturen",
        "impact": "Aufbau-/Expansionserfahrung bleibt offen",
        "profil":
            "Langjährige Tätigkeit bei zwei großen Finanzdienstleistern. "
            "Seit fünf Jahren Leitung einer regionalen Geschäftseinheit "
            "mit rund 120 Mitarbeitenden.",
        "interview":
            "Im Gespräch wird deutlich: Der Kandidat übernahm seine "
            "bisherigen Führungsbereiche jeweils in bereits etablierten "
            "Strukturen. Einen neuen Standort oder eine neue Geschäftseinheit "
            "hat er bisher nicht selbst aufgebaut."
    },

    "Kandidatin B – Die Aufbau-Expertin": {
        "id": "CANDIDATE 02",
        "aktuell": "Managing Director",
        "branche": "Technologie",
        "erfahrung": "13 Jahre Berufserfahrung",
        "fuehrung": "7 Jahre Führungserfahrung",
        "international": "Österreich, Polen, Tschechien",
        "screening_signal": "Direkte Aufbau- und Expansionserfahrung",
        "new_signal": "Aufbauverantwortung bestätigt; keine direkte Finanzbranche",
        "impact": "Aufbau stark belegt, Branchenfit bleibt offen",
        "profil":
            "Begleitete mehrere Expansionsprojekte und war zuletzt für den "
            "Aufbau einer neuen Geschäftseinheit in Zentral- und Osteuropa "
            "verantwortlich.",
        "interview":
            "Im Gespräch konkretisiert sie ihre Rolle: Sie verantwortete den "
            "Aufbau einer neuen Einheit von der Personalgewinnung bis zur "
            "Etablierung operativer Strukturen. Direkte Erfahrung in der "
            "Finanzdienstleistungsbranche hat sie nicht."
    },

    "Kandidat C – Der internationale Manager": {
        "id": "CANDIDATE 03",
        "aktuell": "Vice President Operations",
        "branche": "Industrie",
        "erfahrung": "18 Jahre Berufserfahrung",
        "fuehrung": "11 Jahre Führungserfahrung",
        "international": "Europa, USA, Asien",
        "screening_signal": "Internationale Führung mehrerer Standorte",
        "new_signal": "Standorte gesteuert, aber nicht selbst aufgebaut",
        "impact": "Aufbau-/Expansionserfahrung wird schwächer",
        "profil":
            "Internationale Führungslaufbahn mit Verantwortung für mehrere "
            "Standorte. Langjährige Erfahrung in globalen Unternehmensstrukturen.",
        "interview":
            "Im Gespräch zeigt sich: Seine internationale Verantwortung bezog "
            "sich vor allem auf die Steuerung bereits bestehender Standorte. "
            "Bei deren Aufbau war er selbst nicht beteiligt."
    },

    "Kandidatin D – Die unauffällige Kandidatin": {
        "id": "CANDIDATE 04",
        "aktuell": "Head of Operations",
        "branche": "Finanznahe Dienstleistungen",
        "erfahrung": "12 Jahre Berufserfahrung",
        "fuehrung": "5 Jahre Führungserfahrung",
        "international": "Österreich, Slowenien",
        "screening_signal": "Solide operative Führung, wenig sichtbare Aufbauhistorie",
        "new_signal": "Aktiv am Aufbau eines neuen Standorts beteiligt",
        "impact": "Aufbau-/Expansionserfahrung wird deutlich stärker",
        "profil":
            "Karriere überwiegend bei mittelständischen Unternehmen. "
            "Verantwortung für operative Teams und mehrere interne "
            "Veränderungsprojekte.",
        "interview":
            "Im Gespräch wird eine Information sichtbar, die aus dem Kurzprofil "
            "kaum hervorging: Sie war beim Eintritt in ihr aktuelles Unternehmen "
            "maßgeblich am Aufbau eines neuen österreichischen Standorts beteiligt "
            "und übernahm dort schrittweise Führungsverantwortung."
    },

    "Kandidat E – Der perfekte Lebenslauf?": {
        "id": "CANDIDATE 05",
        "aktuell": "Country Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "17 Jahre Berufserfahrung",
        "fuehrung": "10 Jahre Führungserfahrung",
        "international": "Deutschland, Schweiz, Großbritannien",
        "screening_signal": "Starke Marken, große Teams und Wachstumsprojekte",
        "new_signal": "Wachstumskonzepte waren zentral vorgegeben",
        "impact": "Eigenständige Aufbauverantwortung wird schwächer",
        "profil":
            "Führungspositionen bei mehreren international bekannten Unternehmen. "
            "Verantwortung für große Teams und strategische Wachstumsprojekte.",
        "interview":
            "Im Gespräch wird deutlich: Die strategischen Wachstumsprojekte wurden "
            "zentral vorbereitet. Seine Verantwortung lag vor allem in der Umsetzung "
            "bereits definierter Konzepte und in der Führung bestehender Organisationen."
    }
}


gruende = [
    "Führungserfahrung",
    "Branchenerfahrung",
    "Erfahrung mit Aufbau / Expansion",
    "Internationale Erfahrung",
    "Bisherige Arbeitgeber",
    "Karriereverlauf",
    "Vergleichbare Aufgaben",
    "Sonstiges"
]


gruende2 = [
    "Neue Information aus dem Gespräch",
    "Aufbau- / Expansionserfahrung",
    "Führungserfahrung",
    "Branchenerfahrung",
    "Internationale Erfahrung",
    "Konkretere Beschreibung der bisherigen Aufgaben",
    "Eine frühere Annahme wurde durch neue Informationen korrigiert",
    "Sonstiges"
]


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "phase": 0,
    "shortlist1": [],
    "shortlist2": [],
    "gruende1": [],
    "gruende2": [],
    "sicherheit1": 70,
    "max_phase": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# PHASE 0 – BRIEFING
# ============================================================

if st.session_state.phase == 0:

    st.markdown("""
<div class="exec-header">
<div class="exec-eyebrow">EXECUTIVE SEARCH SIMULATION</div>
<div class="exec-title">MISSION: EXECUTIVE SEARCH</div>
<div class="exec-subtitle">
Ihr übernehmt einen vertraulichen Suchauftrag für eine strategisch wichtige Führungsposition.
</div>
<div class="confidential">● CONFIDENTIAL SEARCH MANDATE</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="process-row">
<div class="process-active">01 · BRIEFING</div>
<div class="process-inactive">02 · FIRST SCREENING</div>
<div class="process-inactive">03 · SECOND LOOK</div>
<div class="process-inactive">04 · FINAL SHORTLIST</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="mandate-card">
<div class="card-label">SEARCH MANDATE</div>
<div class="position-title">Managing Director Austria</div>
<div class="position-meta">
Internationales Unternehmen · Marktausbau Österreich · Executive Leadership
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="mission-box">
<div class="mission-title">EURE MISSION</div>
<div class="mission-text">
Das Executive-Search-Team hat fünf potenzielle Kandidat:innen identifiziert.<br><br>
Sichtet die verfügbaren Profile und erstellt eine
<strong>Shortlist mit genau drei Personen.</strong><br><br>
Die erste Sichtung erfolgt bewusst schnell –
ähnlich einer ersten Vorauswahl im Executive Search.
</div>
</div>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("KANDIDAT:INNEN", "5")

    with col2:
        st.metric("SHORTLIST", "3")

    with col3:
        st.metric("SCREENING-ZEIT", "90 Sek.")

    st.write("")

    if st.button(
        "START FIRST SCREENING  →",
        type="primary",
        key="start_mission",
        use_container_width=True
    ):
        st.session_state.phase = 1
        st.session_state.max_phase = max(st.session_state.max_phase, 1)
        st.rerun()

    st.caption(
        "Demo-Prototyp · Alle Unternehmen, Personen und Angaben "
        "dieser Simulation sind frei erfunden."
    )


# ============================================================
# PHASE 1 – RECRUITER SEARCH / FIRST SCREENING
# ============================================================

elif st.session_state.phase == 1:

    st.markdown("""
<div class="process-row">
<div class="process-inactive">01 · BRIEFING</div>
<div class="process-active">02 · FIRST SCREENING</div>
<div class="process-inactive">03 · SECOND LOOK</div>
<div class="process-inactive">04 · FINAL SHORTLIST</div>
</div>
""", unsafe_allow_html=True)

    # Deutlich abgesetzter Recruiter-/Sourcing-Workspace
    st.markdown("""
<div class="screening-banner">
<div class="screening-banner-label">TALENT SOURCING WORKSPACE</div>
<div class="screening-banner-title">First Screening</div>
<div class="screening-banner-text">Öffentliche berufliche Profile sichten · Suchauftrag prüfen · Top 3 für die Shortlist auswählen</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="recruiter-shell">

<div class="recruiter-topbar">
<div class="recruiter-brand">Recruiter Search</div>
<div class="recruiter-mode">TALENT SOURCING · CONFIDENTIAL</div>
</div>

<div class="recruiter-search">
🔎 Managing Director · Austria · Leadership · Expansion
</div>

<div class="recruiter-summary">
<span><strong>5</strong> Search Results</span>
<span><strong>3</strong> Shortlist Positions</span>
<span>Search Mandate: <strong>Managing Director Austria</strong></span>
</div>

</div>
""", unsafe_allow_html=True)

    # --------------------------------------------------------
    # COUNTDOWN – UNVERÄNDERT
    # --------------------------------------------------------

    components.html(
        """
        <div id="timerbox" style="
            text-align:center;
            padding:12px;
            border-radius:12px;
            background:#f1f3f5;
            font-family:Arial,sans-serif;
        ">

            <div style="
                font-size:14px;
                font-weight:bold;
                letter-spacing:1px;
            ">
                FIRST SCREENING · VERBLEIBENDE ZEIT
            </div>

            <div id="timer" style="
                font-size:40px;
                font-weight:bold;
                margin:4px;
            ">
                01:30
            </div>

            <div id="message" style="font-size:14px;">
                Prüft die Profile und wählt genau 3 Personen aus.
            </div>

        </div>

        <script>

        let timeLeft = 90;

        const timer = document.getElementById("timer");
        const box = document.getElementById("timerbox");
        const message = document.getElementById("message");

        const countdown = setInterval(function() {

            timeLeft--;

            let minutes = Math.floor(timeLeft / 60);
            let seconds = timeLeft % 60;

            timer.innerHTML =
                String(minutes).padStart(2,'0')
                + ":"
                + String(seconds).padStart(2,'0');

            if (timeLeft <= 20 && timeLeft > 5) {

                box.style.background = "#ffe1e1";
                box.style.border = "2px solid #c62828";

                timer.style.color = "#c62828";
                timer.style.fontSize = "54px";

                message.innerHTML =
                    "<b>Noch " + timeLeft +
                    " Sekunden – bitte 3 Personen auswählen!</b>";
            }

            if (timeLeft <= 5 && timeLeft > 0) {

                box.style.background = "#c62828";

                timer.style.color = "white";
                timer.style.fontSize = "70px";

                message.style.color = "white";
                message.innerHTML =
                    "<b>JETZT AUSWAHL ABSCHLIESSEN</b>";
            }

            if (timeLeft <= 0) {

                clearInterval(countdown);

                box.style.background = "#c62828";

                timer.style.color = "white";
                timer.style.fontSize = "34px";
                timer.innerHTML = "ZEIT ABGELAUFEN";

                message.style.color = "white";
                message.innerHTML =
                    "<b>Bitte bestätigt jetzt eure Auswahl.</b>";
            }

        },1000);

        </script>
        """,
        height=145
    )

    st.markdown("### Search Criteria")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="requirement-card">
<div class="requirement-label">MUST-HAVES</div>
<div class="requirement-item">✓ Mehrjährige Führungserfahrung</div>
<div class="requirement-item">✓ Erfahrung mit Wachstum, Aufbau oder Expansion</div>
<div class="requirement-item">✓ Erfahrung in komplexen Unternehmensstrukturen</div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="requirement-card">
<div class="requirement-label">NICE-TO-HAVES</div>
<div class="requirement-item">✓ Internationale Erfahrung</div>
<div class="requirement-item">✓ Kenntnisse der Finanzdienstleistungsbranche</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="results-header">
<div class="results-count">5 Candidate Results</div>
<div class="results-caption">
Profile öffnen, berufliche Informationen prüfen und maximal drei Personen auswählen.
</div>
</div>
""", unsafe_allow_html=True)

    auswahl = []

    kandidatennamen = list(kandidaten.keys())

    for index, name in enumerate(kandidatennamen, start=1):

        daten = kandidaten[name]

        # Im sichtbaren Screening keine wertenden Demo-Namen
        expander_title = (
            f"{daten['id']}  ·  {daten['aktuell']}  ·  {daten['branche']}"
        )

        with st.expander(expander_title):

            st.markdown(
                f"""
<div class="candidate-id">{daten['id']}</div>
<div class="candidate-role">{daten['aktuell']}</div>
<div class="candidate-sector">{daten['branche']}</div>

<span class="profile-chip">{daten['erfahrung']}</span>
<span class="profile-chip">{daten['fuehrung']}</span>
<span class="profile-chip">{daten['international']}</span>
""",
                unsafe_allow_html=True
            )

            st.markdown("**Berufliches Kurzprofil**")
            st.write(daten["profil"])

            if st.checkbox(
                "Zur Shortlist hinzufügen",
                key=f"runde1_{name}"
            ):
                auswahl.append(name)

    nav_back, nav_forward = st.columns(2)
    with nav_back:
        if st.button("← ZURÜCK ZUM BRIEFING", key="back_phase1", use_container_width=True):
            st.session_state.phase = 0
            st.rerun()
    with nav_forward:
        if st.session_state.max_phase >= 2:
            if st.button("WEITER ZUR SHORTLIST 1.0 →", key="forward_phase1", use_container_width=True):
                st.session_state.phase = 2
                st.rerun()

    st.divider()

    st.markdown("## Shortlist 1.0")

    if len(auswahl) < 3:

        st.warning(
            f"SHORTLIST · {len(auswahl)} / 3 ausgewählt"
        )

    elif len(auswahl) > 3:

        st.error(
            "Die Shortlist kann maximal drei Personen enthalten."
        )

    else:

        st.success("✓ SHORTLIST · 3 / 3")

        for person in auswahl:
            daten = kandidaten[person]
            st.write(
                f"🎯 {daten['id']} · {daten['aktuell']}"
            )

        st.markdown("### Was hat eure Entscheidung beeinflusst?")

        ausgewaehlte_gruende = st.multiselect(
            "Mehrfachauswahl möglich",
            options=gruende,
            placeholder="Entscheidungsgründe auswählen",
            key="entscheidungsgruende"
        )

        sonstiges = ""

        if "Sonstiges" in ausgewaehlte_gruende:

            sonstiges = st.text_input(
                "Welcher weitere Grund war wichtig?",
                key="sonstiger_grund"
            )

        st.markdown("### Wie sicher seid ihr euch?")

        sicherheit = st.slider(
            "Entscheidungssicherheit",
            0,
            100,
            70,
            5,
            format="%d%%",
            key="sicherheit_runde1"
        )

        if st.button(
            "🔒 SHORTLIST 1.0 BESTÄTIGEN",
            type="primary",
            key="shortlist1_bestaetigen",
            use_container_width=True
        ):

            if not ausgewaehlte_gruende:

                st.warning(
                    "Bitte mindestens einen Entscheidungsgrund auswählen."
                )

            else:

                st.session_state.shortlist1 = auswahl.copy()
                st.session_state.gruende1 = ausgewaehlte_gruende.copy()

                if sonstiges:
                    st.session_state.gruende1.append(
                        f"Sonstiges: {sonstiges}"
                    )

                st.session_state.sicherheit1 = sicherheit
                st.session_state.phase = 2
                st.session_state.max_phase = max(st.session_state.max_phase, 2)

                st.rerun()


# ============================================================
# PHASE 2 – INTERNAL HANDOVER / PAUSE
# ============================================================

elif st.session_state.phase == 2:

    st.markdown("""
<div class="process-row">
<div class="process-inactive">01 · BRIEFING</div>
<div class="process-inactive">02 · FIRST SCREENING</div>
<div class="process-active">03 · SECOND LOOK</div>
<div class="process-inactive">04 · FINAL SHORTLIST</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="internal-header">
<div class="internal-label">INTERNAL SEARCH PROCESS</div>
<div class="internal-title">Shortlist 1.0 abgeschlossen</div>
<div class="internal-text">
Das öffentliche Profil-Screening ist beendet. Eure Vorauswahl wurde in den internen Auswahlprozess übernommen.
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("### Eure erste Entscheidung")

    for person in st.session_state.shortlist1:

        daten = kandidaten[person]

        st.markdown(
            f"""
<div class="internal-card">
<div class="candidate-id">{daten['id']}</div>
<div class="candidate-role">{daten['aktuell']}</div>
<div class="candidate-sector">{daten['branche']}</div>
</div>
""",
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ENTSCHEIDUNGSSICHERHEIT",
            f"{st.session_state.sicherheit1}%"
        )

    with col2:
        st.metric(
            "SHORTLIST",
            "3 / 3"
        )

    st.markdown("**Eure Entscheidungsgründe:**")

    for grund in st.session_state.gruende1:
        st.write("•", grund)

    st.divider()

    st.warning("""
### ⏸️ STOP

Bitte wartet auf das gemeinsame Signal.

Die nächste Phase wird nach der gemeinsamen Zwischenbesprechung gestartet.
""")

    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("← ZURÜCK ZUM FIRST SCREENING", key="back_phase2", use_container_width=True):
            st.session_state.phase = 1
            st.rerun()
    with nav2:
        if st.button(
            "WEITER ZUM SECOND LOOK  →" if st.session_state.max_phase >= 3 else "SECOND LOOK STARTEN  →",
            type="primary",
            key="interviews_oeffnen",
            use_container_width=True
        ):
            st.session_state.phase = 3
            st.session_state.max_phase = max(st.session_state.max_phase, 3)
            st.rerun()


# ============================================================
# PHASE 3 – SECOND LOOK / INTERNAL ASSESSMENT
# ============================================================

elif st.session_state.phase == 3:

    st.markdown("""
<div class="process-row">
<div class="process-inactive">01 · BRIEFING</div>
<div class="process-inactive">02 · FIRST SCREENING</div>
<div class="process-active">03 · SECOND LOOK</div>
<div class="process-inactive">04 · FINAL SHORTLIST</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="internal-header">
<div class="internal-label">INTERNAL CANDIDATE ASSESSMENT</div>
<div class="internal-title">Second Look</div>
<div class="internal-text">
Zusätzliche Informationen aus ersten Gesprächen liegen vor.
Prüft eure Einschätzung erneut.
</div>
</div>
""", unsafe_allow_html=True)

    st.caption(
        "DEMO: Die Interviewinformationen sind frei erfunden und "
        "didaktisch konstruiert."
    )

    st.write(
        "**Für den aktuellen Prototyp werden noch alle fünf Profile gezeigt. "
        "Die finale Version wird nach Marcs Praxisinput angepasst.**"
    )

    st.divider()

    auswahl2 = []

    for name, daten in kandidaten.items():

        with st.expander(
            f"{daten['id']} · {daten['aktuell']} · {daten['branche']}"
        ):

            st.markdown(
                f"""
<div class="candidate-id">{daten['id']}</div>
<div class="candidate-role">{daten['aktuell']}</div>
<div class="candidate-sector">{daten['branche']}</div>
""",
                unsafe_allow_html=True
            )

            st.markdown("**Bisher bekannte Informationen**")
            st.write(daten["profil"])

            st.markdown("**Neue Information aus dem Gespräch**")

            st.markdown(
                f"""
<div class="interview-box">
{daten['interview']}
</div>
""",
                unsafe_allow_html=True
            )

            war_vorher_dabei = (
                name in st.session_state.shortlist1
            )

            if war_vorher_dabei:
                st.caption(
                    "🎯 War auf eurer Shortlist 1.0"
                )

            if st.checkbox(
                "Für die nächste Phase vormerken",
                value=war_vorher_dabei,
                key=f"runde2_{name}"
            ):
                auswahl2.append(name)

    # Aktuellen Arbeitsstand auch dann behalten, wenn zwischendurch zurück navigiert wird.
    st.session_state["shortlist2_draft"] = auswahl2.copy()

    nav_back, nav_forward = st.columns(2)
    with nav_back:
        if st.button("← ZURÜCK", key="back_phase3", use_container_width=True):
            st.session_state.phase = 2
            st.rerun()
    with nav_forward:
        if st.session_state.max_phase >= 4:
            if st.button("WEITER ZUM DECISION REVIEW →", key="forward_phase3", use_container_width=True):
                st.session_state.phase = 4
                st.rerun()

    st.caption("Zurück/Weiter verändert eure gespeicherten Entscheidungen nicht.")

    # Navigation above replaces the old back-only block.
    nav_back = None
    nav_space = None
    st.divider()

    st.markdown("## Aktuelle Auswahl")

    if len(auswahl2) < 3:

        st.warning(
            f"{len(auswahl2)} / 3 Personen ausgewählt."
        )

    elif len(auswahl2) > 3:

        st.error(
            "Bitte genau drei Personen auswählen."
        )

    else:

        st.success("✓ 3 / 3 Personen ausgewählt.")

        for person in auswahl2:

            daten = kandidaten[person]

            st.write(
                f"🎯 {daten['id']} · {daten['aktuell']}"
            )

        if st.button(
            "AUSWAHL BESTÄTIGEN  →",
            type="primary",
            key="shortlist2_bestaetigen",
            use_container_width=True
        ):

            st.session_state.shortlist2 = auswahl2.copy()
            st.session_state.phase = 4
            st.session_state.max_phase = max(st.session_state.max_phase, 4)

            st.rerun()


# ============================================================
# PHASE 4 – DECISION REVIEW
# ============================================================

elif st.session_state.phase == 4:

    st.markdown("""
<div class="process-row">
<div class="process-inactive">01 · BRIEFING</div>
<div class="process-inactive">02 · FIRST SCREENING</div>
<div class="process-inactive">03 · SECOND LOOK</div>
<div class="process-active">04 · FINAL SHORTLIST</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="internal-header">
<div class="internal-label">DECISION REVIEW</div>
<div class="internal-title">Eure Entscheidung im Vergleich</div>
<div class="internal-text">
Vergleicht eure erste Vorauswahl mit eurer Entscheidung nach den zusätzlichen Informationen.
</div>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### SHORTLIST 1.0")

        for person in st.session_state.shortlist1:

            daten = kandidaten[person]

            st.write(
                f"🎯 {daten['id']} · {daten['aktuell']}"
            )

    with col2:

        st.markdown("### SECOND LOOK")

        for person in st.session_state.shortlist2:

            daten = kandidaten[person]

            st.write(
                f"🎯 {daten['id']} · {daten['aktuell']}"
            )

    vorher = set(st.session_state.shortlist1)
    nachher = set(st.session_state.shortlist2)

    raus = vorher - nachher
    rein = nachher - vorher

    st.divider()

    if vorher == nachher:

        st.success(
            "✓ Eure Auswahl ist gleich geblieben."
        )

        st.write(
            "Die zusätzlichen Informationen haben eure ursprüngliche "
            "Auswahl nicht verändert."
        )

    else:

        st.markdown("""
<div class="change-box">
<strong>💡 EURE ENTSCHEIDUNG HAT SICH VERÄNDERT.</strong><br>
Mindestens eine Person wurde nach den zusätzlichen Informationen anders beurteilt.
</div>
""", unsafe_allow_html=True)

        col3, col4 = st.columns(2)

        with col3:

            st.markdown("#### ↓ Nicht mehr dabei")

            for person in raus:

                daten = kandidaten[person]

                st.write(
                    f"{daten['id']} · {daten['aktuell']}"
                )

        with col4:

            st.markdown("#### ↑ Neu dabei")

            for person in rein:

                daten = kandidaten[person]

                st.write(
                    f"{daten['id']} · {daten['aktuell']}"
                )

        st.divider()

        st.markdown("### Unterschiede auf einen Blick")
        st.caption("Nur die Personen, deren Status sich verändert hat. Details könnt ihr bei Bedarf aufklappen.")

        for person in raus:
            daten = kandidaten[person]
            st.markdown(
                f"""
<div class="diff-card diff-card-out">
<div class="diff-status diff-out">↓ NICHT MEHR AUF DER SHORTLIST</div>
<div class="diff-name">{daten['id']} · {daten['aktuell']}</div>
<div class="diff-row"><div class="diff-label">First Screening</div><div class="diff-value">{daten['screening_signal']}</div></div>
<div class="diff-row"><div class="diff-label">Neue Information</div><div class="diff-value">{daten['new_signal']}</div></div>
<div class="diff-row"><div class="diff-label">Auswirkung</div><div class="diff-value diff-impact">{daten['impact']}</div></div>
</div>
""",
                unsafe_allow_html=True
            )
            with st.expander(f"Details zu {daten['id']} anzeigen"):
                st.markdown("**Information beim First Screening**")
                st.write(daten["profil"])
                st.markdown("**Zusätzliche Information aus dem Gespräch**")
                st.write(daten["interview"])

        for person in rein:
            daten = kandidaten[person]
            st.markdown(
                f"""
<div class="diff-card diff-card-in">
<div class="diff-status diff-in">↑ NEU AUF DER SHORTLIST</div>
<div class="diff-name">{daten['id']} · {daten['aktuell']}</div>
<div class="diff-row"><div class="diff-label">First Screening</div><div class="diff-value">{daten['screening_signal']}</div></div>
<div class="diff-row"><div class="diff-label">Neue Information</div><div class="diff-value">{daten['new_signal']}</div></div>
<div class="diff-row"><div class="diff-label">Auswirkung</div><div class="diff-value diff-impact">{daten['impact']}</div></div>
</div>
""",
                unsafe_allow_html=True
            )
            with st.expander(f"Details zu {daten['id']} anzeigen"):
                st.markdown("**Information beim First Screening**")
                st.write(daten["profil"])
                st.markdown("**Zusätzliche Information aus dem Gespräch**")
                st.write(daten["interview"])

    nav_back, nav_forward = st.columns(2)
    with nav_back:
        if st.button("← ZURÜCK ZUM SECOND LOOK", key="back_phase4", use_container_width=True):
            st.session_state.phase = 3
            st.rerun()
    with nav_forward:
        if st.session_state.max_phase >= 5:
            if st.button("WEITER ZUM ABSCHLUSS →", key="forward_phase4", use_container_width=True):
                st.session_state.phase = 5
                st.rerun()

    st.divider()

    st.markdown("### Was hat eure Entscheidung beeinflusst?")

    ausgewaehlte_gruende2 = st.multiselect(
        "Welche Informationen oder Überlegungen waren ausschlaggebend?",
        options=gruende2,
        placeholder="Entscheidungsgründe auswählen",
        key="entscheidungsgruende2"
    )

    sonstiges2 = ""

    if "Sonstiges" in ausgewaehlte_gruende2:

        sonstiges2 = st.text_input(
            "Welcher weitere Grund war wichtig?",
            key="sonstiger_grund2"
        )

    if st.button(
        "AUSWAHLPROZESS ABSCHLIESSEN  →",
        type="primary",
        key="prozess_abschliessen",
        use_container_width=True
    ):

        if not ausgewaehlte_gruende2:

            st.warning(
                "Bitte mindestens einen Entscheidungsgrund auswählen."
            )

        else:

            st.session_state.gruende2 = (
                ausgewaehlte_gruende2.copy()
            )

            if sonstiges2:

                st.session_state.gruende2.append(
                    f"Sonstiges: {sonstiges2}"
                )

            st.session_state.phase = 5
            st.session_state.max_phase = max(st.session_state.max_phase, 5)
            st.rerun()


# ============================================================
# PHASE 5 – SEARCH COMPLETED
# ============================================================

elif st.session_state.phase == 5:

    st.markdown("""
<div class="complete-box">
<div class="complete-small">EXECUTIVE SEARCH SIMULATION</div>
<div class="complete-title">✓ SEARCH COMPLETED</div>
<div class="complete-text">
Der Auswahlprozess der Simulation ist abgeschlossen.
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("## Eure finale Auswahl")

    for person in st.session_state.shortlist2:

        daten = kandidaten[person]

        st.markdown(
            f"""
<div class="internal-card">
<div class="candidate-id">{daten['id']}</div>
<div class="candidate-role">{daten['aktuell']}</div>
<div class="candidate-sector">{daten['branche']}</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.info(
        "Die Ergebnisse werden jetzt gemeinsam ausgewertet."
    )

    st.markdown(
        "## → Zurück zur gemeinsamen Präsentation"
    )

    st.caption(
        "MISSION: EXECUTIVE SEARCH · Simulation abgeschlossen"
    )

    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("← ZURÜCK ZUM DECISION REVIEW", key="back_phase5", use_container_width=True):
            st.session_state.phase = 4
            st.rerun()

    with nav2:
        restart_demo = st.button(
        "↻ DEMO NEU STARTEN",
        key="demo_neustart",
        use_container_width=True
        )

    if restart_demo:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
