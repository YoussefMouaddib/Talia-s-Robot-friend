## File structure: 
# WSL 
laptop_host/
├── models/

│   ├── llama_3_4b_8bit/           # LLM weights

│   └── embeddings_model/          # sentence-transformers model

├── vector_db/

│   ├── faiss_index.faiss          # FAISS index file

│   └── metadata.json              # summaries + timestamps

├── summaries/                     # optional raw summary text

│   └── summary_logs.json

├── src/

│   ├── main.py                    # orchestrator, TCP server, loop

│   ├── llm_handler.py             # LLM inference & summarization

│   ├── memory_manager.py          # FAISS DB operations (store/retrieve)

│   ├── prompt_builder.py          # builds prompts using system + short-term + memories

│   ├── tcp_server.py              # TCP server to receive ASR & send replies

│   └── logger.py                  # JSON logging

├── config.py                      # system prompt, model paths, hyperparameters

└── requirements.txt               # Python dependencies

# Pi

raspberry_pi_client/

├── audio_input/                    # raw mic recordings (optional)

├── audio_output/                   # TTS files

├── short_term_buffer.json           # last 10 exchanges (user+AI)

├── src/

│   ├── main.py                     # orchestrator, TCP client loop

│   ├── asr_handler.py              # captures mic audio → Whisper.cpp transcription

│   ├── tts_handler.py              # Coqui TTS playback

│   ├── buffer_manager.py           # maintains short-term buffer

│   ├── tcp_client.py               # sends ASR text → laptop, receives AI reply

│   └── logger.py                   # optional local logging of raw audio / short-term buffer

├── config.py                       # model/audio settings, TCP settings

└── requirements.txt                # Python dependencies

