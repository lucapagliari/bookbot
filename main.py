from stats import (
    count_words, 
    count_characters,
    order_characters,
)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    ordered_num_chars = order_characters(num_chars)

    print_report(book_path, num_words, ordered_num_chars)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, num_words, ordered_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in ordered_chars.items():
        if key.isalpha():    
            print(f"{key}: {value}")
    print("============= END ===============")

main()