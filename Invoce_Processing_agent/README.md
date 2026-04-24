
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



