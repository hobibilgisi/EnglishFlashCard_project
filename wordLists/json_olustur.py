import json
word_list = [
    {"word": "apple", "meaning": "a fruit"},
    {"word": "book", "meaning": "a set of written pages"},
    {"word": "car", "meaning": "a vehicle"}
]

# Specify the path to the txt file
txt_file_path = "c:/Users/ilker/Desktop/python/python_projects/EnglishFlashCard_project/wordLists/word_list.txt"

# Read words from the txt file and add them to the word_list
with open(txt_file_path, "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        parts = line.strip().split(" - ")
        if len(parts) == 2:
            word, meaning = parts
            word_list.append({"word": word, "meaning": meaning})

# Write the updated word_list to the JSON file
json_file_path = "c:/Users/ilker/Desktop/python/python_projects/EnglishFlashCard_project/wordLists/word_list.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(word_list, json_file, ensure_ascii=False, indent=4)
