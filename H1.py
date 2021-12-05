import cv2
import sys
import matplotlib.pyplot as plt

read_image = ('cat.jpg','color_spaces.jpg','landscape.jpg')
image1 = cv2.imread(read_image[0])
image2 = cv2.imread(read_image[1])
image3 = cv2.imread(read_image[2])

for img in (read_image,[image1 , image2, image3]) :
        if img[1] is None:
            print(f'Error in reading image \"{img[0]}\"')

cv2.imshow("w_image1", image1)
cv2.imshow("w_image2", image2)
cv2.imshow("w_image3", image3)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'size the image \"cat.jpg\" : {image1.shape}')

image4 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

cv2.imshow("w_image4", image4)
cv2.waitKey(0)
cv2.destroyAllWindows()

fig = plt.figure(figsize=(10, 7))
for i in zip(read_image+('cat_gray.png',),[1,2,3,4],[image1 , image2, image3 ,image4]) :
    fig.add_subplot(2, 2, i[1])
    print(i[0])
    if 'cat_gray' in i[0]:
        plt.imshow(i[2],cmap ='gray')
    else:
        plt.imshow(i[2])
    plt.axis('off')
    plt.title(i[0])
plt.show()