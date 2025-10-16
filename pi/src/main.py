# main.py
from config import *
from tcp_client import TCPClient
from asr_handler import ASRHandler
from tts_handler import TTSHandler

tcp = TCPClient(TCP_HOST, TCP_PORT)
asr = ASRHandler(ASR_MODEL_PATH)
tts = TTSHandler(TTS_VOICE, TTS_OUTPUT_DIR)

while True:
    # Record child input
    audio = asr.record_audio(duration=5)
    user_text = asr.transcribe(audio)
    print(f"[ASR] Transcribed: {user_text}")

    # Send to Laptop
    tcp.send(user_text)

    # Receive AI reply
    ai_reply = tcp.receive()
    print(f"[AI] Reply: {ai_reply}")

    # Speak reply (blocks mic input until done)
    tts.speak(ai_reply)
