import requests
import yfinance as yf
import os
from dotenv import load_dotenv

from app.rag import store_news, query_news
from app.tools.sentiment import simple_sentiment

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


def get_price_history(stock):
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="1mo")

    return {
        "dates": hist.index.strftime("%Y-%m-%d").tolist(),
        "prices": hist["Close"].tolist()
    }


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

    store_news(news)
    relevant_news = query_news(stock)
    sentiment = simple_sentiment(news)

    chart_data = get_price_history(stock)

    prompt = f"""
You are a professional stock analyst.

Stock: {stock}

Financials:
{financials}

Relevant News:
{relevant_news}

Sentiment: {sentiment}

Provide output in this format:

### Financial Health
### News Impact
### Risks
### Final Verdict
"""

    analysis = call_llm(prompt)

    return analysis, chart_data
