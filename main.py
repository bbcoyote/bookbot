def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    get_word_count(text)
    get_character_count(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    words = string.split()
    print(len(words))

def get_character_count(document):
    lower_case_doc = document.lower()
    char_dict = {}
    for character in lower_case_doc:
        char_dict[character] = char_dict.setdefault(character, 0) + 1
    print(char_dict)



# main()
get_character_count("Hello this works like this")
