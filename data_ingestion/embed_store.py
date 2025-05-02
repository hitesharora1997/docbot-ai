import chromadb
from core.embedding import LocalEmbeddingModel

def store_embedding(chunks, metadata_list, persist_path="db"):
    chroma_client = chromadb.PersistentClient(path=persist_path)

    collection = chroma_client.get_or_create_collection(name="doc_chunks")

    embedder = LocalEmbeddingModel()
    embeddings = embedder.embed_documents(chunks)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        documents = chunks,
        embeddings = embeddings,
        ids = ids,
        metadatas = metadata_list
    )

    print(f" Stored {len(chunks)} chunks into ChromaDB.")

