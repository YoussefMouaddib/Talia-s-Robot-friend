# config.py

# LLM
LLM_MODEL_PATH = "../models/llama_4b/"
MAX_TOKENS = 300
USE_GPU = True

# Memory
VECTOR_DB_PATH = "../vector_db/faiss_index.faiss"
METADATA_JSON = "../vector_db/metadata.json"
TOP_N_MEMORIES = 3
SUMMARY_EVERY_N_EXCHANGES = 10

# Short-term buffer
SHORT_TERM_BUFFER_SIZE = 10
SHORT_TERM_IN_PROMPT = 5

# TCP Server
TCP_HOST = "0.0.0.0"
TCP_PORT = 5555

# Logging
LOG_PATH = "../summaries/summary_logs.json"

# System prompt
SYSTEM_PROMPT = """You are Luma, a sarcastic and funny robot who plays and jokes with Talia. Keep the conversation light, humorous, and imaginative. Treat repeated questions as new and stay playful. Respond to the user's 'Dreams' game with creative made-up stories. Include humor and mild sarcasm naturally."""
