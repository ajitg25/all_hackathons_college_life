from youtube_transcript_api import YouTubeTranscriptApi
deployment_name='chatgpt'

import os
import openai

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

def transcript_generator(url, max_length=512, start_time=-1, end_time=-1):
  if start_time == -1 and end_time == -1:
    transcript = YouTubeTranscriptApi.get_transcript(url[32:47])
    text = ''
    for i in transcript:
      new_text = text + i['text']
      if len(new_text) > max_length:
        return text
      text = new_text
    return text


def is_educational(video_link):
    transcript = transcript_generator(video_link)[:512]
    is_edu = edu(transcript).lower()
    if(is_edu.startswith('no')):
      return 0
    else:
      return 1
    
print(is_educational("https://www.youtube.com/watch?v=-bA71tK0scY&ab_channel=TheInfographicsShow"))