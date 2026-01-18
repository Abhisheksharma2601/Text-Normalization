import os
from rapidfuzz import fuzz
from dotenv import load_dotenv

load_dotenv()

THRESHOLD = int(os.getenv("DEDUP_THRESHOLD", 90))

class Deduplicator:
    def __init__(self):
        self.seen_texts = []

    def check_duplicate(self, text: str) -> bool:
        for seen in self.seen_texts:
            score = fuzz.ratio(text, seen)
            if score >= THRESHOLD:
                return True

        self.seen_texts.append(text)
        return False
