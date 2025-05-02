from sentence_transformers import SentenceTransformer

class LocalEmbeddingModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(texts, show_progess_bar=True).tolist()

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()
