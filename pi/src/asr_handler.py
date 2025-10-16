# asr_handler.py
import whisper
import sounddevice as sd
import numpy as np

class ASRHandler:
    def __init__(self, model_path):
        self.model = whisper.load_model(model_path)

    def record_audio(self, duration=5, fs=16000):
        print("[ASR] Recording...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        audio = audio.flatten()
        return audio

    def transcribe(self, audio):
        result = self.model.transcribe(audio)
        return result["text"]
