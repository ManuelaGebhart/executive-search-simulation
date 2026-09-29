import streamlit as st

st.set_page_config(
    page_title="Executive Search Simulation",
    page_icon="🎯",
    layout="wide"
)

# ============================================================
# DEMO-DATEN – ALLE PERSONEN UND INFORMATIONEN FREI ERFUNDEN
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

    Eure Aufgabe:

    **Erstellt aus den fünf Profilen eine Shortlist mit genau zwei Personen.**
    """)

    if st.button("🎯 Suche starten", type="primary"):
        st.session_state.phase = 1
        st.rerun()

# ============================================================
# PHASE 1 – SHORTLIST 1.0
# ============================================================

elif st.session_state.phase == 1:

    st.info("🔒 CONFIDENTIAL SEARCH MANDATE")

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

    st.subheader("Kandidaten-Screening")

    st.write(
        "Prüft die verfügbaren biografischen Informationen. "
        "**Welche zwei Personen würdet ihr in die nächste Phase aufnehmen?**"
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

    if len(auswahl) < 2:
        st.warning(f"Ihr habt {len(auswahl)} von 2 Personen ausgewählt.")

    elif len(auswahl) > 2:
        st.error("Bitte wählt genau zwei Personen aus.")

    else:
        st.success("✓ Eure Shortlist ist vollständig.")

        for person in auswahl:
            st.write("🎯", person)

        st.markdown("### Was hat eure Entscheidung beeinflusst?")

        ausgewaehlte_gruende = st.multiselect(
            "Mehrfachauswahl möglich",
            options=gruende
        )

        sonstiges = ""

        if "Sonstiges" in ausgewaehlte_gruende:
            sonstiges = st.text_input(
                "Welcher weitere Grund war wichtig?"
            )

        st.markdown("### Wie sicher seid ihr euch?")

        sicherheit = st.slider(
            "Entscheidungssicherheit",
            0,
            100,
            70,
            5,
            format="%d%%"
        )

        if st.button("🔒 Shortlist 1.0 bestätigen", type="primary"):

            if not ausgewaehlte_gruende:
                st.warning(
                    "Bitte wählt mindestens einen Entscheidungsgrund aus."
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
# PHASE 2 – INTERVIEW-REVEAL
# ============================================================

elif st.session_state.phase == 2:

    st.warning("🔓 NEUE INFORMATIONEN VERFÜGBAR")

    st.subheader("Die erste Shortlist steht.")

    st.write("Ihr habt ausgewählt:")

    for person in st.session_state.shortlist1:
        st.write("🎯", person)

    st.write(
        f"**Entscheidungssicherheit:** "
        f"{st.session_state.sicherheit1}%"
    )

    st.divider()

    st.markdown("""
    ### Fiktive Interviewrunde

    Ihr erhaltet nun zusätzliche Informationen aus ersten Gesprächen.

    **Wichtig:** Die folgenden Interviewinformationen sind für diese
    Demo didaktisch konstruiert und frei erfunden.

    Prüft danach eure ursprüngliche Entscheidung erneut.
    """)

    for name, daten in kandidaten.items():

        with st.expander(f"🎙️ Interviewinformation – {name}"):
            st.write(daten["interview"])

    st.divider()

    if st.button("➡️ Shortlist erneut prüfen", type="primary"):
        st.session_state.phase = 3
        st.rerun()

# ============================================================
# PHASE 3 – SHORTLIST 2.0
# ============================================================

elif st.session_state.phase == 3:

    st.subheader("SHORTLIST 2.0")

    st.write("""
    Ihr kennt jetzt zusätzliche Informationen.

    **Welche zwei Personen würdet ihr jetzt in die nächste Phase aufnehmen?**

    Ihr dürft eure ursprüngliche Entscheidung beibehalten oder verändern.
    """)

    auswahl2 = []

    for name, daten in kandidaten.items():

        with st.expander(name):

            st.write("**Bisher bekannte Information**")
            st.write(daten["profil"])

            st.info("🎙️ **Zusätzliche Interviewinformation**")
            st.write(daten["interview"])

            vorauswahl = name in st.session_state.shortlist1

            if st.checkbox(
                "Auf meine Shortlist 2.0",
                value=vorauswahl,
                key=f"runde2_{name}"
            ):
                auswahl2.append(name)

    st.divider()

    if len(auswahl2) < 2:
        st.warning(f"Ihr habt {len(auswahl2)} von 2 Personen ausgewählt.")

    elif len(auswahl2) > 2:
        st.error("Bitte wählt genau zwei Personen aus.")

    else:

        st.success("✓ Shortlist 2.0 ist vollständig.")

        if st.button("🎯 Entscheidung abschließen", type="primary"):
            st.session_state.shortlist2 = auswahl2.copy()
            st.session_state.phase = 4
            st.rerun()

# ============================================================
# PHASE 4 – AHA / VERGLEICH
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

        st.success(
            "Ihr seid trotz der zusätzlichen Informationen "
            "bei eurer ursprünglichen Shortlist geblieben."
        )

    else:

        st.warning("💡 Eure Entscheidung hat sich verändert.")

        if raus:
            st.write("**Nicht mehr auf der Shortlist:**")
            for person in raus:
                st.write("↓", person)

        if rein:
            st.write("**Neu auf der Shortlist:**")
            for person in rein:
                st.write("↑", person)

    st.divider()

    st.markdown("## DER BLIND-SPOT-CHECK")

    st.write("""
    Schaut noch einmal auf eure erste Entscheidung.

    **Welche Informationen standen tatsächlich im Profil –
    und was habt ihr daraus geschlossen?**
    """)

    st.info("""
    Beispiel:

    **Information:** „10 Jahre Führungserfahrung“

    **Mögliche Schlussfolgerung:** „Diese Person kann große Teams
    erfolgreich führen.“

    **Frage:** Stand diese Schlussfolgerung tatsächlich im Profil?
    """)

    st.markdown("""
    ### Die entscheidende Frage

    **Welche biografische Information liefert einen begründeten Hinweis
    auf welche konkrete Anforderung der Position?**
    """)

    if st.button("↻ Demo neu starten"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()
