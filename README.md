# Agenti_Ai_projects

# 🚚 AI Logistics Pricing Agent (Open Source)

An AI-powered **Logistics Pricing Agent + Smart Receptionist** that automates the complete pricing workflow — from collecting shipment details to generating the final cost with taxes.

This project demonstrates how **LLMs + Rule-Based Logic** can be combined to solve real-world business problems.

---

## 🔥 Features

### 🤖 AI Receptionist
- Conversationally collects:
  - Package Name  
  - Description  
  - Weight (kg)  
  - Fragility (Yes/No)  
  - Delivery Type (48 hrs / 72 hrs)  

### 💰 Pricing Engine
Automatically calculates:
- Base Rate  
- Fragile Charges  
- Speed Post Fees  
- Bulk Discount  
- GST  
- Final Amount  

### 📦 Structured Output
- Returns clean **JSON output**
- Easily integrable with:
  - Billing systems  
  - Databases  
  - Dashboards  

---

## 🧠 Pricing Logic

| Component        | Rule |
|-----------------|------|
| Base Rate       | ₹50 per kg |
| Fragile Fee     | +40% of base rate |
| Speed Post Fee  | +25% of base rate |
| Bulk Discount   | 25% discount if weight > 20kg |
| GST             | 18% on net total |

---

## 🛠️ Tech Stack

- Python 🐍  
- OpenAI-compatible LLM API (NVIDIA / others)  
- JSON-based structured output  
- Prompt Engineering  

---

## ▶️ Quick Start (Hardcoded Example)

Below is a **ready-to-run example** with hardcoded API config (no separate config file required):

```python
import json
from openai import OpenAI

# 🔑 Hardcoded Config
client = OpenAI(
    base_url="YOUR_BASE_URL",
    api_key="YOUR_API_KEY"
)

MODEL = "YOUR_MODEL_NAME"

SYSTEM_PROMPT = """
You are an Expert Logistic Pricing Agent.

Follow pricing rules:
Base rate: Rs 50/kg
Fragile: +40%
Speed post: +25%
Bulk discount: 25% if >20kg
GST: 18%

Respond ONLY in JSON:
{
"base_rate":float,"fragile_fee":float,"speedpost_fee":float,
"gross_total":float,"bulk_discount":float,
"net_total":float,"GST":float,
"total_amount":float
}
"""

def get_price(summary):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": summary}
        ],
        temperature=0
    )
    
    return json.loads(response.choices[0].message.content)

# ✅ Example Input (Hardcoded)
summary = """
Package: Books
Weight: 25kg
Fragile: Yes
Delivery: 48 hours
"""

result = get_price(summary)
print(result)
