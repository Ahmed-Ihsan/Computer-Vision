# import necessary libraries

import cv2
import sys
from matplotlib import  pyplot as plt
import numpy as np

input_ =[]
for i in sys.argv[1:] :
    try:
        input_.append(int(i))
    except:
        input_.append(i)

mage_path ,x1 ,y1 ,x2 ,y2, x3, y3 ,x4,y4 ,xp1,yp1 ,xp2 ,yp2 ,xp3 ,yp3,xp4 ,yp4 = input_
    
img = cv2.imread(mage_path) 
rows , cols , ch = img.shape

img = cv2.circle(img, (x1,y1), radius=5, color=(0, 0, 255),thickness=-1)
img = cv2.circle(img, (x2,y2), radius=5, color=(0, 255, 0),thickness=-1)
img = cv2.circle(img, (x3,y3), radius=5, color=(255, 0, 0),thickness=-1)
img = cv2.circle(img, (x4,y4), radius=5, color=(255, 255, 0),thickness=-1)

pts1 = np.float32([[x1,y1], [x2,y2], [x3,y3], [x4,y4]])
pts2 = np.float32([[xp1,yp1], [xp2 ,yp2], [xp3 ,yp3], [xp4 ,yp4]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, matrix, (90, 240))

# cv2.imshow('frame', img) 
# cv2.imshow('frame1', result) 

# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.subplot(121)
plt.imshow(img)
plt.title ('original') 
plt.subplot(122)
plt.imshow (result)
plt.title ('Output')
plt.show()