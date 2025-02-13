import pinecone
from sentence_transformers import SentenceTransformer

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")
        self.index = pinecone.Index("oil-gas-db")

    def search_documents(self, query):
        query_embedding = self.model.encode(query).tolist()
        results = self.index.query(query_embedding, top_k=5, include_metadata=True)
        return [match["metadata"]["text"] for match in results["matches"]]
