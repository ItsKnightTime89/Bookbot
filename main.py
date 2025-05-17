import sys
from stats import count_words, count_characters, sort_character

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len (sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("=========== BOOKBOT ===========")
    print("Analyzing book found at {filepath}")

    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_character(character_count)

    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -----------")

    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("=========== End ============")

main()
