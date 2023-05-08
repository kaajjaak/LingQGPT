import json


def save_words_data(filename, word_data):
    with open(f'./word_lists/{filename}.json', 'r', encoding='utf-8') as input_file:
        existing_data = json.load(input_file)

    for word, data in word_data.items():
        existing_data[word] = data

    with open(f'./word_lists/{filename}.json', 'w', encoding='utf-8') as output_file:
        json.dump(existing_data, output_file, indent=4, ensure_ascii=False)


def get_words_from_persistence(filename):
    # get everything from the file including the values
    with open(f'./word_lists/{filename}.json', 'r', encoding='utf-8') as input_file:
        existing_data = json.load(input_file)
    return existing_data
