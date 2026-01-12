import whisper

# Upgrade to "small" or "medium" for better Hindi/Marathi support
model = whisper.load_model("small") 

def transcribe_audio(audio_path: str, language: str = None) -> str:
    # Explicitly providing the language code (e.g., "hi" or "mr") 
    # dramatically improves transcription accuracy.
    result = model.transcribe(audio_path, language=language)
    return result["text"]