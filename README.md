AI Text Summarizer 📝🤖

A Python-based text summarizer powered by Large Language Models (LLMs) and LangChain, capable of summarizing short or long text efficiently.

This project demonstrates how to build an AI summarizer locally using Hugging Face models, with optional cloud API support, using LangChain for structured LLM workflows.

🌟 Features

Summarizes text into concise bullet points.

Supports short and long documents with automatic chunking.

Works fully offline with a local Hugging Face model (facebook/bart-large-cnn).

Optional cloud API integration via Hugging Face if a token is provided.

CLI-friendly — summarize raw text or text files directly from terminal.

Includes unit tests to verify summarizer functionality.

💡 What is an LLM and LangChain?

Large Language Models (LLMs) are AI models trained to understand and generate human-like text. Examples: GPT-4, BART, T5. They can summarize, answer questions, translate, or generate text.

LangChain is a Python library that helps developers structure LLM applications. It provides prompt templates, chains, memory management, and output parsing, making LLMs easier to use in real projects.

In this project, LangChain is used to structure the summarization workflow so that text can be chunked, summarized, and combined efficiently.

📁 Project Structure
ai-text-summarizer/
├── src/
│   ├── main.py         # CLI entrypoint
│   ├── summarizer.py   # Summarization logic
│   └── utils.py        # Text chunking utility
├── tests/
│   └── test_summarizer.py
├── docs/screenshots/   # Screenshots for README
├── .env.example        # Environment variables template
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/TawficaBhuiyan/ai-text-summarizer.git
cd ai-text-summarizer


Create and activate a virtual environment:

python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# CMD
.\.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Configure environment variables (for local model):

# Create .env file
USE_LOCAL_MODEL=true


Optional: If using Hugging Face cloud API, add your token:

HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

🚀 Usage
1️⃣ Summarize raw text
python -m src.main --text "Python is a versatile language used for AI and web development."


Example Output:

2️⃣ Summarize text file

Create a text file (e.g., sample.txt) in your project folder.

Run:

python -m src.main --file sample.txt


Example Output:

3️⃣ CLI Options
Option	Description
--text/-t	Raw text input to summarize
--file/-f	Path to a text file to summarize
🧪 Testing

Run unit tests with pytest:

python -m pytest -q


Ensures the summarizer works for short and long text.

Local Hugging Face model is tested automatically.

📸 Screenshots

Raw Text Summarization:


File Summarization:


Replace screenshots with your own captures from your terminal for best presentation.

📌 Notes

First run downloads the local model (~1.6 GB).

Works on CPU, GPU is optional.

Local summarization is fully offline, no API key or billing required.

📖 References

LangChain Documentation

Hugging Face Transformers

Large Language Models (LLMs) Explained

⚡ License

MIT License
