# tts_handler.py
from TTS.api import TTS
import os

class TTSHandler:
    def __init__(self, voice_preset="child", output_dir="../audio_output/"):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
        self.voice = voice_preset
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def speak(self, text):
        output_path = os.path.join(self.output_dir, "output.wav")
        self.tts.tts_to_file(text=text, file_path=output_path)
        os.system(f"aplay {output_path}")  # or any platform-specific playback
