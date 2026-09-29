import streamlit as st
import streamlit.components.v1 as components
# ============================================================
# PHASE 0 – START
# ============================================================

if st.session_state.phase == 0:

    st.markdown("""
    <div class="exec-header">

        <div class="exec-eyebrow">
            EXECUTIVE SEARCH SIMULATION
        </div>

        <div class="exec-title">
            MISSION: EXECUTIVE SEARCH
        </div>

        <div class="exec-subtitle">
            Ihr übernehmt einen vertraulichen Suchauftrag
            für eine strategisch wichtige Führungsposition.
        </div>

        <div class="confidential">
            ● CONFIDENTIAL SEARCH MANDATE
        </div>

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

        <div class="card-label">
            SEARCH MANDATE
        </div>

        <div class="position-title">
            Managing Director Austria
        </div>

        <div class="position-meta">
            Internationales Unternehmen · Marktausbau Österreich
            · Executive Leadership
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="mission-box">

        <div class="mission-title">
            EURE MISSION
        </div>

        <div class="mission-text">
            Das Executive-Search-Team hat fünf potenzielle
            Kandidat:innen identifiziert.<br><br>

            Sichtet die verfügbaren Profile und erstellt eine
            <strong>Shortlist mit genau drei Personen.</strong><br><br>

            Die erste Sichtung erfolgt bewusst schnell –
            ähnlich einer ersten Vorauswahl im Executive Search.
        </div>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "KANDIDAT:INNEN",
            "5"
        )

    with col2:
        st.metric(
            "SHORTLIST",
            "3"
        )

    with col3:
        st.metric(
            "SCREENING-ZEIT",
            "90 Sek."
        )

    st.write("")

    if st.button(
        "START FIRST SCREENING  →",
        type="primary",
        key="start_mission",
        use_container_width=True
    ):
        st.session_state.phase = 1
        st.rerun()

    st.caption(
        "Demo-Prototyp · Alle Unternehmen, Personen und Angaben "
        "dieser Simulation sind frei erfunden."
    )

# ============================================================
# DESIGN – EXECUTIVE SEARCH
# ============================================================

st.markdown("""
<style>

/* Gesamte App */
.stApp {
    background-color: #f4f6f8;
}

/* Hauptbereich etwas kompakter */
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Standard-Überschrift oben ausblenden wir später über eigene Header */
h1, h2, h3 {
    letter-spacing: -0.02em;
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    font-weight: 700;
    padding: 0.65rem 1.2rem;
}

/* Executive Search Header */
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
    max-width: 720px;
}

/* Confidential Badge */
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

/* Search Mandate */
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

/* Mission Box */
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

/* Ablauf */
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

