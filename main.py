def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    get_word_count(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    words = string.split()
    print(len(words))



main()
