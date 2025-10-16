# main.py
from config import *
from tcp_server import TCPServer
from llm_handler import LLMHandler
from memory_manager import MemoryManager
from prompt_builder import build_prompt
from logger import Logger
from sentence_transformers import SentenceTransformer
from datetime import datetime

# Initialize
tcp = TCPServer(TCP_HOST, TCP_PORT)
tcp.accept_connection()

llm = LLMHandler(LLM_MODEL_PATH, MAX_TOKENS)
memory = MemoryManager(VECTOR_DB_PATH, METADATA_JSON)
logger = Logger(LOG_PATH)
embedder = SentenceTransformer("../models/embeddings_model/")

short_term_buffer = []
exchange_count = 0

while True:
    user_input = tcp.receive()
    if not user_input:
        continue

    # Retrieve top memories
    embedding_input = embedder.encode(user_input)
    top_memories = memory.search(embedding_input, TOP_N_MEMORIES)

    # Build prompt
    prompt = build_prompt(SYSTEM_PROMPT, top_memories, short_term_buffer, user_input, SHORT_TERM_IN_PROMPT)

    # Generate reply
    try:
        ai_reply = llm.generate_reply(prompt)
    except Exception as e:
        print(f"[LLM ERROR]: {e}")
        ai_reply = "Hmm, tell me more"

    # Update short-term buffer
    short_term_buffer.append({"user": user_input, "ai": ai_reply})
    if len(short_term_buffer) > SHORT_TERM_BUFFER_SIZE:
        short_term_buffer = short_term_buffer[-SHORT_TERM_BUFFER_SIZE:]

    # Send reply to Pi
    tcp.send(ai_reply)

    # Summarize every N exchanges
    exchange_count += 1
    if exchange_count % SUMMARY_EVERY_N_EXCHANGES == 0:
        batch_text = "\n".join([f"User: {m['user']} AI: {m['ai']}" for m in short_term_buffer])
        try:
            summary = llm.generate_reply(batch_text)  # use same LLM for summarization
            summary_embedding = embedder.encode(summary)
            memory.add_memory(summary_embedding, summary, datetime.now().isoformat())
            logger.log_summary(summary, summary_embedding)
        except Exception as e:
            print(f"[SUMMARY ERROR]: {e}")
