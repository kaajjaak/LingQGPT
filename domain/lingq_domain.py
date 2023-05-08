import api_wrappers.lingq_api_wrapper as LingQ
from util.persistence import save_words_data, get_words_from_persistence
from util.anki import get_first_words, get_all_words


def get_most_important_lingqs(amount=10, page=1):
    lingqs = LingQ.get_lingqs_to_learn("ja", page_size=amount, page=page)
    words = [word for word in lingqs["results"]]
    terms = [term["term"] for term in words]
    return terms


def add_story_to_lingq(story):
    pass


def create_collection(title, description, language="ja"):
    collection = LingQ.create_collection(title, description, language)
    return collection


def add_story_to_collection(title, text, language="ja", description="", level=1):
    return LingQ.create_lesson_in_collection(title, text, language_code=language, description=description, level=level)


def check_word_status(word, language="ja"):
    word_response = LingQ.check_word_status(word)
    word = word.rstrip()
    formatted_word = {
        word: {}
    }
    if word_response["count"] == 0:
        formatted_word[word]["added"] = False
    else:
        formatted_word[word]["added"] = True
        formatted_word[word]["status"] = word_response["results"][0]["status"]
    return formatted_word


def persist_words_status(filename, words):
    save_words_data(filename, words)


def check_words_status(words):
    words_list = {
    }
    for i in range(len(words)):
        words_list.update(check_word_status(words[i]))
        print(f"Checked word {i + 1} of {len(words)}")
    return words_list


def get_words_from_file(filename):
    words = get_words_from_persistence(filename)
    words = [key for key, value in words.items() if not value["added"] or value["status"] != 3]
    return words



