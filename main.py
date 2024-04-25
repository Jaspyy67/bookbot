import os

def main():
    book_path = "books/frankenstein.txt"
    full_path = os.path.abspath(book_path)
    print("Trying to open:", full_path)
    text = book_text(book_path)
    print(" ")
    num_words = wordcounter(text)
    print(f"{num_words} words found in the document")
    letter_count = lettercounter(text)


def book_text(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        file_contents = f.read()
    return file_contents

def wordcounter(text):
    punctuation_chars = [".", ",", ":", ";", "!", "?"]
    clean_text = text
    for char in punctuation_chars:
        clean_text = clean_text.replace(char, "")
    words = clean_text.split()
    return len(words)

def lettercounter(text):
    letters = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in letters:
                letters[lowered] += 1
            else:
                letters[lowered] = 1
    for x in letters:
        print(f"The {x} character was found {letters[x]} times")
    return letters
    


main()
