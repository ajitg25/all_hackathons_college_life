import cv2
import streamlit as st
import time
import requests
import io
from PIL import Image
import pickle


st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

prediction_text = st.empty()

last_time = time.time() 
API_BASE_URL = 'http://localhost:3001'

while run:
    _, frame = camera.read()
    try:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

        if time.time() - last_time > 1.0:


            image_file = io.BytesIO()
            image = Image.fromarray(frame)
            image.save(image_file, format = 'PNG') 
            image_file.seek(0)

            response = requests.post(API_BASE_URL + '/detect_hand_gesture', files = {'image': image_file})
            data = response.json()
            print(data['prediction'])
            
            prediction_text.write('Prediction: ' + str(data['prediction']))

            last_time = time.time()
    except Exception as e:
        pass

else:
    st.write('Stopped')