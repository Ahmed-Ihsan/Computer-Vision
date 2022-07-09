import cv2
# import numpy as np
# from threading import Thread

def resize(img):
        return cv2.resize(img,(500,500))

video = cv2.VideoCapture(0)
ok,frame=video.read()
frame = resize(frame)

def draw(frame , x=0 , y=0 , n=1, l= 1):
    p1 =  int(x) , int(y-30)
    frame = cv2.rectangle(frame,(p1),(p1[0]+1,p1[1]+60),(0,0,255),-1)
    p1 =  int(x-30) , int(y)
    frame = cv2.rectangle(frame,(p1),(p1[0]+60,p1[1]+1),(0,0,255),-1)
    p1 =  int(frame.shape[1]/2) , int(frame.shape[0]/2)
    frame = cv2.circle(frame,(p1),3,(0,0,255),-1)
    p1 =  int(frame.shape[1]/2) , int(frame.shape[0]/2)
    frame = cv2.circle(frame,(p1),45,(0,0,255),2)
    frame = cv2.circle(frame,(p1),30,(255,255,255),2)
    frame = cv2.circle(frame,(p1),15,(0,255,0),2)
    p1 =  [0 , 0]
    p2 = 0
    cont = 0
    x = 25
    list_an = list(range(n-5,n+5,1))
    list_an2 = list(range(l-5,l+5,1))
    index = 0
    frame = cv2.putText(img=frame, text=f'{list_an[index]%360}', org=(p1[0]-2,0+35),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.3, color=(0, 255, 255),thickness=1)
    for i in range(int(frame.shape[1]/10)):
        cont+=1
        if i == 25:
            frame = cv2.rectangle(frame,(p1[0],p1[1]+60),(p1[0]+3,250),(0,0,255),-1)
            frame = cv2.rectangle(frame,(250,p2),(60,p2+3),(0,0,255),-1)

            frame = cv2.rectangle(frame,(p1),(p1[0],x),(0,0,255),-1)
            frame = cv2.rectangle(frame,(x,p2),(0,p2),(0,0,255),-1)
        else:
            frame = cv2.rectangle(frame,(p1),(p1[0],x),(255,255,255),-1)
            frame = cv2.rectangle(frame,(x,p2),(0,p2),(255,255,255),-1)
        if cont == 5:
            cont = 0
            x = 25
            frame = cv2.putText(img=frame, text=f'{list_an[index]%360}', org=(p1[0]+8,0+35),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.3, color=(0, 255, 255),thickness=1)
            frame = cv2.putText(img=frame, text=f'{list_an2[index]%360}', org=(35,p2+12),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.3, color=(0, 255, 255),thickness=1)
            index +=1
        else:
            x = 15
        p1[0] += 10
        p2 += 10
    index= 0
    return frame

pos_x=0
pos_y=0
speed = 0.5
dataObj = dict()
def click_event(event, x, y, flags, params):
    global pos_x , pos_y , frame_copy ,speed
    pos_x = x
    pos_y = y
    if event == 1:
        for i in range(1):
            dataObj[f"Tracker{i}"] = cv2.TrackerKCF_create()
            dataObj[f"bbox{i}"]= cv2.selectROI('Tracking',frame_copy)
            dataObj[f"ok{i}"] = dataObj[f"Tracker{i}"].init(frame_copy,dataObj[f"bbox{i}"])
    if event == 2:
        if speed >= 1:
            speed = 0.1
        else:
            speed += 0.1

pos_x , pos_y= frame.shape[0],frame.shape[1]
n2 = 1
l2=1
l=1
n = 1
while 1:
    k,frame=video.read()
    frame = resize(frame)
    frame_copy = frame.copy()
    if len(dataObj) > 0:
        for i in range(1):
            dataObj[f"ok{i}"],dataObj[f"bbox{i}"]=dataObj[f"Tracker{i}"].update(frame)
            if dataObj[f"ok{i}"]:
                (x,y,w,h)=[int(v) for v in dataObj[f"bbox{i}"]]
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
    frame = draw(frame, pos_x, pos_y , n ,l)
    cv2.imshow('Tracking',frame)
    cv2.setMouseCallback('Tracking', click_event)
    cv2.waitKey(1)
    if pos_x  < frame.shape[1]/2 - frame.shape[1]/3 :
        n2 -= speed
    elif pos_x  > frame.shape[1]/2 +  frame.shape[1]/3 :
        n2 += speed
    if n2 == 360 or n2 == -360 :
        n2=0
    n = int(n2)
    if pos_y  < frame.shape[0]/2 - frame.shape[0]/3 :
        l2 -= speed
    elif pos_y  > frame.shape[0]/2 +  frame.shape[0]/3 :
        l2 += speed

    if l2 == 360 or l2 == -360 :
        l2=0
    l= int(l2)
