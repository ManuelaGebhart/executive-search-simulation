import streamlit as st

st.set_page_config(
    page_title="Executive Search Simulation",
    page_icon="🎯",
    layout="wide"
)

st.title("MISSION: EXECUTIVE SEARCH")
st.subheader("Biografieorientierte Personalauswahl")

st.info("🔒 VERTRAULICHER SUCHAUFTRAG")

st.write("""
Willkommen im Executive-Search-Team.

Eure Aufgabe: Prüft die verfügbaren Kandidat:innenprofile und entscheidet,
welche Personen ihr in die nächste Phase des Auswahlprozesses aufnehmen würdet.
""")

if st.button("Suche starten"):
    st.success("Die Mission beginnt!")
