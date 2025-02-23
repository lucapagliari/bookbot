def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    occurences = {}
    for char in text:
        c = char.lower()
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    return occurences