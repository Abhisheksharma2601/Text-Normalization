Text Normalization & Deduplication Pipeline
1. Project Goal

The goal of this project is to clean and deduplicate raw text articles so they can be used reliably for analysis or machine learning.

Real-world text data is often messy:

Different casing (uppercase/lowercase)

HTML tags and special characters

Extra spaces

Duplicate or nearly duplicate articles

Mixed languages

This pipeline processes raw JSON articles and produces a clean, structured output.

2. Pipeline Overview
Raw Articles (JSON)
        ↓
Text Normalization
        ↓
Language Detection
        ↓
Duplicate Detection
        ↓
Cleaned Articles (JSON)


Each step is handled by a separate Python file to keep the code clean and easy to understand.

3. Project Structure

Each file has a single responsibility:

main.py – runs the full pipeline

normalizer.py – cleans and normalizes text

language_detector.py – detects article language

deduplicator.py – finds and marks duplicate articles

tests/ – checks that each part works correctly

This structure makes the code easier to test and maintain.

4. Text Normalization (normalizer.py)
Why normalize text?

Cleaning the text first makes language detection and deduplication more accurate.

Steps applied:

Convert text to lowercase

Remove HTML tags

Remove special characters and punctuation

Remove extra spaces

Trim leading and trailing whitespace

Edge cases handled:

Empty strings return empty output

Text with only HTML is cleaned safely

Unicode characters are handled correctly

Example

Before:

"India Launches NEW Policy!!! <br>"


After:

"india launches new policy"

5. Language Detection (language_detector.py)

The pipeline detects the language of each normalized article.

Approach:

Use a language detection library

Run detection after cleaning the text

If detection fails or text is too short, return "unknown"

This keeps the pipeline stable even when input data is poor.

6. Duplicate Detection (deduplicator.py)
Why fuzzy matching?

Exact matching fails when text has:

Small typos

Slight wording differences

Different punctuation

Approach:

Compare normalized titles using fuzzy string similarity

If similarity is above a chosen threshold, mark the article as a duplicate

Trade-off:

Fuzzy matching is slower than exact matching

It catches more real duplicates

This approach balances simplicity and accuracy for small to medium datasets.

7. Pipeline Orchestration (main.py)

main.py controls the flow of the pipeline:

Load raw articles from JSON

Normalize text

Detect language

Check for duplicates

Add metadata (timestamp)

Save cleaned articles to output JSON

This simulates how real data pipelines work in batch processing systems.

8. Testing Strategy

Tests are written to make sure the pipeline works correctly.

Unit tests:

Normalization works for messy text

Language detection handles known and unknown languages

Deduplication detects similar titles

Integration test:

Runs the full pipeline

Confirms output format and correctness

Testing ensures the pipeline is reliable and easy to change in the future.

9. Results & Quality Check

After running the pipeline:

Text is consistent and clean

Duplicate articles are correctly identified

Language information is added

Output data is easier to analyze

A simple before-and-after comparison shows clear improvement in data quality.

10. AI Usage

AI tools were used to:

Get ideas for pipeline design

Identify common edge cases

Suggest testing scenarios

All code was reviewed and written manually to ensure understanding.

11. Future Improvements

Possible improvements include:

Faster duplicate detection for large datasets

Better handling of multiple languages

Semantic duplicate detection using embeddings

12. Conclusion

This project demonstrates:

Clean Python project structure

Basic NLP preprocessing

Handling of real-world text issues

Writing and testing reusable code

It provides a strong foundation for more advanced text processing systems.
