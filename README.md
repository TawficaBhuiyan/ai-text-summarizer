<div align="center">

# 🧠 AI Text Summarizer 📝  
**Efficient | Offline | LLM-Powered | Open Source**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green?logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-🤗-yellow?logo=huggingface&logoColor=white)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/TawficaBhuiyan/ai-text-summarizer/actions)

</div>

---

> ✨ **A Python-based AI summarizer powered by LangChain & LLMs** —  
> Summarize text into clear, concise points. Works offline or with cloud APIs.

---

## 📦 Features

┌────────────────────────────────────────────┐
│ ✨ Summarizes text into concise bullet points │
│ 🧩 Handles long documents via smart chunking │
│ ⚙️ Works fully offline (facebook/bart-large-cnn)│
│ ☁️ Optional Hugging Face API integration │
│ 💻 CLI-friendly for quick summarization │
│ ✅ Includes unit tests for reliability │
└────────────────────────────────────────────┘


---

## 🧠 LLMs + LangChain
╭───────────────────────────────────────────────╮
│ 🤖 LLMs (Large Language Models): │
│ Models like GPT-4, BART, and T5 trained │
│ to understand and generate human-like text. │
│ │
│ 🧩 LangChain: │
│ Python framework for chaining LLM logic, │
│ prompts, and memory for efficient workflows. │
╰───────────────────────────────────────────────╯


---

## 🗂️ Project Structure
📦 ai-text-summarizer/
├── 📂 src/
│ ├── 🧠 main.py → CLI entrypoint
│ ├── ✂️ summarizer.py → Summarization logic
│ └── 🧩 utils.py → Text chunking utilities
│
├── 🧪 tests/
│ └── test_summarizer.py → Unit tests
│
├── 📸 docs/
│ └── screenshots/ → Screenshots for README
│
├── ⚙️ .env.example → Example environment file
├── 📜 requirements.txt → Dependencies
├── 🙈 .gitignore
└── 📘 README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/TawficaBhuiyan/ai-text-summarizer.git
cd ai-text-summarizer


2️⃣ Create & Activate Virtual Environment

PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

CMD
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


🔐 Configure Environment

Create a .env file in your project root:
USE_LOCAL_MODEL=true

For optional cloud summarization (Hugging Face API):

HUGGINGFACEHUB_API_TOKEN=hf_your_token_here


🚀 Usage
📝 Summarize Raw Text
python -m src.main --text "Python is a versatile language used for AI and web development."

📄 Summarize a Text File
python -m src.main --file sample.txt

⚙️ CLI Options
| Option           | Description                   |
| ---------------- | ----------------------------- |
| `--text` or `-t` | Input raw text to summarize   |
| `--file` or `-f` | Summarize from text file path |

🧪 Testing

Run automated tests:

python -m pytest -q


✅ Verifies both short & long text summarization with local models.

📸 Screenshots
🧠 Raw Text Summarization
<p align="center"> <img src="docs/screenshots/summarizer_output.png" alt="Summarizer Output" width="600"/> <br> <i>Example: Summarized output in terminal</i> </p>
✅ Successful Test Run
<p align="center"> <img src="docs/screenshots/testpassed.png" alt="Tests Passed" width="600"/> <br> <i>Example: All unit tests passed</i> </p>


🤝 Contributing
╔═════════════════════════════════════════════╗
║ 💡 Contributions, issues & ideas welcome!    ║
╚═════════════════════════════════════════════╝
Steps
# 1. Fork the repo
# 2. Create your branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "Add amazing feature"

# 4. Push and open PR
git push origin feature/amazing-feature

Guidelines

Follow PEP 8

Add tests for new functionality

Update docs if necessary

📌 Notes
⚙️ First run downloads model (~1.6 GB)
💻 Works perfectly on CPU (GPU optional)
🔒 Offline mode = zero API usage or cost

📚 References

LangChain Documentation

Hugging Face Transformers

LLMs Explained

⚡ License

MIT License © 2025 Tawfica Bhuiyan


---

✅ **Highlights of This Version**
- Uses **Unicode box borders (╭╮╰╯)** for visually grouped explanations  
- Uses **ASCII tree diagrams** for file structure  
- GitHub automatically adds **Copy buttons** for code blocks  
- Fully aligned typography and emoji usage for visual balance  
- Works beautifully in **dark/light themes**  

---

Would you like me to make a **"📽️ Demo Section"** next — showing your summarizer running in the terminal with colored output (in a box or GIF placeholder)? It really boosts project appeal for recruiters & GitHub visitors.
