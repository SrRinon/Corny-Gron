import streamlit as st

st.set_page_config(
    page_title="Corny Gron",
    page_icon="🎲"
)

st.title("🎲 Corny Gron")

st.subheader("Personaje")

nombre = st.text_input("Nombre", value="Aventurero")

vida_actual = st.number_input(
    "Vida actual",
    min_value=0,
    value=15
)

vida_maxima = st.number_input(
    "Vida máxima",
    min_value=1,
    value=15
)

dutki = st.number_input(
    "Dutki",
    min_value=0,
    value=0
)

puntos = st.number_input(
    "Puntos obtenidos",
    min_value=0,
    value=0
)

lugares = st.number_input(
    "Lugares visitados",
    min_value=0,
    value=0
)

st.divider()

st.subheader("Progreso de avance")

st.write(f"Puntos: {puntos}/15")
st.write(f"Lugares: {lugares}/12")

if puntos >= 15 and lugares >= 12:
    st.success("✅ Preparado para avanzar")
