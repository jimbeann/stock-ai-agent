import requests

from app.tools.finance import get_financials, get_price_history
from app.tools.news import get_news
from app.tools.sentiment import simple_sentiment
from app.rag import store_news, query_news

OLLAMA_URL = "http://localhost:11434/api/generate"


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

    # RAG
    store_news(news)
    relevant_news = query_news(stock)

    # Sentiment
    sentiment = simple_sentiment(news)

    # Chart
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
