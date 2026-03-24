# AI Stock Analyzer

A simple AI-powered stock analysis tool using local LLM (Ollama).

## Features
- Financial data from Yahoo Finance
- News analysis using NewsAPI
- AI-generated insights
- Simple web UI

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

Run model:
ollama run phi3
3. Add API Key
Create .env file:
NEWS_API_KEY=your_api_key_here
Get API key from:
https://newsapi.org
4. Run App
uvicorn app.main:app --reload
Open:
http://127.0.0.1:8000
Notes
Do NOT upload .env to GitHub
Works best with 8GB RAM system

---

#  HOW TO PUSH TO GITHUB

```bash
git init
git add .
git commit -m "Initial commit - AI Stock Agent"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
