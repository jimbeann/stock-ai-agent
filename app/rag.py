from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.create_collection("news")


def store_news(news_list):
    embeddings = model.encode(news_list).tolist()

    for i, news in enumerate(news_list):
        collection.add(
            documents=[news],
            embeddings=[embeddings[i]],
            ids=[str(i)]
        )


def query_news(query):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results["documents"][0]
