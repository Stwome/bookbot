def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)  #print(text)
    
    count = word_count(text) #print(f"{count} words found in the document")
    chars_dict = get_chars_dict(text)
    sorted_list = count_sort(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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

def sort_on(dict):
    return dict["num"]

def count_sort(chars_dict):
    sorted_list = []
    for c in chars_dict:
        sorted_list.append({"char": c, "num": chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()