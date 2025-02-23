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

def order_characters(occ_dict):
    return dict(sorted(occ_dict.items(), key=lambda item: item[1], reverse=True))