import json
from datetime import datetime, timezone
from language_detector import detect_language

import normalizer
import language_detector
import deduplicator

INPUT_FILE = "input/raw_articles.json"
OUTPUT_FILE = "output/cleaned_articles.json"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            raise ValueError(f"{INPUT_FILE} is empty")
        articles = json.loads(content)

    dedup = deduplicator.Deduplicator()
    cleaned = []

    for article in articles:
        original = article.get("title", "")
        # NOTE: calling via the module
        normalized = normalizer.normalize_text(original)
        language = language_detector.detect_language(normalized)
        is_duplicate = dedup.check_duplicate(normalized)

        cleaned.append({
            "original_title": original,
            "normalized_title": normalized,
            "language": language,
            "is_duplicate": is_duplicate,
            "cleaned_at": datetime.now(timezone.utc).isoformat()
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