</style>
""", unsafe_allow_html=True)
# ============================================================
# DEMO-DATEN – ALLES FREI ERFUNDEN
# ============================================================

kandidaten = {
    "Kandidat A – Der Branchenprofi": {
        "aktuell": "Regional Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "16 Jahre Berufserfahrung",
        "fuehrung": "9 Jahre Führungserfahrung",
        "international": "Deutschland, Österreich, Schweiz",
        "profil": "Langjährige Tätigkeit bei zwei großen Finanzdienstleistern. "
                  "Seit fünf Jahren Leitung einer regionalen Geschäftseinheit mit rund 120 Mitarbeitenden.",
        "interview": "Im Gespräch wird deutlich: Der Kandidat übernahm seine bisherigen "
                     "Führungsbereiche jeweils in bereits etablierten Strukturen. Einen neuen "
                     "Standort oder eine neue Geschäftseinheit hat er bisher nicht selbst aufgebaut."
    },

    "Kandidatin B – Die Aufbau-Expertin": {
        "aktuell": "Managing Director",
        "branche": "Technologie",
        "erfahrung": "13 Jahre Berufserfahrung",
        "fuehrung": "7 Jahre Führungserfahrung",
        "international": "Österreich, Polen, Tschechien",
        "profil": "Begleitete mehrere Expansionsprojekte und war zuletzt für den Aufbau "
                  "einer neuen Geschäftseinheit in Zentral- und Osteuropa verantwortlich.",
        "interview": "Im Gespräch konkretisiert sie ihre Rolle: Sie verantwortete den Aufbau "
                     "einer neuen Einheit von der Personalgewinnung bis zur Etablierung operativer "
                     "Strukturen. Direkte Erfahrung in der Finanzdienstleistungsbranche hat sie nicht."
    },

    "Kandidat C – Der internationale Manager": {
        "aktuell": "Vice President Operations",
        "branche": "Industrie",
        "erfahrung": "18 Jahre Berufserfahrung",
        "fuehrung": "11 Jahre Führungserfahrung",
        "international": "Europa, USA, Asien",
        "profil": "Internationale Führungslaufbahn mit Verantwortung für mehrere Standorte. "
                  "Langjährige Erfahrung in globalen Unternehmensstrukturen.",
        "interview": "Im Gespräch zeigt sich: Seine internationale Verantwortung bezog sich "
                     "vor allem auf die Steuerung bereits bestehender Standorte. Bei deren Aufbau "
                     "war er selbst nicht beteiligt."
    },

    "Kandidatin D – Die unauffällige Kandidatin": {
        "aktuell": "Head of Operations",
        "branche": "Finanznahe Dienstleistungen",
        "erfahrung": "12 Jahre Berufserfahrung",
        "fuehrung": "5 Jahre Führungserfahrung",
        "international": "Österreich, Slowenien",
        "profil": "Karriere überwiegend bei mittelständischen Unternehmen. "
                  "Verantwortung für operative Teams und mehrere interne Veränderungsprojekte.",
        "interview": "Im Gespräch wird eine Information sichtbar, die aus dem Kurzprofil kaum "
                     "hervorging: Sie war beim Eintritt in ihr aktuelles Unternehmen maßgeblich "
                     "am Aufbau eines neuen österreichischen Standorts beteiligt und übernahm "
                     "dort schrittweise Führungsverantwortung."
    },

    "Kandidat E – Der perfekte Lebenslauf?": {
        "aktuell": "Country Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "17 Jahre Berufserfahrung",
        "fuehrung": "10 Jahre Führungserfahrung",
        "international": "Deutschland, Schweiz, Großbritannien",
        "profil": "Führungspositionen bei mehreren international bekannten Unternehmen. "
                  "Verantwortung für große Teams und strategische Wachstumsprojekte.",
        "interview": "Im Gespräch wird deutlich: Die strategischen Wachstumsprojekte wurden "
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

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "phase": 0,
    "shortlist1": [],
    "shortlist2": [],
    "gruende1": [],
    "sicherheit1": 70
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# KOPF
# ============================================================

st.title("MISSION: EXECUTIVE SEARCH")

st.caption(
    "DEMO-PROTOTYP · Alle Unternehmen, Personen und Angaben sind frei erfunden."
)


# ============================================================
# PHASE 0 – START
# ============================================================

if st.session_state.phase == 0:

    st.subheader("🔒 VERTRAULICHER SUCHAUFTRAG")

    st.markdown("""
### Neue Führung für einen strategisch wichtigen Standort

Ein international tätiges Unternehmen baut seine Präsenz in Österreich aus
und sucht eine neue Führungskraft für die Position:

## **Managing Director Austria**

Das Executive-Search-Team hat fünf potenzielle Kandidat:innen identifiziert.

### Eure Mission

Erstellt aus den fünf Profilen eine **Shortlist mit genau drei Personen**.

Die erste Sichtung erfolgt bewusst schnell – ähnlich einer ersten
Vorauswahl im Executive Search.

