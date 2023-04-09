import openai
# Apply the API key
#读取config.json文件中的apiKey
f = open('config.json','r')
content = f.read()
a = json.loads(content)
openai.api_key = a['apiKey']
# Define the text prompt
# prompt = "you are a cute pig"
def chatGPT(prompt):
# Generate completions using the API
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the message from the API response
    message = completions.choices[0].text
    # print(message)
    return message