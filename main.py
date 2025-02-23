from stats import count_words, count_characters

def main():
    frankestein_path = "books/frankenstein.txt"
    text = get_book_text(frankestein_path)
    print(f"{count_words(text)} words found in the document")
    print(count_characters(text))

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()