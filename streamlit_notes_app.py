import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data():
    data = {
        "Nom": [f"Étudiant {i+1}" for i in range(100)],
        "Mathématiques": np.random.normal(12, 3, 100).clip(0, 20),
        "Physique": np.random.normal(14, 4, 100).clip(0, 20),
        "Chimie": np.random.normal(10, 2, 100).clip(0, 20),
    }
    return pd.DataFrame(data)

def calcul_statistiques(df, matiere):
    freq = df[matiere].value_counts().sort_index()
    probabilites = freq / freq.sum()
    esperance = np.sum(probabilites * freq.index)
    variance = np.sum(probabilites * (freq.index - esperance) ** 2)
    
    return esperance, variance, freq, probabilites

df = generate_data()

st.title("Analyse des Notes des Étudiants")

matiere = st.selectbox("Choisissez une matière :", ["Mathématiques", "Physique", "Chimie"])

esperance, variance, freq, probabilites = calcul_statistiques(df, matiere)

st.write(f"**Espérance (moyenne)** des notes en {matiere} : {esperance:.2f}")
st.write(f"**Variance** des notes en {matiere} : {variance:.2f}")

st.write("### Distribution des Notes")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df[matiere], kde=True, bins=15, color="skyblue", ax=ax)
ax.axvline(esperance, color="red", linestyle="--", label="Espérance")
ax.set_title(f"Distribution des Notes en {matiere}")
ax.legend()
st.pyplot(fig)

st.write("### Probabilités des Notes")
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.bar(freq.index, probabilites, color="orange", alpha=0.7, edgecolor="black")
ax2.set_title(f"Probabilités des Notes en {matiere}")
ax2.set_xlabel("Notes")
ax2.set_ylabel("Probabilité")
st.pyplot(fig2)

st.write("### Fréquences et Probabilités des Notes")
freq_df = pd.DataFrame({"Fréquence": freq, "Probabilité": probabilites})
st.dataframe(freq_df)

st.write("### Données Brutes")
st.dataframe(df)
