# Film Planning

Outil de planification de projet par la méthode du chemin critique (CPM).

## Le problème exemple

Un producteur de cinéma doit planifier les tâches suivantes :

| Tâche | Nature | Durée (jours) | Prérequis |
|-------|--------|---------------|-----------|
| A | Ecriture du scénario | 30 | - |
| B | Casting | 12 | fin A + 15j |
| C | Choix du lieu de tournage | 8 | fin A + 20j |
| D | Découpage technique | 4 | A et C finies |
| E | Décors | 7 | C et D finies |
| F | Tournages extérieurs | 10 | A, B, C et D finies |
| G | Tournages intérieurs | 12 | D, E et F finies |
| H | Synchronisation | 3 | F et G finies |
| I | Montage | 14 | H finie |
| J | Son | 7 | début I + 3j et fin H |
| K | Mixage | 6 | I et J finies |
| L | Tirage | 1 | fin K + 2j |

## Démonstration

Voici le résultat obtenu en entrant ces tâches dans l'interface :

![Interface Streamlit](images/streamlit.png)
Remplace le début de ton README par ça et dis-moi quand c'est fait ! 🚀

## Démonstration

Voici le résultat obtenu en entrant les 12 tâches du film dans l'interface :

![Interface Streamlit](images/streamlit.png)

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

Résultat :