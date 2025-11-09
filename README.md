# 🧠 AI Text Summarizer 📝🤖

A **Python-based text summarizer** powered by **Large Language Models (LLMs)** and **LangChain**, capable of summarizing short or long text efficiently — locally or via API.

This project demonstrates how to build an AI summarizer **locally** using Hugging Face models, with optional **cloud API support**, structured by **LangChain** for modular workflows.

---

## 🌟 **Features**

✅ Summarizes text into **concise bullet points**  
✅ Handles **short and long documents** with automatic chunking  
✅ Works **fully offline** with a local Hugging Face model (`facebook/bart-large-cnn`)  
✅ Supports **cloud API integration** via Hugging Face if a token is provided  
✅ **CLI-friendly** — summarize raw text or files from the terminal  
✅ Includes **unit tests** to ensure summarizer reliability  

---

## 💡 **What Are LLMs and LangChain?**

**Large Language Models (LLMs)** are AI models trained to understand and generate human-like text.  
Examples: GPT-4, BART, T5.  
They can **summarize**, **answer questions**, **translate**, or **generate creative content**.

**LangChain** is a framework that helps developers structure LLM applications with:
- Prompt templates  
- Memory management  
- Chaining and parsing utilities  

👉 In this project, LangChain structures the summarization workflow for **chunking**, **summarization**, and **aggregation** — all optimized for both **speed** and **accuracy**.

---

## 📁 **Project Structure**

ai-text-summarizer/
├── src/
│ ├── main.py # CLI entrypoint
│ ├── summarizer.py # Summarization logic
│ └── utils.py # Text chunking utility
├── tests/
│ └── test_summarizer.py
├── docs/
│ └── screenshots/ # Screenshots for README
├── .env.example # Environment variables template
├── requirements.txt
├── .gitignore
└── README.md



---

## ⚙️ **Installation**

### 🔹 Clone the repository
```bash
git clone https://github.com/TawficaBhuiyan/ai-text-summarizer.git
cd ai-text-summarizer

🔹 Create and activate a virtual environment

Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Windows CMD

python -m venv .venv
.\.venv\Scripts\activate

🔹 Install dependencies
pip install -r requirements.txt

Configure environment variables
Create a .env file:
USE_LOCAL_MODEL=true


Optional — to use Hugging Face API:
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

🚀 Usage
1️⃣ Summarize Raw Text
python -m src.main --text "Python is a versatile language used for AI and web development."

Example Output:

Python is widely used for AI and web development due to its flexibility.

2️⃣ Summarize Text File

Create a file named sample.txt, then run:
python -m src.main --file sample.txt

Example Output:

The text file has been summarized into key bullet points.

3️⃣ CLI Options
Option	Description
--text / -t	Summarize raw text directly
--file / -f	Summarize content from a text file


🧪 Testing

Run all tests with:
python -m pytest -q
✔️ Validates summarization for short and long texts
✔️ Automatically tests local model performance

📸 Screenshots

📄 File Summarization:
![Summarizer Output](docs/screenshots/summarizer_output.png)


📌 Notes

First run downloads the model (~1.6 GB).

Works fully offline (no API or billing required).

Compatible with CPU and GPU systems.

📖 References

LangChain Documentation

Hugging Face Transformers

Large Language Models Explained

⚡ License

Released under the MIT License.

✨ Crafted with ❤️ using Python, LangChain, and Hugging Face.

---

Would you like me to make a **GitHub-styled version** (with badges for Python, LangChain, and License) at the top too?  
It’ll make your project README look like a polished open-source repository.
