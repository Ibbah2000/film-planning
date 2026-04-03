"""Description.

Objets modélisant une tâche et un projet de planification.
"""

from pydantic import BaseModel, PositiveInt, model_validator


class Tache(BaseModel):
    """Modélise une tâche d'un projet.

    nom          : identifiant unique de la tâche (ex: 'A')
    duree        : durée en jours (doit être positive)
    predecesseurs: liste de (nom de la tâche, délai en jours)
    """

    nom: str
    duree: PositiveInt
    predecesseurs: list[tuple[str, int]] = []

    def __str__(self) -> str:
        """Affiche la tâche sous forme lisible."""
        lignes = [
            f"tache: {self.nom}",
            f"duree: {self.duree}j",
        ]
        for predecesseur, delai in self.predecesseurs:
            lignes.append(f"predecesseur: {predecesseur} + {delai}j")
        return "\n".join(lignes)


class Projet(BaseModel):
    """Modélise un projet comme un ensemble de tâches.

    nom   : nom du projet
    taches: liste des tâches du projet
    """

    nom: str
    taches: list[Tache] = []

    @model_validator(mode="after")
    def verifie_predecesseurs(self) -> "Projet":
        """Vérifie que tous les prédécesseurs existent dans le projet."""
        noms = {tache.nom for tache in self.taches}
        for tache in self.taches:
            for predecesseur, _ in tache.predecesseurs:
                if predecesseur not in noms:
                    raise ValueError(f"Prédécesseur '{predecesseur}' introuvable")
        return self

    def get_tache(self, nom: str) -> Tache:
        """Retourne une tâche par son nom."""
        for tache in self.taches:
            if tache.nom == nom:
                return tache
        raise ValueError(f"Tâche '{nom}' introuvable")