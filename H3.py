import cv2
import sys

image , image_up , image_right = sys.argv[1:]

image = cv2.imread(image)
y , x , _ = image.shape

yy = int(50 * y/100)
image2 = image[:yy,:]

xx = int(50 * x/100)
image3 = image[:,xx:]

cv2.imshow('iamg1', image)
cv2.imshow('imag2', image2)
cv2.imshow('image3', image3)

cv2.imwrite(image_up,image2)
cv2.imwrite(image_right,image3)

cv2.waitKey(0)
cv2.destroyAllWindows()