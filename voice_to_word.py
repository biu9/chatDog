import os
import openai
import json


#读取config.json文件中的apiKey
f = open('config.json','r')
content = f.read()
a = json.loads(content)
openai.api_key = a['apiKey']

def get_words(filePath):
    audio_file = open(filePath, "rb")
    print('open file success')
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # print(transcript.text)
    return transcript.text