# Automatic_tresholding_FG

## test_bench.py

### Principe de fonctionnement

Le banc de test est là pour appliquer les algorithmes de seuillage automatique.

La première fonction que contient ce fichier est _display_results_. Cette dernière prend une image, applique respectivement l'algorithme de seuillage automatique **BHT**, **Otsu** et **MultiOtsu** puis retourne les tresholds trouvés pour ces dernières ainsi qu'une potentielle illustrant les résultats.

![Principe de fonction display_results](images/display_results_function.png)

La seconde fonction applique les seuils trouvés pour la méthode **BHT** et **Otsu** à l'image de départ.

![Principe de fonction output algos](images/output_algos_function.png)

La dernière fonction permet de comparer les résultats du seuillage par rapport à une image de référence. Pour ce faire, elle compte le nombre de pixels non noir de l'image de référence et le divise par le nombre de pixels non noir de l'image seuillée (généralement issue de la fonction précédente).

![Principe de fonction comptage pixels](images/comptage_pixels_function.png)

### Fonctionnement

La fonction **displaying_results** s'utilise selon les deux arguments suivant : 
1. im : Une image en niveau de gris,
2. . showR : Un booléen, vrai pour afficher les résultats à l'écran (avec MatPlotLib), Faux pour ne rien afficher.

Prenons l'exemple d'une image préalablement divisé en canaux HSV. En appliquant la fonction sur le canal *Hue* avec le paramètre *ShowR* à 0, voici ce que nous obtenons.

`displaying_results(hue, 1)`

![fonction displaying results sur canal hue](images/displaying_results_hue.png)

Si on décide de retirer cet affichage, on obtient seulement le tableau des seuils comme indiqué dans la section sur le principe de fonctionnement.

`displaying_results(hue, 0)`

### Tests

Avec le banc de test on peut tester les images une par une pour les différents algorithme.
