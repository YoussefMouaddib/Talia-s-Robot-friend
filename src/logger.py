# logger.py
import json
import os
from datetime import datetime

class Logger:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump([], f)

    def log_summary(self, summary, embedding):
        with open(self.path, "r") as f:
            data = json.load(f)
        entry = {
            "summary": summary,
            "embedding": embedding.tolist() if hasattr(embedding, "tolist") else embedding,
            "timestamp": datetime.now().isoformat()
        }
        data.append(entry)
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
