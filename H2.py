import cv2
import sys

def chack(*images):
    for img in images :
        if img[1] is None:
            print(f'Error in reading the image \"{img[0]}\"')
            sys.exit()

def show(*images):
    if len(images) == 1:
        cv2.imshow(images[0][0],images[0][1])
        cv2.waitKey(0)
    else:
        for img in images :
            cv2.imshow(img[0],img[1])
            cv2.waitKey(0)
    cv2.destroyAllWindows()

def shape(*images):
    if len(images) == 1:
        print(f'size the image \"{images[0][0]}\" : {images[0][1].shape}')
    else:
        for img in images :
            print(f'size the image \"{img[0]}\" : {img[1].shape}')

image1 = cv2.imread('cat.jpg')
image2 = cv2.imread('cat.jpg',0)

for img in (image1 , image2) :
    if img is None:
        print('Error in reading the image')

cv2.imshow("w_image1", image1)
cv2.imshow("w_image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('dimensions = ',image1.shape )  
print('total number of pixels = ',image1.size) 
print('number of channels = ', image1.shape[2])

print(image1[20][30])
print(image2[20][30])

print(image1[25][35])
image1[25][35] = [0,0,0]
print(image1[25][35])

print(image2[25][35])
image2[25][35] = 0
print(image2[25][35])

image1[30] = 0
image2[30] = 0 

image1[35:140,35:50] = [255,0,0]

cv2.imshow("w_image1", image1)
cv2.imshow("w_image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()