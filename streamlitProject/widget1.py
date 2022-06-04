# Importer les packages
from ast import Interactive
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Donner un titre
st.title("Exercice Titanic")

# Afficher du text, unsafe_allow_html=True permet d'utiliser des balises html
st.markdown("Ceci <span style='color:red;'>est</span> un exemple avec streamlit",
unsafe_allow_html=True
)

# Afficher une image
st.image("titanic.jpeg", width=400)

# @st.cache(suppress_st_warning=True) permet d'utiliser un système de cache pour ne pas recalculer à chaque fois
# création d'une fonction load_data pour charger le fichier csv
@st.cache(suppress_st_warning=True)
def load_data(f):
    st.warning("CACHE MISS")
    return pd.read_csv(f)

# Upload du fichier csv
f = st.file_uploader("Uploader un fichier csv", "csv")

# Charger les données si le fichier n'est pas null
if f is not None:
    df = load_data(f)

    # Afficher les données si le checkbox Data preview est coché
    # True indique que le checkbox est coché par défaut
    if st.sidebar.checkbox("Data preview", True):
        st.write(df.style.background_gradient(cmap="BuGn"))
    # st.write(df['Name'])
    
    # Affiche la liste déroulante si le checkbox Univariate distribution est coché
    if st.sidebar.checkbox("Univariate distribution"):
        col = st.selectbox("Choisissez une colonne", df.columns)
        # Récupérer comme donnée en absice la colonne choisi à la liste déroulante
        # .interactive permet de rendre intéractif l'histogramme
        chart = alt.Chart(df).mark_bar().encode(
                x=col,
                y="count()",
                tooltip=['Age']
            ).interactive()
        st.altair_chart(chart, use_container_width=True)

    # tracer un histogramme avec Age en absice
    fig, ax = plt.subplots()
    df.hist("Age", ax=ax)
    st.pyplot(fig)

    # Afficher l'histogramme de l'Age en absice et son nombre d'enregistrement en ordonné
    # with st.echo indique d'afficher aussi le code
    with st.echo():
        chart = alt.Chart(df).mark_bar().encode(
            x="Age",
            y="count()",
            tooltip=['Age']
        ).interactive()
    chart
    st.altair_chart(chart, use_container_width=True)