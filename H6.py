import cv2
import sys
from matplotlib import  pyplot as plt
import numpy as np

#to run file H6.py cat.jpg 150 50 50 200 50 50 200 50 100 200 100 50

input_ =[]
for i in sys.argv[1:] :
    try:
        input_.append(int(i))
    except:
        input_.append(i)

mage_path ,x1 ,y1 ,x2 ,y2, x3, y3 ,xp1,yp1 ,xp2 ,yp2 ,xp3 ,yp3= input_

img = cv2.imread(mage_path)
rows , cols , ch = img.shape

img = cv2.circle(img, (x1,y1), radius=5, color=(0, 0, 255),thickness=-1)
img = cv2.circle(img, (x2,y2), radius=5, color=(0, 255, 0),thickness=-1)
img = cv2.circle(img, (x3,y3), radius=5, color=(255, 0, 0),thickness=-1)

input = np.float32([[x1 ,y1],[x2 ,y2],[x3, y3]])
output = np.float32([[yp1 ,xp2],[xp2 ,yp2],[xp3 ,yp3]])

print(output)

M = cv2.getAffineTransform(input,output)
dst = cv2.warpAffine(img, M, (cols, rows)) 

plt.subplot()
plt.subplot(121), plt.imshow (img), plt.title ('Input') 
plt.subplot(122), plt.imshow (dst), plt.title ('Output')
plt.show()