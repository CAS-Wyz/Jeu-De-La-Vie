# Jeu-De-La-Vie

Ce projet implémente le célèbre **Jeu de la Vie** de John Conway, une simulation basée sur des règles simples où des cellules sur une grille évoluent au fil du temps. Le projet contient deux scripts Python : 

- `canonaplasma.py` : Implémente un canon à planeur (Gosper Glider Gun).
- `jeudelavie.py` : Implémente une version aléatoire du Jeu de la Vie.

## Contenu du projet

### 1. `canonaplasma.py`

Ce script initialise une grille contenant un canon à planeur, une structure qui génère des "planeurs" se déplaçant sur la grille. Il utilise la bibliothèque `matplotlib` pour afficher et animer la simulation.

#### Fonctionnalités principales :
- **Initialisation de la grille** : La fonction `initialize_grid(grid_size)` configure la grille avec la structure du canon à planeur.
- **Mise à jour de la grille** : La fonction `update(grid)` applique les règles du Jeu de la Vie pour calculer l'état suivant.
- **Animation** : La fonction `animate(frame, img, grid)` met à jour l'affichage à chaque étape.

#### Exécution :
Pour exécuter ce script, utilisez la commande suivante dans un terminal :
```bash
python [canonaplasma.py](http://_vscodecontentref_/0)
```
