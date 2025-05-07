import os
from unicodedata import category
from langchain_community.document_loaders import PyPDFLoader


def load_text_files(directory: str):
    documents = []
    metadata = []

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            ext = os.path.splitext(filename)[1].lower()

            if ext == ".txt":
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    category = os.path.basename(root)
                    documents.append(content)
                    metadata.append({
                        "source": filename,
                        "category": category
                    })

            elif ext == ".pdf":
                loader = PyPDFLoader(filepath)
                pdf_docs = loader.load()
                category = os.path.basename(root)
                for i, page in enumerate(pdf_docs):
                    documents.append(page.page_content)
                    metadata.append({
                        "source": filename,
                        "category": category,
                        "page_number": i
                    })

    return documents, metadata