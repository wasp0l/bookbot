# python
def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    counts = {}
    for ch in book_text.lower():
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_on(item):
    return item["num"]

def sort_dictionaries(char_counts):
    items = []
    for ch, n in char_counts.items():
        if ch.isalpha():
            items.append({"char": ch, "num": n})
    items.sort(key=sort_on, reverse=True)
    return items