Sobald ihr die Suche startet, habt ihr **90 Sekunden Zeit**.
""")

    if st.button(
        "🎯 Suche starten",
        type="primary",
        key="start_mission"
    ):
        st.session_state.phase = 1
        st.rerun()


# ============================================================
# PHASE 1 – SCHNELLSCREENING / SHORTLIST 1.0
# ============================================================

elif st.session_state.phase == 1:

    st.info("🔒 CONFIDENTIAL SEARCH MANDATE")

    # Countdown – UNVERÄNDERT AUS DEINEM CODE
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

    st.subheader("Anforderungsprofil")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**MUST-HAVES**

✓ Mehrjährige Führungserfahrung  
✓ Erfahrung mit Wachstum, Aufbau oder Expansion  
✓ Erfahrung in komplexen Unternehmensstrukturen
""")

    with col2:
        st.markdown("""
**NICE-TO-HAVES**

✓ Internationale Erfahrung  
✓ Kenntnisse der Finanzdienstleistungsbranche
""")

    st.divider()

    st.subheader("FIRST SCREENING")

    st.write(
        "Prüft die verfügbaren Informationen möglichst zügig. "
        "**Welche drei Personen nehmt ihr in die nächste Phase auf?**"
    )

    auswahl = []

    for name, daten in kandidaten.items():

        with st.expander(name):

            c1, c2 = st.columns(2)

            with c1:
                st.write("**Aktuelle Position:**", daten["aktuell"])
                st.write("**Branche:**", daten["branche"])
                st.write("**Berufserfahrung:**", daten["erfahrung"])

            with c2:
                st.write("**Führung:**", daten["fuehrung"])
                st.write("**International:**", daten["international"])

            st.write("**Kurzprofil**")
            st.write(daten["profil"])

            if st.checkbox(
                "Auf meine Shortlist",
                key=f"runde1_{name}"
            ):
                auswahl.append(name)

    st.divider()

    st.subheader("Eure Shortlist 1.0")

    if len(auswahl) < 3:

        st.warning(
            f"Ihr habt {len(auswahl)} von 3 Personen ausgewählt."
        )

    elif len(auswahl) > 3:

        st.error(
            "Bitte genau drei Personen auswählen."
        )

    else:

        st.success("✓ Drei Personen ausgewählt.")

        for person in auswahl:
            st.write("🎯", person)

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
            "🔒 Shortlist 1.0 bestätigen",
            type="primary",
            key="shortlist1_bestaetigen"
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

                st.rerun()


# ============================================================
# PHASE 2 – SHORTLIST 1.0 / PAUSE
# ============================================================

elif st.session_state.phase == 2:

    st.success("✓ SHORTLIST 1.0 ABGESCHLOSSEN")

    st.markdown("### Eure erste Entscheidung")

    for person in st.session_state.shortlist1:
        st.write("🎯", person)

    st.write(
        f"**Entscheidungssicherheit:** "
        f"{st.session_state.sicherheit1}%"
    )

    st.markdown("**Entscheidungsgründe:**")

    for grund in st.session_state.gruende1:
        st.write("•", grund)

    st.divider()

    st.warning("""
### ⏸️ STOP

Bitte wartet auf das gemeinsame Signal.

Die nächsten Informationen werden erst nach der gemeinsamen
Zwischenphase freigegeben.
""")

    if st.button(
        "🎙️ SECOND LOOK starten",
        type="primary",
        key="interviews_oeffnen"
    ):
        st.session_state.phase = 3
        st.rerun()


# ============================================================
# PHASE 3 – SHORTLIST 2.0
# ============================================================

elif st.session_state.phase == 3:

    st.subheader("🎙️ SECOND LOOK")

    st.write("""
Ihr habt nun zusätzliche Informationen aus ersten Gesprächen.

Prüft alle fünf Kandidat:innen erneut.

**Welche drei Personen nehmt ihr jetzt in die nächste Phase auf?**
""")

    st.caption(
        "Die Interviewinformationen sind für diese Demo "
        "frei erfunden und didaktisch konstruiert."
    )

    st.divider()

    auswahl2 = []

    for name, daten in kandidaten.items():

        with st.expander(name):

            st.markdown("#### Bisher bekannte Informationen")

            c1, c2 = st.columns(2)

            with c1:
                st.write("**Aktuelle Position:**", daten["aktuell"])
                st.write("**Branche:**", daten["branche"])
                st.write("**Berufserfahrung:**", daten["erfahrung"])

            with c2:
                st.write("**Führung:**", daten["fuehrung"])
                st.write("**International:**", daten["international"])

            st.write("**Kurzprofil:**")
            st.write(daten["profil"])

            st.markdown("#### 🔓 NEUE INTERVIEWINFORMATION")

            st.info(daten["interview"])

            war_vorher_dabei = (
                name in st.session_state.shortlist1
            )

            if war_vorher_dabei:
                st.caption(
                    "🎯 Diese Person war auf eurer Shortlist 1.0."
                )

            if st.checkbox(
                "Auf meine Shortlist 2.0",
                value=war_vorher_dabei,
                key=f"runde2_{name}"
            ):
                auswahl2.append(name)

    st.divider()

    st.subheader("Eure Shortlist 2.0")

    if len(auswahl2) < 3:

        st.warning(
            f"Ihr habt {len(auswahl2)} von 3 Personen ausgewählt."
        )

    elif len(auswahl2) > 3:

        st.error(
            "Bitte genau drei Personen auswählen."
        )

    else:

        st.success("✓ Drei Personen ausgewählt.")

        for person in auswahl2:
            st.write("🎯", person)

        if st.button(
            "🎯 Shortlist 2.0 bestätigen",
            type="primary",
            key="shortlist2_bestaetigen"
        ):

            st.session_state.shortlist2 = auswahl2.copy()
            st.session_state.phase = 4

            st.rerun()


