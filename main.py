# python
from stats import get_book_text, count_words, count_characters, sort_dictionaries
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    BOOK_PATH = sys.argv[1]

def main():
    book_text = get_book_text(BOOK_PATH)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)  # count_characters lowercases internally
    sorted_chars = sort_dictionaries(char_counts)

    #print("============ BOOKBOT ============")
    #print(f"Analyzing book found at {BOOK_PATH}...")
    #print("----------- Word Count ----------")
    #print(f"Found {word_count} total words")
    #print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    #print("============= END ===============")

if __name__ == "__main__":
    main()