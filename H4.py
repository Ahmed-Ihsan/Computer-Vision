import pathlib
import cv2
import sys

image_path = sys.argv[1:][0]

path = pathlib.PurePath(image_path)
print(path.suffix)

image = cv2.imread(image_path)
RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
RGB_img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

cv2.imshow('original',image)
cv2.imshow('Change',RGB_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Wrong'+path.suffix,RGB_img)