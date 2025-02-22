from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import pickle
import warnings
from flask_cors import CORS
deployment_name='chatgpt'

warnings.filterwarnings('ignore')

app = Flask(__name__)

CORS(app)

openai.api_key = "739fd2d9541742f481c08d8f79999b6b"
openai.api_base = "https://chi.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview'

def edu(transcript):
    qs_pre = """ create a roadmap of youtube videos along with links to learn
        """
    response = openai.ChatCompletion.create(
    engine="chatgpt", # engine = "deployment_name".
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "is this content informative and educational? " + transcript},
        ]
    )
    return(response['choices'][0]['message']['content'])

def transcript_generator(video):
    transcript = YouTubeTranscriptApi.get_transcript(video[32:])
    l = []
    s = ""
    transcript_text = ""
    for i in transcript:
        l.append(i['text'])
        cur_text =  i['text'] + " "
        s = s + cur_text
    return s

def is_educational(video_link):
    transcript = transcript_generator(video_link)[:512]
    is_edu = edu(transcript).lower()
    if(is_edu.startswith('no')):
      return 0
    else:
      return 1


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=['POST'])
def predict():
    url = request.args.get('url')
    check = is_educational(url)
    return '{ "prediction": "' + str(check) + '" }'

if __name__ == "__main__":
    app.run(port=3333)


