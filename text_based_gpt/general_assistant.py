from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)
messages=[]
# prompt slightly tweaked from what was covered in the video, to fix further edge cases
prompt = {'role': 'system', 
          'content': """You are a general assistant.
          answer the user's questions and provide information on any topic.
          Be sure to provide accurate and up-to-date information.
          Back up your answers with references when possible.
          """}
messages.append(prompt)
while True:
    # send the api call
    response = client.chat.completions.create(messages=messages, model="gpt-3.5-turbo")
    # display response in console
    print(response.choices[0].message.content)
    # expanding the conversation
    messages.append(response.choices[0].message)
    
    # adding prompt again to continue with the quiz
    messages.append(prompt)
    # capture user input
    user_input = input('Enter your answer: ')
    # quit loop if user presses "q"
    if user_input == 'q':
        exit()
    # prompt preparation
    messages.append({'role': 'user', 'content': user_input})