import copy
import serial
import string
from time import sleep
import threading
import time
import cv2
from cam import *
start = time.time()
cap = cv2.VideoCapture(1)
ser = serial.Serial(port='COM12',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=0)
pwm1 = '#1P2500'  #quay F
pwm2 = '#2P1200'
pwm4 = '#4P1200'
pwm6 = '#6P1175'
pwm8 = '#8P1200'
pwm11 ='#2P1700'
pwm12 ='#1P1500'
pwm13 ='#2P1200'
pwm14 ='#1P500' #quay f
pwm15 = '#3P2500'  #quayR
pwm16 = '#4P1700'
pwm17 = '#3P1500'
pwm18 = '#4P1200'
pwm19 = '#3P500'  #quay r
pwm20 = '#5P2500' # quay L
pwm21 = '#6P1700'
pwm22 = '#5P1500'
pwm23 = '#6P1175'
pwm24 = '#5P500' #quay l
pwm25 = '#7P2500' # quay B
pwm26 = '#8P1700'
pwm27 = '#7P1500'
pwm28 = '#8P1200'
pwm29 = '#7P500'#  quay b
pwm30 = '#2P1700'  #quay U
pwm31 = '#8P1700'
pwm32 = '#3P500'
pwm33 = '#5P2500'
pwm34 = '#2P1200'
pwm35 = '#8P1200'
pwm36 ='#4P1700'
pwm37 ='#6P1700'
pwm38 ='#3P1500'
pwm39 ='#5P1500' 
pwm40 = '#4P1200' 
pwm41 = '#6P1175'
pwm42 = '#1P2500'
pwm43 = '#2P1700'
pwm44 = '#1P1500'
pwm45 = '#8P1700' 
pwm46 = '#3P2500' 
pwm47 = '#5P500'
pwm48 = '#3P1500' 
pwm49 = '#5P1500'
pwm50 ='#1P500'
pwm51 ='#7P2500'
pwm52 = '#8P1700'
pwm53 ='#7P1500'
pwm54 ='#2P1700'
pwm55 = '#7P500'
pwm0  ='#2P1900'
pwm00  ='#4P1900'
pwm01 ='#6P1900'
pwm02  ='#8P1900'
#
pwm03 = '#2P1200'
pwm04 = '#4P1200'
pwm05 = '#8P1200'
pwm06 = '#6P1175'
pwm07 = '#2P1900'
pwm08 = '#8P1900'
pwm09 = '#3P500'
pwm010 = '#5P2500'
pwm011 = '#4P1900'
pwm012 = '#6P1900'
pwm013 = '#3P1500'
pwm014 = '#5P1500'
pwm015 = '#3P2500'
pwm016 = '#5P500'#
pwm017 = '#1P500'
pwm018 = '#7P2500'
pwm019 = '#7P500'
pwm020 = '#1P2500'
pwm021 = '#1P1500'
pwm022 = '#7P1500'
class MyClass:
    def __init__(self):        
        # frame1 = Frame(master)
        # frame1.pack()
        # self.master = master
        # self.textbox = Text(root,width = 60 ,height = 5)
        # self.textbox.pack(side= 'right')
        self.face_checked = ''
        self.to_yield = "?"
        # self.button = Button(root, text="Chụp", command=self.func, padx = 20 , pady =20)
        # self.button.pack(side='left')
        self.cube_string = 'M'*54
        self.frame = []
        self.count = 0
        self.state = ''
        self.time_to_capture = 3 #Thay doi thoi gian chup tai day
        self.start_time = time.time()
        self.quit = False
        self.current_image = None        
    def func(self):
        print("Taking picture ",self.count)
        s = self.cube_string
        c = self.state
        s2=''
        s2 = s2+c
        if s2[4]=='H':
            s=s2[0:9] + s[9:54]    
            self.count+=1
            self.face_checked += "H"

        elif s2[4]=='J':  
            s=s[0:9] + s2[0:9] + s[18:54]
            self.count+=1
            self.face_checked += "J"
            
            
        elif s2[4]=='G':
            s=s[0:18] + s2[0:9] + s[27:54]
            self.count+=1
            self.face_checked += "G"
            
        elif s2[4]=='O':
            s=s[0:27] + s2[0:9] + s[36:54]
            self.count+=1
            self.face_checked += "O"
                
        elif s2[4]=='Y':
            s=s[0:36] + s2[0:9] + s[45:54]
            self.count+=1
            self.face_checked += "Y"
                
        elif s2[4]=='W':
            s=s[0:45] + s2[0:9]
            self.count+=1 
            self.face_checked += "W"
        self.cube_string = s       
        if(self.count==6):           
            # print(self.cube_string)  
            # self.textbox.insert(index = tk.END,chars = self.cube_string) 
            self.quit = True
        self.to_yield = self.face_checked
            
        return s       
    def show_frame(self):
        while(1):
            check = False
            current_time = time.time()
            _, frame = cap.read()
            self.state,frame = read(frame)
            self.frame = frame
            cv2image = frame
            if("M" not in self.state):
                if(self.state[4] in self.face_checked):
                    check = False
                else:
                    check = True
            if(check == False):
                self.start_time = time.time()
            if(time.time()-self.start_time>self.time_to_capture):
                self.func()
                self.start_time = time.time()
            self.current_image = cv2image
            cv2.putText(cv2image, str(int(time.time()-self.start_time)) + "- Count to " +str(self.time_to_capture), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) 
            cv2.imshow("Screen",cv2image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if(self.quit):
                cv2.destroyAllWindows()
                cap.release()
                break
def xoaymat():
    ser.write(str(pwm03).encode())
    ser.write(str(pwm04).encode())
    ser.write(str(pwm05).encode())
    ser.write(str(pwm06).encode())
    sleep(0.5)
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode())
    sleep(0.5)
    ser.write(str(pwm09).encode())
    ser.write(str(pwm010).encode())
    sleep(4)#xd
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())
    sleep(0.5)
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())
    sleep(0.5)
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())
    sleep(0.5)
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode()) 
    sleep(0.5)
    ser.write(str(pwm015).encode())
    ser.write(str(pwm016).encode())  
    sleep(4)#do
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())
    sleep(0.5)
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())
    sleep(0.5)
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())
    sleep(0.5)
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode()) 
    sleep(0.5)
    ser.write(str(pwm015).encode())
    ser.write(str(pwm016).encode())  
    sleep(4) #xl
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())
    sleep(0.5)
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())
    sleep(0.5)
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())
    sleep(0.5)
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode()) 
    sleep(0.5)
    ser.write(str(pwm015).encode())
    ser.write(str(pwm016).encode())
    sleep(4)# cam  
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())
    sleep(0.5)
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())
    sleep(0.5)
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())
    sleep(0.5)
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode()) 
    sleep(0.5)
    ser.write(str(pwm015).encode())
    ser.write(str(pwm016).encode())
    sleep(0.5)
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())
    sleep(0.5)
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())
    sleep(0.5)
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())
    sleep(0.5)
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode()) 
    sleep(0.5)
    ser.write(str(pwm015).encode())
    ser.write(str(pwm016).encode())
    ## vang
    sleep(0.5)
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())
    sleep(0.5) 
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())
    sleep(0.5)
    ser.write(str(pwm017).encode())
    ser.write(str(pwm018).encode())          
    sleep(4)
    #Trang
    ser.write(str(pwm019).encode())
    ser.write(str(pwm020).encode())  
    sleep(4)    
                           
def uart():  
    ser.write(str(pwm021).encode())
    ser.write(str(pwm022).encode()) 
    sleep(0.5)
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())  
    sleep(0.5)   
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode())  
    sleep(0.5)  
    ser.write(str(pwm09).encode())
    ser.write(str(pwm010).encode())
    sleep(0.5)
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode())
    sleep(0.5)           
    ser.write(str(pwm011).encode())
    ser.write(str(pwm012).encode())    
    sleep(0.5)
    ser.write(str(pwm013).encode())
    ser.write(str(pwm014).encode())  
    sleep(0.5)         
    ser.write(str(pwm017).encode())
    ser.write(str(pwm018).encode())  
    sleep(0.5)      
    ser.write(str(pwm04).encode())
    ser.write(str(pwm06).encode())     
    sleep(0.5) 
    ser.write(str(pwm07).encode())
    ser.write(str(pwm08).encode()) 
    sleep(0.5)  
    ser.write(str(pwm021).encode())
    ser.write(str(pwm022).encode())  
    sleep(0.5)   
    ser.write(str(pwm03).encode())
    ser.write(str(pwm05).encode()) 
    i = 0
    j = 0 
    for i in sumxoay:    
        j = j + 1 
        if i == 'x':
            print('Giải hoàn thành')
        else:print('Bước thứ',j,'/',len(sumxoay)-1,end = ' : ')
        if  i == 'F':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm1).encode())
            sleep(0.5)
            ser.write(str(pwm11).encode())
            sleep(0.5)
            ser.write(str(pwm12).encode())
            sleep(0.5)
            ser.write(str(pwm13).encode())           
        elif i == 'f': 
            print('xoay',i)   
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm14).encode())
            sleep(0.5)
            ser.write(str(pwm11).encode())
            sleep(0.5)
            ser.write(str(pwm12).encode())
            sleep(0.5)
            ser.write(str(pwm13).encode())        
        elif i == 'R':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm15).encode())
            sleep(0.5)
            ser.write(str(pwm16).encode())
            sleep(0.5)
            ser.write(str(pwm17).encode())
            sleep(0.5)
            ser.write(str(pwm18).encode())       
        elif i == 'r':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm19).encode())
            sleep(0.5)
            ser.write(str(pwm16).encode())
            sleep(0.5)
            ser.write(str(pwm17).encode())
            sleep(0.5)
            ser.write(str(pwm18).encode())            
        elif i =='L':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm20).encode())
            sleep(0.5)
            ser.write(str(pwm21).encode())
            sleep(0.5)
            ser.write(str(pwm22).encode())
            sleep(0.5)
            ser.write(str(pwm23).encode())        
        elif i =='l':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm24).encode())
            sleep(0.5)
            ser.write(str(pwm21).encode())
            sleep(0.5)
            ser.write(str(pwm22).encode())
            sleep(0.5)
            ser.write(str(pwm23).encode())  
        elif i =='B':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm25).encode())
            sleep(0.5)
            ser.write(str(pwm26).encode())
            sleep(0.5)
            ser.write(str(pwm27).encode())
            sleep(0.5)
            ser.write(str(pwm28).encode())                        
        elif i =='b':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm29).encode())
            sleep(0.5)
            ser.write(str(pwm26).encode())
            sleep(0.5)
            ser.write(str(pwm27).encode())
            sleep(0.5)
            ser.write(str(pwm28).encode())
        elif i =='U':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm30).encode())
            ser.write(str(pwm31).encode())
            sleep(0.5)
            ser.write(str(pwm32).encode())
            ser.write(str(pwm33).encode())
            sleep(0.5)              
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)  
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm38).encode())
            ser.write(str(pwm39).encode())
            sleep(0.5)      
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())
            sleep(0.5)
            ser.write(str(pwm42).encode())
            sleep(0.5)
            ser.write(str(pwm43).encode())
            sleep(0.5)
            ser.write(str(pwm44).encode())
            sleep(0.5)
            ser.write(str(pwm45).encode())
            sleep(0.5)
            ser.write(str(pwm46).encode())
            ser.write(str(pwm47).encode())
            sleep(0.5)
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm48).encode())
            ser.write(str(pwm49).encode())
            sleep(0.5) 
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())         
        elif i =='u':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm30).encode())
            ser.write(str(pwm31).encode())
            sleep(0.5)
            ser.write(str(pwm32).encode())
            ser.write(str(pwm33).encode())
            sleep(0.5)              
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)  
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm38).encode())
            ser.write(str(pwm39).encode())
            sleep(0.5)      
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())
            sleep(0.5)
            ser.write(str(pwm50).encode())
            sleep(0.5)
            ser.write(str(pwm43).encode())
            sleep(0.5)
            ser.write(str(pwm44).encode())
            sleep(0.5)
            ser.write(str(pwm45).encode())
            sleep(0.5)
            ser.write(str(pwm46).encode())
            ser.write(str(pwm47).encode())
            sleep(0.5)
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm48).encode())
            ser.write(str(pwm49).encode())
            sleep(0.5) 
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())
        elif i =='D':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm30).encode())
            ser.write(str(pwm31).encode())
            sleep(0.5)
            ser.write(str(pwm32).encode())
            ser.write(str(pwm33).encode())
            sleep(0.5)              
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)  
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm38).encode())
            ser.write(str(pwm39).encode())
            sleep(0.5)      
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())
            sleep(0.5)
            ser.write(str(pwm51).encode())
            sleep(0.5)
            ser.write(str(pwm52).encode())
            sleep(0.5)
            ser.write(str(pwm53).encode())
            sleep(0.5)
            ser.write(str(pwm54).encode())
            sleep(0.5)
            ser.write(str(pwm46).encode())
            ser.write(str(pwm47).encode())
            sleep(0.5)
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm48).encode())
            ser.write(str(pwm49).encode())
            sleep(0.5) 
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())       
        elif i =='d':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm30).encode())
            ser.write(str(pwm31).encode())
            sleep(0.5)
            ser.write(str(pwm32).encode())
            ser.write(str(pwm33).encode())
            sleep(0.5)              
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)  
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm38).encode())
            ser.write(str(pwm39).encode())
            sleep(0.5)      
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())
            sleep(0.5)
            ser.write(str(pwm55).encode())
            sleep(0.5)
            ser.write(str(pwm52).encode())
            sleep(0.5)
            ser.write(str(pwm53).encode())
            sleep(0.5)
            ser.write(str(pwm54).encode())
            sleep(0.5)
            ser.write(str(pwm46).encode())
            ser.write(str(pwm47).encode())
            sleep(0.5)
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm48).encode())
            ser.write(str(pwm49).encode())
            sleep(0.5) 
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())     
        elif i == 'Q':
            print('xoay',i)
            ser.write(str(pwm2).encode())
            ser.write(str(pwm4).encode())
            ser.write(str(pwm6).encode())
            ser.write(str(pwm8).encode())
            sleep(0.5)
            ser.write(str(pwm30).encode())
            ser.write(str(pwm31).encode())
            sleep(0.5)
            ser.write(str(pwm32).encode())
            ser.write(str(pwm33).encode())
            sleep(0.5)              
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)  
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm38).encode())
            ser.write(str(pwm39).encode())
            sleep(0.5)      
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())
            sleep(0.5)
            ser.write(str(pwm42).encode())
            sleep(0.5)
            ser.write(str(pwm43).encode())
            sleep(0.5)
            ser.write(str(pwm44).encode())
            sleep(0.5)
            ser.write(str(pwm34).encode())
            sleep(0.5)
            ser.write(str(pwm42).encode())
            sleep(0.5)
            ser.write(str(pwm43).encode())
            sleep(0.5)
            ser.write(str(pwm44).encode())
            sleep(0.5)
            ser.write(str(pwm45).encode())
            sleep(0.5)
            ser.write(str(pwm46).encode())
            ser.write(str(pwm47).encode())
            sleep(0.5)
            ser.write(str(pwm34).encode())
            ser.write(str(pwm35).encode())
            sleep(0.5)
            ser.write(str(pwm36).encode())
            ser.write(str(pwm37).encode())
            sleep(0.5) 
            ser.write(str(pwm48).encode())
            ser.write(str(pwm49).encode())
            sleep(0.5) 
            ser.write(str(pwm40).encode())
            ser.write(str(pwm41).encode())     
        elif i == 'x':
            ser.write(str(pwm11).encode())
            ser.write(str(pwm16).encode())
            ser.write(str(pwm21).encode())
            ser.write(str(pwm31).encode()) 
            break
def bd():
    ser.write(str(pwm0).encode())
    ser.write(str(pwm00).encode())
    ser.write(str(pwm01).encode())
    ser.write(str(pwm02).encode()) 
    sleep(5)
def kep():
    ser.write(str(pwm2).encode())
    ser.write(str(pwm4).encode())
    ser.write(str(pwm6).encode())
    ser.write(str(pwm8).encode()) 
    sleep(1) 

def test_dieu_khien_song_song():
    while(1):
        print("Check...1")
        bd()
        xoaymat()
        break
    
def run():
    abc = MyClass()
    abc.show_frame()
    return abc.cube_string
rubik = [[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.7, 0.8], [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],
     [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8], [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8],
     [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8], [5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8]]

def inrubik(a):
    print('            |', a[4][0], a[4][1], a[4][2], '|')
    print('            |', a[4][3], a[4][4], a[4][5], '|')
    print('            |', a[4][6], a[4][7], a[4][8], '|')
    print(a[0][0], a[0][1], a[0][2], '|', a[1][0], a[1][1], a[1][2], '|', a[2][0], a[2][1], a[2][2], '|', a[3][0], a[3][1], a[3][2])
    print(a[0][3], a[0][4], a[0][5], '|', a[1][3], a[1][4], a[1][5], '|', a[2][3], a[2][4], a[2][5], '|', a[3][3],a[3][4], a[3][5])
    print(a[0][6], a[0][7], a[0][8], '|', a[1][6], a[1][7], a[1][8], '|', a[2][6], a[2][7], a[2][8], '|', a[3][6],a[3][7], a[3][8])
    print('            |', a[5][0], a[5][1], a[5][2], '|')
    print('            |', a[5][3], a[5][4], a[5][5], '|')
    print('            |', a[5][6], a[5][7], a[5][8], '|')
