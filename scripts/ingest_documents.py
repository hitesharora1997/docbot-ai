from data_ingestion.embed_store import store_embeddings
from data_ingestion.loader import load_text_files
from data_ingestion.chunker import chuck_document

docs, meta = load_text_files("data/")
print(f"Loaded {len(docs)} documents.")

chunks, chunk_meta = chuck_document(docs, meta)
# print(f"🔹 Total chunks created: {len(chunks)}")
# print(f"Sample chunk:\n{chunks[0][:300]}...")
# print(f"Chunk metadata: {chunk_meta[0]}")

store_embeddings(chunks, chunk_meta)