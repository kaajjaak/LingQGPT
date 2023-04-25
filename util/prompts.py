base_prompt_short_easy = "Write me a short story in basic Japanese using simple vocabulary and grammar."
use_words = "Please use the following words in the correct context as I am trying to learn them: "
use_theme = "The theme of the story should be: "


def prompt_get_short_text_from_words(words):
    return base_prompt_short_easy + "\n" + use_words + words.join(", ")


def prompt_get_short_text_from_words_and_theme(words, theme):
    return base_prompt_short_easy + "\n" + use_theme + theme + "\n" + use_words + words.join(", ")
