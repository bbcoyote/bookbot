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

def get_character_count(document):
    lower_case_doc = document.lower()
    char_dict = {}
    value = 0
    for character in lower_case_doc:
        # check if character already exists in dictionary
        # if not add new key with a value of one.
        # if it does exist in the dictionary increment the value.
        # we can use the setdefault dict method to check if a key exists and add to the dictionary if it doesn't
        character_count = char_dict.setdefault(character, value += 1)



main()
