# Film Planning

Outil de planification de projet par la méthode du chemin critique (CPM).

## Installation
```bash
git clone https://github.com/Ibbah2000/film-planning.git
cd film-planning
uv sync
```

## Utilisation

### Interface graphique
```bash
streamlit run app.py
```

### Interface en ligne de commande
```bash
python cli.py "Mon Film"
```

## Exemple

Le projet exemple est le montage d'un film avec 11 tâches.

Résultat : 
```
Tâche A : finit au jour 30
Tâche B : finit au jour 57
Tâche C : finit au jour 58
Tâche D : finit au jour 62
Tâche E : finit au jour 69
Tâche F : finit au jour 72
Tâche G : finit au jour 84
Tâche H : finit au jour 87
Tâche I : finit au jour 101
Tâche K : finit au jour 107
Tâche L : finit au jour 110
Durée totale : 110 jours
```

## Tests
```bash
pytest tests/ -v
```