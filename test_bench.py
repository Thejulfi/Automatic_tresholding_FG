import Otsu
import Balanced_histogram_tresholding
from skimage import data, io, img_as_ubyte
from skimage.filters import threshold_multiotsu
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def test(image):
    for i in range(3):
        print(i)
        if (i==0):
            print('bht')
            im = cv.imread(image,0)
            weight_init = 50
            thr = Balanced_histogram_tresholding.bht(im, weight_init)
        elif (i==1):
            print('mutli otsu')
            im = cv.imread(image, 0)
            # im = io.imread(image,0)
            # b,g,r = cv.split(im)
            thr = threshold_multiotsu(im, classes=3)
            regions = np.digitize(im, bins=thr)
            output = img_as_ubyte(regions)  #Convert 64 bit integer values to uint8
        else:
            print('otsu')
            im = cv.imread(image,0)
            # im_flat = np.reshape(image,(image.shape[0]*image.shape[1]))
            thr = Otsu.otsu(im)


        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))

        ax[0].imshow(im, cmap='gray')
        ax[0].set_title('Original')
        ax[0].axis('off')

        ax[1].hist(im.ravel(), bins=255)
        ax[1].set_title('Histogram')
        if(i==1):
            for thresh in thr:
                ax[1].axvline(thresh, color='r')
                ax[1].text(thresh + 3, 150,str(thresh),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')
        else:
            ax[1].axvline(thr, color='r')
            ax[1].text(thr + 3, 150,str(thr),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')

        if(i==1):
            ax[2].imshow(regions, cmap='Accent')
        else:
            ax[2].imshow(im > thr, cmap = 'gray')
        
        ax[2].set_title("Result")
        ax[2].axis('off')

        plt.subplots_adjust()
        if(i==2):
            plt.show(block=True)
        else:
            plt.show(block=False)




test("data/J+12_PM_GA.jpg")