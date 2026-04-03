"""Description.

Calcul du planning optimal d'un projet.
"""

from src.film_scheduler.models import Projet


def calcule_dates(projet: Projet) -> dict[str, int]:
    """Donne la date de fin au plus tôt pour chaque tâche."""
    fins = {}
    taches_restantes = list(projet.taches)

    while taches_restantes:
        for tache in taches_restantes:
            if all(p in fins for p, _ in tache.predecesseurs):
                debut = max(
                    (fins[p] + delai for p, delai in tache.predecesseurs),
                    default=0,
                )
                fins[tache.nom] = debut + tache.duree
                taches_restantes.remove(tache)
                break

    return fins


def duree_totale(projet: Projet) -> int:
    """Donne la durée totale du projet en jours."""
    fins = calcule_dates(projet)
    return max(fins.values())