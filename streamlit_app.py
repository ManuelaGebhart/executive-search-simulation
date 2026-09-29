import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Executive Search Simulation",
    page_icon="🎯",
    layout="wide"
)

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

    veraenderungsgrund = st.text_area(
        "Welche neue Information oder Überlegung war für euch ausschlaggebend?",
        placeholder="Kurz festhalten ...",
        key="veraenderungsgrund"
    )

    if st.button(
        "✓ Auswahlprozess abschließen",
        type="primary",
        key="prozess_abschliessen"
    ):
        st.session_state.veraenderungsgrund = veraenderungsgrund
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
