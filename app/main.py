from fastapi import FastAPI, UploadFile, File, HTTPException
from pydub import AudioSegment
import json, uuid, os

from app.services.speech_service import transcribe_audio
from app.utils.text_utils import normalize_text
from app.services.evaluator import evaluate

app = FastAPI()

CHAPTER_PATH = "data/chapters.json"


@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/assess/audio")
async def assess_audio(
    chapter_id: str = "1",
    file: UploadFile = File(...)
):
    if not file.filename.endswith((".wav", ".mp3")):
        raise HTTPException(status_code=400, detail="Invalid audio format")

    # Save temp audio
    temp_name = f"temp_{uuid.uuid4()}.wav"
    audio = AudioSegment.from_file(file.file)
    audio.export(temp_name, format="wav")

    duration_seconds = len(audio) / 1000

    # Speech to text
    transcript = transcribe_audio(temp_name)

    # Load chapter
    with open(CHAPTER_PATH, "r", encoding="utf-8") as f:
        chapters = json.load(f)

    if chapter_id not in chapters:
        os.remove(temp_name)
        raise HTTPException(status_code=404, detail="Chapter not found")

    reference_text = chapters[chapter_id]["text"]

    # Normalize
    student_words = normalize_text(transcript)
    reference_words = normalize_text(reference_text)

    # Evaluate
    metrics = evaluate(student_words, reference_words, duration_seconds)

    # Cleanup
    os.remove(temp_name)

    return {
        "transcript": transcript,
        **metrics
    }
