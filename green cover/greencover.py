import cv2 
import numpy as np  
  
# And thus it begins 
cap = cv2.VideoCapture(0)  
font = cv2.FONT_HERSHEY_COMPLEX 
#lala 

while(1):        
    j=0
    area =0 
    
    _, frame = cap.read()  
    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([43,10,10]) 
    upper_red = np.array([80,255,255]) 
    lower_re = np.array([0,0,0]) 
    upper_re = np.array([255,255,255]) 
    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
  

    mask = cv2.inRange(hsv, lower_red, upper_red) 
    mask1 = cv2.inRange(hsv, lower_re, upper_re) 

     
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    
    if int(cv2.__version__[0]) > 3:
        # Opencv 4.x.x
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        # Opencv 3.x.x
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area =area + cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.00001*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        g = cv2.countNonZero(mask);
        r = cv2.countNonZero(mask1);
       

        if area > 8000 and ( len(approx) != 4 or len(approx) != 6):
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            j=j+cv2.contourArea(cnt)
            #print(area)

            #if len(approx) != 3 or  len(approx) != 4 or len(approx) != 5 :
                   # cv2.putText(frame, "", (x, y), font, 1, (0, 0, 0))          

                              

   
    cv2.imshow('This is whats seen',frame) 
    cv2.imshow('mask',mask) 
    #cv2.imshow('res',res) 
    #cv2.imshow('res',hsv1) 
   
    
    
    #print('green cover percentage:', np.round(j/r*100, 2))
    k = cv2.waitKey(5)
    if k == 'a':
        print('green cover percentage:', np.round(j/r*100, 2))
        break
  
    #ch =input("enter o if u wanna see green cover percentage") #can change to something that sounds cooler 
    #if ch=='o':
        

cv2.destroyAllWindows() 

    
cap.release() 

