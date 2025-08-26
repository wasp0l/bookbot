def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text

def count_words(book_text):
    word_list = book_text.split()
    i = len(word_list)
    return i

def count_characters(book_text):
    character_count = {}
    for character in book_text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_dictionaries(character_count):
    dictionary_list = []
    for character in character_count:
        if character.isalpha():
            dictionary_list.append({"char": character, "num": character_count[character]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list