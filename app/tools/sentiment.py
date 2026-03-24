def simple_sentiment(news_list):
    positive_words = ["growth", "profit", "gain", "strong"]
    negative_words = ["loss", "decline", "drop", "risk"]

    score = 0

    for news in news_list:
        for word in positive_words:
            if word in news.lower():
                score += 1
        for word in negative_words:
            if word in news.lower():
                score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"
