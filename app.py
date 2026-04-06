"""Description.

Interface graphique pour planifier un projet.
"""

import streamlit as st
from src.film_scheduler.models import Tache, Projet
from src.film_scheduler.scheduler import calcule_dates, duree_totale

st.title("Planificateur de projet")

st.header("1. Entrez vos tâches")

nombre_taches = st.number_input(
    "Combien de tâches a votre projet ?",
    min_value=1,
    max_value=20,
    value=3,
)

taches = []
for i in range(nombre_taches):
    st.subheader(f"Tâche {i+1}")
    col1, col2 = st.columns(2)
    with col1:
        nom = st.text_input(f"Nom de la tâche", key=f"nom_{i}", value=f"T{i+1}")
    with col2:
        duree = st.number_input(f"Durée (jours)", key=f"duree_{i}", min_value=1, value=1)
    predecesseurs_str = st.text_input(
        "Prédécesseurs (ex: A:0, B:15)",
        key=f"pred_{i}",
        value="",
    )
    predecesseurs = []
    if predecesseurs_str.strip():
        for item in predecesseurs_str.split(","):
            parts = item.strip().split(":")
            if len(parts) == 2:
                predecesseurs.append((parts[0].strip(), int(parts[1].strip())))
    taches.append(Tache(nom=nom, duree=duree, predecesseurs=predecesseurs))

if st.button("Calculer le planning"):
    try:
        projet = Projet(nom="Mon projet", taches=taches)
        fins = calcule_dates(projet)
        st.header("2. Résultat")
        st.success(f"Durée totale : {duree_totale(projet)} jours")
        st.table([
            {"Tâche": nom, "Fin au jour": fin}
            for nom, fin in fins.items()
        ])
    except ValueError as e:
        st.error(f"Erreur : {e}")