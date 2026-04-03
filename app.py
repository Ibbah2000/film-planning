"""Description.

Interface graphique pour planifier un projet de film.
"""

import streamlit as st
from src.film_scheduler.models import Tache, Projet
from src.film_scheduler.scheduler import calcule_dates, duree_totale

projet = Projet(nom="Montage d'un film", taches=[
    Tache(nom="A", duree=30, predecesseurs=[]),
    Tache(nom="B", duree=12, predecesseurs=[("A", 15)]),
    Tache(nom="C", duree=8, predecesseurs=[("A", 20)]),
    Tache(nom="D", duree=4, predecesseurs=[("A", 0), ("C", 0)]),
    Tache(nom="E", duree=7, predecesseurs=[("C", 0), ("D", 0)]),
    Tache(nom="F", duree=10, predecesseurs=[("A", 0), ("B", 0), ("C", 0), ("D", 0)]),
    Tache(nom="G", duree=12, predecesseurs=[("D", 0), ("E", 0), ("F", 0)]),
    Tache(nom="H", duree=3, predecesseurs=[("F", 0), ("G", 0)]),
    Tache(nom="I", duree=14, predecesseurs=[("H", 0)]),
    Tache(nom="K", duree=6, predecesseurs=[("I", 0)]),
    Tache(nom="L", duree=1, predecesseurs=[("K", 2)]),
])

st.title("Planning du film")
st.write(f"Durée totale : **{duree_totale(projet)} jours**")

fins = calcule_dates(projet)
st.table([
    {"Tâche": nom, "Fin au jour": fin}
    for nom, fin in fins.items()
])