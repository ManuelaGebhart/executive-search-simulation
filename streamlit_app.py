import streamlit as st
import time
from datetime import datetime, timedelta

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
        ),
        "reflexion": (
            "Aus langer Führungserfahrung allein lässt sich noch nicht ableiten, "
            "dass Erfahrung mit dem Aufbau eines neuen Standorts vorliegt."
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
        ),
        "reflexion": (
            "Die neue Information konkretisiert, was mit „Aufbau“ tatsächlich "
            "gemeint war und welche Verantwortung sie dabei selbst trug."
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
        ),
        "reflexion": (
            "„Verantwortung für mehrere Standorte“ und „Erfahrung mit dem Aufbau "
            "von Standorten“ sind nicht dieselbe Information."
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
        ),
        "reflexion": (
            "Das ursprüngliche Kurzprofil enthielt relevante Erfahrung, machte "
            "deren konkreten Bezug zum Standortaufbau aber kaum sichtbar."
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
        ),
        "reflexion": (
            "Bekannte Arbeitgeber und strategische Wachstumsprojekte können einen "
            "starken ersten Eindruck erzeugen. Entscheidend bleibt, welche konkrete "
            "Rolle die Person selbst übernommen hat."
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
        st.markdown("#### 🔓 Neue Interviewinformation")
        st.info(daten["interview"])


# ============================================================
# KOPF
# ============================================================

st.title("MISSION: EXECUTIVE SEARCH")

st.caption(
    "DEMO-PROTOTYP · Alle Personen, Unternehmen und Angaben "
    "dieser Simulation sind frei erfunden."
)

# ============================================================
# PHASE 0 – MISSION
# ============================================================

if st.session_state.phase == 0:

    st.subheader("🔒 VERTRAULICHER SUCHAUFTRAG")

    st.markdown("""
### Neue Führung für einen strategisch wichtigen Standort

Ein international tätiges Unternehmen baut seine Präsenz in Österreich aus
und sucht eine neue Führungskraft:

## **Managing Director Austria**

Das Executive-Search-Team hat fünf potenzielle Kandidat:innen identifiziert.

### Eure Mission

Erstellt aus den fünf Profilen eine **Shortlist mit genau drei Personen**.

Die erste Sichtung erfolgt bewusst schnell.

Nach dem Start habt ihr:

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

    elapsed = time.time() - st.session_state.screening_start

    # --------------------------------------------------------
    # ZEITSTATUS
    # --------------------------------------------------------

    if elapsed < 90:
        rest = max(0, int(90 - elapsed))
        modus = "screening"

    elif elapsed < 105:
        rest = max(0, int(105 - elapsed))
        modus = "final"

    else:
        rest = 0
        modus = "locked"
        st.session_state.screening_locked = True

    # --------------------------------------------------------
    # TIMERANZEIGE
    # --------------------------------------------------------

    timer_placeholder = st.empty()

    if modus == "screening":

        if rest > 20:
            timer_placeholder.info(
                f"⏱️ FIRST SCREENING · Noch **{rest} Sekunden**"
            )

        else:
            timer_placeholder.error(
                f"🔴 NOCH **{rest} SEKUNDEN** · "
                "Bitte eure drei Personen auswählen!"
            )

    elif modus == "final":

        timer_placeholder.error(
            f"🚨 **FINAL DECISION · {rest} SEKUNDEN**\n\n"
            "Keine Detailanalyse mehr – legt jetzt eure drei Personen fest."
        )

    else:

        timer_placeholder.error(
            "🔒 **ZEIT ABGELAUFEN · AUSWAHL FIXIERT**"
        )

    # --------------------------------------------------------
    # ANFORDERUNGSPROFIL
    # --------------------------------------------------------

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
        "**Welche drei Personen nehmt ihr in die nächste Phase auf?**"
    )

    # --------------------------------------------------------
    # AUSWAHL
    # --------------------------------------------------------

    auswahl = []

    for name, daten in kandidaten.items():

        with st.expander(name):

            kandidatenkarte(name, daten)

            checkbox_key = f"runde1_{name}"

            if st.checkbox(
                "Auf meine Shortlist",
                key=checkbox_key,
                disabled=st.session_state.screening_locked
            ):
                auswahl.append(name)

    # --------------------------------------------------------
    # TIMER AKTUALISIEREN
    # --------------------------------------------------------

    if not st.session_state.screening_locked:

        if st.button(
            "⟳ Countdown aktualisieren",
            key="timer_refresh"
        ):
            st.rerun()

        st.caption(
            "Der Countdown läuft weiter. Die Anzeige aktualisiert sich "
            "bei Interaktionen automatisch; mit dem Button könnt ihr "
            "den aktuellen Stand zusätzlich abrufen."
        )

    st.divider()

    # --------------------------------------------------------
    # NACH ABLAUF
    # --------------------------------------------------------

    if st.session_state.screening_locked:

        # Auswahl aus den gespeicherten Checkbox-Zuständen lesen
        auswahl = []

        for name in kandidaten:
            if st.session_state.get(f"runde1_{name}", False):
                auswahl.append(name)

        st.subheader("🔒 Eure fixierte Vorauswahl")

        if len(auswahl) == 3:

            st.success("✓ Ihr habt genau drei Personen ausgewählt.")

            for person in auswahl:
                st.write("🎯", person)

            st.markdown("### Was hat eure Entscheidung beeinflusst?")

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

            st.markdown("### Wie sicher seid ihr euch?")

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
                    st.session_state.gruende1 = ausgewaehlte_gruende.copy()

                    if sonstiges:
                        st.session_state.gruende1.append(
                            f"Sonstiges: {sonstiges}"
                        )

                    st.session_state.sicherheit1 = sicherheit
                    st.session_state.phase = 2
                    st.rerun()

        else:

            st.warning(
                f"Ihr habt innerhalb der Zeit **{len(auswahl)} Personen** "
                "ausgewählt. Für die Simulation werden genau drei benötigt."
            )

            st.write(
                "Für den Demo-Prototyp könnt ihr die Runde neu starten. "
                "Für die endgültige Version bauen wir hier noch eine "
                "kontrollierte Notfalllösung ein."
            )

            if st.button(
                "↻ Screening neu starten",
                key="screening_restart"
            ):
                reset_demo()


# ============================================================
# PHASE 2 – ERSTER THEORIE-IMPULS
# ============================================================

elif st.session_state.phase == 2:

    st.success("✓ SHORTLIST 1.0 ABGESCHLOSSEN")

    st.subheader("Was habt ihr gerade eigentlich gemacht?")

    st.write("""
Ihr habt Informationen aus der **beruflichen Vergangenheit**
der Kandidat:innen verwendet, um einzuschätzen, wer für eine
zukünftige Position geeignet sein könnte.
""")

    with st.expander(
        "💡 THEORIE-IMPULS · Biografieorientierte Verfahren"
    ):

        st.markdown("""
Bei **biografieorientierten Verfahren** wird Berufserfolg dadurch
vorhergesagt, dass von vergangenem Verhalten beziehungsweise
früher erbrachten Leistungen auf zukünftige Leistungen geschlossen wird.

Zu den bedeutsamen biografieorientierten Verfahren werden in der
Kursunterlage unter anderem die **Prüfung von Bewerbungsunterlagen**
und das **Vorstellungsgespräch** gezählt.

**Quelle:** Furtmüller & Zdravkovic, *Personalauswahl*, S. 297.
""")

    st.divider()

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
🔓 **NEUE INFORMATIONEN SIND VERFÜGBAR**

Ihr erhaltet jetzt zusätzliche Informationen aus fiktiven
Erstgesprächen.

Prüft danach eure ursprüngliche Entscheidung erneut.
""")

    if st.button(
        "🎙️ SECOND LOOK starten",
        type="primary",
        key="second_look_start"
    ):
        st.session_state.phase = 3
        st.rerun()


# ============================================================
# PHASE 3 – SECOND LOOK / SHORTLIST 2.0
# ============================================================

elif st.session_state.phase == 3:

    st.subheader("🎙️ SECOND LOOK")

    st.write("""
Jetzt stehen zusätzliche Informationen zur Verfügung.

Prüft **alle fünf Kandidat:innen erneut** und erstellt danach
wieder eine Shortlist mit **genau drei Personen**.
""")

    with st.expander(
        "🧭 DIAGNOSTIK-CHECK"
    ):

        st.markdown("""
### Prüft eure Schlussfolgerung

**Was wissen wir tatsächlich?**

↓

**Was schließen wir daraus?**

↓

**Welche konkrete Anforderung betrifft diese Schlussfolgerung?**

↓

**Reicht die vorhandene Information für diesen Schluss?**

*Dieser Vier-Schritt-Check ist eine didaktische Aufbereitung
für unsere Simulation und kein wörtlich übernommenes Literaturmodell.*
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
# PHASE 4 – VERGLEICH
# ============================================================

elif st.session_state.phase == 4:

    st.subheader("🔍 EURE ENTSCHEIDUNG IM VERGLEICH")

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

    # --------------------------------------------------------
    # VERÄNDERUNG
    # --------------------------------------------------------

    if vorher == nachher:

        st.success("""
### Eure Shortlist ist gleich geblieben.

Die zusätzlichen Informationen haben eure Auswahl nicht verändert.

Auch dann lohnt sich die Frage:
**Haben sich eure Gründe für dieselbe Auswahl verändert?**
""")

        relevante_personen = list(st.session_state.shortlist2)

    else:

        st.warning(
            "💡 **EURE ENTSCHEIDUNG HAT SICH VERÄNDERT.**"
        )

        relevante_personen = list(raus | rein)

        for person in relevante_personen:

            daten = kandidaten[person]

            if person in raus:
                status = "↓ NICHT MEHR AUF DER SHORTLIST"
            else:
                status = "↑ NEU AUF DER SHORTLIST"

            st.markdown(f"## {status}")
            st.markdown(f"### {person}")

            st.markdown("**Was ihr zuerst wusstet:**")
            st.write(daten["profil"])

            st.markdown("**Was ihr später erfahren habt:**")
            st.info(daten["interview"])

            st.divider()

    # --------------------------------------------------------
    # DYNAMISCHE REFLEXION
    # --------------------------------------------------------

    st.subheader("🔎 INFORMATION ODER INTERPRETATION?")

    st.write("""
Schaut euch genau die Kandidat:innen an, die für eure
Entscheidung relevant waren.

**Was stand tatsächlich in den Informationen – und was habt ihr
selbst daraus geschlossen?**
""")

    for person in relevante_personen:

        daten = kandidaten[person]

        with st.expander(
            f"Reflexion · {person}"
        ):
            st.write(daten["reflexion"])

            st.markdown("""
Fragt euch:

- Welche Information war tatsächlich vorhanden?
- Welche Bedeutung haben wir ihr gegeben?
- Welche konkrete Stellenanforderung wollten wir damit beurteilen?
- Hat die neue Information unsere Interpretation bestätigt oder verändert?
""")

    st.caption(
        "Die Reflexionshinweise sind Teil der didaktisch konstruierten "
        "Demo. Sie werden später an die endgültigen Profile und an "
        "Marcs Praxisfall angepasst."
    )

    st.divider()

    # --------------------------------------------------------
    # THEORIE / GRENZEN
    # --------------------------------------------------------

    with st.expander(
        "💡 THEORIE-IMPULS · Aussagekraft biografischer Informationen"
    ):

        st.markdown("""
Biografische Informationen können für eine Eignungsprognose
herangezogen werden. Entscheidend ist jedoch der Bezug zu den
Anforderungen der konkreten Position.

In der in der Kursunterlage dargestellten Übersicht wird für
**Bewerbungsunterlagen eine prognostische Validität von .18**
angeführt.

Das bedeutet **nicht**, dass jede Form biografischer Information
generell „schlecht“ oder nutzlos wäre. Der Wert bezieht sich auf
die in der Unterlage dargestellte Verfahrensübersicht.

**Quelle:** Furtmüller & Zdravkovic, *Personalauswahl*,
Übersicht zur prognostischen Validität von Auswahlverfahren.
""")

    st.divider()

    st.markdown("## TAKE-AWAY")

    st.success("""
### Vergangenheit ≠ automatisch Eignung

**Biografische Information**

↓

**Interpretation**

↓

**Bezug zur konkreten Anforderung**

↓

**begründete Eignungsprognose**
""")

    if st.button(
        "↻ Demo neu starten",
        key="demo_neustart"
    ):
        reset_demo()
