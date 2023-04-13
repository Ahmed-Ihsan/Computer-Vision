# Get set up
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Capture3.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Fixes color read issue

av3 = cv2.blur(img,(3,3))
av5 = cv2.blur(img,(5,5))

# Plot the image. This code is excluded for the rest of the article.
plt.gcf().set_size_inches(25,25)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(av3),plt.title('Averaging - 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(av5),plt.title('Averaging - 5x5')
plt.xticks([]), plt.yticks([])
plt.show()

def noisy(image):

    row,col,ch = image.shape
    s_vs_p = 0.0005
    amount = 0.04
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in image.shape]
    for i in coords:
        print(i)
        out[i] = [np.random.randint(0,245),np.random.randint(0,245),np.random.randint(0,245)]
        
    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in image.shape]
    for i in coords:
        print(i)
        out[i] = [np.random.randint(0,245),np.random.randint(0,245),np.random.randint(0,245)]
    return out

img = cv2.imread("Capture3.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

from wand.image import Image
 
# Read image using Image() function
with Image(filename ="koala.jpeg") as img:
 
    # Generate noise image using noise() function
    img.noise("laplacian", attenuate = 1.0)
noisy_img = noisy(img)
median = cv2.medianBlur(img,5)

plt.gcf().set_size_inches(25,25)
plt.subplot(131),plt.imshow(noisy_img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.show()


