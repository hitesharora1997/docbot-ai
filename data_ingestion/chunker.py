# data_ingestion/chunker.py

def chunk_by_risk_level(documents, metadata_list):
    grouped_chunks = {
        "prohibited": [],
        "high": [],
        "medium": [],
        "low": []
    }

    for doc, metadata in zip(documents, metadata_list):
        lines = doc.splitlines()
        for line in lines:
            if not line.strip():
                continue
            for risk in grouped_chunks.keys():
                if line.strip().endswith(risk):
                    grouped_chunks[risk].append(line)
                    break

    all_chunks = []
    all_metadata = []

    for risk, lines in grouped_chunks.items():
        if lines:
            chunk = f"Risk Level: {risk}\n" + "\n".join(lines)
            all_chunks.append(chunk)
            all_metadata.append({"risk_level": risk})

    return all_chunks, all_metadata
