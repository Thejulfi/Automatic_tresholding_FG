import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#seuil automatique par la méthode BHT.
def bht(hist, min_count: int = 5):
    """Balanced histogram thresholding."""
    n_bins = len(hist)
    h_s = 0

    #Tant que la valeur de teinte est inférieur à "min_count", h_s + 1 -> Cela donne la valeur de teinte partie inférieur.
    while hist[h_s] < min_count:
        h_s += 1
    #h_e = 255
    h_e = n_bins - 1
    #Tant que la valeur de teinte est inférieur à "min_count", h_e - 1 -> Cela donne la valeur de teinte partie supérieur.
    while hist[h_e] < min_count:
        h_e -= 1
    #Création d'un tableau de dimension 1 pour stocker le contenu de l'histogramme.
    table = np.zeros((256))
    for i in range(256):
        table[i] = hist[i][0]
    
    #Moyenne des valeurs inférieure et supérieure. - MÉTHODE 1
    #h_c = (h_s + h_e) / 2

    #Moyenne des valeurs inférieure et supérieure. - MÉTHODE 2
    #Arrondie de la mise en moyenne du tableau pondéré par les valeurs de tables.
    h_c = int(round(np.average(np.linspace(0, 2 ** 8 - 1, n_bins),weights=table)))

    #Somme des poids de la partie de gauche jusqu'à la teinte inférieur et supérieur.
    w_l = np.sum(hist[int(h_s):int(h_c)])
    w_r = np.sum(hist[int(h_c): int(h_e + 1)])

    while h_s < h_e:
        if w_l > w_r:  # left part became heavier
            w_l -= hist[h_s]
            h_s += 1
        else:  # right part became heavier
            w_r -= hist[h_e]
            h_e -= 1
        new_c = int(round((h_e + h_s) / 2))  # re-center the weighing scale

        if new_c < h_c:  # move bin to the other side
            w_l -= hist[h_c]
            w_r += hist[h_c]
        elif new_c > h_c:
            w_l += hist[h_c]
            w_r -= hist[h_c]

        h_c = new_c

    return h_c

'''Chargement de l'image'''
img = "data/Stade_12_1.10.png"
image = cv.cvtColor(cv.imread(img),cv.COLOR_BGR2RGB)

'''Création de l'histogramme'''
histo = cv.calcHist(image,[1],None,[256],[0,256])
histo = histo.astype(int)

'''Paramètre de départ pour bht'''
weight_init = 50

'''Affichage du seuil trouvé'''
print(bht(histo, weight_init))

