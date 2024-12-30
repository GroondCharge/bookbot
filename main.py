def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count = unique_characters(text)
    sorted_list = to_sorted_list(letter_count)
    print(f"--- Begin report of {book_path} ---")
    sum = 0
    for character in sorted_list:
        sum += character["num"]
    print(f"{sum} words found in the document")
    for character in sorted_list:
        letter = character["letter"]
        number = character["num"]
        if letter.isalpha():
            print(f"The '{letter}' character was found {number} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(book):
    value = book.split()
    return len(value)
def unique_characters(book):
    characters = {}
    letters = list(book)
    for letter in letters:
        letter = letter.lower()
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters
def to_sorted_list(letters):
    new_list = []
    for key in letters:
        new_list.append({"letter": key, "num": letters[key]})
    new_list.sort(reverse = True,key=lambda x: x['num'])
    return new_list

main()