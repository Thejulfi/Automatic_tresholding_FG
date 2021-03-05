# Automatic_tresholding_FG

## test_bench.py

Le banc de test est là pour appliquer les algorithmes de seuillage automatique.

La première fonction que contient ce fichier est _display_results_. Cette dernière prend une image, applique respectivement l'algorithme de seuillage automatique **BHT**, **Otsu** et **MultiOtsu** puis retourne les tresholds trouvés pour ces dernières ainsi qu'une potentielle illustrant les résultats.

![Principe de fonction display_results](images/display_results_function.png)

La seconde fonction applique les seuils trouvés pour la méthode **BHT** et **Otsu** à l'image de départ (celle qui a permise de calculer les seuils).

![Principe de fonction output algos](images/output_algos_function.png)

### Résultats et interprétation 
