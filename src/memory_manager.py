# memory_manager.py
import faiss
import json
import numpy as np
import os

class MemoryManager:
    def __init__(self, index_path, metadata_path, embedding_dim=384):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.embedding_dim = embedding_dim

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            with open(metadata_path, "r") as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(embedding_dim)
            self.metadata = []

    def add_memory(self, embedding, summary, timestamp):
        embedding_np = np.array([embedding], dtype=np.float32)
        self.index.add(embedding_np)
        self.metadata.append({"summary": summary, "timestamp": timestamp})
        self.save()

    def search(self, embedding, top_n=3):
        embedding_np = np.array([embedding], dtype=np.float32)
        distances, indices = self.index.search(embedding_np, top_n)
        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i]["summary"])
        return results

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "w") as f:
            json.dump(self.metadata, f, indent=2)
