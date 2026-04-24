
# 🚀 AI-Powered Invoice Processing & Automation System

An end-to-end **Agentic AI pipeline** that extracts structured data from raw invoices (text/PDF-ready), processes it, and stores it into a relational database for downstream analytics and business automation.

---

## 📌 Project Overview

This project demonstrates how to build a **real-world finance automation system** using:

- LLM-powered data extraction  
- Structured data pipelines  
- Inventory & payable tracking  
- SQL-based storage for analytics  

The system converts:

Unstructured Invoice → Structured JSON → DataFrames → SQL Tables

---

## 🧠 Key Features

✔ Extracts invoice data using LLM  
✔ Handles multiple invoice formats  
✔ Converts raw text into structured schema  
✔ Separates:
- Inventory data
- Payables (if unpaid)

✔ Saves data into:
- CSV files  
- SQLite database  

✔ Scalable for:
- PDF parsing  
- RAG pipelines  
- Finance automation workflows  

---

## 🏗️ System Architecture

```text
Raw Invoice (Text / PDF)
        ↓
LLM Extraction (Structured JSON)
        ↓
Data Processing (Pandas)
        ↓
Inventory Table + Payables Table
        ↓
SQLite Database

```



---

## ⚙️ Tech Stack

- Python  
- OpenAI / NVIDIA LLM API  
- Pandas  
- SQLite  
- JSON Processing  

---

## 📂 Project Structure
``` text
├── main.py
├── config.py
├── Agentic_ai.db
├── README.md
```





---

## 🧾 Data Schema

### Extracted JSON Format

```json
{
  "vendor_name": "string",
  "invoice_number": "string",
  "invoice_date": "YYYY-MM-DD",
  "due_date": "YYYY-MM-DD",
  "line_items": [
    {
      "description": "string",
      "quantity": number,
      "unit_price": number,
      "total": number
    }
  ],
  "subtotal": number,
  "tax_amount": number,
  "total_amount": number,
  "currency": "string",
  "payment_status": "paid/unpaid/partial"
}
```
