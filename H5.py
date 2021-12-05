import cv2
import matplotlib.pyplot as plt
import numpy as np


# fig  = plt.figure(figsize=(600,400),dpi=100,facecolor = (0.5,0.5,0.5))
# plt.show()

image = np.zeros((400,600,3), np.uint8)
image[:,:] = (127,127,127)      # (B, G, R)
# cv2.imshow('aa' , image)
# cv2.waitKey(0)

start_point , end_point  ,color ,thickness = (30, 40) , (300, 200) ,(0, 0, 255),5
image = cv2.line(image, start_point, end_point, color, thickness)

center , radius  ,color ,thickness = (300, 200) ,100,(255, 0, 0),5
image = cv2.circle(image, center, radius, color, thickness)

pt1 , pt2  ,color ,thickness = (70, 80) ,(170,280),(0, 255, 250),5
image = cv2.rectangle(image, pt1, pt2, color, thickness)

cv2.imshow('image' , image)
plt.imshow(image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
