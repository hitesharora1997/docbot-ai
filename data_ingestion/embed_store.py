import chromadb
from core.embedding import LocalEmbeddingModel

def store_embeddings(chunks, metadata_list, persist_path="db", batch_size=500):
    import chromadb
    from core.embedding import LocalEmbeddingModel

    client = chromadb.PersistentClient(path=persist_path)
    collection = client.get_or_create_collection(name="doc_chunks")

    embedder = LocalEmbeddingModel()
    embeddings = embedder.embed_documents(chunks)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    for i in range(0, len(chunks), batch_size):
        collection.add(
            documents=chunks[i:i+batch_size],
            embeddings=embeddings[i:i+batch_size],
            ids=ids[i:i+batch_size],
            metadatas=metadata_list[i:i+batch_size],
        )

    print(f"✅ Stored {len(chunks)} chunks in ChromaDB.")
