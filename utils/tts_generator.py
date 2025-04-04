from gtts import gTTS
import os

def generate_tts_audio(narrations, output_dir="assets/audio"):
    os.makedirs(output_dir, exist_ok=True)
    audio_paths = []
    for i, text in enumerate(narrations):
        tts = gTTS(text)
        path = os.path.join(output_dir, f"audio_{i}.mp3")
        tts.save(path)
        audio_paths.append(path)
    return audio_paths
