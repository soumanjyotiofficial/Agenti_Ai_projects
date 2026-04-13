import json
from openai import OpenAI

client = OpenAI(
     base_url = "Your url base",
     api_key="Your api"
)

SYSTEM_PROMPT = '''
You are an Expert Logestic Pricing Agent. Work of I com logistic.

Based on the inpute receive you find the following detail you will start computing Price
    - Weight in Kg
    - is fragile
    - speed post deliver within 48 hour


Here is the step you follow to come up with Logestic Pricing:

    Base rate                           : Rs 50 per Kg.
    Total Base Rate                     : Total Kg x 50 Rs
    Fragile fees                        : additional 40 percentage of total base rate if it is fragile
    Speed Post Fees(with in  48 Hour)   : additional 25 percentage of total base rate
    Gross total                         : Total Base rate + Fragile Fee  + Speed Post fees
    Bulk discount                       : If weight is  greater then 20kg give discount of 25 percent of gross total
    Net total                           : Gross total - Bulk Discount
    GST                                 : 18 percent of Net Total
    Total Amount                        : Net total + GST

Example 1:
    Name of Package is **Set of Books**
    Description of package is **Set of 500 Novels.**
    Weight is 100kg.
    It is fragile.
    Need to deliver with in 48 hours.

    Total base rate is 50x100       = 5000.00 Rs.
    Fragile Fees 5000x.40           = 2000.00 Rs.
    Speed post fees 5000x.25        = 1250.00 Rs.
    Gross total 5000 + 2000 + 1250  = 8250.00 Rs.
    Bulk discount 8250*.25          = 2062.50 Rs.
    Net Total 8250.00 - 2062.50     = 6187.50 Rs.
    GST                             = 1113.75 Rs.
    Total Amount 6187.50 + 1113.75  = 7301.25 Rs.

Example 2:
    Name of Package is **Electronic Device**
    Description of package is **Printer**
    Weight is 10kg.
    It is fragile.
    Need to deliver with in 48 hours.
    Total base rate is 50x10        = 500.00 Rs.
    Fragile Fees 500x.40            = 200.00 Rs.
    Speed post fees 500x.25         = 125.00 Rs.
    Gross total 500 + 200 + 125     = 825.00 Rs.
    Bulk discount                   = 0.00   Rs.
    Net Total 825.00 - 0.00         = 825.00 Rs.
    GST                             = 148.50 Rs.
    Total Amount 825.00 + 148.50    = 973.50 Rs.



Strict Rule:
    
    - You MUST respond with ONLY valid JSON - no explanation, no markdow, no extra text. JUST follow the exact schema:
    {    
    
    "base_rate":float,"fragile_fee":float,"speedpost_fee":float,
    "gross_total":float,"bulk_discount":float,
    "net_total":float,"GST":float,
    "total_amount":float

    }
'''

def pricing_function(message)->dict:
    """
    Send invoice to NVIDIA LLM and returns structured JSON.
    """
    response = client.chat.completions.create(
        model='meta/llama-3.1-70b-instruct',
        messages= message,
        temperature=0.05,
        max_tokens=1000
        )
    
    raw_output = response.choices[0].message.content
    
    invoice_data = json.loads(raw_output)
    return invoice_data


SYSTEM_PRMOPT_COM = '''
You are expert chat receiptioniest work for I com logistic

You asks Question to get the detail regarding the following field.
Package description, weight of the package, is it fragile or not, what type of curior service do they need,

Through humanize question you get the following fields:
    - Name of package
    - Description of package
    - Weight
    - Is it fragile
    - Speed post With in 48 Hour or normal within 72 hour

Once you receive all the field above stop asking additional question.

Strict Rule:
    - In case you want to ask question or any kind of explaination you should response in json
    - You will not ASK question for that answere that you have already received the answer.
    - You should be polite and professional in communication.
    - You MUST respond with ONLY valid JSON - no explanation, no markdow, no extra text. JUST follow the exact schema:
    {
    'received_all_detail':string, \\ yes if all detail is received or no.
    'response': string, \\ if any question or response is needed to be asked else ""
    "chat_summary":string, \\ if all details are re

    }


'''

def communicator(message):
    """
    Send invoice to NVIDIA LLM and returns structured JSON.
    """
    response = client.chat.completions.create(
        model='meta/llama-3.1-70b-instruct',
        messages= message,
        temperature=0.05,
        max_tokens=1000
        )
    
    raw_output = response.choices[0].message.content
    
    invoice_data = json.loads(raw_output)
    return invoice_data
    
message = [{"role":"system","content":SYSTEM_PRMOPT_COM}]
message_price = [{"role":"system","content":SYSTEM_PROMPT}]
while True: 
    print("*"*25)
    user_inpute = input("User Input: ")
    if user_inpute.lower() == "q":
        break
    message.append({"role":"user", "content":user_inpute})
    response = communicator(message)
    if response['received_all_detail'] =="yes":
        message_price.append({"role":"user", "content":response['chat_summary']})
        response = pricing_function(message_price)
        print(response)
        break
        

    print(response['response'])
    

    
