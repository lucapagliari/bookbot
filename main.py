def get_book_text(filepath):
    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():

    import os
    print(os.getcwd())  # prints the Current Working Directory

    frankestein_path = "books/frankenstein.txt"
    print(get_book_text(frankestein_path))

main()