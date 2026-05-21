import re
from collections import Counter

def extract_keywords(text, top_n=10):
    stopwords = {
        "the", "is", "in", "and", "to", "of", "a", "for", "on", "with",
        "this", "that", "it", "as", "are", "was", "were", "be", "by",
        "an", "or", "from", "at", "we", "you", "i", "they", "he", "she"
    }

    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    filtered_words = [word for word in words if word not in stopwords]

    word_counts = Counter(filtered_words)
    keywords = word_counts.most_common(top_n)

    return keywords