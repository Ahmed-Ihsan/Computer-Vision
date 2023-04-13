import cv2
import matplotlib.pyplot as plt  
 
 
file = "Capture4.JPG"
img0 = cv2.imread(file)
img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show() 
 
gaussian = cv2.GaussianBlur(img, (5, 5), 5)
plt.imshow(gaussian)
plt.show()  

median = cv2.medianBlur(img, 7)
plt.imshow(median)
plt.show()  
 
bilateral = cv2.bilateralFilter(img, 7, 75, 75)
plt.imshow(bilateral)
plt.show()    
 
averaging = cv2.blur(img, (5, 7))
plt.imshow(averaging)
plt.show()     

 
gaussian = cv2.GaussianBlur(img, (15, 15), 5)
median = cv2.medianBlur(img, 25)
bilateral = cv2.bilateralFilter(img, 21,61,61)
average = cv2.blur(img, (25,25))

blurs = { 
    "Gaussian blur":gaussian,
    "Median blur": median,
    "Average blur": average,
    "Bilateral blur": bilateral }

i = 0
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
for row in range(2):
    for col in range(2):
        ax[row][col].imshow(list(blurs.values())[i])
        ax[row][col].set_title(list(blurs.keys())[i], fontsize=20)
        ax[row][col].axis('off')
        i = i + 1
        
plt.tight_layout()        
plt.show()      
