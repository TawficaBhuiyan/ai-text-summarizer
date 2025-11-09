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

## 📁 Project Structure  
ai-text-summarizer/
├── src/
│ ├── main.py # CLI entrypoint
│ ├── summarizer.py # Summarization logic
│ └── utils.py # Text chunking utility
│
├── tests/
│ └── test_summarizer.py # Unit tests
│
├── docs/
│ └── screenshots/ # Screenshots for README
│
├── .env.example # Environment template
├── requirements.txt # Dependencies
├── .gitignore
└── README.md



---

## ⚙️ Installation  

### 🧩 1️⃣ Clone the repository  
```bash
git clone https://github.com/TawficaBhuiyan/ai-text-summarizer.git
cd ai-text-summarizer

🧱 2️⃣ Create & activate a virtual environment

PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1


🧱 2️⃣ Create & activate a virtual environment
PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

CMD
python -m venv .venv
.venv\Scripts\activate

📦 3️⃣ Install dependencies
pip install -r requirements.txt


🔐 Configure Environment Variables
Create a .env file in the project root:
USE_LOCAL_MODEL=true

Optional (for Hugging Face cloud API):
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here


🚀 Usage
📝 1️⃣ Summarize raw text
python -m src.main --text "Python is a versatile language used for AI and web development."

📄 2️⃣ Summarize a text file
python -m src.main --file sample.txt


⚙️ CLI Options
OptionDescription--text or -tSummarize raw text input--file or -fSummarize from a text file path

🧪 Testing
Run tests using pytest:
python -m pytest -q

This verifies that summarization works for both short and long inputs using the local model.

📸 Screenshots
🧠 Raw Text Summarization
<p align="center">
  <img src="docs/screenshots/summarizer_output.png" alt="Summarizer Output" width="600"/>
  <br>
  <i>Example: Summarized output from terminal</i>
</p>
<p align="center">
  <img src="docs/screenshots/testpassed.png" alt="Tests Passed" width="600"/>
  <br>
  <i>Example: All tests passed successfully</i>
</p>

🤝 Contributing
Contributions, issues, and feature requests are welcome! 💬
🔧 Steps to Contribute


Fork the repository


Create your feature branch
git checkout -b feature/amazing-feature



Commit your changes
git commit -m "Add amazing feature"



Push to the branch
git push origin feature/amazing-feature



Open a Pull Request 🎉


💡 Guidelines


Follow PEP 8 code style


Include unit tests for new features


Update documentation where needed



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

---

✅ **What’s New**
- **Contributing 🤝 section** with clean step-by-step GitHub workflow  
- **Guidelines subsection** for PEP8 + testing  
- Consistent line spacing & Markdown hierarchy  
- Code blocks use syntax highlighting (`bash`, `powershell`, `cmd`) so GitHub automatically adds “Copy” buttons  
- The overall structure now matches top open-source Python projects  

---

Would you like me to add a **small “Demo GIF or Preview”** section (📽️ showing the summarizer running in terminal or a short GIF banner)? It gives the repo a powerful first impression.