# ============================================================
# PHASE 4 – VERGLEICH / AHA
# ============================================================

elif st.session_state.phase == 4:

    st.subheader("🔍 EURE ENTSCHEIDUNG IM VERGLEICH")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### SHORTLIST 1.0")

        for person in st.session_state.shortlist1:
            st.write("🎯", person)

    with col2:

        st.markdown("### SHORTLIST 2.0")

        for person in st.session_state.shortlist2:
            st.write("🎯", person)

    vorher = set(st.session_state.shortlist1)
    nachher = set(st.session_state.shortlist2)

    raus = vorher - nachher
    rein = nachher - vorher

    st.divider()

    if vorher == nachher:

        st.success("""
### Eure Shortlist ist gleich geblieben.

Die zusätzlichen Informationen haben eure ursprüngliche
Auswahl nicht verändert.
""")

    else:

        st.warning(
            "💡 EURE ENTSCHEIDUNG HAT SICH VERÄNDERT."
        )

        col3, col4 = st.columns(2)

        with col3:

            st.markdown("#### ↓ Nicht mehr auf der Shortlist")

            for person in raus:
                st.write(person)

        with col4:

            st.markdown("#### ↑ Neu auf der Shortlist")

            for person in rein:
                st.write(person)

        st.divider()

        st.markdown("### Was war anders?")

        # Nur die Kandidat:innen zeigen,
        # die tatsächlich ausgetauscht wurden.
        for person in raus:

            daten = kandidaten[person]

            st.markdown(f"#### ↓ {person}")

            st.write("**Information beim First Screening:**")
            st.write(daten["profil"])

            st.write("**Zusätzliche Information aus dem Gespräch:**")
            st.info(daten["interview"])

        for person in rein:

            daten = kandidaten[person]

            st.markdown(f"#### ↑ {person}")

            st.write("**Information beim First Screening:**")
            st.write(daten["profil"])

            st.write("**Zusätzliche Information aus dem Gespräch:**")
            st.info(daten["interview"])

    st.divider()

 st.markdown("### Was hat eure Entscheidung beeinflusst?")

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

ausgewaehlte_gruende2 = st.multiselect(
    "Welche Informationen oder Überlegungen waren für eure zweite Entscheidung ausschlaggebend?",
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
    "✓ Auswahlprozess abschließen",
    type="primary",
    key="prozess_abschliessen"
):

    if not ausgewaehlte_gruende2:
        st.warning(
            "Bitte mindestens einen Entscheidungsgrund auswählen."
        )

    else:
        st.session_state.gruende2 = ausgewaehlte_gruende2.copy()

        if sonstiges2:
            st.session_state.gruende2.append(
                f"Sonstiges: {sonstiges2}"
            )

        st.session_state.phase = 5
        st.rerun()


# ============================================================
# PHASE 5 – ABSCHLUSS DER SIMULATION
# ============================================================

elif st.session_state.phase == 5:

    st.markdown("# ✓ SEARCH COMPLETED")

    st.markdown("""
## Eure finale Shortlist steht.

Der Auswahlprozess in der Simulation ist damit abgeschlossen.
""")

    st.divider()

    st.markdown("### FINAL SHORTLIST")

    for person in st.session_state.shortlist2:
        st.write("🎯", person)

    st.divider()

    st.info("""
### Bitte bleibt bei eurer Entscheidung.

Die Ergebnisse werden jetzt gemeinsam ausgewertet.
""")

    st.markdown("## → Zurück zur gemeinsamen Präsentation")

    st.caption(
        "MISSION: EXECUTIVE SEARCH · Simulation abgeschlossen"
    )

    if st.button(
        "↻ Demo neu starten",
        key="demo_neustart"
    ):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()
