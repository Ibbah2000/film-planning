"""Description.

Interface en ligne de commande pour planifier un projet.
"""

import typer
from src.film_scheduler.models import Tache, Projet
from src.film_scheduler.scheduler import calcule_dates, duree_totale

app = typer.Typer()


@app.command()
def planifier(nom: str = typer.Argument(help="Nom du projet")):
    """Calcule et affiche le planning d'un projet exemple."""
    projet = Projet(nom=nom, taches=[
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

    fins = calcule_dates(projet)
    for tache, fin in fins.items():
        typer.echo(f"Tâche {tache} : finit au jour {fin}")

    typer.echo(f"\nDurée totale : {duree_totale(projet)} jours")


if __name__ == "__main__":
    app()