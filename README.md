🧠 AI Text Summarizer 📝

A Python-based AI text summarizer powered by LangChain and Large Language Models (LLMs) — built to efficiently summarize both short and long text.

This project demonstrates how to build an offline or cloud-connected summarizer using Hugging Face and LangChain, making it a great starting point for LLM-based applications.

🌟 Features

✨ Summarizes text into concise bullet points

🧩 Supports short & long documents via automatic chunking

⚙️ Works fully offline using facebook/bart-large-cnn

☁️ Optional cloud API (Hugging Face Hub integration)

💻 CLI-friendly — summarize raw text or text files directly

✅ Includes unit tests for summarizer verification

💡 What Are LLMs & LangChain?

Large Language Models (LLMs) — AI models like GPT-4, BART, and T5 trained to understand and generate human-like text.
They can summarize, answer questions, translate, or generate coherent text.

LangChain — a Python library that helps structure LLM workflows through chains, prompt templates, and memory.
Here, it’s used to chunk, summarize, and combine text efficiently.

📁 Project Structure
ai-text-summarizer/
├── src/
│   ├── main.py              # CLI entrypoint
│   ├── summarizer.py        # Summarization logic
│   └── utils.py             # Text chunking utility
│
├── tests/
│   └── test_summarizer.py   # Unit tests
│
├── docs/
│   └── screenshots/         # Screenshots for README
│
├── .env.example             # Environment template
├── requirements.txt         # Dependencies
├── .gitignore
└── README.md

⚙️ Installation
🧩 Clone the repository
git clone https://github.com/TawficaBhuiyan/ai-text-summarizer.git
cd ai-text-summarizer

🧱 Create & activate a virtual environment

PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1


CMD

python -m venv .venv
.venv\Scripts\activate

📦 Install dependencies
pip install -r requirements.txt

🔐 Configure environment variables

Create a .env file in the project root:

USE_LOCAL_MODEL=true


Optional (for Hugging Face cloud API):

HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

🚀 Usage
📝 1️⃣ Summarize raw text
python -m src.main --text "Python is a versatile language used for AI and web development."

📄 2️⃣ Summarize text file
python -m src.main --file sample.txt

⚙️ 3️⃣ CLI Options
Option	Description
--text or -t	Raw text input to summarize
--file or -f	Path to a text file to summarize
🧪 Testing

Run tests using pytest:

python -m pytest -q


Verifies that summarization works for short and long inputs using the local model.

📸 Screenshots
🧠 Raw Text Summarization
<p align="center"> <img src="docs/screenshots/summarizer_output.png" alt="Summarizer Output" width="600"/> <br> <i>Example: Summarized output from terminal</i> </p>

(Add more screenshots to docs/screenshots/ and update here as needed.)

📌 Notes

⏬ The first run downloads the model (~1.6 GB)

💻 Works perfectly on CPU; GPU optional

🔒 Local summarization is fully offline (no billing or API calls)

📚 References

LangChain Documentation

Hugging Face Transformers

LLMs Explained

⚡ License

MIT License © 2025 Tawfica Bhuiyan
