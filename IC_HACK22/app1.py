
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from PIL import Image
# from keras.preprocessing import image, img_to_array
import tensorflow as tf
from tensorflow.keras.utils import img_to_array

# from tensorflow.keras import datasets, layers, models
from numpy import asarray

import matplotlib.pyplot as plt
import cv2

#app=Flask(__name__)
#Swagger(app)

model_file = open("./regmodel.pkl","rb")
model=pickle.load(model_file)



#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict(img):
    dic={10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"o",25:"p",26:"q",27:"r",28:"s",29:"t",30:"u",31:"v",32:"w",33:"x",34:"y",35:"z"}
    
    x=np.asarray(img)
    print(x.shape)
    test_img=np.expand_dims(x, axis=0)
    
    result = model.predict(test_img)
    pred = np.argmax(result) # get the index of max value
    print(pred-1)
    x = pred-1
    if(x>=10):
      print(dic[x])
    
    # for fn in uploaded.keys():


def main():
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    _,frame = camera.read()
    print("FRAME: " , frame.shape)
    # predict(frame)
    while run:
        _, frame = camera.read()
        # print(type(frame))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        predict(frame)
    else:
        st.write('Stopped')
   
    # result=""
    # if st.button("Predict"):
    #     result=predict_note_authentication(variance,skewness,curtosis,entropy)
    # st.success('The output is {}'.format(result))
    # if st.button("About"):
    #     st.text("Lets LEarn")
    #     st.text("Built with Streamlit")

if __name__=='__main__':
    main()