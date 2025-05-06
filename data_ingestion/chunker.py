from langchain.text_splitter import RecursiveCharacterTextSplitter

def chuck_document(documents, metadata_list,  chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )

    all_chucks = []
    all_metadata = []

    for doc, metadata in zip(documents, metadata_list):
        chunks = splitter.split_text(doc)
        for i, chunk in enumerate(chunks):
            all_chucks.append(chunk)
            new_metadata = metadata.copy()
            new_metadata["chunk_index"] = i
            all_metadata.append(new_metadata)

    return all_chucks, all_metadata

