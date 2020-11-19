import cv2
import colorsys
import solver
import serial
import cv2

# cap = cv2.VideoCapture(0)
green = [80,255,255]    
blue = [160,50,50]      
yellow = [45,255,255]     
white = [0,5,5]  
orange = [19,100,100]  
red = [167,255,255]
black= [0,0,0]

green_bgr = [0,255,0]
blue_bgr = [255,0,0]
red_bgr = [0,0,255]
yellow_bgr = [0,255,255]
orange_bgr = [0,128,255]
white_bgr = [255,255,255]



# This function fixes the color of the pixel into the standard color
def colorFix(color):   
    # The color of the pixel at first is in BGR 
    # Now we have to convert it into HSV
    color = colorsys.rgb_to_hsv(color[2]/255, color[1]/255, color[0]/255)
    color = (color[0]*255,color[1]*255,color[2]*255)
    # print(color)
    color = list(color)
    # Depend on the color code in HSV, we classify them into 6 different color
    if(color[2]>=150) and color[1]<80 :
        # print('White')
        return white_bgr
    elif (color>[yellow[0]-15,50,50]) and color < [yellow[0]+20,255,255]:
        # print('Yellow')
        return yellow_bgr
    elif (color>[orange[0]-7,50,50]) and color < [orange[0]+10,255,255]:
        # print('Orange')
        return orange_bgr
    elif ((color<[12,255,255]) and color > [0,50,50]) or (color>[200,100,100]) and color < [255,255,255]:
        # print('Red')
        return red_bgr
    elif (color>[green[0]-20,50,50]) and color < [green[0]+40,255,255]:
        # print('Green')
        return green_bgr
    elif (color>[blue[0]-15,50,50]) and color < [blue[0]+15,255,255]:
        # print('Blue')
        return blue_bgr
    
    else:
        return black
def read(frame):
#Initialize the coordinates of the scanning pixel
    c = [[]]
    X = 240
    Y = 100
    originX = (X,Y)
    originY = (X+50,Y+50)
    X1 =((originX[0]+originY[0])/2)
    Y1 = ((originX[1]+originY[1])/2)
    origin = (int (X1),int (Y1))

    #Take the center pixel of each square
    
    cl1 = frame[int (Y1),int (X1)]
    cl12 = frame[int (Y1)-20,int (X1)]
    cl13 = frame[int (Y1)+20,int (X1)]    
    cl11=cl1
    cl1[0] = (cl11[0]/3+cl12[0]/3+cl13[0]/3)
    c1 = cl1.tolist()   #Convert the tuple into a list
    c1 = colorFix(c1)   #Turn the color of the pixel 
    
    
    cl2 = frame[int (Y1)+100,int (X1)]
    cl22 = frame[int (Y1)+100-20,int (X1)]
    cl23 = frame[int (Y1)+100+20,int (X1)]    
    cl21=cl2
    cl2[0] = (cl21[0]/3+cl22[0]/3+cl23[0]/3)
    c2 = cl2.tolist()
    c2 =  colorFix(c2)
    
    cl3 = frame[int (Y1)+200,int (X1)]
    cl32 = frame[int (Y1)+200-20,int (X1)]
    cl33 = frame[int (Y1)+200+20,int (X1)]    
    cl31=cl3
    cl3[0] = (cl31[0]/3+cl32[0]/3+cl33[0]/3)
    c3 = cl3.tolist()
    c3 =  colorFix(c3)
    
    cl4= frame[int (Y1),int (X1) +100]
    cl42 = frame[int (Y1)-20,int (X1)+100]  
    cl43 = frame[int (Y1)+20,int (X1)+100]    
    cl41=cl4
    cl4[0] = (cl41[0]/3+cl42[0]/3+cl43[0]/3)
    c4 = cl4.tolist()
    c4 =  colorFix(c4)
    
    cl5 = frame[int (Y1)+100,int (X1)+100]
    cl52 = frame[int (Y1)+100-20,int (X1)+100]
    cl53 = frame[int (Y1)+100+20,int (X1)+100]    
    cl51=cl5
    cl5[0] = (cl51[0]/3+cl52[0]/3+cl53[0]/3)
    c5 = cl5.tolist()
    c5 =  colorFix(c5)
    
    cl6 = frame[int (Y1)+200,int (X1)+100]
    cl62 = frame[int (Y1)+200-20,int (X1)+100]
    cl63 = frame[int (Y1)+200+20,int (X1)+100]    
    cl61=cl6
    cl6[0] = (cl61[0]/3+cl62[0]/3+cl63[0]/3)
    c6 = cl6.tolist()
    c6 =  colorFix(c6)
    
    cl7 = frame[int (Y1),int (X1)+200]
    cl72 = frame[int (Y1)-20,int (X1)+200]
    cl73 = frame[int (Y1)+20,int (X1)+200]    
    cl71=cl7
    cl7[0] = (cl71[0]/3+cl72[0]/3+cl73[0]/3)
    c7 = cl7.tolist()
    c7 =  colorFix(c7)
    
    cl8 = frame[int (Y1)+100,int (X1)+200]
    cl82 = frame[int (Y1)+100-20,int (X1)+200]
    cl83 = frame[int (Y1)+100+20,int (X1)+200]    
    cl81=cl8
    cl8[0] = (cl81[0]/3+cl82[0]/3+cl83[0]/3)
    c8 = cl8.tolist()
    c8 =  colorFix(c8)
    
    cl9 = frame[int (Y1)+200,int (X1)+200]
    cl92 = frame[int (Y1)+200-20,int (X1)+200]
    cl93 = frame[int (Y1)+200+20,int (X1)+200]    
    cl91=cl9
    cl9[0] = (cl91[0]/3+cl92[0]/3+cl93[0]/3)
    c9 = cl9.tolist()
    c9 =  colorFix(c9)
 
    #Draw the square and the point
    # Square 1
    cv2.rectangle(frame, originX, originY, color = c1, thickness=15, lineType=8, shift=0)
    cv2.circle(frame, origin, radius = 10, color = c1, thickness=15, lineType=8, shift=0)    
    # Square 2
    cv2.rectangle(frame, (originX[0]+100,originX[1]), (originY[0]+100,originY[1]), color = c4, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0]+100,origin[1]), radius = 10, color = c4, thickness=15, lineType=8, shift=0)
    # Square 3
    cv2.rectangle(frame, (originX[0]+200,originX[1]), (originY[0]+200,originY[1]), color = c7, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0]+200,origin[1]), radius = 10, color = c7, thickness=15, lineType=8, shift=0)
    # Square 4
    cv2.rectangle(frame, (originX[0],originX[1]+100), (originY[0],originY[1]+100), color = c2, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0],origin[1]+100), radius = 10, color = c2, thickness=15, lineType=8, shift=0)
    # Square 5
    cv2.rectangle(frame, (originX[0]+100,originX[1]+100), (originY[0]+100,originY[1]+100), color = c5, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0]+100,origin[1]+100), radius = 10, color = c5, thickness=15, lineType=8, shift=0)
    # Square 6
    cv2.rectangle(frame, (originX[0]+200,originX[1]+100), (originY[0]+200,originY[1]+100), color = c8, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0]+200,origin[1]+100), radius = 10, color = c8, thickness=15, lineType=8, shift=0)
    # Square 7
    cv2.rectangle(frame, (originX[0],originX[1]+200), (originY[0],originY[1]+200), color = c3, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0],origin[1]+200), radius = 10, color = c3, thickness=15, lineType=8, shift=0)
    # Square 8
    cv2.rectangle(frame, (originX[0]+100,originX[1]+200), (originY[0]+100,originY[1]+200), color = c6, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0]+100,origin[1]+200), radius = 10, color = c6, thickness=15, lineType=8, shift=0)
    # Square 9
    cv2.rectangle(frame, (originX[0]+200,originX[1]+200), (originY[0]+200,originY[1]+200), color = c9, thickness=15, lineType=8, shift=0)    
    cv2.circle(frame, (origin[0]+200,origin[1]+200), radius = 10, color = c9, thickness=15, lineType=8, shift=0)
    
    # Show the frame to scan
    # cv2.imshow('Frame',frame)
    s=''
    s+=check(c1)
    s+=check(c4)
    s+=check(c7)
    s+=check(c2)
    s+=check(c5)
    s+=check(c8)
    s+=check(c3)
    s+=check(c6)
    s+=check(c9) 
    return s,frame
