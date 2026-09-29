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

    Entscheidet ausschließlich auf Basis der Informationen,
    die euch zu diesem Zeitpunkt zur Verfügung stehen.
    """)

    if st.button("🎯 Suche starten", type="primary"):
        st.session_state.phase = 1
        st.rerun()

# ============================================================
# PHASE 1 – SHORTLIST 1.0
# ============================================================

elif st.session_state.phase == 1:

    st.info("🔒 CONFIDENTIAL SEARCH MANDATE")
    # ========================================================
    # COUNTDOWN – FIRST SCREENING
    # ========================================================

    components.html(
        """
        <div id="timerbox" style="
            text-align:center;
            padding:14px;
            border-radius:12px;
            margin-bottom:15px;
            background:#f1f3f5;
            font-family:Arial, sans-serif;
        ">
            <div style="font-size:14px; font-weight:bold;">
                FIRST SCREENING · VERBLEIBENDE ZEIT
            </div>

            <div id="timer" style="
                font-size:38px;
                font-weight:bold;
                margin-top:4px;
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
                    String(minutes).padStart(2, '0') + ":" +
                    String(seconds).padStart(2, '0');

                // Letzte 20 Sekunden
                if (timeLeft <= 20 && timeLeft > 5) {
                    box.style.background = "#ffe0e0";
                    box.style.border = "2px solid #c62828";
                    timer.style.color = "#c62828";
                    timer.style.fontSize = "52px";
                    message.innerHTML =
                        "<b>Noch " + timeLeft +
                        " Sekunden – bitte 3 Personen auswählen!</b>";
                }

                // Letzte 5 Sekunden
                if (timeLeft <= 5 && timeLeft > 0) {
                    box.style.background = "#c62828";
                    timer.style.color = "white";
                    timer.style.fontSize = "70px";
                    message.style.color = "white";
                    message.innerHTML =
                        "<b>JETZT AUSWAHL ABSCHLIESSEN</b>";
                }

                // Zeit abgelaufen
                if (timeLeft <= 0) {
                    clearInterval(countdown);

                    timer.innerHTML = "ZEIT ABGELAUFEN";
                    timer.style.fontSize = "36px";
                    timer.style.color = "white";

                    box.style.background = "#c62828";

                    message.style.color = "white";
                    message.innerHTML =
                        "<b>Bitte bestätigt jetzt eure 3 ausgewählten Personen.</b>";
                }

            }, 1000);
        </script>
        """,
        height=155
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

    st.subheader("Kandidaten-Screening")

    st.write(
        "Prüft die verfügbaren Informationen und entscheidet: "
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
            "Ihr könnt genau drei Personen auswählen. "
            "Bitte entfernt eine Person."
        )

    else:

        st.success("✓ Eure Shortlist ist vollständig.")

        for person in auswahl:
            st.write("🎯", person)

        st.markdown("### Was hat eure Entscheidung beeinflusst?")

        ausgewaehlte_gruende = st.multiselect(
            "Mehrfachauswahl möglich",
            options=gruende,
            placeholder="Entscheidungsgründe auswählen"
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

        if st.button(
            "🔒 Shortlist 1.0 bestätigen",
            type="primary"
        ):

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
# PHASE 2 – THEORIE NACH DER ERSTEN ENTSCHEIDUNG
# ============================================================

elif st.session_state.phase == 2:

    st.success("✓ SHORTLIST 1.0 ABGESCHLOSSEN")

    st.subheader("Was habt ihr gerade eigentlich gemacht?")

    st.write("""
    Ihr habt Informationen aus der **beruflichen Vergangenheit**
    der Kandidat:innen verwendet, um einzuschätzen, wer für eine
    zukünftige Position geeignet sein könnte.
    """)

    with st.expander("💡 THEORIE-IMPULS: Biografieorientierter Ansatz"):

        st.markdown("""
        **Biografieorientierte Personalauswahl**

        Bei biografieorientierten Verfahren werden Informationen über
        vergangenes Verhalten beziehungsweise früher erbrachte Leistungen
        genutzt, um zukünftige Leistungen bzw. Eignung vorherzusagen.

        Bewerbungsunterlagen und Lebenslauf können dabei Quellen
        biografischer Informationen sein.

        **Aber:** Eine Information aus der Vergangenheit ist noch
        nicht automatisch ein Beleg für die Eignung für eine konkrete
        Position.
        """)

    st.divider()

    st.markdown("### Eure erste Entscheidung")

    for person in st.session_state.shortlist1:
        st.write("🎯", person)

    st.write(
        f"**Eure Entscheidungssicherheit:** "
        f"{st.session_state.sicherheit1}%"
    )

    st.markdown("**Eure wichtigsten Entscheidungsgründe:**")

    for grund in st.session_state.gruende1:
        st.write("•", grund)

    st.divider()

    st.warning("""
    🔓 **NEUE INFORMATIONEN SIND VERFÜGBAR**

    Im nächsten Schritt erhaltet ihr zusätzliche Informationen
    aus fiktiven Erstgesprächen.

    Ihr seht dort bei jeder Person sowohl die bisher bekannten
    Informationen als auch die neuen Interviewinformationen.

    Danach erstellt ihr eure **Shortlist 2.0**.
    """)

    if st.button(
        "🎙️ Interviewinformationen öffnen",
        type="primary"
    ):
        st.session_state.phase = 3
        st.rerun()

# ============================================================
# PHASE 3 – INTERVIEW + SHORTLIST 2.0
# ============================================================

elif st.session_state.phase == 3:

    st.subheader("🎙️ NEUE INFORMATIONEN")

    st.write("""
    Ihr habt nun zusätzliche Informationen aus ersten Gesprächen.

    Prüft alle fünf Kandidat:innen erneut.

    **Welche drei Personen würdet ihr jetzt in die nächste Phase aufnehmen?**
    """)

    with st.expander("🧭 DIAGNOSTIK-CHECK: Worauf solltet ihr jetzt achten?"):

        st.markdown("""
        Stellt euch bei jeder Information vier Fragen:

        **1. Was wissen wir tatsächlich?**  
        ↓  
        **2. Was schließen wir daraus?**  
        ↓  
        **3. Welche konkrete Anforderung betrifft diese Schlussfolgerung?**  
        ↓  
        **4. Reicht die vorhandene Information für diesen Schluss?**
        """)

    st.caption(
        "Die Interviewinformationen dieser Demo sind frei erfunden "
        "und wurden ausschließlich für die Übung konstruiert."
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

            st.markdown("#### 🔓 Neue Interviewinformation")
            st.info(daten["interview"])

            war_vorher_dabei = name in st.session_state.shortlist1

            if war_vorher_dabei:
                st.caption("🎯 Diese Person war auf eurer Shortlist 1.0.")

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
            "Ihr könnt genau drei Personen auswählen. "
            "Bitte entfernt eine Person."
        )

    else:

        st.success("✓ Eure neue Shortlist ist vollständig.")

        for person in auswahl2:
            st.write("🎯", person)

        if st.button(
            "🎯 Shortlist 2.0 bestätigen",
            type="primary"
        ):
            st.session_state.shortlist2 = auswahl2.copy()
            st.session_state.phase = 4
            st.rerun()

# ============================================================
# PHASE 4 – VERGLEICH / AHA-EFFEKT
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
        Eure Shortlist ist gleich geblieben.

        Auch das ist ein Ergebnis:
        Die zusätzlichen Informationen haben eure ursprüngliche
        Auswahl nicht verändert.
        """)

    else:

        st.warning("💡 EURE ENTSCHEIDUNG HAT SICH VERÄNDERT.")

        col3, col4 = st.columns(2)

        with col3:
            if raus:
                st.markdown("#### ↓ Nicht mehr auf der Shortlist")
                for person in raus:
                    st.write(person)

        with col4:
            if rein:
                st.markdown("#### ↑ Neu auf der Shortlist")
                for person in rein:
                    st.write(person)

    st.divider()

    st.markdown("## 🧠 BLIND-SPOT-CHECK")

    st.write("""
    Erinnert euch an eure erste Entscheidung.

    **Welche Informationen standen tatsächlich im Profil –
    und welche Schlussfolgerungen habt ihr selbst daraus gezogen?**
    """)

    st.info("""
    **Beispiel**

    Information im Profil:

    „10 Jahre Führungserfahrung“

    ↓

    Mögliche Schlussfolgerung:

    „Diese Person kann große Teams erfolgreich führen.“

    ↓

    **Aber: Stand diese Schlussfolgerung tatsächlich im Profil?**
    """)

    st.markdown("""
    ### Die entscheidende Frage

    **Welche biografische Information liefert einen begründeten
    Hinweis auf welche konkrete Anforderung der Position?**
    """)

    with st.expander("💡 THEORIE-IMPULS: Aussagekraft und Grenzen"):

        st.markdown("""
        Biografische Informationen können für eine
        Eignungsprognose genutzt werden.

        Entscheidend ist jedoch nicht nur, **wie viele Informationen**
        über die Vergangenheit einer Person vorliegen.

        Entscheidend ist, **welche Schlussfolgerung daraus gezogen wird**
        und ob diese Schlussfolgerung mit den Anforderungen der konkreten
        Position begründet verknüpft werden kann.

        Zusätzliche diagnostische Informationen können eine erste
        Einschätzung bestätigen, differenzieren oder verändern.
        """)

    st.divider()

    st.markdown("### TAKE-AWAY")

    st.success("""
    **Vergangenheit ≠ automatisch Eignung**

    Biografische Information  
    → Interpretation  
    → konkrete Anforderung  
    → begründete Eignungsprognose
    """)

    if st.button("↻ Demo neu starten"):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()
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

    Entscheidet ausschließlich auf Basis der Informationen,
    die euch zu diesem Zeitpunkt zur Verfügung stehen.
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
        "Prüft die verfügbaren Informationen und entscheidet: "
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
            "Ihr könnt genau drei Personen auswählen. "
            "Bitte entfernt eine Person."
        )

    else:

        st.success("✓ Eure Shortlist ist vollständig.")

        for person in auswahl:
            st.write("🎯", person)

        st.markdown("### Was hat eure Entscheidung beeinflusst?")

        ausgewaehlte_gruende = st.multiselect(
            "Mehrfachauswahl möglich",
            options=gruende,
            placeholder="Entscheidungsgründe auswählen"
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

        if st.button(
            "🔒 Shortlist 1.0 bestätigen",
            type="primary"
        ):

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
# PHASE 2 – THEORIE NACH DER ERSTEN ENTSCHEIDUNG
# ============================================================

elif st.session_state.phase == 2:

    st.success("✓ SHORTLIST 1.0 ABGESCHLOSSEN")

    st.subheader("Was habt ihr gerade eigentlich gemacht?")

    st.write("""
    Ihr habt Informationen aus der **beruflichen Vergangenheit**
    der Kandidat:innen verwendet, um einzuschätzen, wer für eine
    zukünftige Position geeignet sein könnte.
    """)

    with st.expander("💡 THEORIE-IMPULS: Biografieorientierter Ansatz"):

        st.markdown("""
        **Biografieorientierte Personalauswahl**

        Bei biografieorientierten Verfahren werden Informationen über
        vergangenes Verhalten beziehungsweise früher erbrachte Leistungen
        genutzt, um zukünftige Leistungen bzw. Eignung vorherzusagen.

        Bewerbungsunterlagen und Lebenslauf können dabei Quellen
        biografischer Informationen sein.

        **Aber:** Eine Information aus der Vergangenheit ist noch
        nicht automatisch ein Beleg für die Eignung für eine konkrete
        Position.
        """)

    st.divider()

    st.markdown("### Eure erste Entscheidung")

    for person in st.session_state.shortlist1:
        st.write("🎯", person)

    st.write(
        f"**Eure Entscheidungssicherheit:** "
        f"{st.session_state.sicherheit1}%"
    )

    st.markdown("**Eure wichtigsten Entscheidungsgründe:**")

    for grund in st.session_state.gruende1:
        st.write("•", grund)

    st.divider()

    st.warning("""
    🔓 **NEUE INFORMATIONEN SIND VERFÜGBAR**

    Im nächsten Schritt erhaltet ihr zusätzliche Informationen
    aus fiktiven Erstgesprächen.

    Ihr seht dort bei jeder Person sowohl die bisher bekannten
    Informationen als auch die neuen Interviewinformationen.

    Danach erstellt ihr eure **Shortlist 2.0**.
    """)

    if st.button(
        "🎙️ Interviewinformationen öffnen",
        type="primary"
    ):
        st.session_state.phase = 3
        st.rerun()

# ============================================================
# PHASE 3 – INTERVIEW + SHORTLIST 2.0
# ============================================================

elif st.session_state.phase == 3:

    st.subheader("🎙️ NEUE INFORMATIONEN")

    st.write("""
    Ihr habt nun zusätzliche Informationen aus ersten Gesprächen.

    Prüft alle fünf Kandidat:innen erneut.

    **Welche drei Personen würdet ihr jetzt in die nächste Phase aufnehmen?**
    """)

    with st.expander("🧭 DIAGNOSTIK-CHECK: Worauf solltet ihr jetzt achten?"):

        st.markdown("""
        Stellt euch bei jeder Information vier Fragen:

        **1. Was wissen wir tatsächlich?**  
        ↓  
        **2. Was schließen wir daraus?**  
        ↓  
        **3. Welche konkrete Anforderung betrifft diese Schlussfolgerung?**  
        ↓  
        **4. Reicht die vorhandene Information für diesen Schluss?**
        """)

    st.caption(
        "Die Interviewinformationen dieser Demo sind frei erfunden "
        "und wurden ausschließlich für die Übung konstruiert."
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

            st.markdown("#### 🔓 Neue Interviewinformation")
            st.info(daten["interview"])

            war_vorher_dabei = name in st.session_state.shortlist1

            if war_vorher_dabei:
                st.caption("🎯 Diese Person war auf eurer Shortlist 1.0.")

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
            "Ihr könnt genau drei Personen auswählen. "
            "Bitte entfernt eine Person."
        )

    else:

        st.success("✓ Eure neue Shortlist ist vollständig.")

        for person in auswahl2:
            st.write("🎯", person)

        if st.button(
            "🎯 Shortlist 2.0 bestätigen",
            type="primary"
        ):
            st.session_state.shortlist2 = auswahl2.copy()
            st.session_state.phase = 4
            st.rerun()

# ============================================================
# PHASE 4 – VERGLEICH / AHA-EFFEKT
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
        Eure Shortlist ist gleich geblieben.

        Auch das ist ein Ergebnis:
        Die zusätzlichen Informationen haben eure ursprüngliche
        Auswahl nicht verändert.
        """)

    else:

        st.warning("💡 EURE ENTSCHEIDUNG HAT SICH VERÄNDERT.")

        col3, col4 = st.columns(2)

        with col3:
            if raus:
                st.markdown("#### ↓ Nicht mehr auf der Shortlist")
                for person in raus:
                    st.write(person)

        with col4:
            if rein:
                st.markdown("#### ↑ Neu auf der Shortlist")
                for person in rein:
                    st.write(person)

    st.divider()

    st.markdown("## 🧠 BLIND-SPOT-CHECK")

    st.write("""
    Erinnert euch an eure erste Entscheidung.

    **Welche Informationen standen tatsächlich im Profil –
    und welche Schlussfolgerungen habt ihr selbst daraus gezogen?**
    """)

    st.info("""
    **Beispiel**

    Information im Profil:

    „10 Jahre Führungserfahrung“

    ↓

    Mögliche Schlussfolgerung:

    „Diese Person kann große Teams erfolgreich führen.“

    ↓

    **Aber: Stand diese Schlussfolgerung tatsächlich im Profil?**
    """)

    st.markdown("""
    ### Die entscheidende Frage

    **Welche biografische Information liefert einen begründeten
    Hinweis auf welche konkrete Anforderung der Position?**
    """)

    with st.expander("💡 THEORIE-IMPULS: Aussagekraft und Grenzen"):

        st.markdown("""
        Biografische Informationen können für eine
        Eignungsprognose genutzt werden.

        Entscheidend ist jedoch nicht nur, **wie viele Informationen**
        über die Vergangenheit einer Person vorliegen.

        Entscheidend ist, **welche Schlussfolgerung daraus gezogen wird**
        und ob diese Schlussfolgerung mit den Anforderungen der konkreten
        Position begründet verknüpft werden kann.

        Zusätzliche diagnostische Informationen können eine erste
        Einschätzung bestätigen, differenzieren oder verändern.
        """)

    st.divider()

    st.markdown("### TAKE-AWAY")

    st.success("""
    **Vergangenheit ≠ automatisch Eignung**

    Biografische Information  
    → Interpretation  
    → konkrete Anforderung  
    → begründete Eignungsprognose
    """)

    if st.button("↻ Demo neu starten"):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()
