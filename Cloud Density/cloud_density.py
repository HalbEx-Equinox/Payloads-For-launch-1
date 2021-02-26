import cv2 
import numpy as np
import itertools
  
# And thus it begins 
cap = cv2.VideoCapture(0)  
font = cv2.FONT_HERSHEY_COMPLEX 
#lala 

while(1):        
    j=0
    j1=0
    j2=0
    area =0 
    area2=0
    area3=0
    
    _, frame = cap.read()
    _,lee=cap.read()
    _,lee1=cap.read()
    
    #print(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([0,0,220]) 
    upper_red = np.array([180,140,255]) 
   
    
    """lower_ed = np.array([170,0,230]) 
    upper_ed = np.array([180,80,255])
    lower_e = np.array([0,1,180]) 
    upper_e = np.array([180,140,255]) 
    lower_i = np.array([80,0,200]) 
    upper_i = np.array([82,80,255])""" 
    lower_re = np.array([0,0,0]) 
    upper_re = np.array([255,255,255])
    lower_w = np.array([0,140,160]) 
    upper_w = np.array([180,190,220])
    lower_w1 = np.array([0,180,90]) 
    upper_w1 = np.array([180,200,160])
    
    hsv1 = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV) 
  

    mask = cv2.inRange(hsv, lower_red, upper_red)
    #mask2 = cv2.inRange(hsv, lower_ed, upper_ed)
   # mask0 = cv2.inRange(hsv, lower_e, upper_e)
    #mask9 = cv2.inRange(hsv, lower_i, upper_i)
    #mask=mask + mask2 + mask0 + mask9
    mask1 = cv2.inRange(hsv1, lower_re, upper_re) 
    maskC = cv2.inRange(hsv1, lower_w1, upper_w1) 

    mast=cv2.inRange(hsv, lower_w, upper_w) 
    res = cv2.bitwise_and(frame,frame, mask= mask)
    tres = cv2.cvtColor(res, cv2.COLOR_BGR2HSV) 
    #maskx = cv2.inRange(tres, lower_ree, upper_ree)
    #
    masky = mask
    #rest = cv2.bitwise_and(frame,frame, mask= maskx)
    rest1 = cv2.bitwise_and(frame,frame, mask= masky)
    #maskz= cv2.inRange(tres, lower_ee, upper_ee)
    #print(lower_red[1])
    if int(cv2.__version__[0]) > 3:
        # Opencv 4.x.x
        contours, _ = cv2.findContours(mast, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours2, _ = cv2.findContours(masky, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours3, _ = cv2.findContours(maskC, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        # Opencv 3.x.x
        _, contours, _ = cv2.findContours(mast, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours2, _ = cv2.findContours(masky, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours3, _ = cv2.findContours(maskC, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area =area + cv2.contourArea(cnt)
       
        approx = cv2.approxPolyDP(cnt, 0.00000001*cv2.arcLength(cnt, True), True)
        
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        g = cv2.countNonZero(mask);
        g1 = cv2.countNonZero(mast);
        r = cv2.countNonZero(mask1);
        if area > 88 and ( len(approx) != 4 or len(approx) != 6):
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            j=j+cv2.contourArea(cnt)
            
    for cnt2 in contours2:
        area2 =area2 + cv2.contourArea(cnt2)
        approx2 = cv2.approxPolyDP(cnt2, 0.00000001*cv2.arcLength(cnt2, True), True)
        #g1 = cv2.countNonZero(maskx);
        x1 = approx2.ravel()[0]
        y1 = approx2.ravel()[1]
        g2 = cv2.countNonZero(masky);
        r1 = cv2.countNonZero(mask1);
        if area2 > 0 and ( len(approx2) != 4 or len(approx2) != 6):
            cv2.drawContours(lee, [approx2], 0, (60, 255, 127.5), 5)
            j1=j1+cv2.contourArea(cnt2)


                              
    for cnt3 in contours3:
        area3 =area3 + cv2.contourArea(cnt3)
        approx3 = cv2.approxPolyDP(cnt3, 0.00000001*cv2.arcLength(cnt3, True), True)
        x2 = approx3.ravel()[0]
        y2 = approx3.ravel()[1]
        g3 = cv2.countNonZero(maskC);
        r2 = cv2.countNonZero(mask1);
        if area3 > 0 and ( len(approx3) != 4 or len(approx3) != 6) :
            cv2.drawContours(lee1, [approx3], 0, (180, 255, 127.5), 5)
            j1=j1+cv2.contourArea(cnt3)
   
    cv2.imshow('GREY COVER',frame) 
    cv2.imshow('WHITE COVER',lee) 
    cv2.imshow('DARK GREY COVER',lee1) 
    
    #cv2.imshow('res1',mast) 
    #cv2.imshow('res',mask) 
   
    
    
    #print('green cover percentage:', np.round(j/r*100, 2))
    k = cv2.waitKey(5)
    if k == 'a':
        print('grey cloud density', np.round(j/r*100*.5))
        print('white cloud density', np.round(j1/r*100*.497))
        print('dark grey cloud density', np.round(j2/r*100*.504))
        print('average cloud density', np.round(((j/r*100*.5) + (j1/r*100*.497) + (j2/r*100*.504))/3 ))
               
               
                     
               
        break
  
    
        

cv2.destroyAllWindows() 

    
cap.release() 