def mau(a,s): 
    y=copy.deepcopy(a) 
    if s[0:1] =='H' and s[29:30]=='O' and s[36:37]=='Y':
        y[0][0] = a[0][0]
        y[3][2] = a[3][2]
        y[4][0] = a[4][0]
    elif s[0:1] =='H' and s[29:30]=='Y' and s[36:37]=='J':     
        y[0][0] = a[0][2]
        y[3][2] = a[4][6]
        y[4][0] = a[1][0]
    elif s[0:1] =='H' and s[29:30]=='W' and s[36:37]=='O':     
        y[0][0] = a[0][6]
        y[3][2] = a[5][6]
        y[4][0] = a[3][8]
    elif s[0:1] =='H' and s[29:30]=='J' and s[36:37]=='W':     
        y[0][0] = a[0][8]
        y[3][2] = a[1][6]
        y[4][0] = a[5][0]
    elif s[0:1] =='J' and s[29:30]=='H' and s[36:37]=='Y':
        y[0][0] = a[1][0]
        y[3][2] = a[0][2]
        y[4][0] = a[4][6]
    elif s[0:1] =='J' and s[29:30]=='Y' and s[36:37]=='G':
        y[0][0] = a[1][2]
        y[3][2] = a[4][8]
        y[4][0] = a[2][0]
    elif s[0:1] =='J' and s[29:30]=='W' and s[36:37]=='H':
        y[0][0] = a[1][6]
        y[3][2] = a[5][0]
        y[4][0] = a[0][8]
    elif s[0:1] =='J' and s[29:30]=='G' and s[36:37]=='W':
        y[0][0] = a[1][8]
        y[3][2] = a[2][6]
        y[4][0] = a[5][2]
    elif s[0:1] =='G' and s[29:30]=='J' and s[36:37]=='Y':
        y[0][0] = a[2][0]
        y[3][2] = a[1][2]
        y[4][0] = a[4][8]
    elif s[0:1] =='G' and s[29:30]=='Y' and s[36:37]=='O':
        y[0][0] = a[2][2]
        y[3][2] = a[4][2]
        y[4][0] = a[3][0]
    elif s[0:1] =='G' and s[29:30]=='W' and s[36:37]=='J':
        y[0][0] = a[2][6]
        y[3][2] = a[5][2]
        y[4][0] = a[1][8]
    elif s[0:1] =='G' and s[29:30]=='O' and s[36:37]=='W':
        y[0][0] = a[2][8]
        y[3][2] = a[3][6]
        y[4][0] = a[5][8]
    elif s[0:1] =='O' and s[29:30]=='G' and s[36:37]=='Y':
        y[0][0] = a[3][0]
        y[3][2] = a[2][2]
        y[4][0] = a[4][2]
    elif s[0:1] =='O' and s[29:30]=='Y' and s[36:37]=='H':
        y[0][0] = a[3][2]
        y[3][2] = a[4][0]
        y[4][0] = a[0][0]
    elif s[0:1] =='O' and s[29:30]=='W' and s[36:37]=='G':
        y[0][0] = a[3][6]
        y[3][2] = a[5][8]
        y[4][0] = a[2][8]
    elif s[0:1] =='O' and s[29:30]=='H' and s[36:37]=='W':
        y[0][0] = a[3][8]
        y[3][2] = a[0][6]
        y[4][0] = a[5][6]
    elif s[0:1] =='Y' and s[29:30]=='O' and s[36:37]=='G':
        y[0][0] = a[4][2]
        y[3][2] = a[3][0]
        y[4][0] = a[2][2]
    elif s[0:1] =='Y' and s[29:30]=='H' and s[36:37]=='O':
        y[0][0] = a[4][0]
        y[3][2] = a[0][0]
        y[4][0] = a[3][2] 
    elif s[0:1] =='Y' and s[29:30]=='J' and s[36:37]=='H':
        y[0][0] = a[4][6]
        y[3][2] = a[1][0]
        y[4][0] = a[0][2]
    elif s[0:1] =='Y' and s[29:30]=='G' and s[36:37]=='J':
        y[0][0] = a[4][8]
        y[3][2] = a[2][0]
        y[4][0] = a[1][2]    
    elif s[0:1] =='W'and s[29:30]=='O' and s[36:37]=='H':
        y[0][0] = a[5][6]
        y[3][2] = a[3][8]
        y[4][0] = a[0][6]
    elif s[0:1] =='W'and s[29:30]=='H' and s[36:37]=='J':
        y[0][0] = a[5][0]
        y[3][2] = a[0][8]
        y[4][0] = a[1][6] 
    elif s[0:1] =='W'and s[29:30]=='G' and s[36:37]=='O':
        y[0][0] = a[5][8]
        y[3][2] = a[2][8]
        y[4][0] = a[3][6]   
    elif s[0:1] =='W'and s[29:30]=='J' and s[36:37]=='G':    
        y[0][0] = a[5][2]
        y[3][2] = a[1][8]
        y[4][0] = a[2][6]       
    if s[1:2] =='H' and s[39:40]=='Y':
        y[0][1] = a[0][1]
        y[4][3] = a[4][3]   
    elif s[1:2] =='H' and s[39:40]=='O':
        y[0][1] = a[0][3]
        y[4][3] = a[3][5]    
    elif s[1:2] =='H' and s[39:40]=='J':
        y[0][1] = a[0][5]
        y[4][3] = a[1][3]   
    elif s[1:2] =='H' and s[39:40]=='W':
        y[0][1] = a[0][7]
        y[4][3] = a[5][3]   
    elif s[1:2] =='J' and s[39:40]=='Y':
        y[0][1] = a[1][1]
        y[4][3] = a[4][7]   
    elif s[1:2] =='J' and s[39:40]=='H':
        y[0][1] = a[1][3]
        y[4][3] = a[0][5]    
    elif s[1:2] =='J' and s[39:40]=='W':
        y[0][1] = a[1][7]
        y[4][3] = a[5][1]   
    elif s[1:2] =='J' and s[39:40]=='G':
        y[0][1] = a[1][5]
        y[4][3] = a[2][3]   
    elif s[1:2] =='G' and s[39:40]=='Y':
        y[0][1] = a[2][1]
        y[4][3] = a[4][5]   
    elif s[1:2] =='G' and s[39:40]=='J':
        y[0][1] = a[2][3]
        y[4][3] = a[1][5]    
    elif s[1:2] =='G' and s[39:40]=='O':
        y[0][1] = a[2][5]
        y[4][3] = a[3][3]   
    elif s[1:2] =='G' and s[39:40]=='W':
        y[0][1] = a[2][7]
        y[4][3] = a[5][5]   
    elif s[1:2] =='O' and s[39:40]=='Y':
        y[0][1] = a[3][1]
        y[4][3] = a[4][1]   
    elif s[1:2] =='O' and s[39:40]=='G':
        y[0][1] = a[3][3]
        y[4][3] = a[2][5]    
    elif s[1:2] =='O' and s[39:40]=='H':
        y[0][1] = a[3][5] 
        y[4][3] = a[0][3]  
    elif s[1:2] =='O' and s[39:40]=='W':
        y[0][1] = a[3][7]
        y[4][3] = a[5][7]   
    elif s[1:2] =='Y' and s[39:40]=='O':
        y[0][1] = a[4][1]
        y[4][3] = a[3][1]   
    elif s[1:2] =='Y' and s[39:40]=='G':
        y[0][1] = a[4][5]
        y[4][3] = a[2][1]    
    elif s[1:2] =='Y' and s[39:40]=='H':
        y[0][1] = a[4][3]
        y[4][3] = a[0][1]   
    elif s[1:2] =='Y' and s[39:40]=='J':
        y[0][1] = a[4][7]
        y[4][3] = a[1][1]    
    elif s[1:2] =='W' and s[39:40]=='H':
        y[0][1] = a[5][3]
        y[4][3] = a[0][7]   
    elif s[1:2] =='W' and s[39:40]=='J':
        y[0][1] = a[5][1]
        y[4][3] = a[1][7]    
    elif s[1:2] =='W' and s[39:40]=='G':
        y[0][1] = a[5][5]
        y[4][3] = a[2][7]   
    elif s[1:2] =='W' and s[39:40]=='O':
        y[0][1] = a[5][7]
        y[4][3] = a[3][7]          
    if s[2:3] =='H' and s[9:10]=='J' and s[42:43]=='Y': 
        y[0][2] = a[0][2]
        y[1][0] = a[1][0]
        y[4][6] = a[4][6]      
    elif s[2:3] =='H' and s[9:10]=='Y' and s[42:43]=='O':
        y[0][2] = a[0][0]
        y[1][0] = a[4][0]
        y[4][6] = a[3][2]     
    elif s[2:3] =='H' and s[9:10]=='W' and s[42:43]=='J':
        y[0][2] = a[0][8]
        y[1][0] = a[5][0]
        y[4][6] = a[1][6]      
    elif s[2:3] =='H' and s[9:10]=='O' and s[42:43]=='W' : 
        y[0][2] = a[0][6]
        y[1][0] = a[3][8]
        y[4][6] = a[5][6]      
    elif s[2:3] =='J' and s[9:10]=='G' and s[42:43]=='Y': 
        y[0][2] = a[1][2]
        y[1][0] = a[2][0]
        y[4][6] = a[4][8]      
    elif s[2:3] =='J' and s[9:10]=='Y' and s[42:43]=='H':
        y[0][2] = a[1][0]
        y[1][0] = a[4][6]
        y[4][6] = a[0][2]     
    elif s[2:3] =='J' and s[9:10]=='H' and s[42:43]=='W':
        y[0][2] = a[1][6]
        y[1][0] = a[0][8]
        y[4][6] = a[5][0]      
    elif s[2:3] =='J' and s[9:10]=='W' and s[42:43]=='G' : 
        y[0][2] = a[1][8]
        y[1][0] = a[5][2]
        y[4][6] = a[2][6]
    elif s[2:3] =='G' and s[9:10]=='Y' and s[42:43]=='J': 
        y[0][2] = a[2][0]
        y[1][0] = a[4][8]
        y[4][6] = a[1][2]      
    elif s[2:3] =='G' and s[9:10]=='O' and s[42:43]=='Y':
        y[0][2] = a[2][2]
        y[1][0] = a[3][0]
        y[4][6] = a[4][2]     
    elif s[2:3] =='G' and s[9:10]=='J' and s[42:43]=='W':
        y[0][2] = a[2][6]
        y[1][0] = a[1][8]
        y[4][6] = a[5][2]      
    elif s[2:3] =='G' and s[9:10]=='W' and s[42:43]=='O' : 
        y[0][2] = a[2][8]
        y[1][0] = a[5][8]
        y[4][6] = a[3][6]          
    elif s[2:3] =='O' and s[9:10]=='H' and s[42:43]=='Y': 
        y[0][2] = a[3][2]
        y[1][0] = a[0][0]
        y[4][6] = a[4][0]      
    elif s[2:3] =='O' and s[9:10]=='W' and s[42:43]=='H':
        y[0][2] = a[3][8]
        y[1][0] = a[5][6]
        y[4][6] = a[0][6]     
    elif s[2:3] =='O' and s[9:10]=='Y' and s[42:43]=='G':
        y[0][2] = a[3][0]
        y[1][0] = a[4][2]
        y[4][6] = a[2][2]      
    elif s[2:3] =='O' and s[9:10]=='G' and s[42:43]=='W' : 
        y[0][2] = a[3][6]
        y[1][0] = a[2][8]
        y[4][6] = a[5][8] 
    elif s[2:3] =='Y' and s[9:10]=='H' and s[42:43]=='J': 
        y[0][2] = a[4][6]
        y[1][0] = a[0][2]
        y[4][6] = a[1][0]      
    elif s[2:3] =='Y' and s[9:10]=='J' and s[42:43]=='G':
        y[0][2] = a[4][8]
        y[1][0] = a[1][2]
        y[4][6] = a[2][0]     
    elif s[2:3] =='Y' and s[9:10]=='O' and s[42:43]=='H':
        y[0][2] = a[4][0]
        y[1][0] = a[3][2]
        y[4][6] = a[0][0]      
    elif s[2:3] =='Y' and s[9:10]=='G' and s[42:43]=='O' : 
        y[0][2] = a[4][2]
        y[1][0] = a[2][2]
        y[4][6] = a[3][0]  
    elif s[2:3] =='W' and s[9:10]=='J' and s[42:43]=='H': 
        y[0][2] = a[5][0]
        y[1][0] = a[1][6]
        y[4][6] = a[0][8]      
    elif s[2:3] =='W' and s[9:10]=='G' and s[42:43]=='J':
        y[0][2] = a[5][2]
        y[1][0] = a[2][6]
        y[4][6] = a[1][8]     
    elif s[2:3] =='W' and s[9:10]=='O' and s[42:43]=='G':
        y[0][2] = a[5][8]
        y[1][0] = a[3][6]
        y[4][6] = a[2][8]      
    elif s[2:3] =='W' and s[9:10]=='H' and s[42:43]=='O' : 
        y[0][2] = a[5][6]
        y[1][0] = a[0][6]
        y[4][6] = a[3][8]   
    if  s[3:4] == 'H' and s[32:33] =='O':
        y[0][3] = a[0][3]
        y[3][5] = a[3][5]
    elif s[3:4] == 'H' and s[32:33] =='Y':
        y[0][3] = a[0][1]
        y[3][5] = a[4][3]   
    elif s[3:4] == 'H' and s[32:33] =='W':
        y[0][3] = a[0][7]
        y[3][5] = a[5][3]   
    elif s[3:4] == 'H' and s[32:33] =='J':
        y[0][3] = a[0][5]
        y[3][5] = a[1][3]   
    elif s[3:4] == 'J' and s[32:33] =='H':
        y[0][3] = a[1][3]
        y[3][5] = a[0][5]
    elif s[3:4] == 'J' and s[32:33] =='Y':
        y[0][3] = a[1][1]
        y[3][5] = a[4][7]   
    elif s[3:4] == 'J' and s[32:33] =='W':
        y[0][3] = a[1][7]
        y[3][5] = a[5][1]   
    elif s[3:4] == 'J' and s[32:33] =='G':
        y[0][3] = a[1][5]
        y[3][5] = a[2][3] 
    elif s[3:4] == 'G' and s[32:33] =='Y':
        y[0][3] = a[2][1]
        y[3][5] = a[4][5]
    elif s[3:4] == 'G' and s[32:33] =='J':
        y[0][3] = a[2][3]
        y[3][5] = a[1][5]   
    elif s[3:4] == 'G' and s[32:33] =='O':
        y[0][3] = a[2][5]
        y[3][5] = a[3][3]   
    elif s[3:4] == 'G' and s[32:33] =='W':
        y[0][3] = a[2][7]
        y[3][5] = a[5][5]  
    elif s[3:4] == 'O' and s[32:33] =='Y':
        y[0][3] = a[3][1]
        y[3][5] = a[4][1]
    elif s[3:4] == 'O' and s[32:33] =='G':
        y[0][3] = a[3][3]
        y[3][5] = a[2][5]   
    elif s[3:4] == 'O' and s[32:33] =='H':
        y[0][3]  =a[3][5]
        y[3][5] = a[0][3]   
    elif s[3:4] == 'O' and s[32:33] =='W':
        y[0][3] = a[3][7]
        y[3][5] = a[5][7]     
    elif s[3:4] == 'Y' and s[32:33] =='H':
        y[0][3] = a[4][3]
        y[3][5] = a[0][1]
    elif s[3:4] == 'Y' and s[32:33] =='O':
        y[0][3] = a[4][1]
        y[3][5] = a[3][1]   
    elif s[3:4] == 'Y' and s[32:33] =='J':
        y[0][3] = a[4][7]
        y[3][5] = a[1][1]   
    elif s[3:4] == 'Y' and s[32:33] =='G':
        y[0][3] = a[4][5]
        y[3][5] = a[2][1]  
    elif s[3:4] == 'W' and s[32:33] =='O':
        y[0][3] = a[5][7]
        y[3][5] = a[3][7]
    elif s[3:4] == 'W' and s[32:33] =='H':
        y[0][3] = a[5][3]
        y[3][5] = a[0][7]   
    elif s[3:4] == 'W' and s[32:33] =='J':
        y[0][3] = a[5][1]
        y[3][5] = a[1][7]   
    elif s[3:4] == 'W' and s[32:33] =='G':
        y[0][3] = a[5][5]
        y[3][5] = a[2][7]   
    if  s[5:6] == 'H' and s[12:13] =='J':
        y[0][5] = a[0][5]
        y[1][3] = a[1][3]
    elif s[5:6] == 'H' and s[12:13] =='Y':
        y[0][5] = a[0][1]
        y[1][3] = a[4][3]
    elif s[5:6] == 'H' and s[12:13] =='O':
        y[0][5] = a[0][3]
        y[1][3] = a[3][5]  
    elif s[5:6] == 'H' and s[12:13] =='W':
        y[0][5] = a[0][7]
        y[1][3] = a[5][3]
    elif s[5:6] == 'J' and s[12:13] =='H':
        y[0][5] = a[1][3]
        y[1][3] = a[0][5]
    elif s[5:6] == 'J' and s[12:13] =='Y':
        y[0][5] = a[1][1]
        y[1][3] = a[4][7]
    elif s[5:6] == 'J' and s[12:13] =='G':
        y[0][5] = a[1][5]
        y[1][3] = a[2][3]  
    elif s[5:6] == 'J' and s[12:13] =='W':
        y[0][5] = a[1][7]
        y[1][3] = a[5][1]
    elif s[5:6] == 'G' and s[12:13] =='Y':
        y[0][5] = a[2][1]
        y[1][3] = a[4][5]
    elif s[5:6] == 'G' and s[12:13] =='J':
        y[0][5] = a[2][3]
        y[1][3] = a[1][5]
    elif s[5:6] == 'G' and s[12:13] =='O':
        y[0][5] = a[2][5]
        y[1][3] = a[3][3]  
    elif s[5:6] == 'G' and s[12:13] =='W':
        y[0][5] = a[2][7]
        y[1][3] = a[5][5]
    elif s[5:6] == 'O' and s[12:13] =='Y':
        y[0][5] = a[3][1]
        y[1][3] = a[4][1]
    elif s[5:6] == 'O' and s[12:13] =='G':
        y[0][5] = a[3][3]
        y[1][3] = a[2][5]
    elif s[5:6] == 'O' and s[12:13] =='H':
        y[0][5] = a[3][5]
        y[1][3] = a[0][3]  
    elif s[5:6] == 'O' and s[12:13] =='W':
        y[0][5] = a[3][7]
        y[1][3] = a[5][7]
    elif s[5:6] == 'Y' and s[12:13] =='G':
        y[0][5] = a[4][5]
        y[1][3] = a[2][1]
    elif s[5:6] == 'Y' and s[12:13] =='O':
        y[0][5] = a[4][1]
        y[1][3] = a[3][1]
    elif s[5:6] == 'Y' and s[12:13] =='H':
        y[0][5] = a[4][3]
        y[1][3] = a[0][1]  
    elif s[5:6] == 'Y' and s[12:13] =='J':
        y[0][5] = a[4][7]
        y[1][3] = a[1][1]
    elif s[5:6] == 'W' and s[12:13] =='H':
        y[0][5] = a[5][3]
        y[1][3] = a[0][7]
    elif s[5:6] == 'W' and s[12:13] =='O':
        y[0][5] = a[5][7]
        y[1][3] = a[3][7]
    elif s[5:6] == 'W' and s[12:13] =='J':
        y[0][5] = a[5][1]
        y[1][3] = a[1][7]  
    elif s[5:6] == 'W' and s[12:13] =='G':
        y[0][5] = a[5][5]
        y[1][3] = a[2][7]   
    if s[6:7] =='H' and s[35:36]=='O' and s[51:52]=='W':              
        y[0][6] = a[0][6]
        y[3][8] = a[3][8]
        y[5][6] = a[5][6] 
    elif s[6:7] =='H' and s[35:36]=='Y' and s[51:52]=='O':              
        y[0][6] = a[0][0]
        y[3][8] = a[4][0]
        y[5][6] = a[3][2]   
    elif s[6:7] =='H' and s[35:36]=='J' and s[51:52]=='Y':              
        y[0][6] = a[0][2]
        y[3][8] = a[1][0]
        y[5][6] = a[4][6] 
    elif s[6:7] =='H' and s[35:36]=='W' and s[51:52]=='J':              
        y[0][6] = a[0][8]
        y[3][8] = a[5][0]
        y[5][6] = a[1][6]
    elif s[6:7] =='J' and s[35:36]=='H' and s[51:52]=='W':              
        y[0][6] = a[1][6]
        y[3][8] = a[0][8]
        y[5][6] = a[5][0] 
    elif s[6:7] =='J' and s[35:36]=='W' and s[51:52]=='G':              
        y[0][6] = a[1][8]
        y[3][8] = a[5][2]
        y[5][6] = a[2][6]   
    elif s[6:7] =='J' and s[35:36]=='Y' and s[51:52]=='H':              
        y[0][6] = a[1][0]
        y[3][8] = a[4][6]
        y[5][6] = a[0][2] 
    elif s[6:7] =='J' and s[35:36]=='G' and s[51:52]=='Y':              
        y[0][6] = a[1][2]
        y[3][8] = a[2][0]
        y[5][6] = a[4][8]
    elif s[6:7] =='G' and s[35:36]=='J' and s[51:52]=='W':              
        y[0][6] = a[2][6]
        y[3][8] = a[1][8]
        y[5][6] = a[5][2] 
    elif s[6:7] =='G' and s[35:36]=='W' and s[51:52]=='O':              
        y[0][6] = a[2][8]
        y[3][8] = a[5][8]
        y[5][6] = a[3][6]   
    elif s[6:7] =='G' and s[35:36]=='O' and s[51:52]=='Y':              
        y[0][6] = a[2][2]
        y[3][8] = a[3][0]
        y[5][6] = a[4][2] 
    elif s[6:7] =='G' and s[35:36]=='Y' and s[51:52]=='J':              
        y[0][6] = a[2][0]
        y[3][8] = a[4][8]
        y[5][6] = a[1][2]
    elif s[6:7] =='O' and s[35:36]=='H' and s[51:52]=='Y':              
        y[0][6] = a[3][2]
        y[3][8] = a[0][0]
        y[5][6] = a[4][0] 
    elif s[6:7] =='O' and s[35:36]=='Y' and s[51:52]=='G':              
        y[0][6] = a[3][0]
        y[3][8] = a[4][2]
        y[5][6] = a[2][2]   
    elif s[6:7] =='O' and s[35:36]=='W' and s[51:52]=='H':              
        y[0][6] = a[3][8]
        y[3][8] = a[5][6]
        y[5][6] = a[0][6] 
    elif s[6:7] =='O' and s[35:36]=='G' and s[51:52]=='W':              
        y[0][6] = a[3][6]
        y[3][8] = a[2][8]
        y[5][6] = a[5][8]
    elif s[6:7] =='Y' and s[35:36]=='O' and s[51:52]=='H':              
        y[0][6] = a[4][0]
        y[3][8] = a[3][2]
        y[5][6] = a[0][0] 
    elif s[6:7] =='Y' and s[35:36]=='G' and s[51:52]=='O':              
        y[0][6] = a[4][2]
        y[3][8] = a[2][2]
        y[5][6] = a[3][0]   
    elif s[6:7] =='Y' and s[35:36]=='J' and s[51:52]=='G':              
        y[0][6] = a[4][8]
        y[3][8] = a[1][2]
        y[5][6] = a[2][0] 
    elif s[6:7] =='Y' and s[35:36]=='H' and s[51:52]=='J':              
        y[0][6] = a[4][6]
        y[3][8] = a[0][2]
        y[5][6] = a[1][0]
    elif s[6:7] =='W' and s[35:36]=='H' and s[51:52]=='O':              
        y[0][6] = a[5][6]
        y[3][8] = a[0][6]
        y[5][6] = a[3][8] 
    elif s[6:7] =='W' and s[35:36]=='O' and s[51:52]=='G':              
        y[0][6] = a[5][8]
        y[3][8] = a[3][6]
        y[5][6] = a[2][8]   
    elif s[6:7] =='W' and s[35:36]=='J' and s[51:52]=='H':              
        y[0][6] = a[5][0]
        y[3][8] = a[1][6]
        y[5][6] = a[0][8] 
    elif s[6:7] =='W' and s[35:36]=='G' and s[51:52]=='J':              
        y[0][6] = a[5][2]
        y[3][8] = a[2][6]
        y[5][6] = a[1][8]
    if s[7:8] =='H' and s[48:49]=='W':
        y[0][7] = a[0][7]
        y[5][3] = a[5][3]
    elif s[7:8] =='H' and s[48:49]=='Y':
        y[0][7] = a[0][1]
        y[5][3] = a[4][3]   
    elif s[7:8] =='H' and s[48:49]=='O':
        y[0][7] = a[0][3]
        y[5][3] = a[3][5]  
    elif s[7:8] =='H' and s[48:49]=='J':
        y[0][7] = a[0][5]
        y[5][3] = a[1][3]   
    elif s[7:8] =='J' and s[48:49]=='Y':
        y[0][7] = a[1][1]
        y[5][3] = a[4][7]
    elif s[7:8] =='J' and s[48:49]=='H':
        y[0][7] = a[1][3]
        y[5][3] = a[0][5]  
    elif s[7:8] =='J' and s[48:49]=='G':
        y[0][7] = a[1][5]
        y[5][3] = a[2][3]  
    elif s[7:8] =='J' and s[48:49]=='W':
        y[0][7] = a[1][7]
        y[5][3] = a[5][1]
    elif s[7:8] =='G' and s[48:49]=='Y':
        y[0][7] = a[2][1]
        y[5][3] = a[4][5]  
    elif s[7:8] =='G' and s[48:49]=='J':
        y[0][7] = a[2][3]
        y[5][3] = a[1][5]  
    elif s[7:8] =='G' and s[48:49]=='O':
        y[0][7] = a[2][5]
        y[5][3] = a[3][3]  
    elif s[7:8] =='G' and s[48:49]=='W':
        y[0][7] = a[2][7]
        y[5][3] = a[5][5]
    elif s[7:8] =='O' and s[48:49]=='Y':
        y[0][7] = a[3][1]
        y[5][3] = a[4][1]  
    elif s[7:8] =='O' and s[48:49]=='H':
        y[0][7] = a[3][5]
        y[5][3] = a[0][3]  
    elif s[7:8] =='O' and s[48:49]=='G':
        y[0][7] = a[3][3]
        y[5][3] = a[2][5]  
    elif s[7:8] =='O' and s[48:49]=='W':
        y[0][7] = a[3][7]
        y[5][3] = a[5][7]
    elif s[7:8] =='Y' and s[48:49]=='H':
        y[0][7] = a[4][3]
        y[5][3] = a[0][1]  
    elif s[7:8] =='Y' and s[48:49]=='O':
        y[0][7] = a[4][1]
        y[5][3] = a[3][1]   
    elif s[7:8] =='Y' and s[48:49]=='J':
        y[0][7] = a[4][7]
        y[5][3] = a[1][1]  
    elif s[7:8] =='Y' and s[48:49]=='G':
        y[0][7] = a[4][5]
        y[5][3] = a[2][1]         
    elif s[7:8] =='W' and s[48:49]=='H':
        y[0][7] = a[5][3]
        y[5][3] = a[0][7]  
    elif s[7:8] =='W' and s[48:49]=='O':
        y[0][7] = a[5][7]
        y[5][3] = a[3][7]  
    elif s[7:8] =='W' and s[48:49]=='J':
        y[0][7] = a[5][1]
        y[5][3] = a[1][7]  
    elif s[7:8] =='W' and s[48:49]=='G':
        y[0][7] = a[5][5]
        y[5][3] = a[2][7]  
    if   s[8:9] =='H' and s[15:16]=='J' and s[45:46]=='W':
            y[0][8] = a[0][8]
            y[1][6] = a[1][6]  
            y[5][0] = a[5][0]
    elif s[8:9] =='H' and s[15:16]=='W' and s[45:46]=='O':
            y[0][8] = a[0][6]
            y[1][6] = a[5][6]  
            y[5][0] = a[3][8] 
    elif s[8:9] =='H' and s[15:16]=='Y' and s[45:46]=='J':
            y[0][8] = a[0][2]
            y[1][6] = a[4][6]  
            y[5][0] = a[1][0] 
    elif s[8:9] =='H' and s[15:16]=='O' and s[45:46]=='Y': 
            y[0][8] = a[0][0]
            y[1][6] = a[3][2]  
            y[5][0] = a[4][0]      
    elif s[8:9] =='J' and s[15:16]=='W' and s[45:46]=='H':
            y[0][8] = a[1][6]
            y[1][6] = a[5][0]  
            y[5][0] = a[0][8] 
    elif s[8:9] =='J' and s[15:16]=='G' and s[45:46]=='W':
            y[0][8] = a[1][8]
            y[1][6] = a[2][6]  
            y[5][0] = a[5][2] 
    elif s[8:9] =='J' and s[15:16]=='H' and s[45:46]=='Y':
            y[0][8] = a[1][0]
            y[1][6] = a[0][2]  
            y[5][0] = a[4][6] 
    elif s[8:9] =='J' and s[15:16]=='Y' and s[45:46]=='G':
            y[0][8] = a[1][2]
            y[1][6] = a[4][8]  
            y[5][0] = a[2][0]    
    elif s[8:9] =='G' and s[15:16]=='J' and s[45:46]=='Y':
            y[0][8] = a[2][0]
            y[1][6] = a[1][2]  
            y[5][0] = a[4][8] 
    elif s[8:9] =='G' and s[15:16]=='W' and s[45:46]=='J':
            y[0][8] = a[2][6]
            y[1][6] = a[5][2]  
            y[5][0] = a[1][8] 
    elif s[8:9] =='G' and s[15:16]=='O' and s[45:46]=='W':
            y[0][8] = a[2][8]
            y[1][6] = a[3][6]  
            y[5][0] = a[5][8] 
    elif s[8:9] =='G' and s[15:16]=='Y' and s[45:46]=='O':
            y[0][8] = a[2][2]
            y[1][6] = a[4][2]  
            y[5][0] = a[3][0] 
    elif s[8:9] =='O' and s[15:16]=='H' and s[45:46]=='W':
            y[0][8] = a[3][8]
            y[1][6] = a[0][6]  
            y[5][0] = a[5][6] 
    elif s[8:9] =='O' and s[15:16]=='W' and s[45:46]=='G':
            y[0][8] = a[3][6]
            y[1][6] = a[5][8]  
            y[5][0] = a[2][8] 
    elif s[8:9] =='O' and s[15:16]=='Y' and s[45:46]=='H':
            y[0][8] = a[3][2]
            y[1][6] = a[4][0]  
            y[5][0] = a[0][0] 
    elif s[8:9] =='O' and s[15:16]=='G' and s[45:46]=='Y':
            y[0][8] = a[3][0]
            y[1][6] = a[2][2]  
            y[5][0] = a[4][2]   
    elif s[8:9] =='Y' and s[15:16]=='J' and s[45:46]=='H':
            y[0][8] = a[4][6]
            y[1][6] = a[1][0]  
            y[5][0] = a[0][2] 
    elif s[8:9] =='Y' and s[15:16]=='G' and s[45:46]=='J':
            y[0][8] = a[4][8]
            y[1][6] = a[2][0]  
            y[5][0] = a[1][2] 
    elif s[8:9] =='Y' and s[15:16]=='H' and s[45:46]=='O':
            y[0][8] = a[4][0]
            y[1][6] = a[0][0]  
            y[5][0] = a[3][2] 
    elif s[8:9] =='Y' and s[15:16]=='O' and s[45:46]=='G':
            y[0][8] = a[4][2]
            y[1][6] = a[3][0]  
            y[5][0] = a[2][2] 
    elif s[8:9] =='W' and s[15:16]=='H' and s[45:46]=='J':
            y[0][8] = a[5][0]
            y[1][6] = a[0][8]  
            y[5][0] = a[1][6] 
    elif s[8:9] =='W' and s[15:16]=='J' and s[45:46]=='G':
            y[0][8] = a[5][2]
            y[1][6] = a[1][8]  
            y[5][0] = a[2][6] 
    elif s[8:9] =='W' and s[15:16]=='O' and s[45:46]=='H':
            y[0][8] = a[5][6]
            y[1][6] = a[3][8]  
            y[5][0] = a[0][6] 
    elif s[8:9] =='W' and s[15:16]=='G' and s[45:46]=='O':
            y[0][8] = a[5][8]
            y[1][6] = a[2][8]  
            y[5][0] = a[3][6] 
    if s[10:11]=='J' and s[43:44]=='Y':
        y[1][1] = a[1][1]
        y[4][7] = a[4][7]
    elif s[10:11]=='J' and s[43:44]=='G':
        y[1][1] = a[1][5]
        y[4][7] = a[2][3]
    elif s[10:11]=='J' and s[43:44]=='W':
        y[1][1] = a[1][7]
        y[4][7] = a[5][1]
    elif s[10:11]=='J' and s[43:44]=='H':
        y[1][1] = a[1][3]
        y[4][7] = a[0][5]            
    elif s[10:11]=='G' and s[43:44]=='Y':
        y[1][1] = a[2][1]
        y[4][7] = a[4][5]
    elif s[10:11]=='G' and s[43:44]=='J':
        y[1][1] = a[2][3]
        y[4][7] = a[1][5]
    elif s[10:11]=='G' and s[43:44]=='O':
        y[1][1] = a[2][5]
        y[4][7] = a[3][3]            
    elif s[10:11]=='G' and s[43:44]=='W':
        y[1][1] = a[2][7]
        y[4][7] = a[5][5]       
    elif s[10:11]=='O' and s[43:44]=='Y':
        y[1][1] = a[3][1]
        y[4][7] = a[4][1]
    elif s[10:11]=='O' and s[43:44]=='G':
        y[1][1] = a[3][3]
        y[4][7] = a[2][5]
    elif s[10:11]=='O' and s[43:44]=='H':
        y[1][1] = a[3][5]
        y[4][7] = a[0][3]            
    elif s[10:11]=='O' and s[43:44]=='W':
        y[1][1] = a[3][7]
        y[4][7] = a[5][7]       
    elif s[10:11]=='H' and s[43:44]=='Y':
        y[1][1] = a[0][1]
        y[4][7] = a[4][3]
    elif s[10:11]=='H' and s[43:44]=='O':
        y[1][1] = a[0][3]
        y[4][7] = a[3][5]
    elif s[10:11]=='H' and s[43:44]=='J':
        y[1][1] = a[0][5]
        y[4][7] = a[1][3]            
    elif s[10:11]=='H' and s[43:44]=='W':
        y[1][1] = a[0][7]
        y[4][7] = a[5][3]                    
    elif s[10:11]=='Y' and s[43:44]=='G':
        y[1][1] = a[4][5]
        y[4][7] = a[2][1]
    elif s[10:11]=='Y' and s[43:44]=='O':
        y[1][1] = a[4][1]
        y[4][7] = a[3][1]
    elif s[10:11]=='Y' and s[43:44]=='H':
        y[1][1] = a[4][3]
        y[4][7] = a[0][1]            
    elif s[10:11]=='Y' and s[43:44]=='J':
        y[1][1] = a[4][7]
        y[4][7] = a[1][1] 
    elif s[10:11]=='W' and s[43:44]=='G':
        y[1][1] = a[5][5]
        y[4][7] = a[2][7]
    elif s[10:11]=='W' and s[43:44]=='O':
        y[1][1] = a[5][7]
        y[4][7] = a[3][7]
    elif s[10:11]=='W' and s[43:44]=='H':
        y[1][1] = a[5][3]
        y[4][7] = a[0][7]            
    elif s[10:11]=='W' and s[43:44]=='J':
        y[1][1] = a[5][1]
        y[4][7] = a[1][7] 
    if s[14:15]=='J' and s[21:22]=='G':
        y[1][5] = a[1][5]
        y[2][3] = a[2][3] 
    elif s[14:15]=='J' and s[21:22]=='Y':
        y[1][5] = a[1][1]
        y[2][3] = a[4][7]
    elif s[14:15]=='J' and s[21:22]=='W':
        y[1][5] = a[1][7]
        y[2][3] = a[5][1]            
    elif s[14:15]=='J' and s[21:22]=='H':
        y[1][5] = a[1][3]
        y[2][3] = a[0][5]  
    elif s[14:15]=='G' and s[21:22]=='Y':
        y[1][5] = a[2][1]
        y[2][3] = a[4][5] 
    elif s[14:15]=='G' and s[21:22]=='O':
        y[1][5] = a[2][5]
        y[2][3] = a[3][3]
    elif s[14:15]=='G' and s[21:22]=='W':
        y[1][5] = a[2][7]
        y[2][3] = a[5][5]            
    elif s[14:15]=='G' and s[21:22]=='J':
        y[1][5] = a[2][3]
        y[2][3] = a[1][5]
    elif s[14:15]=='O' and s[21:22]=='Y':
        y[1][5] = a[3][1]
        y[2][3] = a[4][1] 
    elif s[14:15]=='O' and s[21:22]=='H':
        y[1][5] = a[3][5]
        y[2][3] = a[0][3]
    elif s[14:15]=='O' and s[21:22]=='W':
        y[1][5] = a[3][7]
        y[2][3] = a[5][7]            
    elif s[14:15]=='O' and s[21:22]=='G':
        y[1][5] = a[3][3]
        y[2][3] = a[2][5]
    elif s[14:15]=='H' and s[21:22]=='Y':
        y[1][5] = a[0][1]
        y[2][3] = a[4][3] 
    elif s[14:15]=='H' and s[21:22]=='J':
        y[1][5] = a[0][5]
        y[2][3] = a[1][3]
    elif s[14:15]=='H' and s[21:22]=='O':
        y[1][5] = a[0][3]
        y[2][3] = a[3][5]            
    elif s[14:15]=='H' and s[21:22]=='W':
        y[1][5] = a[0][7]
        y[2][3] = a[5][3] 
    elif s[14:15]=='Y' and s[21:22]=='O':
        y[1][5] = a[4][1]
        y[2][3] = a[3][1] 
    elif s[14:15]=='Y' and s[21:22]=='G':
        y[1][5] = a[4][5]
        y[2][3] = a[2][1]
    elif s[14:15]=='Y' and s[21:22]=='J':
        y[1][5] = a[4][7]
        y[2][3] = a[1][1]            
    elif s[14:15]=='Y' and s[21:22]=='H':
        y[1][5] = a[4][3]
        y[2][3] = a[0][1]
    elif s[14:15]=='W' and s[21:22]=='J':
        y[1][5] = a[5][1]
        y[2][3] = a[1][7] 
    elif s[14:15]=='W' and s[21:22]=='G':
        y[1][5] = a[5][5]
        y[2][3] = a[2][7]
    elif s[14:15]=='W' and s[21:22]=='O':
        y[1][5] = a[5][7]
        y[2][3] = a[3][7]            
    elif s[14:15]=='W' and s[21:22]=='H':
        y[1][5] = a[5][3]
        y[2][3] = a[0][7]
    if s[16:17]=='J' and s[46:47]== 'W':
        y[1][7] = a[1][7]
        y[5][1] = a[5][1] 
    elif s[16:17]=='J' and s[46:47]=='Y':
        y[1][7] = a[1][1]
        y[5][1] = a[4][7] 
    elif s[16:17]=='J' and s[46:47]=='G':
        y[1][7] = a[1][5]
        y[5][1] = a[2][3] 
    elif s[16:17]=='J' and s[46:47]=='H':
        y[1][7] = a[1][3]
        y[5][1] = a[0][5] 
    elif s[16:17]=='G' and s[46:47]=='J':
        y[1][7] = a[2][3]
        y[5][1] = a[1][5] 
    elif s[16:17]=='G' and s[46:47]=='O':
        y[1][7] = a[2][5]
        y[5][1] = a[3][3] 
    elif s[16:17]=='G' and s[46:47]=='Y':
        y[1][7] = a[2][1]
        y[5][1] = a[4][5] 
    elif s[16:17]=='G' and s[46:47]=='W':
        y[1][7] = a[2][7]
        y[5][1] = a[5][5]    
    elif s[16:17]=='O' and s[46:47]=='Y':
        y[1][7] = a[3][1]
        y[5][1] = a[4][1] 
    elif s[16:17]=='O' and s[46:47]=='H':
        y[1][7] = a[3][5]
        y[5][1] = a[0][3] 
    elif s[16:17]=='O' and s[46:47]=='W':
        y[1][7] = a[3][7]
        y[5][1] = a[5][7] 
    elif s[16:17]=='O' and s[46:47]=='G':
        y[1][7] = a[3][3]
        y[5][1] = a[2][5]
    elif s[16:17]=='H' and s[46:47]=='Y':
        y[1][7] = a[0][1]
        y[5][1] = a[4][3] 
    elif s[16:17]=='H' and s[46:47]=='J':
        y[1][7] = a[0][5]
        y[5][1] = a[1][3] 
    elif s[16:17]=='H' and s[46:47]=='W':
        y[1][7] = a[0][7]
        y[5][1] = a[5][3] 
    elif s[16:17]=='H' and s[46:47]=='O':
        y[1][7] = a[0][3]
        y[5][1] = a[3][5]     
    elif s[16:17]=='Y' and s[46:47]=='O':
        y[1][7] = a[4][1]
        y[5][1] = a[3][1] 
    elif s[16:17]=='Y' and s[46:47]=='G':
        y[1][7] = a[4][5]
        y[5][1] = a[2][1] 
    elif s[16:17]=='Y' and s[46:47]=='J':
        y[1][7] = a[4][7]
        y[5][1] = a[1][1] 
    elif s[16:17]=='Y' and s[46:47]=='H':
        y[1][7] = a[4][3]
        y[5][1] = a[0][1]
    elif s[16:17]=='W' and s[46:47]=='J':
        y[1][7] = a[5][1]
        y[5][1] = a[1][7] 
    elif s[16:17]=='W' and s[46:47]=='G':
        y[1][7] = a[5][5]
        y[5][1] = a[2][7] 
    elif s[16:17]=='W' and s[46:47]=='O':
        y[1][7] = a[5][7]
        y[5][1] = a[3][7] 
    elif s[16:17]=='W' and s[46:47]=='H':
        y[1][7] = a[5][3]
        y[5][1] = a[0][7]     
    if s[11:12]=='J' and s[18:19]=='G' and s[44:45] == 'Y':
        y[1][2] = a[1][2]
        y[2][0] = a[2][0]     
        y[4][8] = a[4][8] 
    elif s[11:12]=='J' and s[18:19]=='Y' and s[44:45] == 'H':
        y[1][2] = a[1][0]
        y[2][0] = a[4][6]     
        y[4][8] = a[0][2] 
    elif s[11:12]=='J' and s[18:19]=='W' and s[44:45] == 'G':
        y[1][2] = a[1][8]
        y[2][0] = a[5][2]     
        y[4][8] = a[2][6] 
    elif s[11:12]=='J' and s[18:19]=='H' and s[44:45] == 'W':
        y[1][2] = a[1][6]
        y[2][0] = a[0][8]     
        y[4][8] = a[5][0]       
    elif s[11:12]=='G' and s[18:19]=='Y' and s[44:45] == 'J':
        y[1][2] = a[2][0]
        y[2][0] = a[4][8]     
        y[4][8] = a[1][2] 
    elif s[11:12]=='G' and s[18:19]=='O' and s[44:45] == 'Y':
        y[1][2] = a[2][2]
        y[2][0] = a[3][0]     
        y[4][8] = a[4][2] 
    elif s[11:12]=='G' and s[18:19]=='J' and s[44:45] == 'W':
        y[1][2] = a[2][6]
        y[2][0] = a[1][8]     
        y[4][8] = a[5][2] 
    elif s[11:12]=='G' and s[18:19]=='W' and s[44:45] == 'O':
        y[1][2] = a[2][8]
        y[2][0] = a[5][8]     
        y[4][8] = a[3][6]       
    elif s[11:12]=='O' and s[18:19]=='H' and s[44:45] == 'Y':
        y[1][2] = a[3][2]
        y[2][0] = a[0][0]     
        y[4][8] = a[4][0] 
    elif s[11:12]=='O' and s[18:19]=='Y' and s[44:45] == 'G':
        y[1][2] = a[3][0]
        y[2][0] = a[4][2]     
        y[4][8] = a[2][2] 
    elif s[11:12]=='O' and s[18:19]=='G' and s[44:45] == 'W':
        y[1][2] = a[3][6]
        y[2][0] = a[2][8]     
        y[4][8] = a[5][8] 
    elif s[11:12]=='O' and s[18:19]=='W' and s[44:45] == 'H':
        y[1][2] = a[3][8]
        y[2][0] = a[5][6]     
        y[4][8] = a[0][6]
    elif s[11:12]=='H' and s[18:19]=='J' and s[44:45] == 'Y':
        y[1][2] = a[0][2]
        y[2][0] = a[1][0]     
        y[4][8] = a[4][6] 
    elif s[11:12]=='H' and s[18:19]=='Y' and s[44:45] == 'O':
        y[1][2] = a[0][0]
        y[2][0] = a[4][0]     
        y[4][8] = a[3][2] 
    elif s[11:12]=='H' and s[18:19]=='W' and s[44:45] == 'J':
        y[1][2] = a[0][8]
        y[2][0] = a[5][0]     
        y[4][8] = a[1][6] 
    elif s[11:12]=='H' and s[18:19]=='O' and s[44:45] == 'W':
        y[1][2] = a[0][6]
        y[2][0] = a[3][8]     
        y[4][8] = a[5][6]     
    elif s[11:12]=='Y' and s[18:19]=='G' and s[44:45] == 'O':
        y[1][2] = a[4][2]
        y[2][0] = a[2][2]     
        y[4][8] = a[3][0] 
    elif s[11:12]=='Y' and s[18:19]=='J' and s[44:45] == 'G':
        y[1][2] = a[4][8]
        y[2][0] = a[1][2]     
        y[4][8] = a[2][0] 
    elif s[11:12]=='Y' and s[18:19]=='O' and s[44:45] == 'H':
        y[1][2] = a[4][0]
        y[2][0] = a[3][2]     
        y[4][8] = a[0][0] 
    elif s[11:12]=='Y' and s[18:19]=='H' and s[44:45] == 'J':
        y[1][2] = a[4][6]
        y[2][0] = a[0][2]     
        y[4][8] = a[1][0]
    elif s[11:12]=='W' and s[18:19]=='G' and s[44:45] == 'J':
        y[1][2] = a[5][2]
        y[2][0] = a[2][6]     
        y[4][8] = a[1][8] 
    elif s[11:12]=='W' and s[18:19]=='O' and s[44:45] == 'G':
        y[1][2] = a[5][8]
        y[2][0] = a[3][6]     
        y[4][8] = a[2][8] 
    elif s[11:12]=='W' and s[18:19]=='J' and s[44:45] == 'H':
        y[1][2] = a[5][0]
        y[2][0] = a[1][6]     
        y[4][8] = a[0][8] 
    elif s[11:12]=='W' and s[18:19]=='H' and s[44:45] == 'O':
        y[1][2] = a[5][6]
        y[2][0] = a[0][6]     
        y[4][8] = a[3][8]   
    if s[17:18]=='J' and s[24:25]=='G'and s[47:48]=='W':
        y[1][8] = a[1][8] 
        y[2][6] = a[2][6]
        y[5][2] = a[5][2] 
    elif  s[17:18]=='J' and s[24:25]=='W'and s[47:48]=='H':
        y[1][8] = a[1][6] 
        y[2][6] = a[5][0]
        y[5][2] = a[0][8]  
    elif  s[17:18]=='J' and s[24:25]=='Y'and s[47:48]=='G':
        y[1][8] = a[1][2] 
        y[2][6] = a[4][8]
        y[5][2] = a[2][0]  
    elif  s[17:18]=='J' and s[24:25]=='H'and s[47:48]=='Y':
        y[1][8] = a[1][0] 
        y[2][6] = a[0][2]
        y[5][2] = a[4][6]
    elif s[17:18]=='G' and s[24:25]=='W'and s[47:48]=='J':
        y[1][8] = a[2][6] 
        y[2][6] = a[5][2]
        y[5][2] = a[1][8] 
    elif  s[17:18]=='G' and s[24:25]=='O'and s[47:48]=='W':
        y[1][8] = a[2][8] 
        y[2][6] = a[3][6]
        y[5][2] = a[5][8]  
    elif  s[17:18]=='G' and s[24:25]=='J'and s[47:48]=='Y':
        y[1][8] = a[2][0] 
        y[2][6] = a[1][2]
        y[5][2] = a[4][8]  
    elif  s[17:18]=='G' and s[24:25]=='Y'and s[47:48]=='O':
        y[1][8] = a[2][2] 
        y[2][6] = a[4][2]
        y[5][2] = a[3][0] 
    elif s[17:18]=='O' and s[24:25]=='G'and s[47:48]=='Y':
        y[1][8] = a[3][0] 
        y[2][6] = a[2][2]
        y[5][2] = a[4][2] 
    elif  s[17:18]=='O' and s[24:25]=='W'and s[47:48]=='G':
        y[1][8] = a[3][6] 
        y[2][6] = a[5][8]
        y[5][2] = a[2][8]  
    elif  s[17:18]=='O' and s[24:25]=='H'and s[47:48]=='W':
        y[1][8] = a[3][8] 
        y[2][6] = a[0][6]
        y[5][2] = a[5][6]  
    elif  s[17:18]=='O' and s[24:25]=='Y'and s[47:48]=='H':
        y[1][8] = a[3][2] 
        y[2][6] = a[4][0]
        y[5][2] = a[0][0]    
    elif s[17:18]=='H' and s[24:25]=='J'and s[47:48]=='W':
        y[1][8] = a[0][8] 
        y[2][6] = a[1][6]
        y[5][2] = a[5][0] 
    elif  s[17:18]=='H' and s[24:25]=='W'and s[47:48]=='O':
        y[1][8] = a[0][6] 
        y[2][6] = a[5][6]
        y[5][2] = a[3][8]  
    elif  s[17:18]=='H' and s[24:25]=='Y'and s[47:48]=='J':
        y[1][8] = a[0][2] 
        y[2][6] = a[4][6]
        y[5][2] = a[1][0]  
    elif  s[17:18]=='H' and s[24:25]=='O'and s[47:48]=='Y':
        y[1][8] = a[0][0] 
        y[2][6] = a[3][2]
        y[5][2] = a[4][0]           
    elif s[17:18]=='Y' and s[24:25]=='G'and s[47:48]=='J':
        y[1][8] = a[4][8] 
        y[2][6] = a[2][0]
        y[5][2] = a[1][2] 
    elif  s[17:18]=='Y' and s[24:25]=='O'and s[47:48]=='G':
        y[1][8] = a[4][2] 
        y[2][6] = a[3][0]
        y[5][2] = a[2][2]  
    elif  s[17:18]=='Y'and s[24:25]=='J'and s[47:48]=='H':
        y[1][8] = a[4][6] 
        y[2][6] = a[1][0]
        y[5][2] = a[0][2]  
    elif  s[17:18]=='Y' and s[24:25]=='H'and s[47:48]=='O':
        y[1][8] = a[4][0] 
        y[2][6] = a[0][0]
        y[5][2] = a[3][2]    
    elif s[17:18]=='W' and s[24:25]=='J'and s[47:48]=='G':
        y[1][8] = a[5][2] 
        y[2][6] = a[1][8]
        y[5][2] = a[2][6] 
    elif  s[17:18]=='W' and s[24:25]=='H'and s[47:48]=='J':
        y[1][8] = a[5][0] 
        y[2][6] = a[0][8]
        y[5][2] = a[1][6]  
    elif  s[17:18]=='W'and s[24:25]=='O'and s[47:48]=='H':
        y[1][8] = a[5][6] 
        y[2][6] = a[3][8]
        y[5][2] = a[0][6]  
    elif  s[17:18]=='W' and s[24:25]=='G'and s[47:48]=='O':
        y[1][8] = a[5][8] 
        y[2][6] = a[2][8]
        y[5][2] = a[3][6]     
    if s[19:20] == 'G' and s[41:42] == 'Y':
       y[2][1] = a[2][1]
       y[4][5] = a[4][5]   
    elif s[19:20] == 'G' and s[41:42] == 'O':
        y[2][1] = a[2][5]
        y[4][5] = a[3][3]   
    elif s[19:20] == 'G' and s[41:42] == 'W':
        y[2][1] = a[2][7]
        y[4][5] = a[5][5]       
    elif s[19:20] == 'G' and s[41:42] == 'J':
        y[2][1] = a[2][3]
        y[4][5] = a[1][5]   
    elif s[19:20] == 'O' and s[41:42] == 'Y':
        y[2][1] = a[3][1]
        y[4][5] = a[4][1] 
    elif s[19:20] == 'O' and s[41:42] == 'H':
        y[2][1] = a[3][5]
        y[4][5] = a[0][3]   
    elif s[19:20] == 'O' and s[41:42] == 'G':
        y[2][1] = a[3][3]
        y[4][5] = a[2][5]        
    elif s[19:20] == 'O' and s[41:42] == 'W':
        y[2][1] = a[3][7]
        y[4][5] = a[5][7]   
    elif s[19:20] == 'H' and s[41:42] == 'Y':
        y[2][1] = a[0][1]
        y[4][5] = a[4][3]    
    elif s[19:20] == 'H' and s[41:42] == 'J':
        y[2][1] = a[0][5]
        y[4][5] = a[1][3]   
    elif s[19:20] == 'H' and s[41:42] == 'O':
        y[2][1] = a[0][3]
        y[4][5] = a[3][5] 
    elif s[19:20] == 'H' and s[41:42] == 'W':
        y[2][1] = a[0][7]
        y[4][5] = a[5][3]    
    elif s[19:20] == 'J' and s[41:42] == 'Y':
        y[2][1] = a[1][1]
        y[4][5] = a[4][7]    
    elif s[19:20] == 'J' and s[41:42] == 'G':
        y[2][1] = a[1][5]
        y[4][5] = a[2][3]   
    elif s[19:20] == 'J' and s[41:42] == 'H':
        y[2][1] = a[1][3]
        y[4][5] = a[0][5] 
    elif s[19:20] == 'J' and s[41:42] == 'W':
        y[2][1] = a[1][7]
        y[4][5] = a[5][1]        
    elif s[19:20] == 'Y' and s[41:42] == 'H':
        y[2][1] = a[4][3]
        y[4][5] = a[0][1]    
    elif s[19:20] == 'Y' and s[41:42] == 'O':
        y[2][1] = a[4][1]
        y[4][5] = a[3][1]   
    elif s[19:20] == 'Y' and s[41:42] == 'G':
        y[2][1] = a[4][5]
        y[4][5] = a[2][1] 
    elif s[19:20] == 'Y' and s[41:42] == 'J':
        y[2][1] = a[4][7]
        y[4][5] = a[1][1] 
    elif s[19:20] == 'W' and s[41:42] == 'G':
        y[2][1] = a[5][5]
        y[4][5] = a[2][7]    
    elif s[19:20] == 'W' and s[41:42] == 'J':
        y[2][1] = a[5][1]
        y[4][5] = a[1][7]   
    elif s[19:20] == 'W' and s[41:42] == 'H':
        y[2][1] = a[5][3]
        y[4][5] = a[0][7] 
    elif s[19:20] == 'W' and s[41:42] == 'O':
        y[2][1] = a[5][7]
        y[4][5] = a[3][7]                    
    if s[20:21] == 'G' and s[27:28] == 'O' and s[38:39] == 'Y':
        y[2][2] = a[2][2]
        y[3][0] = a[3][0]
        y[4][2] = a[4][2]
    elif s[20:21] == 'G' and s[27:28] == 'W' and s[38:39] == 'O':
        y[2][2] = a[2][8]
        y[3][0] = a[5][8]
        y[4][2] = a[3][6]
    elif s[20:21] == 'G' and s[27:28] == 'J' and s[38:39] == 'W':
        y[2][2] = a[2][6]
        y[3][0] = a[1][8]
        y[4][2] = a[5][2]
    elif s[20:21] == 'G' and s[27:28] == 'Y' and s[38:39] == 'J':
        y[2][2] = a[2][0]
        y[3][0] = a[4][8]
        y[4][2] = a[1][2]
    elif s[20:21] == 'J' and s[27:28] == 'Y' and s[38:39] == 'H':
        y[2][2] = a[1][0]
        y[3][0] = a[4][6]
        y[4][2] = a[0][2]
    elif s[20:21] == 'J' and s[27:28] == 'G' and s[38:39] == 'Y':
        y[2][2] = a[1][2]
        y[3][0] = a[2][0]
        y[4][2] = a[4][8]
    elif s[20:21] == 'J' and s[27:28] == 'H' and s[38:39] == 'W':
        y[2][2] = a[1][6]
        y[3][0] = a[0][8]
        y[4][2] = a[5][0]
    elif s[20:21] == 'J' and s[27:28] == 'W' and s[38:39] == 'G':
        y[2][2] = a[1][8]
        y[3][0] = a[5][2]
        y[4][2] = a[2][6]
    elif s[20:21] == 'H' and s[27:28] == 'J' and s[38:39] == 'Y':
        y[2][2] = a[0][2]
        y[3][0] = a[1][0]
        y[4][2] = a[4][6]
    elif s[20:21] == 'H' and s[27:28] == 'W' and s[38:39] == 'J':
        y[2][2] = a[0][8]
        y[3][0] = a[5][0]
        y[4][2] = a[1][6]
    elif s[20:21] == 'H' and s[27:28] == 'O' and s[38:39] == 'W':
        y[2][2] = a[0][6]
        y[3][0] = a[3][8]
        y[4][2] = a[5][6]
    elif s[20:21] == 'H' and s[27:28] == 'Y' and s[38:39] == 'O':
        y[2][2] = a[0][0]
        y[3][0] = a[4][0]
        y[4][2] = a[3][2]
    elif s[20:21] == 'O' and s[27:28] == 'Y' and s[38:39] == 'G':
        y[2][2] = a[3][0]
        y[3][0] = a[4][2]
        y[4][2] = a[2][2]
    elif s[20:21] == 'O' and s[27:28] == 'H' and s[38:39] == 'Y':
        y[2][2] = a[3][2]
        y[3][0] = a[0][0]
        y[4][2] = a[4][0]
    elif s[20:21] == 'O' and s[27:28] == 'G' and s[38:39] == 'W':
        y[2][2] = a[3][6]
        y[3][0] = a[2][8]
        y[4][2] = a[5][8]
    elif s[20:21] == 'O' and s[27:28] == 'W' and s[38:39] == 'H':
        y[2][2] = a[3][8]
        y[3][0] = a[5][6]
        y[4][2] = a[0][6]
    elif s[20:21] == 'Y' and s[27:28] == 'G' and s[38:39] == 'O':
        y[2][2] = a[4][2]
        y[3][0] = a[2][2]
        y[4][2] = a[3][0]
    elif s[20:21] == 'Y' and s[27:28] == 'O' and s[38:39] == 'H':
        y[2][2] = a[4][0]
        y[3][0] = a[3][2]
        y[4][2] = a[0][0]
    elif s[20:21] == 'Y' and s[27:28] == 'H' and s[38:39] == 'J':
        y[2][2] = a[4][6]
        y[3][0] = a[0][2]
        y[4][2] = a[1][0]
    elif s[20:21] == 'Y' and s[27:28] == 'J' and s[38:39] == 'G':
        y[2][2] = a[4][8]
        y[3][0] = a[1][2]
        y[4][2] = a[2][0]
    elif s[20:21] == 'W' and s[27:28] == 'H' and s[38:39] == 'O':
        y[2][2] = a[5][6]
        y[3][0] = a[0][6]
        y[4][2] = a[3][8]
    elif s[20:21] == 'W' and s[27:28] == 'J' and s[38:39] == 'H':
        y[2][2] = a[5][0]
        y[3][0] = a[1][6]
        y[4][2] = a[0][8]
    elif s[20:21] == 'W' and s[27:28] == 'O' and s[38:39] == 'G':
        y[2][2] = a[5][8]
        y[3][0] = a[3][6]
        y[4][2] = a[2][8]
    elif s[20:21] == 'W' and s[27:28] == 'G' and s[38:39] == 'J':
        y[2][2] = a[5][2]
        y[3][0] = a[2][6]
        y[4][2] = a[1][8]
    if s[23:24] == 'G' and s[30:31] == 'O':
        y[2][5] = a[2][5]
        y[3][3] = a[3][3]
    elif s[23:24] == 'G' and s[30:31] == 'Y':
        y[2][5] = a[2][1]
        y[3][3] = a[4][5]    
    elif s[23:24] == 'G' and s[30:31] == 'W':
        y[2][5] = a[2][7]
        y[3][3] = a[5][5]
    elif s[23:24] == 'G' and s[30:31] == 'J':
        y[2][5] = a[2][3]
        y[3][3] = a[1][5]
    elif s[23:24] == 'O' and s[30:31] == 'Y':
        y[2][5] = a[3][1]
        y[3][3] = a[4][1]
    elif s[23:24] == 'O' and s[30:31] == 'H':
        y[2][5] = a[3][5]
        y[3][3] = a[0][3]
    elif s[23:24] == 'O' and s[30:31] == 'W':
        y[2][5] = a[3][7]
        y[3][3] = a[5][7]
    elif s[23:24] == 'O' and s[30:31] == 'G':
        y[2][5] = a[3][3]
        y[3][3] = a[2][5]
    elif s[23:24] == 'H' and s[30:31] == 'Y':
        y[2][5] = a[0][1]
        y[3][3] = a[4][3]
    elif s[23:24] == 'H' and s[30:31] == 'J':
        y[2][5] = a[0][5]
        y[3][3] = a[1][3]
    elif s[23:24] == 'H' and s[30:31] == 'W':
        y[2][5] = a[0][7]
        y[3][3] = a[5][3]
    elif s[23:24] == 'H' and s[30:31] == 'O':
        y[2][5] = a[0][3]
        y[3][3] = a[3][5]
    elif s[23:24] == 'J' and s[30:31] == 'Y':
        y[2][5] = a[1][1]
        y[3][3] = a[4][7]
    elif s[23:24] == 'J' and s[30:31] == 'G':
        y[2][5] = a[1][5]
        y[3][3] = a[2][3]
    elif s[23:24] == 'J' and s[30:31] == 'W':
        y[2][5] = a[1][7]
        y[3][3] = a[5][1]
    elif s[23:24] == 'J' and s[30:31] == 'H':
        y[2][5] = a[1][3]
        y[3][3] = a[0][5]
    elif s[23:24] == 'Y' and s[30:31] == 'O':
        y[2][5] = a[4][1]
        y[3][3] = a[3][1]
    elif s[23:24] == 'Y' and s[30:31] == 'G':
        y[2][5] = a[4][5]
        y[3][3] = a[2][1]
    elif s[23:24] == 'Y' and s[30:31] == 'J':
        y[2][5] = a[4][7]
        y[3][3] = a[1][1]
    elif s[23:24] == 'Y' and s[30:31] == 'H':
        y[2][5] = a[4][3]
        y[3][3] = a[0][1]
    elif s[23:24] == 'W' and s[30:31] == 'J':
        y[2][5] = a[5][1]
        y[3][3] = a[1][7]
    elif s[23:24] == 'W' and s[30:31] == 'G':
        y[2][5] = a[5][5]
        y[3][3] = a[2][7]
    elif s[23:24] == 'W' and s[30:31] == 'O':
        y[2][5] = a[5][7]
        y[3][3] = a[3][7]
    elif s[23:24] == 'W' and s[30:31] == 'H':
        y[2][5] = a[5][3]
        y[3][3] = a[0][7]
    if s[25:26] == 'G' and s[50:51] == 'Y':
        y[2][7] = a[2][1]
        y[5][5] = a[4][5]
    elif s[25:26] == 'G' and s[50:51] == 'O':
        y[2][7] = a[2][5]
        y[5][5] = a[3][3]
    elif s[25:26] == 'G' and s[50:51] == 'W':
        y[2][7] = a[2][7]
        y[5][5] = a[5][5]
    elif s[25:26] == 'G' and s[50:51] == 'J':
        y[2][7] = a[2][3]
        y[5][5] = a[1][5]
    elif s[25:26] == 'O' and s[50:51] == 'Y':
        y[2][7] = a[3][1]
        y[5][5] = a[4][1]
    elif s[25:26] == 'O' and s[50:51] == 'H':
        y[2][7] = a[3][5]
        y[5][5] = a[0][3]
    elif s[25:26] == 'O' and s[50:51] == 'W':
        y[2][7] = a[3][7]
        y[5][5] = a[5][7]
    elif s[25:26] == 'O' and s[50:51] == 'G':
        y[2][7] = a[3][3]
        y[5][5] = a[2][5]
    elif s[25:26] == 'H' and s[50:51] == 'Y':
        y[2][7] = a[0][1]
        y[5][5] = a[4][3]
    elif s[25:26] == 'H' and s[50:51] == 'J':
        y[2][7] = a[0][5]
        y[5][5] = a[1][3]
    elif s[25:26] == 'H' and s[50:51] == 'W':
        y[2][7] = a[0][7]
        y[5][5] = a[5][3]
    elif s[25:26] == 'H' and s[50:51] == 'O':
        y[2][7] = a[0][3]
        y[5][5] = a[3][5]
    elif s[25:26] == 'J' and s[50:51] == 'Y':
        y[2][7] = a[1][1]
        y[5][5] = a[4][7]
    elif s[25:26] == 'J' and s[50:51] == 'G':
        y[2][7] = a[1][5]
        y[5][5] = a[2][3]
    elif s[25:26] == 'J' and s[50:51] == 'W':
        y[2][7] = a[1][7]
        y[5][5] = a[5][1]
    elif s[25:26] == 'J' and s[50:51] == 'H':
        y[2][7] = a[1][3]
        y[5][5] = a[0][5]
    elif s[25:26] == 'Y' and s[50:51] == 'O':
        y[2][7] = a[4][1]
        y[5][5] = a[3][1]
    elif s[25:26] == 'Y' and s[50:51] == 'G':
        y[2][7] = a[4][5]
        y[5][5] = a[2][1]
    elif s[25:26] == 'Y' and s[50:51] == 'J':
        y[2][7] = a[4][7]
        y[5][5] = a[1][1]
    elif s[25:26] == 'Y' and s[50:51] == 'H':
        y[2][7] = a[4][3]
        y[5][5] = a[0][1]
    elif s[25:26] == 'W' and s[50:51] == 'J':
        y[2][7] = a[5][1]
        y[5][5] = a[1][7]
    elif s[25:26] == 'W' and s[50:51] == 'G':
        y[2][7] = a[5][5]
        y[5][5] = a[2][7]
    elif s[25:26] == 'W' and s[50:51] == 'O':
        y[2][7] = a[5][7]
        y[5][5] = a[3][7]
    elif s[25:26] == 'W' and s[50:51] == 'H':
        y[2][7] = a[5][3]
        y[5][5] = a[0][7]
    if s[26:27] == 'H' and s[33:34] == 'J' and s[53:54] == 'W':
        y[2][8] = a[0][8]
        y[3][6] = a[1][6]
        y[5][8] = a[5][0]
    elif s[26:27] == 'H' and s[33:34] == 'W' and s[53:54] == 'O':
        y[2][8] = a[0][6]
        y[3][6] = a[5][6]
        y[5][8] = a[3][8]
    elif s[26:27] == 'H' and s[33:34] == 'Y' and s[53:54] == 'J':
        y[2][8] = a[0][2]
        y[3][6] = a[4][6]
        y[5][8] = a[1][0]
    elif s[26:27] == 'H' and s[33:34] == 'O' and s[53:54] == 'Y':
        y[2][8] = a[0][0]
        y[3][6] = a[3][2]
        y[5][8] = a[4][0]
    elif s[26:27] == 'J' and s[33:34] == 'W' and s[53:54] == 'H':
        y[2][8] = a[1][6]
        y[3][6] = a[5][0]
        y[5][8] = a[0][8]
    elif s[26:27] == 'J' and s[33:34] == 'G' and s[53:54] == 'W':
        y[2][8] = a[1][8]
        y[3][6] = a[2][6]
        y[5][8] = a[5][2]
    elif s[26:27] == 'J' and s[33:34] == 'H' and s[53:54] == 'Y':
        y[2][8] = a[1][0]
        y[3][6] = a[0][2]
        y[5][8] = a[4][6]
    elif s[26:27] == 'J' and s[33:34] == 'Y' and s[53:54] == 'G':
        y[2][8] = a[1][2]
        y[3][6] = a[4][8]
        y[5][8] = a[2][0]
    elif s[26:27] == 'G' and s[33:34] == 'J' and s[53:54] == 'Y':
        y[2][8] = a[2][0]
        y[3][6] = a[1][2]
        y[5][8] = a[4][8]
    elif s[26:27] == 'G' and s[33:34] == 'W' and s[53:54] == 'J':
        y[2][8] = a[2][6]
        y[3][6] = a[5][2]
        y[5][8] = a[1][8]
    elif s[26:27] == 'G' and s[33:34] == 'O' and s[54:55] == 'W':
        y[2][8] = a[2][8]
        y[3][6] = a[3][6]
        y[5][8] = a[5][8]
    elif s[26:27] == 'G' and s[33:34] == 'Y' and s[53:54] == 'O':
        y[2][8] = a[2][2]
        y[3][6] = a[4][2]
        y[5][8] = a[3][0]
    elif s[26:27] == 'O' and s[33:34] == 'H' and s[53:54] == 'W':
        y[2][8] = a[3][8]
        y[3][6] = a[0][6]
        y[5][8] = a[5][6]
    elif s[26:27] == 'O' and s[33:34] == 'W' and s[53:54] == 'G':
        y[2][8] = a[3][6]
        y[3][6] = a[5][8]
        y[5][8] = a[2][8]
    elif s[26:27] == 'O' and s[33:34] == 'Y' and s[53:54] == 'H':
        y[2][8] = a[3][2]
        y[3][6] = a[4][0]
        y[5][8] = a[0][0]
    elif s[26:27] == 'O' and s[33:34] == 'G' and s[53:54] == 'Y':
        y[2][8] = a[3][0]
        y[3][6] = a[2][2]
        y[5][8] = a[4][2]
    elif s[26:27] == 'Y' and s[33:34] == 'J' and s[53:54] == 'H':
        y[2][8] = a[4][6]
        y[3][6] = a[1][0]
        y[5][8] = a[0][2]
    elif s[26:27] == 'Y' and s[33:34] == 'G' and s[53:54] == 'J':
        y[2][8] = a[4][8]
        y[3][6] = a[2][0]
        y[5][8] = a[1][2]
    elif s[26:27] == 'Y' and s[33:34] == 'H' and s[53:54] == 'O':
        y[2][8] = a[4][0]
        y[3][6] = a[0][0]
        y[5][8] = a[3][2]
    elif s[26:27] == 'Y' and s[33:34] == 'O' and s[53:54] == 'G':
        y[2][8] = a[4][2]
        y[3][6] = a[3][0]
        y[5][8] = a[2][2]
    elif s[26:27] == 'W' and s[33:34] == 'H' and s[53:54] == 'J':
        y[2][8] = a[5][0]
        y[3][6] = a[0][8]
        y[5][8] = a[1][6]
    elif s[26:27] == 'W' and s[33:34] == 'J' and s[53:54] == 'G':
        y[2][8] = a[5][2]
        y[3][6] = a[1][8]
        y[5][8] = a[2][6]
    elif s[26:27] == 'W' and s[33:34] == 'O' and s[53:54] == 'H':
        y[2][8] = a[5][6]
        y[3][6] = a[3][8]
        y[5][8] = a[0][6]
    elif s[26:27] == 'W' and s[33:34] == 'G' and s[53:54] == 'O':
        y[2][8] = a[5][8]
        y[3][6] = a[2][8]
        y[5][8] = a[3][6]
    if s[28:29] == 'O' and s[37:38] == 'Y':
        y[3][1] = a[3][1]
        y[4][1] = a[4][1]
    elif s[28:29] == 'O' and s[37:38] == 'H':
        y[3][1] = a[3][5]
        y[4][1] = a[0][3]
    elif s[28:29] == 'O' and s[37:38] == 'W':
        y[3][1] = a[3][7]
        y[4][1] = a[5][7]
    elif s[28:29] == 'O' and s[37:38] == 'G':
        y[3][1] = a[3][3]
        y[4][1] = a[2][5]
    elif s[28:29] == 'G' and s[37:38] == 'Y':
        y[3][1] = a[2][1]
        y[4][1] = a[4][5]
    elif s[28:29] == 'G' and s[37:38] == 'O':
        y[3][1] = a[2][5]
        y[4][1] = a[3][3]
    elif s[28:29] == 'G' and s[37:38] == 'W':
        y[3][1] = a[2][7]
        y[4][1] = a[5][5]
    elif s[28:29] == 'G' and s[37:38] == 'J':
        y[3][1] = a[2][3]
        y[4][1] = a[1][5]    
    elif s[28:29] == 'H' and s[37:38] == 'Y':
        y[3][1] = a[0][1]
        y[4][1] = a[4][3]
    elif s[28:29] == 'H' and s[37:38] == 'J':
        y[3][1] = a[0][5]
        y[4][1] = a[1][3]
    elif s[28:29] == 'H' and s[37:38] == 'W':
        y[3][1] = a[0][7]
        y[4][1] = a[5][3]
    elif s[28:29] == 'H' and s[37:38] == 'O':
        y[3][1] = a[0][3]
        y[4][1] = a[3][5]
    elif s[28:29] == 'J' and s[37:38] == 'Y':
        y[3][1] = a[1][1]
        y[4][1] = a[4][7]
    elif s[28:29] == 'J' and s[37:38] == 'G':
        y[3][1] = a[1][5]
        y[4][1] = a[2][3]
    elif s[28:29] == 'J' and s[37:38] == 'W':
        y[3][1] = a[1][7]
        y[4][1] = a[5][1]
    elif s[28:29] == 'J' and s[37:38] == 'H':
        y[3][1] = a[1][3]
        y[4][1] = a[0][5]
    elif s[28:29] == 'Y' and s[37:38] == 'O':
        y[3][1] = a[4][1]
        y[4][1] = a[3][1]
    elif s[28:29] == 'Y' and s[37:38] == 'G':
        y[3][1] = a[4][5]
        y[4][1] = a[2][1]
    elif s[28:29] == 'Y' and s[37:38] == 'J':
        y[3][1] = a[4][7]
        y[4][1] = a[1][1]
    elif s[28:29] == 'Y' and s[37:38] == 'H':
        y[3][1] = a[4][3]
        y[4][1] = a[0][1]
    elif s[28:29] == 'W' and s[37:38] == 'J':
        y[3][1] = a[5][1]
        y[4][1] = a[1][7]
    elif s[28:29] == 'W' and s[37:38] == 'G':
        y[3][1] = a[5][5]
        y[4][1] = a[2][7]
    elif s[28:29] == 'W' and s[37:38] == 'O':
        y[3][1] = a[5][7]
        y[4][1] = a[3][7]
    elif s[28:29] == 'W' and s[37:38] == 'H':
        y[3][1] = a[5][3]
        y[4][1] = a[0][7]
    if s[34:35] == 'O' and s[52:53] == 'W':
        y[3][7] = a[3][7]
        y[5][7] = a[5][7]
    elif s[34:35] == 'O' and s[52:53] == 'Y':
        y[3][7] = a[3][1]
        y[5][7] = a[4][1]
    elif s[34:35] == 'O' and s[52:53] == 'H':
        y[3][7] = a[3][5]
        y[5][7] = a[0][3]
    elif s[34:35] == 'O' and s[52:53] == 'G':
        y[3][7] = a[3][3]
        y[5][7] = a[2][5]
    elif s[34:35] == 'G' and s[52:53] == 'Y':
        y[3][7] = a[2][1]
        y[5][7] = a[4][5]
    elif s[34:35] == 'G' and s[52:53] == 'O':
        y[3][7] = a[2][5]
        y[5][7] = a[3][3]
    elif s[34:35] == 'G' and s[52:53] == 'W':
        y[3][7] = a[2][7]
        y[5][7] = a[5][5]
    elif s[34:35] == 'G' and s[52:53] == 'J':
        y[3][7] = a[2][3]
        y[5][7] = a[1][5]   
    elif s[34:35] == 'H' and s[52:53] == 'Y':
        y[3][7] = a[0][1]
        y[5][7] = a[4][3]
    elif s[34:35] == 'H' and s[52:53] == 'J':
        y[3][7] = a[0][5]
        y[5][7] = a[1][3]
    elif s[34:35] == 'H' and s[52:53] == 'W':
        y[3][7] = a[0][7]
        y[5][7] = a[5][3]
    elif s[34:35] == 'H' and s[52:53] == 'O':
        y[3][7] = a[0][3]
        y[5][7] = a[3][5]
    elif s[34:35] == 'J' and s[52:53] == 'Y':
        y[3][7] = a[1][1]
        y[5][7] = a[4][7]
    elif s[34:35] == 'J' and s[52:53] == 'G':
        y[3][7] = a[1][5]
        y[5][7] = a[2][3]
    elif s[34:35] == 'J' and s[52:53] == 'W':
        y[3][7] = a[1][7]
        y[5][7] = a[5][1]
    elif s[34:35] == 'J' and s[52:53] == 'H':
        y[3][7] = a[1][3]
        y[5][7] = a[0][5]
    elif s[34:35] == 'Y' and s[52:53] == 'O':
        y[3][7] = a[4][1]
        y[5][7] = a[3][1]
    elif s[34:35] == 'Y' and s[52:53] == 'G':
        y[3][7] = a[4][5]
        y[5][7] = a[2][1]
    elif s[34:35] == 'Y' and s[52:53] == 'J':
        y[3][7] = a[4][7]
        y[5][7] = a[1][1]
    elif s[34:35] == 'Y' and s[52:53] == 'H':
        y[3][7] = a[4][3]
        y[5][7] = a[0][1]
    elif s[34:35] == 'W' and s[52:53] == 'J':
        y[3][7] = a[5][1]
        y[5][7] = a[1][7]
    elif s[34:35] == 'W' and s[52:53] == 'G':
        y[3][7] = a[5][5]
        y[5][7] = a[2][7]
    elif s[34:35] == 'W' and s[52:53] == 'O':
        y[3][7] = a[5][7]
        y[5][7] = a[3][7]
    elif s[34:35] == 'W' and s[52:53] == 'H':
        y[3][7] = a[5][3]
        y[5][7] = a[0][7]
    return y               
