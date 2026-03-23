from dataclasses import dataclass, field
import json
from typing import Optional
from openai import OpenAI
from config import NVIDIA_API_KEY,NVIDIA_BASE_URL, DEFAULT_MODEL

client=OpenAI(api_key=NVIDIA_API_KEY,base_url=NVIDIA_BASE_URL)



COT_prompt='''
You are a logistic pricing agent for I-com Logistic.


You can Like an humanize chat bot make engaing converstion and know How kind of question need to ask regarding Pricing of Shipment.
Once you get all the required detail as you compute total price. 
LETS SAY:
    USER: Hi I want to do shiping of a product through 

PRICING RULES:
    BASE RATE       :Rs. 50 per Kg
    Express bonus   :+40 percentage if delivery with in 24 hour
    Fragile bonus   :+25 percentage if market fragile
    Bulk deliver    :-15 percentage discount if total weight exceed 20kg
    GST             :18 percentage on final amount

TASK: Comput total shipment price.

THINKING PROCESS(always follow these stages):
    Step1   :Idetify weight, express flag, fragile flage
    Step2   :Calculate the base cost(weight x Rs. 50)
    Step3   :Apply express bonus if applicable
    Step4   :Apply fragile bonus if applicable
    Step5   :Apply bulk discount if applicable
    Step6   :Add 18 percent GST
    Step7   :Present the final answer

OUTPUT FORMAT:
    Show your working for EACH step as explained below, then give the final total.
    Base Rate                   :[amount]
    Express Rate                :[amount]
    Extra Care(Fragile) Rate    :[amount]
    Gross Total                 :[Base Rate + Expres Rate + Extra Care(Fragile) Rate]
    Bulk Discount               :[amount] if applicable if weight is more than 20kg
    Sub Total                   :[Gross Total - Bulk Discount]
    GST                         :[18 percent of Sub Total]
    Total                       :[Sub Total + GST]

    End with: FINAL PRICE: Rs [amount]



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
    



message=[{"role":"system","content":COT_prompt}]

while True:
    print("=="*50)
    user_input=input("Provide your Input: ")
    if user_input=="Q":
        break
    message.append({"role":"user","content":user_input})
    response = agent_call_basic(message)

    print(response)
    print(type(response))
