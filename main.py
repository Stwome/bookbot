def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = word_count(text)
    print(f"{count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(path):
    words = path.split()
    return len(words)

main()