def ganmau(rubik): 
    rubik_a = copy.deepcopy(rubik) 
    xoay = s
    print("Vị trí màu ban đầu",xoay)
    rubik_a = mau(rubik_a,s)
    return rubik_a 
def hoanvi(a,m): 
    y = copy.deepcopy(a)
    if m == 'R':
        y[1][2] = a[5][2]
        y[1][5] = a[5][5]
        y[1][8] = a[5][8]
        y[4][2] = a[1][2]
        y[4][5] = a[1][5]
        y[4][8] = a[1][8]
        y[5][2] = a[3][6]
        y[5][5] = a[3][3]
        y[5][8] = a[3][0]
        y[3][0] = a[4][8]
        y[3][3] = a[4][5]
        y[3][6] = a[4][2]
        y[2][0] = a[2][6]
        y[2][1] = a[2][3]
        y[2][2] = a[2][0]
        y[2][5] = a[2][1]
        y[2][0] = a[2][6]
        y[2][8] = a[2][2]
        y[2][7] = a[2][5]
        y[2][6] = a[2][8]
        y[2][3] = a[2][7]
        y[2][4] = a[2][4]
    elif m == 'r':
        y[1][2] = a[4][2]
        y[1][5] = a[4][5]
        y[1][8] = a[4][8]
        y[4][2] = a[3][6]
        y[4][5] = a[3][3]
        y[4][8] = a[3][0]
        y[5][2] = a[1][2]
        y[5][5] = a[1][5]
        y[5][8] = a[1][8]
        y[3][0] = a[5][8]
        y[3][3] = a[5][5]
        y[3][6] = a[5][2]
        y[2][0] = a[2][2]
        y[2][1] = a[2][5]
        y[2][2] = a[2][8]
        y[2][3] = a[2][1]
        y[2][4] = a[2][4]
        y[2][5] = a[2][7]
        y[2][6] = a[2][0]
        y[2][7] = a[2][3]
        y[2][8] = a[2][6]
    elif m == 'l':
        y[1][0] = a[5][0]
        y[1][3] = a[5][3]
        y[1][6] = a[5][6]
        y[4][0] = a[1][0]
        y[4][3] = a[1][3]
        y[4][6] = a[1][6]
        y[5][0] = a[3][8]
        y[5][3] = a[3][5]
        y[5][6] = a[3][2]
        y[3][2] = a[4][6]
        y[3][5] = a[4][3]
        y[3][8] = a[4][0]
        y[0][0] = a[0][2]
        y[0][1] = a[0][5]
        y[0][2] = a[0][8]
        y[0][3] = a[0][1]
        y[0][4] = a[0][4]
        y[0][5] = a[0][7]
        y[0][6] = a[0][0]
        y[0][7] = a[0][3]
        y[0][8] = a[0][6]
    elif m == 'L':
        y[1][0] = a[4][0]
        y[1][3] = a[4][3]
        y[1][6] = a[4][6]
        y[4][0] = a[3][8]
        y[4][3] = a[3][5]
        y[4][6] = a[3][2]
        y[5][0] = a[1][0]
        y[5][3] = a[1][3]
        y[5][6] = a[1][6]
        y[3][2] = a[5][6]
        y[3][5] = a[5][3]
        y[3][8] = a[5][0]
        y[0][0] = a[0][6]
        y[0][1] = a[0][3]
        y[0][2] = a[0][0]
        y[0][3] = a[0][7]
        y[0][4] = a[0][4]
        y[0][5] = a[0][1]
        y[0][6] = a[0][8]
        y[0][7] = a[0][5]
        y[0][8] = a[0][2]
    elif m == 'B':
        y[3][0] = a[3][6]
        y[3][1] = a[3][3]
        y[3][2] = a[3][0]
        y[3][3] = a[3][7]
        y[3][4] = a[3][4]
        y[3][5] = a[3][1]
        y[3][6] = a[3][8]
        y[3][7] = a[3][5]
        y[3][8] = a[3][2]
        y[2][2] = a[5][8]
        y[2][5] = a[5][7]
        y[2][8] = a[5][6]
        y[4][0] = a[2][2]
        y[4][1] = a[2][5]
        y[4][2] = a[2][8]
        y[5][6] = a[0][0]
        y[5][7] = a[0][3]
        y[5][8] = a[0][6]
        y[0][0] = a[4][2]
        y[0][3] = a[4][1]
        y[0][6] = a[4][0]
    elif m == 'b':
        y[3][0] = a[3][2]
        y[3][1] = a[3][5]
        y[3][2] = a[3][8]
        y[3][3] = a[3][1]
        y[3][4] = a[3][4]
        y[3][5] = a[3][7]
        y[3][6] = a[3][0]
        y[3][7] = a[3][3]
        y[3][8] = a[3][6]
        y[2][2] = a[4][0]
        y[2][5] = a[4][1]
        y[2][8] = a[4][2]
        y[4][0] = a[0][6]
        y[4][1] = a[0][3]
        y[4][2] = a[0][0]
        y[5][6] = a[2][8]
        y[5][7] = a[2][5]
        y[5][8] = a[2][2]
        y[0][0] = a[5][6]
        y[0][3] = a[5][7]
        y[0][6] = a[5][8]
    elif m == 'U':
        y[4][0] = a[4][6]
        y[4][1] = a[4][3]
        y[4][2] = a[4][0]
        y[4][3] = a[4][7]
        y[4][4] = a[4][4]
        y[4][5] = a[4][1]
        y[4][6] = a[4][8]
        y[4][7] = a[4][5]
        y[4][8] = a[4][2]
        y[0][0] = a[1][0]
        y[0][1] = a[1][1]
        y[0][2] = a[1][2]
        y[1][0] = a[2][0]
        y[1][1] = a[2][1]
        y[1][2] = a[2][2]
        y[2][0] = a[3][0]
        y[2][1] = a[3][1]
        y[2][2] = a[3][2]
        y[3][0] = a[0][0]
        y[3][1] = a[0][1]
        y[3][2] = a[0][2]
    elif m == 'u':
        y[4][0] = a[4][2]
        y[4][1] = a[4][5]
        y[4][2] = a[4][8]
        y[4][3] = a[4][1]
        y[4][4] = a[4][4]
        y[4][5] = a[4][7]
        y[4][6] = a[4][0]
        y[4][7] = a[4][3]
        y[4][8] = a[4][6]
        y[0][0] = a[3][0]
        y[0][1] = a[3][1]
        y[0][2] = a[3][2]
        y[1][0] = a[0][0]
        y[1][1] = a[0][1]
        y[1][2] = a[0][2]
        y[2][0] = a[1][0]
        y[2][1] = a[1][1]
        y[2][2] = a[1][2]
        y[3][0] = a[2][0]
        y[3][1] = a[2][1]
        y[3][2] = a[2][2]
    elif m == 'F':
        y[1][0] = a[1][6]
        y[1][1] = a[1][3]
        y[1][2] = a[1][0]
        y[1][3] = a[1][7]
        y[1][4] = a[1][4]
        y[1][5] = a[1][1]
        y[1][6] = a[1][8]
        y[1][7] = a[1][5]
        y[1][8] = a[1][2]
        y[0][2] = a[5][0]
        y[0][5] = a[5][1]
        y[0][8] = a[5][2]
        y[4][6] = a[0][8]
        y[4][7] = a[0][5]
        y[4][8] = a[0][2]
        y[2][0] = a[4][6]
        y[2][3] = a[4][7]
        y[2][6] = a[4][8]
        y[5][0] = a[2][6]
        y[5][1] = a[2][3]
        y[5][2] = a[2][0]
    elif m == 'f':
        y[1][0] = a[1][2]
        y[1][1] = a[1][5]
        y[1][2] = a[1][8]
        y[1][3] = a[1][1]
        y[1][4] = a[1][4]
        y[1][5] = a[1][7]
        y[1][6] = a[1][0]
        y[1][7] = a[1][3]
        y[1][8] = a[1][6]
        y[0][2] = a[4][8]
        y[0][5] = a[4][7]
        y[0][8] = a[4][6]
        y[4][6] = a[2][0]
        y[4][7] = a[2][3]
        y[4][8] = a[2][6]
        y[2][0] = a[5][2]
        y[2][3] = a[5][1]
        y[2][6] = a[5][0]
        y[5][0] = a[0][2]
        y[5][1] = a[0][5]
        y[5][2] = a[0][8]
    elif m == 'D':
        y[5][0] = a[5][6]
        y[5][1] = a[5][3]
        y[5][2] = a[5][0]
        y[5][3] = a[5][7]
        y[5][4] = a[5][4]
        y[5][5] = a[5][1]
        y[5][6] = a[5][8]
        y[5][7] = a[5][5]
        y[5][8] = a[5][2]
        y[1][6] = a[0][6]
        y[1][7] = a[0][7]
        y[1][8] = a[0][8]
        y[0][6] = a[3][6]
        y[0][7] = a[3][7]
        y[0][8] = a[3][8]
        y[2][6] = a[1][6]
        y[2][7] = a[1][7]
        y[2][8] = a[1][8]
        y[3][6] = a[2][6]
        y[3][7] = a[2][7]
        y[3][8] = a[2][8]
    elif m == 'd':
        y[5][0] = a[5][2]
        y[5][1] = a[5][5]
        y[5][2] = a[5][8]
        y[5][3] = a[5][1]
        y[5][4] = a[5][4]
        y[5][5] = a[5][7]
        y[5][6] = a[5][0]
        y[5][7] = a[5][3]
        y[5][8] = a[5][6]
        y[1][6] = a[2][6]
        y[1][7] = a[2][7]
        y[1][8] = a[2][8]
        y[0][6] = a[1][6]
        y[0][7] = a[1][7]
        y[0][8] = a[1][8]
        y[2][6] = a[3][6]
        y[2][7] = a[3][7]
        y[2][8] = a[3][8]
        y[3][6] = a[0][6]
        y[3][7] = a[0][7]
        y[3][8] = a[0][8]
    elif m == 'Q': 
        y[4][0] = a[4][8]
        y[4][1] = a[4][7]
        y[4][2] = a[4][6]
        y[4][3] = a[4][5]
        y[4][4] = a[4][4]
        y[4][5] = a[4][3]
        y[4][6] = a[4][2]
        y[4][7] = a[4][1]
        y[4][8] = a[4][0]
        y[0][0] = a[2][0]
        y[0][1] = a[2][1]
        y[0][2] = a[2][2]
        y[1][0] = a[3][0]
        y[1][1] = a[3][1]
        y[1][2] = a[3][2]
        y[2][0] = a[0][0]
        y[2][1] = a[0][1]
        y[2][2] = a[0][2]
        y[3][0] = a[1][0]
        y[3][1] = a[1][1]
        y[3][2] = a[1][2]    
    return y
