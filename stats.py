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

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text.lower())
    print(f"{word_count} words found in the document")
    print (f"{character_count}")

main()