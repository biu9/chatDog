import openai
import json
import requests


# Apply the API key
# Define the text prompt
# prompt = "you are a cute pig"

server = 'http://43.156.70.168:1234/'

def chatGPT(prompt):
    '''
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content":prompt}]
    )
    output_text = completion['choices'][0]['message']['content']
    '''
    response = requests.post(server+'api/gpt', json={
        'text':prompt
    })
    print('response: ',response.json()['data'])
    output_text = response.json()['data']
    return output_text