import chromadb
from core.embedding import LocalEmbeddingModel  # make sure this exists

def retrieve_similar_chunks(query: str, top_k=5, db_path="db"):
    client = chromadb.PersistentClient(path="db")
    collection = client.get_collection("doc_chunks")

    embedder = LocalEmbeddingModel()
    query_vector = embedder.embed_query(query)

    results = collection.query(query_embeddings=[query_vector], n_results=top_k)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return documents, metadatas
