import cv2 as cv

import streamlit as st

st.title("Webcam Application")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cam = cv.VideoCapture(1)

while run:
    ret, frame = cam.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')