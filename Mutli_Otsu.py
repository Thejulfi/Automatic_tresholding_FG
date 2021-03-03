import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

from skimage import data, io, img_as_ubyte
from skimage.filters import threshold_multiotsu


image = cv.imread("data/J+12_PM_GA.jpg",0)

# b,g,r = cv.split(image)

 
thresholds = threshold_multiotsu(image, classes=3)

# Digitize (segment) original image into multiple classes.
#np.digitize assign values 0, 1, 2, 3, ... to pixels in each class.
regions = np.digitize(image, bins=thresholds)
output = img_as_ubyte(regions)  #Convert 64 bit integer values to uint8

#plt.imsave("Otsu_Segmented.jpg", output)

for thr,i in enumerate(thresholds):
    print("Threshold #{}: {}".format(thr,i))

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
for thresh in thresholds:
    ax[1].axvline(thresh, color='r')
    ax[1].text(thresh + 3, 150,str(thresh),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')

# Plotting the Multi Otsu result.
ax[2].imshow(regions, cmap='Accent')
ax[2].set_title('Multi-Otsu result')
ax[2].axis('off')

plt.subplots_adjust()
plt.show()
