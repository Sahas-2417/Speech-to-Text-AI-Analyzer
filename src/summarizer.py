def generate_summary(text):
    sentences = text.split(".")
    
    if len(sentences) <= 3:
        return text

    summary = ". ".join(sentences[:3])
    return summary.strip() + "."