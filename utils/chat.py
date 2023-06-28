import os
import openai
from dotenv import load_dotenv


def persona_creation(context, system=None):
    if not context:
        context = {
            'role': "system", "content": system
        }
    return context


def openai_ask(model='gpt-4', messages=None):
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=386

    )

    response = completion.choices[0].message['content']
    response = {"role": 'assistant', "content": response}
    return response


message = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "dupa!"}
      ]
#
# openai_ask(messages=message)
#
# context = []
#
# persona_creation(context)