def daucong1(rubik):
    var = 1
    sumxoay=''
    while var == 1:
        rubik_a = copy.deepcopy(rubik)          # vien trang tang 3
        if rubik[1][7] == 5.1:
            xoay = "DRdF"
            print(xoay) 
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[2][7] == 5.1:
            xoay = "RF"
            print(xoay)          
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][7] == 5.1:
            xoay = "dRF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[0][7] == 5.1:
            xoay = "lf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[5][7] == 5.1:
            xoay = "BBQFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][1] == 5.1:
            xoay = "FRUrFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[2][1] == 5.1:
            xoay = "rF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][1] == 5.1:
            xoay = "UrF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[0][1] == 5.1:
            xoay = "Lf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 5.1:
            xoay = "FF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1] == 5.1:
            xoay = "QFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][5] == 5.1:
            xoay = "RUrFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a= hoanvi(rubik_a, i)
        elif rubik[5][5] == 5.1:
            xoay = "RRUrrFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a= hoanvi(rubik_a, i)
        elif rubik[3][3] == 5.1:
            xoay = "rURFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 5.1:
            xoay = "UFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                 rubik_a = hoanvi(rubik_a, i)
        elif rubik[2][3] == 5.1:
            xoay = "F"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[2][5] == 5.1:
            xoay = "rrFRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][3] == 5.1:
            xoay = "luLFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[5][3] == 5.1:
            xoay = "LLullFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][5] == 5.1:
            xoay = "LulFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 5.1:
            xoay = "uFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[0][5] == 5.1:
            xoay = "f"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[0][3] == 5.1:
            xoay = "LLfll"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        else:
             xoay=''
        if rubik_a[5][1] == 5.1:
            break
        else:rubik = copy.deepcopy(rubik_a)
    return rubik_a,sumxoay