def check(c):
    if c == green_bgr:
        return 'G'
    if c == blue_bgr:
        return 'H'
    if c == red_bgr:
        return 'J'
    if c == orange_bgr:
         return 'O'
    if c == yellow_bgr:
        return 'Y'
    if c == white_bgr:
        return 'W'
    else:
        return'M'
# def process():
#     while True:
#         #Turn the capture into a frame
#         s='M'*54
#         _, frame = cap.read()
#         c = read(frame)
#         k = cv2.waitKey(5) & 0xFF 
#         n=0
#         k=0
#         if k == 0:
#             count = 0
#             print('Enter input mode')
#             while(count<6):
#                 _, frame = cap.read()
#                 c = read(frame)
#                 key = cv2.waitKey(5) & 0xFF
#                 print(count)
#                 if key == ord(" "):
#                     s2=''
#                     s2 = s2+c
#                     if s2[4]=='H':
#                         s=s2[0:9] + s[9:54]    
#                         count+=1
                            
#                     elif s2[4]=='J':  
#                         s=s[0:9] + s2[0:9] + s[18:54]
#                         count+=1
                        
#                     elif s2[4]=='G':
#                         s=s[0:18] + s2[0:9] + s[27:54]
#                         count+=1
                        
#                     elif s2[4]=='O':
#                         s=s[0:27] + s2[0:9] + s[36:54]
#                         count+=1
                            
#                     elif s2[4]=='Y':
#                         s=s[0:36] + s2[0:9] + s[45:54]
#                         count+=1
                            
#                     elif s2[4]=='W':
#                         s=s[0:45] + s2[0:9]
#                         count+=1 
#                     # print(s2) 
#                 # print(s)
#             k=27   
#         if k == 27:
#             break   

#     t = s
#     print(t)
#     cv2.destroyAllWindows()
#     cap.release()
#     return t