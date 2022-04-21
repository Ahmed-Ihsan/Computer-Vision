import math

# xCenter = (x1 + x2) / 2
# yCenter = (y1 + y2) / 2

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

print(calculateDistance(20, 20, 20, 20))
