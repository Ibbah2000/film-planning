
"""Description.

Tests unitaires du module models.py
"""

import pytest
from src.film_scheduler.models import Tache, Projet


def test_tache_duree_negative():
    with pytest.raises(Exception):
        Tache(nom="A", duree=-5, predecesseurs=[])


def test_tache_duree_nulle():
    with pytest.raises(Exception):
        Tache(nom="A", duree=0, predecesseurs=[])


def test_projet_tache_introuvable():
    projet = Projet(nom="Film", taches=[
        Tache(nom="A", duree=30, predecesseurs=[])
    ])
    with pytest.raises(ValueError):
        projet.get_tache("Z")


def test_projet_predecesseur_introuvable():
    with pytest.raises(Exception):
        Projet(nom="Film", taches=[
            Tache(nom="B", duree=12, predecesseurs=["Z"])
        ])