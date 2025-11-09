# 🧠 AI Text Summarizer 📝  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green?logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-🤗-yellow?logo=huggingface&logoColor=white)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/TawficaBhuiyan/ai-text-summarizer/actions)

---

A **Python-based AI text summarizer** powered by **LangChain** and **Large Language Models (LLMs)** — built to efficiently summarize both short and long texts.  

This project demonstrates how to build an **offline or cloud-connected summarizer** using Hugging Face and LangChain — a great starting point for LLM-based applications.  

---

## 🌟 Features  

- ✨ Summarizes text into concise bullet points  
- 🧩 Supports short & long documents via automatic chunking  
- ⚙️ Works fully **offline** using `facebook/bart-large-cnn`  
- ☁️ Optional **cloud API** (Hugging Face Hub integration)  
- 💻 **CLI-friendly** — summarize raw text or text files directly  
- ✅ Includes **unit tests** for summarizer verification  

---

## 💡 What Are LLMs & LangChain?  

**Large Language Models (LLMs)** — AI models like *GPT-4*, *BART*, and *T5* trained to understand and generate human-like text.  
They can summarize, answer questions, translate, or generate coherent text.  

**LangChain** — a Python library that structures LLM workflows through **chains**, **prompt templates**, and **memory**.  
Here, it’s used to **chunk**, **summarize**, and **combine** text efficiently.  

---

## 🗂️ Project Structure  

```text
📦 ai-text-summarizer/
├── 📂 src/
│   ├── 🧠 main.py       → CLI entrypoint
│   ├── ✂️ summarizer.py → Summarization logic
│   └── 🧩 utils.py      → Text chunking utilities
├── 🧪 tests/
│   └── test_summarizer.py → Unit tests
├── 📸 docs/
│   └── screenshots/    → README images
├── ⚙️ .env.example      → Environment template
├── 📜 requirements.txt  → Dependencies
├── 🙈 .gitignore
└── 📘 README.md

⚙️ Installation
🧩 1️⃣ Clone the Repository

```bash
git clone https://github.com/TawficaBhuiyan/ai-text-summarizer.git
cd ai-text-summarizer

⚙️ 2️⃣ Create and Activate Virtual Environment
# Windows (PowerShell)

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Windows (CMD)

```bash
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate

📦 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt

🔑 4️⃣ Configure Environment Variables
# Create a .env file

```bash
USE_LOCAL_MODEL=true

# Optional (if using Hugging Face API)

```bash
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

🚀 Usage
🔹 Summarize Raw Text

```bash
python -m src.main --text "Python is versatile for AI & web development."

🔹 Summarize a Text File

```bash
python -m src.main --file sample.txt

⚙️ CLI Options
Option	Description
--text or -t	Raw text input to summarize
--file or -f	Path to a text file to summarize
🧪 Testing

```bash
python -m pytest -q

<img width="492" height="61" alt="testpassed" src="https://github.com/user-attachments/assets/e796e1b1-e5d3-4d0e-9046-4e1fdf3500ac" />


📸 Screenshots

🧠 Sample text summarization output:
<img width="1672" height="98" alt="summarizer_output" src="https://github.com/user-attachments/assets/7d286bf5-5528-4cd3-b739-e0b5ffa1b443" />


🤝 Contributing

```bash
# Fork the repo & create a feature branch
git checkout -b feature/your-feature

# Commit changes

```bash
git commit -m "Add feature"

# Push & open PR

```bash
git push origin feature/your-feature


💡 Guidelines: Follow PEP 8, add unit tests, and update documentation as needed.

📌 Notes

⏬ First run downloads the model (~1.6 GB)

💻 Works perfectly on CPU; GPU optional

🔒 Local summarization is fully offline (no billing or API calls)

📚 References

LangChain Documentation

Hugging Face Transformers

LLMs Explained

⚡ License

MIT License © 2025 Tawfica Bhuiyan

