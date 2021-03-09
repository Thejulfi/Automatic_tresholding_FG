import numpy as np
import cv2
from matplotlib import pyplot as plt

def otsu(im):
    [hist, _] = np.histogram(im, bins=256, range=(0, 255))
    # Normalization so we have probabilities-like values (sum=1)
    hist = 1.0*hist/np.sum(hist)

    val_max = -999
    thr = -1

    for t in range(1,255):
        # Non-efficient implementation
        q1 = np.sum(hist[:t])
        q2 = np.sum(hist[t:])
        m1 = np.sum(np.array([i for i in range(t)])*hist[:t])/q1
        m2 = np.sum(np.array([i for i in range(t,256)])*hist[t:])/q2
        val = q1*(1-q1)*np.power(m1-m2,2)
        if val_max < val:
            val_max = val
            thr = t
    return thr



# image = cv2.imread("data/J+12_PM_GA.jpg",0)
# im_flat = np.reshape(image,(image.shape[0]*image.shape[1]))

# thr = otsu(image)

# print("Threshold: {}".format(thr))

# fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))

# ax[0].imshow(image, cmap='gray')
# ax[0].set_title('Original')
# ax[0].axis('off')

# ax[1].hist(image.ravel(), bins=255)
# ax[1].set_title('Histogram')
# ax[1].axvline(thr, color='r')
# ax[1].text(thr + 3, 150,str(thr),rotation=0, bbox=dict(facecolor='red', alpha=0.5), color='white', fontweight='bold')

# ax[2].imshow(image > thr, cmap = 'gray')
# ax[2].set_title("Otsu result")
# ax[2].axis('off')

# plt.subplots_adjust()
# plt.show()

print("cc")
print("cc bg, synchronise là!!!")