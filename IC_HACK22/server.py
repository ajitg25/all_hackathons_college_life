# web server using flask
from flask import Flask, send_from_directory, request
import json
import pickle
import numpy as np
from PIL import Image
import cv2
import os
from keras.preprocessing import image
import tensorflow
import json
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.utils import load_img, img_to_array
# port of our API
PORT = 3001

# model = pickle.load(open('predictor.pkl','rb'))
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

dic={10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"o",25:"p",26:"q",27:"r",28:"s",29:"t",30:"u",31:"v",32:"w",33:"x",34:"y",35:"z"}

# in case we want to serve pages
app = Flask(__name__, static_url_path='', static_folder='./public')
@app.route('/')
def home_page():
    return send_from_directory('./public', 'index.html')

# entry point
def main():
    app.run(port=PORT)

@app.route('/detect_hand_gesture', methods=['POST'])
def detect_hand_gesture():

    file = request.files['image']
    file.save('a.png')
    fn = 'a.png'

    img= load_img(fn, target_size=(200, 200))
  
    x= img_to_array(img)
    test_img=np.expand_dims(x, axis=0)


    result = loaded_model.predict(test_img)
    pred = np.argmax(result) # get the index of max value  
    if pred >= 10:
        pred = dic[pred]
    

    return json.dumps({'success':True, 'prediction':pred}), 200, {'ContentType':'application/json'}


# run only if run as a script
if __name__ == '__main__':
    main()