from dataclasses import dataclass, field
import json
from typing import Optional
from openai import OpenAI
from config import NVIDIA_API_KEY,NVIDIA_BASE_URL, DEFAULT_MODEL

client=OpenAI(api_key=NVIDIA_API_KEY,base_url=NVIDIA_BASE_URL)

Basic_prompt = '''

Your are a logestic pricing agent.
Given shipment detail, you calculate the total price.


'''


def agent_call_basic(message:list):
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=message,
        temperature=0.3,
    )
    try:
        data_ =  json.loads(response.choices[0].message.content.strip("'"))
        return data_        
    except:
        return response.choices[0].message.content
    



message=[{"role":"system","content":Basic_prompt}]

while True:
    print("=="*50)
    user_input=input("Provide your Input: ")
    if user_input=="Q":
        break
    message.append({"role":"user","content":user_input})
    response = agent_call_basic(message)

    print(response)
    print(type(response))
