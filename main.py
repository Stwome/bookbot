def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    count = word_count(text)
    #print(f"{count} words found in the document")
    chars_dict = get_chars_dict(text)

    chars_list = list(chars_dict.items())
    chars_list.sort() #sorts alphabetically

    print(chars_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(path):
    words = path.split()
    return len(words)

def get_chars_dict(text):
    chars = {}  #create a directory
    for c in text: #search each character in the text
        lowered = c.lower()
        if lowered.isalpha() == False:
            pass
        elif lowered in chars:
            chars[lowered] += 1 
        else:
            chars[lowered] = 1
    return chars


main()