def daucong2(rubik):
    var = 1
    sumxoay=''
    while var == 1:
        rubik_b = copy.deepcopy(rubik)  # mau luc
        if rubik [2][7] == 5.5:
            xoay = "DBdR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik [3][7] == 5.5:
            xoay = "BR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[0][7] == 5.5:
            xoay = "dBDR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik [1][7] == 5.5:
            xoay = "frF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik [5][3] == 5.5:
            xoay = "LLQRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[2][1] == 5.5:
            xoay = "RBUbRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[3][1] == 5.5:
            xoay = "bR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[0][1] == 5.5:
            xoay = "UbR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[1][1] == 5.5:
            xoay = "Frf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[4][5] == 5.5:
            xoay = "RR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[4][3] == 5.5:
            xoay = "QRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[2][5] == 5.5:
            xoay = "BUbRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b= hoanvi(rubik_b, i)
        elif rubik[5][7] == 5.5:
            xoay = "bbUBBRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[0][3] == 5.5:
            xoay = "bUBRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[4][1] == 5.5:
            xoay = "URR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[3][3] == 5.5:
            xoay = "R"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[3][5] == 5.5:
            xoay = "bbRBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[2][3] == 5.5:
            xoay = "fuFRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[5][1] == 5.5:
            xoay = "FFuffRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[0][5] == 5.5:
            xoay = "FufRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[4][7] == 5.5:
            xoay = "uRR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[1][5] == 5.5:
            xoay = "r"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        elif rubik[1][3] == 5.5:
            xoay = "FFrff"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_b = hoanvi(rubik_b, i)
        else: xoay =''
        if rubik_b[5][5] == 5.5:
            break
        else:rubik = copy.deepcopy(rubik_b)
    return rubik_b, sumxoay
