import Otsu
import Balanced_histogram_tresholding
from skimage.filters import threshold_multiotsu

from skimage import data, io, img_as_ubyte
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def displaying_results(im, showR=0):
    algos = ['bht', 'mutli otsu', 'otsu']
    thr_res = np.ndarray((4,1), int)
    masks = []
    # for image in images:

    if (showR):
        fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10, 3.5), constrained_layout=True)
    c=0
    for i in range(len(algos)):
        if (i==0):
            # print('bht')
            # im = cv.imread(image,0)
            weight_init = 50
            thr = Balanced_histogram_tresholding.bht(im, weight_init)
        elif (i==1):
            # print('mutli otsu')
            # im = cv.imread(image, 0)
            # im = io.imread(image,0)
            # b,g,r = cv.split(im)  
            thr = threshold_multiotsu(im, classes=3)
            regions = np.digitize(im, bins=thr)
            output = img_as_ubyte(regions)  #Convert 64 bit integer values to uint8
        else:
            # print('otsu')
            # im = cv.imread(image,0)
            # im_flat = np.reshape(image,(image.shape[0]*image.shape[1]))
            thr = Otsu.otsu(im)

        if(showR):
            
            ax[i][0].imshow(im, cmap='gray')
            ax[i][0].set_title('Original {}'.format(algos[i]))
            ax[i][0].set_ylabel("test")
            ax[i][0].axis('off')

            ax[i][1].hist(im.ravel(), bins=255)
            ax[i][1].set_title('Histogram')
            if(i==1):
                for thresh in thr:
                    ax[i][1].axvline(thresh, color='r')
                    ax[i][1].text(thresh + 3, 150,str(thresh),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')
            else:
                ax[i][1].axvline(thr, color='r')
                ax[i][1].text(thr + 3, 150,str(thr),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')

            if(i==1):
                ax[i][2].imshow(regions, cmap='Accent')
            else:
                ax[i][2].imshow(im > thr, cmap = 'gray')
            
            ax[i][2].set_title('Result {}'.format(algos[i]))
            ax[i][2].axis('off')

            plt.subplots_adjust()
            print(thr)
        # else:
        if(c ==1):
            thr_res.put(c, thr[0])
            c+=1
            thr_res.put(c, thr[1])
            c+=1
        else:
            thr_res.put(c, thr)
            c+=1

            # masks.append((im > thr))

    if (showR):
        plt.show()
    # else:
    return thr_res
    
def output_algos(thresholds, im):
    output = []
    for i in thresholds:
        output.append((im>i)*im)
    return output

def compare_hist(img_ref, img):
    hist1 = cv.calcHist(img_ref,[1],None,[256],[1,256])
    plt.plot(hist1,color = 'r')
    plt.plot(hist1)
    hist2 = cv.calcHist(img,[1],None,[256],[1,256])
    plt.plot(hist2,color = 'b')
    plt.plot(hist2)
    for i in range(len(hist1)):
        if(hist2[i] < hist1[i]):
            plt.axvline(i, color='r', alpha=0.2, linewidth=1)
    plt.show()

def comptage_pixels(img_ref,img):
    ratio = np.sum(img!= 0) / np.sum(img_ref!= 0)
    return ratio
    
im_graal = cv.imread("data/Graal_J+12_PM_GA.jpg", 0)

# '''Test pour la canal vert'''

# image = cv.imread('data/J+12_PM_GA.jpg')

# b,g,r = cv.split(image)

# result_algos = displaying_results(g, 1)
# output_images = output_algos(result_algos, g)

# print("Ratio pixels pour BHT : {}".format(comptage_pixels(im_graal, output_images[1])))
# print("Ratio pixels pour Otsu : {}".format(comptage_pixels(im_graal, output_images[3])))

# '''Test en grayscale'''

# im_graal = cv.imread("data/Graal_J+12_PM_GA.jpg", 0)

# image = cv.imread('data/J+12_PM_GA.jpg', 0)

# result_algos = displaying_results(image, 1)
# output_images = output_algos(result_algos, image)

# print("Ratio pixels pour BHT : {}".format(comptage_pixels(im_graal, output_images[1])))
# print("Ratio pixels pour Otsu : {}".format(comptage_pixels(im_graal, output_images[3])))


'''Test avec canal Hue'''

image = cv.imread('data/J+12_PM_GA.jpg')

hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
hue,sat,val = cv.split(hsv)

result_algos = displaying_results(hue, 1) 
output_images = output_algos(result_algos, hue)

print("Ratio pixels pour Otsu : {}".format(comptage_pixels(im_graal, output_images[3])))
