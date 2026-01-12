from rapidfuzz import fuzz

def evaluate(student_words, reference_words, duration_seconds):
    matched = 0
    used_refs = set()

    for word in student_words:
        for i, ref in enumerate(reference_words):
            if i in used_refs:
                continue
            if fuzz.ratio(word, ref) >= 85:
                matched += 1
                used_refs.add(i)
                break

    accuracy = (matched / len(student_words)) * 100 if student_words else 0
    completeness = (matched / len(reference_words)) * 100 if reference_words else 0
    wpm = (len(student_words) / duration_seconds) * 60 if duration_seconds else 0

    remarks = "Good reading performance"
    if accuracy < 50:
        remarks = "Needs improvement"
    elif wpm > 180:
        remarks = "Reading too fast (suspicious)"

    return {
        "accuracy": round(accuracy, 2),
        "completeness": round(completeness, 2),
        "fluency_wpm": round(wpm),
        "remarks": remarks
    }