def daucong3(rubik):
    var = 1
    sumxoay=''
    while var == 1:
        rubik_c = copy.deepcopy(rubik)# mau cam
        if rubik [3][7] == 5.7:
            xoay = "DLdB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik [0][7] == 5.7:
            xoay = "LB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik [1][7] == 5.7:
            xoay = "dLB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik [2][7] == 5.7:
            xoay = "rbR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik [5][1] == 5.7:
            xoay = "FFQBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[3][1] == 5.7:
            xoay = "BLUlBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[0][1] == 5.7:
            xoay = "lB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[1][1] == 5.7:
            xoay = "UlB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[2][1] == 5.7:
            xoay = "Rbr"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[4][1] == 5.7:
            xoay = "BB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[4][7] == 5.7:
            xoay = "QBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[3][5] == 5.7:
            xoay = "LUlBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[5][3] == 5.7:
            xoay = "llULLBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c= hoanvi(rubik_c, i)
        elif rubik[1][3] == 5.7:
            xoay = "lULBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[4][3] == 5.7:
            xoay = "UBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[0][3] == 5.7:
            xoay = "B"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[0][5] == 5.7:
            xoay = "llBLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[3][3] == 5.7:
            xoay = "ruRBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[5][5] == 5.7:
            xoay = "RRurrBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[1][5] == 5.7:
            xoay = "RurBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[4][5] == 5.7:
            xoay = "uBB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[2][5] == 5.7:
            xoay = "b"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        elif rubik[2][3] == 5.7:
            xoay = "RRbrr"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_c = hoanvi(rubik_c, i)
        else:
            xoay =''
        if rubik_c[5][7] == 5.7:
            break
        else:rubik = copy.deepcopy(rubik_c)
    return rubik_c, sumxoay
