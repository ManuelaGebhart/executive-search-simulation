import streamlit as st
import time

st.set_page_config(
    page_title="Executive Search Simulation",
    page_icon="🎯",
    layout="wide"
)

# ============================================================
# DEMO-DATEN
# ============================================================

kandidaten = {
    "Kandidat A – Der Branchenprofi": {
        "aktuell": "Regional Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "16 Jahre Berufserfahrung",
        "fuehrung": "9 Jahre Führungserfahrung",
        "international": "Deutschland, Österreich, Schweiz",
        "profil": (
            "Langjährige Tätigkeit bei zwei großen Finanzdienstleistern. "
            "Seit fünf Jahren Leitung einer regionalen Geschäftseinheit "
            "mit rund 120 Mitarbeitenden."
        ),
        "interview": (
            "Im Gespräch wird deutlich: Der Kandidat übernahm seine "
            "bisherigen Führungsbereiche jeweils in bereits etablierten "
            "Strukturen. Einen neuen Standort oder eine neue Geschäftseinheit "
            "hat er bisher nicht selbst aufgebaut."
        )
    },

    "Kandidatin B – Die Aufbau-Expertin": {
        "aktuell": "Managing Director",
        "branche": "Technologie",
        "erfahrung": "13 Jahre Berufserfahrung",
        "fuehrung": "7 Jahre Führungserfahrung",
        "international": "Österreich, Polen, Tschechien",
        "profil": (
            "Begleitete mehrere Expansionsprojekte und war zuletzt für den "
            "Aufbau einer neuen Geschäftseinheit in Zentral- und Osteuropa "
            "verantwortlich."
        ),
        "interview": (
            "Im Gespräch konkretisiert sie ihre Rolle: Sie verantwortete den "
            "Aufbau einer neuen Einheit von der Personalgewinnung bis zur "
            "Etablierung operativer Strukturen. Direkte Erfahrung in der "
            "Finanzdienstleistungsbranche hat sie nicht."
        )
    },

    "Kandidat C – Der internationale Manager": {
        "aktuell": "Vice President Operations",
        "branche": "Industrie",
        "erfahrung": "18 Jahre Berufserfahrung",
        "fuehrung": "11 Jahre Führungserfahrung",
        "international": "Europa, USA, Asien",
        "profil": (
            "Internationale Führungslaufbahn mit Verantwortung für mehrere "
            "Standorte. Langjährige Erfahrung in globalen Unternehmensstrukturen."
        ),
        "interview": (
            "Im Gespräch zeigt sich: Seine internationale Verantwortung bezog "
            "sich vor allem auf die Steuerung bereits bestehender Standorte. "
            "Bei deren Aufbau war er selbst nicht beteiligt."
        )
    },

    "Kandidatin D – Die unauffällige Kandidatin": {
        "aktuell": "Head of Operations",
        "branche": "Finanznahe Dienstleistungen",
        "erfahrung": "12 Jahre Berufserfahrung",
        "fuehrung": "5 Jahre Führungserfahrung",
        "international": "Österreich, Slowenien",
        "profil": (
            "Karriere überwiegend bei mittelständischen Unternehmen. "
            "Verantwortung für operative Teams und mehrere interne "
            "Veränderungsprojekte."
        ),
        "interview": (
            "Im Gespräch wird eine Information sichtbar, die aus dem Kurzprofil "
            "kaum hervorging: Sie war beim Eintritt in ihr aktuelles Unternehmen "
            "maßgeblich am Aufbau eines neuen österreichischen Standorts beteiligt "
            "und übernahm dort schrittweise Führungsverantwortung."
        )
    },

    "Kandidat E – Der perfekte Lebenslauf?": {
        "aktuell": "Country Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "17 Jahre Berufserfahrung",
        "fuehrung": "10 Jahre Führungserfahrung",
        "international": "Deutschland, Schweiz, Großbritannien",
        "profil": (
            "Führungspositionen bei mehreren international bekannten Unternehmen. "
            "Verantwortung für große Teams und strategische Wachstumsprojekte."
        ),
        "interview": (
            "Im Gespräch wird deutlich: Die strategischen Wachstumsprojekte wurden "
            "zentral vorbereitet. Seine Verantwortung lag vor allem in der Umsetzung "
            "bereits definierter Konzepte und in der Führung bestehender Organisationen."
        )
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
    "sicherheit1": 70,
    "screening_start": None,
    "screening_locked": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def reset_demo():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


def kandidatenkarte(name, daten, interview=False):
    st.markdown(f"### {name}")

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

    if interview:
        st.markdown("#### 🔓 Neue Information aus dem Erstgespräch")
        st.info(daten["interview"])


# ============================================================
# HEADER
# ============================================================

st.title("MISSION: EXECUTIVE SEARCH")

st.caption(
    "DEMO-PROTOTYP · Alle Personen, Unternehmen und Angaben "
    "dieser Simulation sind frei erfunden."
)


# ============================================================
# PHASE 0 – SUCHAUFTRAG
# ============================================================

if st.session_state.phase == 0:

    st.subheader("🔒 VERTRAULICHER SUCHAUFTRAG")

    st.markdown("""
### Neue Führung für einen strategisch wichtigen Standort

Ein international tätiges Unternehmen baut seine Präsenz in Österreich aus
und sucht eine neue Führungskraft:

## **Managing Director Austria**

Das Executive-Search-Team hat fünf potenzielle Kandidat:innen identifiziert.

### Eure Aufgabe

Sichtet die Profile und erstellt eine **Shortlist mit genau drei Personen**.

Die erste Sichtung erfolgt bewusst unter Zeitdruck.

**90 Sekunden FIRST SCREENING**

danach

**15 Sekunden FINAL DECISION**

Anschließend wird eure Auswahl fixiert.
""")

    if st.button(
        "🎯 Suche starten",
        type="primary",
        key="start_mission"
    ):
        st.session_state.screening_start = time.time()
        st.session_state.phase = 1
        st.rerun()


# ============================================================
# PHASE 1 – FIRST SCREENING
# ============================================================

elif st.session_state.phase == 1:

    if st.session_state.screening_start is None:
        st.session_state.screening_start = time.time()

    @st.fragment(run_every="1s")
    def screening_fragment():

        elapsed = time.time() - st.session_state.screening_start

        # ----------------------------------------------------
        # ZEITPHASEN
        # ----------------------------------------------------

        if elapsed < 90:
            remaining = max(0, 90 - int(elapsed))
            mode = "screening"

        elif elapsed < 105:
            remaining = max(0, 105 - int(elapsed))
            mode = "final"

        else:
            remaining = 0
            mode = "locked"
            st.session_state.screening_locked = True

        # ----------------------------------------------------
        # COUNTDOWN
        # ----------------------------------------------------

        if mode == "screening":

            if remaining > 20:

                st.markdown(
                    f"""
                    <div style="
                        padding:18px;
                        border-radius:12px;
                        background:#eef4ff;
                        text-align:center;
                        margin-bottom:20px;
                    ">
                        <div style="
                            font-size:15px;
                            font-weight:700;
                            letter-spacing:1px;
                        ">
                            FIRST SCREENING
                        </div>

                        <div style="
                            font-size:42px;
                            font-weight:800;
                            margin-top:4px;
                        ">
                            {remaining}
                        </div>

                        <div style="font-size:14px;">
                            SEKUNDEN
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div style="
                        padding:20px;
                        border-radius:12px;
                        background:#ffe8e8;
                        border:2px solid #d60000;
                        text-align:center;
                        margin-bottom:20px;
                    ">
                        <div style="
                            color:#b00000;
                            font-size:17px;
                            font-weight:800;
                        ">
                            ⚠ FIRST SCREENING
                        </div>

                        <div style="
                            color:#d00000;
                            font-size:55px;
                            font-weight:900;
                        ">
                            {remaining}
                        </div>

                        <div style="
                            color:#b00000;
                            font-weight:700;
                        ">
                            SEKUNDEN VERBLEIBEN
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        elif mode == "final":

            st.markdown(
                f"""
                <div style="
                    padding:25px;
                    border-radius:12px;
                    background:#ffdede;
                    border:3px solid #c40000;
                    text-align:center;
                    margin-bottom:20px;
                ">

                    <div style="
                        color:#a00000;
                        font-size:22px;
                        font-weight:900;
                        letter-spacing:1px;
                    ">
                        🚨 FINAL DECISION
                    </div>

                    <div style="
                        color:#c00000;
                        font-size:70px;
                        font-weight:900;
                        line-height:1.1;
                    ">
                        {remaining}
                    </div>

                    <div style="
                        color:#a00000;
                        font-size:16px;
                        font-weight:800;
                    ">
                        SEKUNDEN
                    </div>

                    <div style="
                        margin-top:10px;
                        font-weight:700;
                    ">
                        Legt jetzt eure endgültigen drei Personen fest.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div style="
                    padding:22px;
                    border-radius:12px;
                    background:#eeeeee;
                    border:2px solid #555555;
                    text-align:center;
                    margin-bottom:20px;
                ">
                    <div style="
                        font-size:23px;
                        font-weight:900;
                    ">
                        🔒 AUSWAHL FIXIERT
                    </div>

                    <div style="margin-top:5px;">
                        Die Entscheidungszeit ist abgelaufen.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # ANFORDERUNGSPROFIL
        # ----------------------------------------------------

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

        if mode == "screening":
            st.write(
                "**Welche drei Personen nehmt ihr in die nächste Phase auf?**"
            )

        elif mode == "final":
            st.write(
                "**FINAL DECISION: Prüft nur noch eure Auswahl und legt drei Personen fest.**"
            )

        else:
            st.write(
                "**Die Auswahl kann nicht mehr verändert werden.**"
            )

        # ----------------------------------------------------
        # KANDIDAT:INNEN
        # ----------------------------------------------------

        for name, daten in kandidaten.items():

            with st.expander(name):

                kandidatenkarte(name, daten)

                st.checkbox(
                    "Auf meine Shortlist",
                    key=f"runde1_{name}",
                    disabled=(mode == "locked")
                )

        # ----------------------------------------------------
        # NACH ABLAUF
        # ----------------------------------------------------

        if mode == "locked":

            auswahl = []

            for name in kandidaten:
                if st.session_state.get(f"runde1_{name}", False):
                    auswahl.append(name)

            st.divider()

            st.subheader("🔒 Eure fixierte Vorauswahl")

            if len(auswahl) == 3:

                st.success("✓ Drei Personen ausgewählt.")

                for person in auswahl:
                    st.write("🎯", person)

                st.markdown(
                    "### Was hat eure Entscheidung beeinflusst?"
                )

                ausgewaehlte_gruende = st.multiselect(
                    "Mehrfachauswahl möglich",
                    options=gruende,
                    key="entscheidungsgruende"
                )

                sonstiges = ""

                if "Sonstiges" in ausgewaehlte_gruende:

                    sonstiges = st.text_input(
                        "Welcher weitere Grund war wichtig?",
                        key="sonstiger_grund"
                    )

                st.markdown(
                    "### Wie sicher seid ihr euch?"
                )

                sicherheit = st.slider(
                    "Entscheidungssicherheit",
                    min_value=0,
                    max_value=100,
                    value=70,
                    step=5,
                    format="%d%%",
                    key="sicherheit_runde1"
                )

                if st.button(
                    "Shortlist 1.0 speichern",
                    type="primary",
                    key="shortlist1_speichern"
                ):

                    if not ausgewaehlte_gruende:

                        st.warning(
                            "Bitte mindestens einen Entscheidungsgrund auswählen."
                        )

                    else:

                        st.session_state.shortlist1 = auswahl.copy()
                        st.session_state.gruende1 = (
                            ausgewaehlte_gruende.copy()
                        )

                        if sonstiges:
                            st.session_state.gruende1.append(
                                f"Sonstiges: {sonstiges}"
                            )

                        st.session_state.sicherheit1 = sicherheit
                        st.session_state.phase = 2

                        st.rerun()

            else:

                st.warning(
                    f"Ihr habt **{len(auswahl)} Personen** ausgewählt. "
                    "Für die Simulation werden genau drei benötigt."
                )

                st.write(
                    "Die Entscheidungszeit ist beendet. "
                    "Startet die Runde bitte erneut."
                )

                if st.button(
                    "↻ First Screening neu starten",
                    key="screening_restart"
                ):
                    reset_demo()

    screening_fragment()


# ============================================================
# PHASE 2 – SHORTLIST 1.0 / STOP
# ============================================================

elif st.session_state.phase == 2:

    st.success("✓ SHORTLIST 1.0 GESPEICHERT")

    st.subheader("Eure erste Vorauswahl")

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

    st.markdown("""
### ⏸️ STOP

Bitte wartet auf das Signal der Lehrenden.

Die neuen Informationen werden gemeinsam freigegeben.
""")

    st.divider()

    # WICHTIG:
    # Button für Runde 2 wieder klar sichtbar
    if st.button(
        "🔓 SECOND LOOK starten",
        type="primary",
        key="second_look_start"
    ):
        st.session_state.phase = 3
        st.rerun()


# ============================================================
# PHASE 3 – SECOND LOOK
# ============================================================

elif st.session_state.phase == 3:

    st.subheader("🔓 SECOND LOOK")

    st.markdown("""
### Neue Informationen liegen vor

Mit den Kandidat:innen wurden erste Gespräche geführt.

Ihr erhaltet jetzt zusätzliche Informationen, die beim
ersten Screening noch nicht verfügbar waren.

### Eure Aufgabe

Prüft **alle Kandidat:innen erneut** und erstellt eine neue
Shortlist mit **genau drei Personen**.
""")

    st.caption(
        "Alle Interviewinformationen dieser Demo sind frei erfunden "
        "und didaktisch konstruiert."
    )

    st.divider()

    auswahl2 = []

    for name, daten in kandidaten.items():

        with st.expander(name):

            kandidatenkarte(
                name,
                daten,
                interview=True
            )

            war_vorher_dabei = (
                name in st.session_state.shortlist1
            )

            if war_vorher_dabei:
                st.caption(
                    "🎯 War auf eurer Shortlist 1.0"
                )

            if st.checkbox(
                "Auf meine Shortlist 2.0",
                value=war_vorher_dabei,
                key=f"runde2_{name}"
            ):
                auswahl2.append(name)

    st.divider()

    st.subheader("Shortlist 2.0")

    if len(auswahl2) < 3:

        st.warning(
            f"Noch {3 - len(auswahl2)} Person(en) auswählen."
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
            "Shortlist 2.0 übermitteln",
            type="primary",
            key="shortlist2_bestaetigen"
        ):
            st.session_state.shortlist2 = auswahl2.copy()
            st.session_state.phase = 4
            st.rerun()


# ============================================================
# PHASE 4 – VERGLEICH
# ============================================================

elif st.session_state.phase == 4:

    st.subheader("EURE ENTSCHEIDUNG IM VERGLEICH")

    vorher = set(st.session_state.shortlist1)
    nachher = set(st.session_state.shortlist2)

    raus = vorher - nachher
    rein = nachher - vorher

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### SHORTLIST 1.0")

        for person in st.session_state.shortlist1:
            st.write("🎯", person)

    with col2:

        st.markdown("### SHORTLIST 2.0")

        for person in st.session_state.shortlist2:
            st.write("🎯", person)

    st.divider()

    if vorher == nachher:

        st.success(
            "### Eure Shortlist ist unverändert."
        )

        st.write(
            "Die zusätzlichen Informationen haben nicht dazu geführt, "
            "dass ihr eine andere Person aufgenommen habt."
        )

    else:

        st.warning(
            "### Eure Entscheidung hat sich verändert."
        )

        if raus:

            st.markdown(
                "## ↓ Nicht mehr auf der Shortlist"
            )

            for person in raus:

                daten = kandidaten[person]

                st.markdown(f"### {person}")

                st.markdown(
                    "**Information beim First Screening**"
                )
                st.write(daten["profil"])

                st.markdown(
                    "**Neue Information aus dem Gespräch**"
                )
                st.info(daten["interview"])

                st.divider()

        if rein:

            st.markdown(
                "## ↑ Neu auf der Shortlist"
            )

            for person in rein:

                daten = kandidaten[person]

                st.markdown(f"### {person}")

                st.markdown(
                    "**Information beim First Screening**"
                )
                st.write(daten["profil"])

                st.markdown(
                    "**Neue Information aus dem Gespräch**"
                )
                st.info(daten["interview"])

                st.divider()

    st.markdown(
        "### Was hat eure Entscheidung beeinflusst?"
    )

    veraenderungsgrund = st.text_area(
        "Welche neue Information oder Überlegung war ausschlaggebend?",
        placeholder="Zum Beispiel: Die zusätzliche Information über ...",
        key="veraenderungsgrund"
    )

    if st.button(
        "✓ Auswahlprozess abschließen",
        type="primary",
        key="prozess_abschliessen"
    ):

        st.session_state["veraenderungsgrund_final"] = (
            veraenderungsgrund
        )

        st.session_state.phase = 5
        st.rerun()


# ============================================================
# PHASE 5 – ENDE
# ============================================================

elif st.session_state.phase == 5:

    st.markdown("# ✓ SEARCH COMPLETED")

    st.markdown("""
## Eure Shortlist 2.0 wurde übermittelt.

Der Auswahlprozess in der Simulation ist abgeschlossen.
""")

    st.divider()

    for person in st.session_state.shortlist2:
        st.markdown(f"### 🎯 {person}")

    st.divider()

    st.info("""
### Bitte bleibt bei eurer Entscheidung.

Die Ergebnisse werden jetzt gemeinsam ausgewertet.
""")

    st.markdown(
        "## → Zurück zur gemeinsamen Präsentation"
    )

    st.caption(
        "MISSION: EXECUTIVE SEARCH · Simulation abgeschlossen"
    )

    if st.button(
        "↻ Demo neu starten",
        key="demo_neustart"
    ):
        reset_demo()
