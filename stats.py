def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_character(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list