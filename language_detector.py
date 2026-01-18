from langdetect import detect, LangDetectException

def detect_language(text: str) -> str:
    """
    Detect the language of the given text.
    Returns ISO 639-1 code (e.g., 'en') or 'unknown'.
    """
    if not text or len(text.strip()) == 0:
        return "unknown"
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"