def daucong4(rubik):
    var = 1
    sumxoay=''
    while var == 1:
        rubik_d = copy.deepcopy(rubik)         # mau xanh
        if rubik [0][7] == 5.3:
            xoay = "DFdL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[1][7] == 5.3:
            xoay = "FLf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[2][7] == 5.3:
            xoay = "dFLf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[5][5] == 5.3:
            xoay = "RRQLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[0][1] == 5.3:
            xoay = "LFUfLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d= hoanvi(rubik_d, i)
        elif rubik[1][1] == 5.3:
            xoay = "fLF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)               
        elif rubik[2][1] == 5.3:
            xoay = "UfLF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d= hoanvi(rubik_d, i)
        elif rubik[3][1] == 5.3:
            xoay = "Blb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d= hoanvi(rubik_d, i)
        elif rubik[4][3] == 5.3:
            xoay = "LL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d= hoanvi(rubik_d, i)
        elif rubik[4][5] == 5.3:
            xoay = "QLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d= hoanvi(rubik_d, i)
        elif rubik[0][5] == 5.3:
            xoay = "FUfLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[5][1] == 5.3:
            xoay = "ffUFFLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[2][3] == 5.3:
            xoay = "fUFLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[4][7] == 5.3:
            xoay = "ULL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[1][3] == 5.3:
            xoay = "L"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[1][5] == 5.3:
            xoay = "ffLFF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[0][3] == 5.3:
            xoay = "buBLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[5][1] == 5.3:
            xoay = "BBubbLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[2][5] == 5.3:
            xoay = "BubLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[4][1] == 5.3:
            xoay = "uLL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[3][5] == 5.3:
            xoay = "l"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        elif rubik[3][3] == 5.3:
            xoay = "BBlbb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_d = hoanvi(rubik_d, i)
        else: 
            xoay =''
        if rubik_d[5][3] == 5.3:
            break
        else:rubik = copy.deepcopy(rubik_d)
    return rubik_d, sumxoay
def goc(rubik): #goc tang1
    x= 1
    sumxoay = ''
    while x == 1:
        rubik_g = copy.deepcopy(rubik)
        if rubik[1][2] == 5.2: #XLDO
            xoay = "fuF"             
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[2][0] == 5.2:
            xoay = "RUr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[4][8] == 5.2:
            xoay = "RurQ"
            print(xoay)           
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[2][6] == 5.2 or rubik [1][8]==5.2:
            xoay = "RUru"
            print(xoay)           
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[1][0] == 5.2 or rubik[0][2] == 5.2 or rubik[4][6] == 5.2:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[1][6] == 5.2 or rubik[0][8] == 5.2 or rubik[5][0] == 5.2:
            xoay = "luL"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[4][0] == 5.2 or rubik[3][2] == 5.2 or rubik[0][0] == 5.2:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[0][6] == 5.2 or rubik[3][8] == 5.2 or rubik[5][6] == 5.2:
            xoay = "buB"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[3][6] == 5.2 or rubik[5][8] == 5.2 or rubik[2][8] == 5.2:
            xoay = "BUb"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)
        elif rubik[2][2] == 5.2 or rubik[4][2] == 5.2 or rubik[3][0] == 5.2:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_g = hoanvi(rubik_g, i)        
        else: xoay=''        
        if rubik_g[5][2] == 5.2 :
            break
        else:     rubik = copy.deepcopy(rubik_g)
    return rubik_g, sumxoay
def goc1(rubik):
    x = 1
    sumxoay=''
    while x == 1:
        rubik_g1 = copy.deepcopy(rubik)
        if rubik[1][0] == 5.0:
            xoay = "FUf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1= hoanvi(rubik_g1, i)
        elif rubik[0][2] == 5.0:
            xoay = "luL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1= hoanvi(rubik_g1, i)
        elif rubik[4][6] == 5.0:
            xoay = "lQLU"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1 = hoanvi(rubik_g1, i)
        elif rubik[0][8] == 5.0 or rubik[1][6] == 5.0:
            xoay = "luLU"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1 = hoanvi(rubik_g1, i)
        elif rubik[0][0] == 5.0 or rubik[3][2] == 5.0 or rubik[4][0] == 5.0:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1 = hoanvi(rubik_g1, i)
        elif rubik[0][6] == 5.0 or rubik[3][8] == 5.0 or rubik[5][6] == 5.0:
            xoay = "LulU"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1 = hoanvi(rubik_g1, i)
        elif rubik[2][2] == 5.0 or rubik[3][0] == 5.0 or rubik[4][2] == 5.0:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1 = hoanvi(rubik_g1, i)
        elif rubik[2][8] == 5.0 or rubik[3][6] == 5.0 or rubik[5][8] == 5.0:
            xoay = "Bub"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1= hoanvi(rubik_g1, i)
        elif rubik[1][2] == 5.0 or rubik[2][0] == 5.0 or rubik[4][8] == 5.0:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1= hoanvi(rubik_g1, i)
        elif rubik[1][8] == 5.0 or rubik[2][6] == 5.0 or rubik[5][2] == 5.0:
            xoay = "RUr"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g1= hoanvi(rubik_g1, i)
        else: xoay=''        
        if rubik_g1 [5][2]==5.2 and rubik_g1[5][0]==5.0:
            break
        else: rubik = copy.deepcopy(rubik_g1)
    return  rubik_g1, sumxoay
def goc2(rubik):
    x = 1
    sumxoay=''
    while x == 1:
        rubik_g2 = copy.deepcopy(rubik)  # xdcam
        if rubik[0][0] == 5.6:  ##
            xoay = "LUl"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[3][2] == 5.6:
            xoay = "buB"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[4][0] == 5.6:
            xoay = "LQlu"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[3][8] == 5.6 or rubik[0][6] == 5.6:
            xoay = "LUlu"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[4][2] == 5.6 or rubik[2][2] == 5.6 or rubik[3][0] == 5.6:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[3][6] == 5.6 or rubik[2][8] == 5.6 or rubik[5][8] == 5.6:
            xoay = "ruRU"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[4][8] == 5.6 or rubik[1][2] == 5.6 or rubik[2][0] == 5.6:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        elif rubik[1][0] == 5.6 or rubik[0][2] == 5.6 or rubik[4][6] == 5.6:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g2 = hoanvi(rubik_g2, i)
        else: xoay=''       
        if rubik_g2[5][6] == 5.6 and rubik_g2[5][2] == 5.2 and rubik_g2[5][0] == 5.0:
            break
        else: rubik = copy.deepcopy(rubik_g2)
    return rubik_g2, sumxoay
def goc3(rubik):
    x = 1
    sumxoay=''
    while x == 1:
        rubik_g3 = copy.deepcopy(rubik)  # xlcam
        if   rubik[2][2] == 5.8:
            xoay = "ruR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g3 = hoanvi(rubik_g3, i)
        elif rubik[4][2] == 5.8 or rubik[3][0] == 5.8:
            xoay = "BUb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g3 = hoanvi(rubik_g3, i)
        elif rubik[2][8] == 5.8 or rubik[3][6] == 5.8:
            xoay = "BUbu"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g3 = hoanvi(rubik_g3, i)
        elif rubik[2][0] == 5.8 or rubik[1][2] == 5.8 or rubik[4][8]==5.8 :
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g3 = hoanvi(rubik_g3, i)
        elif rubik[1][0] == 5.8 or rubik[0][2] == 5.8 or rubik[4][6] == 5.8:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g3 = hoanvi(rubik_g3, i)
        elif rubik[0][0] == 5.8 or rubik[3][2] == 5.8 or rubik[4][0] == 5.8:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_g3 = hoanvi(rubik_g3, i)
        else: xoay=''
        if rubik_g3[5][2] == 5.2 and rubik_g3[5][0] == 5.0 and rubik_g3[5][6] == 5.6 and rubik_g3[5][8] == 5.8:
            break
        else:
            rubik = copy.deepcopy(rubik_g3)
    return rubik_g3,sumxoay
def tang2xl1(rubik): #cac cach tang2 mau xanh la
    x = 1
    sumxoay=''
    while x == 1:
        rubik_e = copy.deepcopy(rubik)  #xl
        if rubik[2][1] == 2.3 :
            xoay = "ufuFURUr"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif  rubik[4][5] == 2.3:
            xoay = "QRUrufuF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[1][5] == 2.3  :
            xoay = "fuFURUrQ"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[4][7] == 2.3 :
            xoay = "URUrufuF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[2][5] == 2.3 or rubik[3][3] == 2.3:
            xoay = "BUburuRQ"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[1][3] == 2.3 or rubik[0][5] == 2.3:
            xoay = "luLUFUfU"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[3][5] == 2.3 or rubik[0][3] == 2.3:
            xoay = "buBULUl"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[3][3] == 2.3 or rubik[2][5] == 2.3:
            xoay = "BUburuR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[1][1] == 2.3 or rubik[4][7] == 2.3:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[0][1] == 2.3 or rubik[4][3] == 2.3:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        elif rubik[3][1] == 2.3 or rubik[4][1] == 2.3:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_e = hoanvi(rubik_e, i)
        else: xoay=''
        if rubik_e[2][3]==2.3:
            break
        else: rubik = copy.deepcopy(rubik_e)
    return rubik_e,sumxoay
def tang2xl2(rubik):
    x= 1
    sumxoay=''
    while x ==1:
        rubik_f= copy.deepcopy(rubik)
        if rubik[2][1] == 2.5 :
            xoay = "UBUburuR"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[4][5] == 2.5:
            xoay = "QruRUBUb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[3][3] == 2.5:
            xoay = "BUburuRQ"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[3][1] == 2.5  or rubik[4][3] == 2.5:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[4][1] == 2.5:
            xoay = "uruRUBUb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[3][5] == 2.5 or rubik[0][3] == 2.5:
            xoay = "LUlubuBu"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[0][1] == 2.5  or rubik[4][7] == 2.5 :
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[1][1] == 2.5  :
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        elif rubik[0][5] == 2.5 or rubik[1][3] == 2.5:
            xoay = "luLUFUf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_f = hoanvi(rubik_f, i)
        else: xoay=''       
        if rubik_f [2][5]==2.5 and rubik_f[2][3]==2.3:
            break
        else: rubik = copy.deepcopy(rubik_f)
    return  rubik_f,sumxoay
def tang2xd (rubik): #tang 2 mau xanh duong
    var = 1
    sumxoay=''
    while var == 1:        # phai
        rubik_a = copy.deepcopy(rubik)
        if rubik[0][1] == 0.5 :
            xoay = "UFufLflF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 0.5:
            xoay = "QlULfLFl"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][1] == 0.5 or rubik[4][1] == 0.5:
            xoay = "FufLflF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[2][1] == 0.5 or rubik[4][5] == 0.5:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][1] == 0.5 or rubik[4][7] == 0.5:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][5] == 0.5 or rubik[0][3] == 0.5:
            xoay = "ULulBlbL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][3] == 0.5 :
            xoay = "FUfQFQfUluL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[0][1] == 0.3:        #trai
            xoay = "ubUBlBLb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 0.3:
            xoay = "QLulBlbL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][1] == 0.3 or rubik[4][1] == 0.3:
            xoay = "bUBlBLb"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[2][1] == 0.3 or rubik[4][5] == 0.3:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][1] == 0.3 or rubik[4][7] == 0.3:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[3][5] == 0.3 :
            xoay = "ULulBlbL"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[1][3] == 0.3:
            xoay = "UFufLflF"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        else: xoay=''
        if rubik_a[0][5] == 0.5 and rubik_a[0][3]==0.3:
            break
        else:rubik = copy.deepcopy(rubik_a)
    return rubik_a,sumxoay
