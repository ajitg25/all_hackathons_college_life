import urllib.parse as urlparse
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


url_data = urlparse.urlparse("https://www.youtube.com/watch?v=fFcQwlJBrn0&ab_channel=StudyGlows")
query = urlparse.parse_qs(url_data.query)
videoID = query["v"][0]
print(videoID)
trans = ""

try:
    srt = YouTubeTranscriptApi.get_transcript(videoID,languages=['en'])
    for i in srt:
        trans+= i['text'] + ' '
    print(trans)
except TranscriptsDisabled:
    print("Transcript not available")
    



