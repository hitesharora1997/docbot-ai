import os
from unicodedata import category


def load_text_files(directory: str):
    documents = []
    metadata = []

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".txt"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    category = os.path.basename(root)
                    documents.append(content)
                    metadata.append({
                        "source": filename,
                        "category": category
                    })

    return documents, metadata