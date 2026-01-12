from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def to_roman(text: str, language: str) -> str:
    """
    Converts Devanagari Hindi/Marathi to Roman.
    English is returned as-is.
    """
    if language in ["hi", "mr"]:
        return transliterate(
            text,
            sanscript.DEVANAGARI,
            sanscript.ITRANS
        )
    return text
