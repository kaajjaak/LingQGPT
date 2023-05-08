def convert_anki_to_wordlist(filename):
    with open(f'../anki_decks/{filename}.txt', 'r', encoding='utf-8') as deck:
        lines = deck.readlines()[2:]
        converted_lines = [line.split(' ')[0] + '\n' for line in lines]
        converted_lines[-1] = converted_lines[-1].rstrip('\n')

        with open(f'../word_lists/{filename}_converted.txt', 'w', encoding='utf-8') as output_file:
            output_file.writelines(converted_lines)

    return f'{filename}_converted'


# convert_anki_to_wordlist("decks")

def get_word_count(filename):
    with open(f'../word_lists/{filename}.txt', 'r', encoding='utf8') as wordlist:
        lines = wordlist.readlines()
        word_count = len(lines)
    return word_count