
import numpy as np
import cv2

dir = 'C:/Users/lfkop/Desktop/imagensalvo/'
kernel = np.ones((5,5),np.uint8)
for i in range(1,4):
    img = cv2.imread(dir + str(i) + '.dib')
    img = cv2.resize(img, (0,0), fx=3, fy=3)
    gray = img[:,:,0]
    mask = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)[1]
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in cnts:
        (x,y),r = cv2.minEnclosingCircle(c)
        center = (int(x),int(y))
        r = int(r)-2
        if r > 120:
            cv2.circle(img,center,r,(0, 0, 244),2)
            break
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(img, maxLoc, 10, (255, 0, 0), 2)
    #cv2.circle(img, center, 10, (255, 255, 0), 2)
    cv2.line(img, maxLoc, center, (255,0,255))
    dist = int(( (int(maxLoc[0]) - int(x))**2 + (int(maxLoc[1]) - int(y))**2 ) **0.5)
    cv2.putText(img, str(dist), (int((center[0] + maxLoc[0])/2),int((center[1] + maxLoc[1])/2)) , cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)
    if dist < int(r):
        cv2.putText(img, "NA MOSCA!!!!", (30,50), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), lineType=cv2.LINE_AA)
    print(center,maxLoc)
    cv2.imshow('img',img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
