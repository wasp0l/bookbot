def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text

def count_words(book_text):
    word_list = book_text.split()
    i = len(word_list)
    return i
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

main()