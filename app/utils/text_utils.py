import re
import unicodedata

def normalize_text(text: str, language: str = "en") -> list:
    """
    Normalize text for evaluation.
    Handles English, Hindi (Devanagari), and Marathi (Devanagari) scripts.
    
    Args:
        text: Input text to normalize
        language: Language code ('en', 'hi', 'mr') - kept for API compatibility
    
    Returns:
        List of normalized words
    """
    # Normalize Unicode characters to ensure consistent comparison
    # NFKC normalization works well for Devanagari scripts
    text = unicodedata.normalize("NFKC", text)
    # Devanagari doesn't have case, but this is safe for English
    text = text.lower() 
    # \w correctly identifies Devanagari letters as word characters
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().split()