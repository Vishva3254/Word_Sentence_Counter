# Total no.of words and sentence counter
import re

# Word count
def count_words(text):
    if isinstance(text, str):
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        return len(words)
    return 0

# Sentence count
def count_sentences(text):
    if isinstance(text, str):
        sentences = re.split(r'(?<!\d)\.(?!\d)|[!?]|\n', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    return 0