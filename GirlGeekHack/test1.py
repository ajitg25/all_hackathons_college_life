# Python
#import libraries 
import datetime 

import time
import os
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
from gtts import gTTS




import cv2
import numpy as np
thres = 0.45 # Threshold to detect object
nms_threshold = 0.2
print("ajit")
cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,150)
 
classNames= []
classFile = "D:\hackathon\GirlGeekHack\coco.names"
# with open(classFile,'rt') as f:
#     classNames = f.read().rstrip('n').split('n')
with open(classFile,'rt') as f:
    classNames = [line.rstrip() for line in f]

 
#print(classNames)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'
 
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

prev =''
while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    # print(classIds," ",confs," ",bbox)
    bbox = list(bbox)
    # print(bbox)
    confs = list(np.array(confs).reshape(1,-1)[0])
    confs = list(map(float,confs))
    # print(type(confs[0]))
    # print(" ss ",confs)
    # if(confs[0]<0.6):
    #     continue
 
    indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
    # print(objectsss[indices[0][0]])
    # print(objectsss[indices])
    
    text =''
    for i in indices:
        # print(i)
        # print(objectsss[i])
        i = i[0]
        # print(objectsss[i]," " ,confs[0])
        if (prev==classNames[classIds[i][0]-1].upper()):
            continue

        box = bbox[i]
        # print(box)
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)
        cv2.putText(img,classNames[classIds[i][0]-1].upper(),(box[0]+10,box[1]+30),
        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        # print(classNames[classIds[i][0]-1].upper())

        # converting text sample to audio
        
        text+='There is a '+ classNames[classIds[i][0]-1].upper()+' '
        print(text)
        # text+=classNames[classIds[i][0]-1].upper()+' '
        prev = classNames[classIds[i][0]-1].upper()


    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%m/%d/%Y%H:%M:%S")
# print("Output 2:", d)	
    # print(current_time)
    current_time = current_time[10:12]+current_time[13:15]+current_time[16:]

    # print(current_time)
    if(text!=''):
        with open(current_time, 'w') as f:
            f.write(text)
    if(text!=''):
        # using English language as output
        language = 'en' #english
        speech = gTTS(text = text, lang = language, slow = False)
        # saving the audio file in mp3 format
        # speech.save('english_sample.mp3')
        speech.save(current_time+'.mp3')
        #to play string in wav
        os.system(current_time+'.mp3')
        # os.system('english_sample.mp3')

    time.sleep(1)

 
    cv2.imshow("Output",img)
    cv2.waitKey(1)