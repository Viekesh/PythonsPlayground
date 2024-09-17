def text_processor(text):
    words = text.split()
    unique_words = set(words)
    words_length = [len(word) for word in words]
    max_length = max(words_length) if words_length else 0
    longest_word = [word for word in unique_words if len(word) == max_length]
    return longest_word, len(unique_words)
