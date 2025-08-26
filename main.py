from stats import get_book_text, count_words, count_characters, sort_dictionaries

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text.lower())
    dictionary_list = sort_dictionaries(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dictionary in dictionary_list:
        print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()