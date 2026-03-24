import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


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
