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
        # print(hist[h_s])
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
image = cv.imread("data/J+12_PM_GA.jpg",0)

'''Création de l'histogramme'''
hist = cv.calcHist(image,[1],None,[256],[0,256])
hist = hist.astype(int)

'''Paramètre de départ pour bht'''
weight_init = 20

'''Affichage du seuil trouvé'''
# print(bht(histo, weight_init))
thr = bht(hist, weight_init)


print("Threshold: {}".format(thr))

#Let us look at the input image, thresholds on thehistogram and final segmented image
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))

# Plotting the original image.
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original')
ax[0].axis('off')

# Plotting the histogram and the two thresholds obtained from
# multi-Otsu.
ax[1].hist(image.ravel(), bins=255)
ax[1].set_title('Histogram')
ax[1].axvline(thr, color='r')
ax[1].text(thr + 3, 150,str(thr),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')

# Plotting the original image.
ax[2].imshow(image > thr, cmap='gray')
ax[2].set_title('Original')
ax[2].axis('off')

plt.subplots_adjust()

plt.show()
