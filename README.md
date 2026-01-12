# ThynkLearn: Reading Evaluation Module (AI + Backend)

## Project Overview
**ThynkLearn** is an automated Reading Evaluation Module designed for **ThynkChat INDIA V2**. ]Its primary objective is to evaluate a student's reading performance by comparing their spoken audio input against reference textbook content].This service streamlines the assessment process for educators by providing data-driven metrics on student fluency and accuracy.

The system follows a comprehensive AI pipeline:
**Audio Input → Speech Recognition (ASR) → Text Normalization → Text Comparison → Scoring → API Response**.

---

## Key Features
* **Speech-to-Text (ASR):** Converts student audio into a text transcript using high-accuracy engines like OpenAI Whisper or Google Speech API.
* **Reference Retrieval:** Fetches specific chapter text from storage (JSON/Database) to use as the evaluation gold standard.
* **Text Normalization:** Ensures fair evaluation by converting text to lowercase, removing punctuation, and handling extra spaces
* **Advanced Comparison:** Utilizes RapidFuzz and Levenshtein distance for fuzzy matching to account for minor speech variations
* **Automated Scoring:** Generates critical metrics including Accuracy, Completeness, and Fluency (Words Per Minute).

---

## Tech Stack
* **Language:** Python 3.9+ 
* **Framework:** FastAPI 
* **ASR Engine:** OpenAI Whisper / Google Speech
* **Text Matching:** RapidFuzz 
* **Database:** SQLite / PostgreSQL / Local JSON 
* **Audio Handling:** Pydub / Soundfile 
---

## Project Structure
```
reading-evaluation/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── api/             # API routes and endpoint definitions
│   ├── services/        # ASR, Evaluation, and Comparison logic 
│   ├── utils/           # Normalization and audio utility functions
│   └── data/
│       └── chapters.json # Reference textbook storage
├── requirements.txt      # Project dependencies 
└── README.md             # Project documentation
```
---
## Setup Instructions
### 1. Clone the Repository
```
git clone https://github.com/Adi1exe/reading-evaluation.git
cd reading-evaluation
```
### 2. 2. Create a Virtual Environment
```
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run the Server
```
uvicorn app.main:app --reload
```
The service will be accessible at http://127.0.0.1:8000/docs.
---
## API Usage

### Health Check
- Endpoint: /health 
- Method: GET 
- Description: Verifies the service status.

### Assess Reading

- Endpoint: /assess/audio 
- Method: POST 
- Input: Multipart form-data with an audio file (.wav or .mp3).

- Process:
  1. Transcribes audio to text.
  2. Normalizes transcript and reference text.
  3. Calculates accuracy and completeness.
  4. Computes Fluency (WPM) based on audio duration.
---
Sample Response
```
{
  "transcript": "this is the transcribed student reading",
  "completeness": 75.0,
  "accuracy": 82.5,
  "fluency_wpm": 110,
  "remarks": "Good reading performance"
}
```
---
## Evaluation Metrics Defined
- **Accuracy %**: Percentage of correctly matched words compared to the reference.
- **Completeness %**: Percentage of the reference text actually covered/read by the student.
- **Fluency (WPM)**: The reading speed measured in words per minute.
---
