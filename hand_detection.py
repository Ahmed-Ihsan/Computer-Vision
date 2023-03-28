import cv2             #type in the shell pip install cv2
import mediapipe as mp  # type in the shell pip install mediapipe
import time             
import numpy as np

read = 'image'
capvide =''

if read == 'video':
    capvide = cv2.VideoCapture('vide.mp4')
elif read == 'image':
    pass
    
def removeBlack(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold the image based on Value channel
    lower_value = np.array([0, 0, 0], dtype=np.uint8)
    upper_value = np.array([10, 10, 10], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_value, upper_value)

    # Invert the mask to get the black background
    mask = cv2.bitwise_not(mask)

    # Extract the object from the black background
    result = cv2.bitwise_and(img, img, mask=mask)
    
    return result

def rotedImage(img):
        # Get the height and width of the image
    height, width = img.shape[:2]

    # Define the rotation angle in degrees
    angle = 180

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

    # Rotate the image
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    return rotated_img

def readimageinsert(dist):
    global capvide ,read
    
    if read == 'video':
        ret, imgInsert = capvide.read()
        if not ret:
            capvide = cv2.VideoCapture('vide.mp4')
    elif read == 'image':
        imgInsert = cv2.imread('M1.png')
   

    #imgInsert = removeBlack(imgInsert)
        
    # percent of original size
    try:

        #print(int(dist)- 20)
        if (int(dist) - 20 >= 0) and (int(dist) - 60 < 7) :
            scale_percent = 5
        elif (int(dist) - 20 >= 7) and (int(dist) - 60 < 8) :
            scale_percent = 7
        elif (int(dist) - 20 >= 8) and (int(dist) - 60 < 10) :
            scale_percent = 8
        elif (int(dist) - 20 >= 10) and (int(dist) - 60 < 12) :
            scale_percent = 10
        elif (int(dist) - 20 >= 12) and (int(dist) - 60 < 14) :
            scale_percent = 12
        elif (int(dist) - 20 >= 0) and (int(dist) - 60 < 7) :
            scale_percent = 14
        else:
            scale_percent = 16
    except:
        scale_percent = 0
    width = int(imgInsert.shape[1] * scale_percent / 100)
    height = int(imgInsert.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    imgInsert = cv2.resize(imgInsert, dim, interpolation = cv2.INTER_AREA)

    return imgInsert

def insert(img2 ,img1 ,y,x):
    # Get the size of the images
    rows, cols, channels = img2.shape

    # Define the roi for inserting the second image
    roi = img1[0:rows, 0:cols ]

    # Create a mask for the second image
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Black out the area of the roi
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # Take the bitwise and of the second image with the mask
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # Add the two images
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols ] = dst
    
    return dst

def insert2(img2 ,img1 ,x,y):
    # Define x and y coordinates for placing img2 on img1
    #x, y = 100, 100

    # Add img2 to img1 at x, y position
    img_result = cv2.addWeighted(img1[y:y+img2.shape[0], x:x+img2.shape[1], :], 1 , img2, 1, 0)

    # Paste the result back on img1
    img1[y:y+img2.shape[0], x:x+img2.shape[1], :] = img_result
    
    # Show the final image
    return img1

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = rotedImage(img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            points = []          
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                points.append([cx, cy]) 
                cv2.circle(img, (cx,cy), 3, (255,0,0), cv2.FILLED)
            #insert(imgInsert ,img,x,y)
            try:
                point1 = np.array(points[-17], dtype = np.float32)
                point2 = np.array(points[-13], dtype = np.float32)
                distance = cv2.norm(point1 - point2)
                cv2.line(img, points[-17], points[-13], (0, 255, 0), thickness=2)
                imgInsert = readimageinsert(distance )
                img = insert2(imgInsert ,img ,points[-17][0],points[-17][1])
                #img = insert2(imgInsert ,img ,points[-1][0],points[-1][1])
            except:
                pass
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
