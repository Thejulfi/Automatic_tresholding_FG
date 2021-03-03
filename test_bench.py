import Otsu
import Balanced_histogram_tresholding
from skimage.filters import threshold_multiotsu

from skimage import data, io, img_as_ubyte
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def displaying_results(images, showR=0):
    algos = ['bht', 'mutli otsu', 'otsu']

    for image in images:
        print("\n")
        fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10, 3.5), constrained_layout=True)
        for i in range(len(algos)):
            if (i==0):
                # print('bht')
                im = cv.imread(image,0)
                weight_init = 50
                thr = Balanced_histogram_tresholding.bht(im, weight_init)
            elif (i==1):
                # print('mutli otsu')
                im = cv.imread(image, 0)
                # im = io.imread(image,0)
                # b,g,r = cv.split(im)
                thr = threshold_multiotsu(im, classes=3)
                regions = np.digitize(im, bins=thr)
                output = img_as_ubyte(regions)  #Convert 64 bit integer values to uint8
            else:
                # print('otsu')
                im = cv.imread(image,0)
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
                # if(i==2):
                #     plt.show(block=True)
                # else:
                #     plt.show(block=False)
            else:
                print("Treshold #{} = {}".format(algos[i],thr))
        plt.show()


my_images = ["data/J+12_PM_GA.jpg"]
displaying_results(my_images, 1)