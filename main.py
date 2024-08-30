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
    char_dict_list = []
    for character in lower_case_doc:
        char_dict[character] = char_dict.setdefault(character, 0) + 1
    for key_pair in char_dict:
        if key_pair.isalpha():
            char_dict_list.append({"character": key_pair, "count": char_dict[key_pair]})
    char_dict_list.sort(reverse=True, key=lambda d: d["count"])
    print(char_dict_list)



main()

