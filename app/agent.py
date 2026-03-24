import requests
import yfinance as yf
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OLLAMA_URL = "http://localhost:11434/api/generate"


def get_financials(stock):
    ticker = yf.Ticker(stock)
    info = ticker.info

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "marketCap": info.get("marketCap"),
        "pe": info.get("trailingPE"),
        "revenueGrowth": info.get("revenueGrowth"),
    }


def get_news(stock):
    if not NEWS_API_KEY:
        return ["No API key provided"]

    url = f"https://newsapi.org/v2/everything?q={stock}&apiKey={NEWS_API_KEY}"

    try:
        res = requests.get(url).json()
        articles = res.get("articles", [])[:5]
        return [a["title"] for a in articles]
    except:
        return ["Error fetching news"]


def call_llm(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]


def analyze_stock(stock):
    financials = get_financials(stock)
    news = get_news(stock)

    prompt = f"""
You are a stock analyst.

Analyze this stock:

Stock: {stock}

Financials:
{financials}

News:
{news}

Give:
1. Financial Summary
2. News Sentiment
3. Risks
4. Final Insight
"""

    return call_llm(prompt)
