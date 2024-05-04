from openai import OpenAI
import gradio as gr
import time
import os

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

messages = []
messages.append({
    'role': 'system',
    'content': """You are a general assistant. 
    You can ask me anything you want. 
    I will try to answer your questions to the best of my ability.
    """})

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    user_input = gr.Textbox()
    clear = gr.ClearButton([user_input, chatbot])

    def respond(history, new_message):
        messages.append({'role': 'user', 'content': new_message})
         # send the api call
        response = client.chat.completions.create(messages=messages, model="gpt-3.5-turbo")
        # obtain response
        assistant_message = response.choices[0].message
        messages.append(assistant_message)
        time.sleep(2)

        return history + [[new_message, assistant_message.content]]

    user_input.submit(respond, [chatbot, user_input], chatbot)

demo.launch()
