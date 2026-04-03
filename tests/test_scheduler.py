"""Description.

Tests unitaires du module scheduler.py
"""

from src.film_scheduler.models import Tache, Projet
from src.film_scheduler.scheduler import calcule_dates, duree_totale


def test_calcule_dates_simple():
    projet = Projet(nom="Test", taches=[
        Tache(nom="A", duree=10, predecesseurs=[]),
        Tache(nom="B", duree=5, predecesseurs=["A"]),
    ])
    fins = calcule_dates(projet)
    assert fins["A"] == 10
    assert fins["B"] == 15


def test_duree_totale():
    projet = Projet(nom="Test", taches=[
        Tache(nom="A", duree=10, predecesseurs=[]),
        Tache(nom="B", duree=5, predecesseurs=["A"]),
    ])
    assert duree_totale(projet) == 15


def test_calcule_dates_deux_predecesseurs():
    projet = Projet(nom="Test", taches=[
        Tache(nom="A", duree=10, predecesseurs=[]),
        Tache(nom="B", duree=20, predecesseurs=[]),
        Tache(nom="C", duree=5, predecesseurs=["A", "B"]),
    ])
    fins = calcule_dates(projet)
    assert fins["C"] == 25