def chuL(rubik):
    var = 1
    sumxoay=''
    while var == 1:
        rubik_a = copy.deepcopy(rubik)
        if (rubik[4][5] == 4.5 or rubik[4][5] == 4.3 or rubik[4][5] == 4.1 or rubik[4][5] == 4.7) and (
            rubik[4][3] == 4.3 or rubik[4][3] == 4.1 or rubik[4][3] == 4.5 or rubik[4][3] == 4.7)and (rubik[4][1] == 4.1 or rubik[4][1] == 4.3 or rubik[4][1] == 4.5 or rubik[4][1] == 4.7 ) and (rubik[4][7] == 4.1 or rubik[4][7] == 4.3 or rubik[4][7] == 4.5 or rubik[4][7] == 4.7) :
            break
        elif rubik[4][1]== 4.1 and rubik[4][3] == 4.3 :
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1]== 4.1 and rubik[4][3] == 4.5 :
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1]== 4.1 and rubik[4][3] == 4.7 :
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 4.1 and rubik [4][1] == 4.3: # 4.1 4.3
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.1 and rubik [4][5] == 4.3:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.1 and rubik [4][7] == 4.3:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 4.1 and rubik [4][1] == 4.5:  #4.1 4.5
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.1 and rubik [4][5] == 4.5:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.1 and rubik [4][7] == 4.5:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 4.1 and rubik[4][1] == 4.7:    #4.1 4.7
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.1 and rubik[4][5] == 4.7:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.1 and rubik[4][7] == 4.7:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1]== 4.5 and rubik[4][3] == 4.1 :    # 4.5
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1]== 4.5 and rubik[4][3] == 4.3 :
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1]== 4.5 and rubik[4][3] == 4.7 :
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 4.5 and rubik[4][1] == 4.1:  # 4.5 4.1
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.5 and rubik[4][5] == 4.1:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.5 and rubik[4][7] == 4.1:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 4.5 and rubik[4][1] == 4.3:   #4.5 4.3
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.5 and rubik[4][5] == 4.3:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.5 and rubik[4][7] == 4.3:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5] == 4.5 and rubik[4][1] == 4.7:    # 4.5 4.7
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.5 and rubik[4][5] == 4.7:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.5 and rubik[4][7] == 4.7:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1] == 4.7 and rubik[4][3] == 4.1:
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1] == 4.7 and rubik[4][3] == 4.3:
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1] == 4.7 and rubik[4][3] == 4.5:
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)    #4.7
        elif rubik[4][5] == 4.7 and rubik[4][1] == 4.1:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.7 and rubik[4][5] == 4.1:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.7 and rubik[4][7] == 4.1:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)     # 4.7 4.1
        elif rubik[4][5] == 4.7 and rubik[4][1] == 4.5:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.7 and rubik[4][5] == 4.5:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.7 and rubik[4][7] == 4.5:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)      # 4.7 4.5
        elif rubik[4][5] == 4.7 and rubik[4][1] == 4.3:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.7 and rubik[4][5] == 4.3:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.7 and rubik[4][7] == 4.3:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)    #4.7 4.3
        elif rubik[4][1] == 4.3 and rubik[4][3] == 4.1:
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1] == 4.3 and rubik[4][3] == 4.5:
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][1] == 4.3 and rubik[4][3] == 4.7:
            xoay = "FURurf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)    #4.3
        elif rubik[4][5] == 4.3 and rubik[4][1] == 4.1:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.3 and rubik[4][5] == 4.1:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.3 and rubik[4][7] == 4.1:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)    # 4.3 4.1
        elif rubik[4][5] == 4.3 and rubik[4][1] == 4.5:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.3 and rubik[4][5] == 4.5:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.3 and rubik[4][7] == 4.5:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)    #4.3 4.5
        elif rubik[4][5] == 4.3 and rubik[4][1] == 4.7:
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][7] == 4.3 and rubik[4][5] == 4.7:
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3] == 4.3 and rubik[4][7] == 4.7:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)    # 4.3 4.7
        elif rubik[4][3]== 4.1 and rubik[4][5] == 4.3 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3]== 4.1 and rubik[4][5] == 4.5 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3]== 4.1 and rubik[4][5] == 4.7 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.1 trai
        elif rubik[4][5]== 4.1 and rubik[4][3] == 4.3 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5]== 4.1 and rubik[4][3] == 4.5 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][5]== 4.1 and rubik[4][3] == 4.7 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.1 phai
        elif (rubik[4][1] == 4.1) and (rubik[4][7] == 4.3 or rubik[4][7] == 4.5 or rubik[4][7] == 4.7):
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.1 tren
        elif rubik[4][7] == 4.1 and(rubik[4][1] == 4.3 or rubik[4][1] == 4.5 or rubik[4][1] == 4.7) :
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.1 duoi
        elif rubik[4][3]== 4.5 and rubik[4][5] == 4.3 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.5 trai
        elif rubik[4][3]== 4.5 and rubik[4][5] == 4.7 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif rubik[4][3]== 4.3 and rubik[4][5] == 4.5 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.5 phai
        elif rubik[4][3]== 4.7 and rubik[4][5] == 4.5 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.5) and (rubik[4][7] == 4.3 or rubik[4][7] == 4.7):
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.5 tren
        elif (rubik[4][7] == 4.5) and (rubik[4][1] == 4.3 or rubik[4][1] == 4.7):
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.5 duoi
        elif rubik[4][3]== 4.7 and rubik[4][5] == 4.3 :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.7 trai
        elif rubik[4][3] == 4.3 and rubik[4][5] == 4.7:
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.7 phai
        elif rubik[4][1] == 4.7 and  rubik[4][7] == 4.3:
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.7 tren
        elif rubik[4][7] == 4.7 and rubik[4][1] == 4.3 :
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)#4.7 duoi
        elif(rubik[4][5] != 4.5 and rubik[4][5] != 4.3 and rubik[4][5] != 4.1 and rubik[4][5] != 4.7) and (
                rubik[4][3] != 4.3 and rubik[4][3] != 4.1 and rubik[4][3] != 4.5 and rubik[4][3] != 4.7)and (rubik[4][1] != 4.1 and rubik[4][1] != 4.3 and rubik[4][1] != 4.5 and rubik[4][1] != 4.7 ) and (rubik[4][7] != 4.1 and rubik[4][7] != 4.3 and rubik[4][7] != 4.5 and rubik[4][7] != 4.7) :
            xoay = "FRUruf"
            print(xoay)
            sumxoay = sumxoay+ xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        else: xoay=''        
        if(rubik_a[4][5] == 4.5 or rubik_a[4][5] == 4.3 or rubik_a[4][5] == 4.1 or rubik_a[4][5] == 4.7) and (
        rubik_a[4][3] == 4.3 or rubik_a[4][3] == 4.1 or rubik_a[4][3] == 4.5 or rubik_a[4][3] == 4.7) and (rubik_a[4][1] == 4.1 or rubik_a[4][1] == 4.3 or rubik_a[4][1] == 4.5 or rubik_a[4][1] == 4.7 ) and (rubik_a[4][7] == 4.1 or rubik_a[4][7] == 4.3 or rubik_a[4][7] == 4.5 or rubik_a[4][7] == 4.7) :
            break
        else: rubik = copy.deepcopy(rubik_a)
    return rubik_a,sumxoay
def fullmat(rubik):
    var = 1
    sumxoay = ''
    while var == 1:
        rubik_a = copy.deepcopy(rubik)
        if (rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6) and (
                rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6) and (
                rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6):
            xoay = "RUrURQr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6) and (
                rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6)and (
                rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6):
            xoay = "BUbUBQb"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (

                 rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6) and (
                 rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6)and (
                rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6):
            xoay = "LUlULQl"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6) and (
             rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6) and (
             rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6):


            xoay = "FUfUFQf"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
            rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6) and (
            rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6) and (
            rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6):
            xoay = "RQruRur"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6) and (
             rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6) and (
             rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6):
            xoay = "BQbuBub"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6) and (
             rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6) and (
             rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6):
            xoay = "LQluLul"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6) and (
             rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6) and (
             rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6):
            xoay = "FQfuFuf"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6) and (
             rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6) and (
             rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6) and (
            rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6):
            xoay = "RQruRUruRur"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (
             rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6) and (
             rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6) and (
             rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6) and (
            rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6):
            xoay = "BQbuBUbuBub"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (
             rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6) and (
             rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6) and (
             rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6) and (
            rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6):
            xoay = "RQrruRRurrQR"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6) and (
             rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6) and (
             rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6) and (
            rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6):
            xoay = "BQbbuBBubbQB"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6) and (
             rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6) and (
             rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6) and (
            rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6):
            xoay = "LQlluLLullQL"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6) and (
             rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6) and (
             rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6) and (
            rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6):
            xoay = "FQffuFFuffQF"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
             rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6) and (
             rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6):

            xoay = "RRDrQRdrQr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6) and (
                rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6):

            xoay = "BBDbQBdbQb"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6) and (
                rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6):

            xoay = "LLDlQLdlQl"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6) and (
                rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6):

            xoay = "FFDfQFdfQf"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6) and (
                rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6):

            xoay = "LFrflFRf"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6) and (
                rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6):

            xoay = "FRbrfRBr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6) and (
                rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6):

            xoay = "RBlbrBLb"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (
                rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6) and (
                rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6):

            xoay = "BLflbLFl"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (
                rubik[1][2] == 4.0 or rubik[1][2] == 4.2 or rubik[1][2] == 4.8 or rubik[1][2] == 4.6) and (
                rubik[0][0] == 4.0 or rubik[0][0] == 4.2 or rubik[0][0] == 4.8 or rubik[0][0] == 4.6):

            xoay = "fLFrflFR"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (
                rubik[2][2] == 4.0 or rubik[2][2] == 4.2 or rubik[2][2] == 4.8 or rubik[2][2] == 4.6) and (
                rubik[1][0] == 4.0 or rubik[1][0] == 4.2 or rubik[1][0] == 4.8 or rubik[1][0] == 4.6):

            xoay = "rFRbrfRB"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (
                rubik[3][2] == 4.0 or rubik[3][2] == 4.2 or rubik[3][2] == 4.8 or rubik[3][2] == 4.6) and (
                rubik[2][0] == 4.0 or rubik[2][0] == 4.2 or rubik[2][0] == 4.8 or rubik[2][0] == 4.6):

            xoay = "bRBlbrBL"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (
                rubik[0][2] == 4.0 or rubik[0][2] == 4.2 or rubik[0][2] == 4.8 or rubik[0][2] == 4.6) and (
                rubik[3][0] == 4.0 or rubik[3][0] == 4.2 or rubik[3][0] == 4.8 or rubik[3][0] == 4.6):

            xoay = "lBLflbLF"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)


        if (rubik_a[4][5] == 4.5 or rubik_a[4][5] == 4.3 or rubik_a[4][5] == 4.1 or rubik_a[4][5] == 4.7) and (
                rubik_a[4][3] == 4.3 or rubik_a[4][3] == 4.1 or rubik_a[4][3] == 4.5 or rubik_a[4][3] == 4.7) and (
                rubik_a[4][1] == 4.1 or rubik_a[4][1] == 4.3 or rubik_a[4][1] == 4.5 or rubik_a[4][1] == 4.7) and (
                rubik_a[4][7] == 4.1 or rubik_a[4][7] == 4.3 or rubik_a[4][7] == 4.5 or rubik_a[4][7] == 4.7) and (
                rubik_a[4][0] == 4.0 or rubik_a[4][0] == 4.2 or rubik_a[4][0] == 4.8 or rubik_a[4][0] == 4.6) and (
                rubik_a[4][2] == 4.0 or rubik_a[4][2] == 4.2 or rubik_a[4][2] == 4.8 or rubik_a[4][2] == 4.6) and (
                rubik_a[4][6] == 4.0 or rubik_a[4][6] == 4.2 or rubik_a[4][6] == 4.8 or rubik_a[4][6] == 4.6) and (
                rubik_a[4][8] == 4.0 or rubik_a[4][8] == 4.2 or rubik_a[4][8] == 4.8 or rubik_a[4][8] == 4.6):

            break
        else :
            xoay= ''
            rubik = copy.deepcopy(rubik_a)
    return rubik_a , sumxoay
def gocvang(rubik):
    var = 1
    sumxoay = ''
    while var == 1:
        rubik_a = copy.deepcopy(rubik)
        if (rubik[4][0] == 4.0 and rubik[4][6] == 4.6 and rubik[4][2] == 4.8 and rubik[4][8] == 4.2) or (
                rubik[4][0] == 4.2 and rubik[4][6] == 4.0 and rubik[4][2] == 4.6 and rubik[4][8] == 4.8) or (
                rubik[4][0] == 4.8 and rubik[4][6] == 4.2 and rubik[4][2] == 4.0 and rubik[4][8] == 4.6 )or (
                rubik[4][0] == 4.6 and rubik[4][6] == 4.8 and rubik[4][2] == 4.2 and rubik[4][8] == 4.0):
            xoay = "RUrfRUrurFRRur"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][6] == 4.0 and rubik[4][8] == 4.6 and rubik[4][0] == 4.8 and rubik[4][2] == 4.2) or (
                rubik[4][6] == 4.2 and rubik[4][8] == 4.0 and rubik[4][0] == 4.6 and rubik[4][2] == 4.8) or (
                rubik[4][6] == 4.8 and rubik[4][8] == 4.2 and rubik[4][0] == 4.0 and rubik[4][2] == 4.6 )or (
                rubik[4][6] == 4.6 and rubik[4][8] == 4.8 and rubik[4][0] == 4.2 and rubik[4][2] == 4.0):
            xoay = "BUbrBUbubRBBub"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][8] == 4.0 and rubik[4][2] == 4.6 and rubik[4][6] == 4.8 and rubik[4][0] == 4.2) or (
                rubik[4][8] == 4.2 and rubik[4][2] == 4.0 and rubik[4][6] == 4.6 and rubik[4][0] == 4.8) or (
                rubik[4][8] == 4.8 and rubik[4][2] == 4.2 and rubik[4][6] == 4.0 and rubik[4][0] == 4.6 )or (
                rubik[4][8] == 4.6 and rubik[4][2] == 4.8 and rubik[4][6] == 4.2 and rubik[4][0] == 4.0):
            xoay = "LUlbLUlulBLLul"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][2] == 4.0 and rubik[4][0] == 4.6 and rubik[4][8] == 4.8 and rubik[4][6] == 4.2) or (
                rubik[4][2] == 4.2 and rubik[4][0] == 4.0 and rubik[4][8] == 4.6 and rubik[4][6] == 4.8) or (
                rubik[4][2] == 4.8 and rubik[4][0] == 4.2 and rubik[4][8] == 4.0 and rubik[4][6] == 4.6 )or (
                rubik[4][2] == 4.6 and rubik[4][0] == 4.8 and rubik[4][8] == 4.2 and rubik[4][6] == 4.0):
            xoay = "FUflFUfufLFFuf"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][0] == 4.8 and rubik[4][2] == 4.2 and rubik[4][8] == 4.0 and rubik[4][6] == 4.6) or (
                rubik[4][0] == 4.6 and rubik[4][2] == 4.8 and rubik[4][8] == 4.2 and rubik[4][6] == 4.0) :
            xoay = "FRuruRUrfRUrurFRf"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][0] == 4.0 and rubik[4][2] == 4.6 and rubik[4][8] == 4.8 and rubik[4][6] == 4.2) or (
                rubik[4][0] == 4.2 and rubik[4][2] == 4.0 and rubik[4][8] == 4.6 and rubik[4][6] == 4.8) :
            xoay = "RBubuBUbrBUbubRBr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (rubik[4][0] == 4.2 and rubik[4][2] == 4.8 and rubik[4][8] == 4.6 and rubik[4][6] == 4.0) :
            xoay = "U"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][0] == 4.8 and rubik[4][2] == 4.6 and rubik[4][8] == 4.0 and rubik[4][6] == 4.2) :
            xoay = "Q"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][0] == 4.6 and rubik[4][2] == 4.0 and rubik[4][8] == 4.2 and rubik[4][6] == 4.8):
            xoay = "u"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)


        if  ( rubik_a[4][0] == 4.0 and rubik_a[4][2] == 4.2 and rubik_a[4][8] == 4.8 and rubik_a[4][6] == 4.6) :
            break
        else:
            xoay = ''
            rubik = copy.deepcopy(rubik_a)
    return rubik_a, sumxoay
def canhvang(rubik):
    var = 1
    sumxoay = ''
    while var == 1:
        rubik_a = copy.deepcopy(rubik)
        if (rubik[4][1] == 4.1 and rubik[4][5] == 4.7 and rubik[4][7] == 4.3 and rubik[4][3] == 4.5):
            xoay = "RRURUrururUr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)

        elif (rubik[4][1] == 4.5 and rubik[4][5] == 4.7 and rubik[4][7] == 4.1 and rubik[4][3] == 4.3):
            xoay = "BBUBUbububUb"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.5 and rubik[4][5] == 4.3 and rubik[4][7] == 4.7 and rubik[4][3] == 4.1):
            xoay = "LLULUlululUl"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.7 and rubik[4][5] == 4.5 and rubik[4][7] == 4.3 and rubik[4][3] == 4.1):
            xoay = "LLULUlululUl"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.1 and rubik[4][5] == 4.3 and rubik[4][7] == 4.5 and rubik[4][3] == 4.7):
            xoay = "RuRURURuruRR"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.7 and rubik[4][5] == 4.1 and rubik[4][7] == 4.5 and rubik[4][3] == 4.3):
            xoay = "BuBUBUBubuBB"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.3 and rubik[4][5] == 4.1 and rubik[4][7] == 4.7 and rubik[4][3] == 4.5):
            xoay = "LuLULULuluLL"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] == 4.3 and rubik[4][5] == 4.5 and rubik[4][7] == 4.1 and rubik[4][3] == 4.7):
            xoay = "FuFUFUFufuFF"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)
        elif (rubik[4][1] != 4.1 and rubik[4][5] != 4.5 and rubik[4][7] != 4.7 and rubik[4][3] != 4.3):
            xoay = "RRURUrururUr"
            print(xoay)
            sumxoay = sumxoay + xoay
            for i in xoay:
                rubik_a = hoanvi(rubik_a, i)



        if (rubik_a[4][1] == 4.1 and rubik_a[4][5] == 4.5 and rubik_a[4][7] == 4.7 and rubik_a[4][3] == 4.3):
            break
        else:
            xoay = ''
            rubik = copy.deepcopy(rubik_a)
    return rubik_a, sumxoay

t1 = threading.Thread(target=test_dieu_khien_song_song)
t1.start()

s = run()
print(s)
sumxoay =""  
rubik=ganmau(rubik)
inrubik(rubik)        
ketqua = daucong1(rubik)   
sumxoay = sumxoay + ketqua[1]         
ketqua = daucong2(ketqua[0])          
sumxoay = sumxoay + ketqua[1] 
ketqua = daucong3(ketqua[0])            
sumxoay = sumxoay + ketqua[1] 
ketqua = daucong4(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = goc(ketqua[0]) 
sumxoay = sumxoay + ketqua[1]
ketqua = goc1(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = goc2(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua= goc3(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = tang2xl1(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = tang2xl2(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = tang2xd(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = chuL(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = fullmat(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = gocvang(ketqua[0])
sumxoay = sumxoay + ketqua[1]
ketqua = canhvang(ketqua[0])
sumxoay = sumxoay + ketqua[1]
sumxoay = sumxoay + "x"
inrubik(ketqua[0])
print(sumxoay)
print("Số bước giải",len(sumxoay)-1)
uart()
