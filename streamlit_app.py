import streamlit as st

st.set_page_config(
    page_title="Executive Search Simulation",
    page_icon="🎯",
    layout="wide"
)

# ----------------------------
# DEMO-DATEN – FREI ERFUNDEN
# ----------------------------

kandidaten = {
    "Kandidat A – Der Branchenprofi": {
        "aktuell": "Regional Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "16 Jahre Berufserfahrung",
        "fuehrung": "9 Jahre Führungserfahrung",
        "international": "Deutschland, Österreich, Schweiz",
        "profil": "Langjährige Tätigkeit bei zwei großen Finanzdienstleistern. "
                  "Seit fünf Jahren Leitung einer regionalen Geschäftseinheit mit rund 120 Mitarbeitenden."
    },

    "Kandidatin B – Die Aufbau-Expertin": {
        "aktuell": "Managing Director",
        "branche": "Technologie",
        "erfahrung": "13 Jahre Berufserfahrung",
        "fuehrung": "7 Jahre Führungserfahrung",
        "international": "Österreich, Polen, Tschechien",
        "profil": "Begleitete mehrere Expansionsprojekte und war zuletzt für den Aufbau "
                  "einer neuen Geschäftseinheit in Zentral- und Osteuropa verantwortlich."
    },

    "Kandidat C – Der internationale Manager": {
        "aktuell": "Vice President Operations",
        "branche": "Industrie",
        "erfahrung": "18 Jahre Berufserfahrung",
        "fuehrung": "11 Jahre Führungserfahrung",
        "international": "Europa, USA, Asien",
        "profil": "Internationale Führungslaufbahn mit Verantwortung für mehrere Standorte. "
                  "Langjährige Erfahrung in globalen Unternehmensstrukturen."
    },

    "Kandidatin D – Die unauffällige Kandidatin": {
        "aktuell": "Head of Operations",
        "branche": "Finanznahe Dienstleistungen",
        "erfahrung": "12 Jahre Berufserfahrung",
        "fuehrung": "5 Jahre Führungserfahrung",
        "international": "Österreich, Slowenien",
        "profil": "Karriere überwiegend bei mittelständischen Unternehmen. "
                  "Verantwortung für operative Teams und mehrere interne Veränderungsprojekte."
    },

    "Kandidat E – Der perfekte Lebenslauf?": {
        "aktuell": "Country Director",
        "branche": "Finanzdienstleistungen",
        "erfahrung": "17 Jahre Berufserfahrung",
        "fuehrung": "10 Jahre Führungserfahrung",
        "international": "Deutschland, Schweiz, Großbritannien",
        "profil": "Führungspositionen bei mehreren international bekannten Unternehmen. "
                  "Verantwortung für große Teams und strategische Wachstumsprojekte."
    }
}

# Session State
if "gestartet" not in st.session_state:
    st.session_state.gestartet = False

# ----------------------------
# START
# ----------------------------

st.title("MISSION: EXECUTIVE SEARCH")
st.caption("DEMO-PROTOTYP · Alle Unternehmen, Personen und Angaben sind frei erfunden.")

if not st.session_state.gestartet:

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
        st.session_state.gestartet = True
        st.rerun()

# ----------------------------
# SUCHAUFTRAG
# ----------------------------

else:

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
                key=f"select_{name}"
            ):
                auswahl.append(name)

    st.divider()

    st.subheader("Eure Shortlist 1.0")

    if len(auswahl) == 0:
        st.warning("Noch keine Person ausgewählt.")

    elif len(auswahl) == 1:
        st.warning("Ihr müsst noch eine zweite Person auswählen.")
        st.write("Bisher ausgewählt:", auswahl[0])

    elif len(auswahl) == 2:
        st.success("✓ Eure Shortlist ist vollständig.")

        for person in auswahl:
            st.write("🎯", person)

        st.markdown("### Wie sicher seid ihr euch?")

        sicherheit = st.slider(
            "Sicherheit der Entscheidung",
            min_value=0,
            max_value=100,
            value=70,
            step=5,
            format="%d%%"
        )

        begruendung = st.text_area(
            "Warum habt ihr gerade diese beiden Personen ausgewählt?",
            placeholder="Welche Informationen waren für eure Entscheidung besonders wichtig?"
        )

        if st.button("🔒 Shortlist 1.0 bestätigen", type="primary"):

            if begruendung.strip() == "":
                st.warning("Bitte gebt zuerst kurz an, warum ihr diese Personen ausgewählt habt.")

            else:
                st.success(
                    f"Shortlist gespeichert – Entscheidungssicherheit: {sicherheit}%"
                )

                st.info(
                    "DEMO: Im nächsten Schritt würden nun zusätzliche "
                    "Interviewinformationen freigeschaltet."
                )

    else:
        st.error(
            "Ihr dürft nur zwei Personen auswählen. "
            "Bitte entfernt mindestens eine Person von der Shortlist."
        )
