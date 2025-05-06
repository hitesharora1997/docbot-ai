import chromadb
from core.embedding import LocalEmbeddingModel

def store_embeddings(chunks, metadata_list, persist_path="db"):

    client = chromadb.PersistentClient(path=persist_path)
    collection = client.get_or_create_collection(name="doc_chunks")

    embedder = LocalEmbeddingModel()
    embeddings = embedder.embed_documents(chunks)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadata_list,
    )

    print(f"✅ Stored {len(chunks)} chunks into ChromaDB.")
