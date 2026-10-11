# EduGenie Learning Studio

An original modular learning assistant built with FastAPI, HTML, CSS, and Google's Gemini API.

## Features
- Academic question and answer
- Beginner-friendly concept explanations
- Five-question MCQ generation with interactive answer checking
- Revision summaries
- Beginner-to-advanced learning roadmaps
- Responsive purple-themed UI, input validation, health endpoint, and safe error messages

## Requirements
- Python 3.10 or later
- A Google AI Studio API key with Gemini API access
- Internet access for AI requests

## Run on Windows (PowerShell)

1. Open this folder in VS Code.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Create your local environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Open `.env` and replace `paste_your_key_here` with your API key. Never commit `.env` to GitHub.
6. Start the server:

   ```powershell
   uvicorn main:app --reload
   ```

7. Open `http://127.0.0.1:8000` in your browser. API documentation is at `http://127.0.0.1:8000/docs`; health check is `http://127.0.0.1:8000/health`.

## Project layout

```text
EduGenie_Original/
├── main.py
├── ai_core.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Troubleshooting
- `GEMINI_API_KEY is missing`: check that `.env` exists in this project folder and contains the key.
- `ModuleNotFoundError`: activate `.venv` and run `pip install -r requirements.txt` again.
- API errors or quota messages: verify the key, enabled API access, network, and current account/model availability.
- Port already in use: stop the other server or run `uvicorn main:app --reload --port 8001`, then open port 8001.

## Academic integrity and originality
Use this as a starting implementation you can explain and customize. Test every feature, cite external assets or sources if your institution requires it, and follow your course rules on AI-assisted code. A different codebase does not guarantee a duplicate-check result.
