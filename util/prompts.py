base_prompt_short_easy = "Write me a short story in basic Japanese using simple vocabulary and grammar."
use_words = "Please use the following words in the correct context as I am trying to learn them: "
use_theme = "The theme of the story should be: "
title_prompt = "Start your response with \"Title: \" and then a title for your story."


def prompt_get_short_text_from_words(words):
    return base_prompt_short_easy + "\n" + title_prompt + "\n" + use_words + ", ".join(words)


def prompt_get_short_text_from_words_and_theme(words, theme):
    return base_prompt_short_easy + "\n" + title_prompt + "\n" + use_theme + theme + "\n" + use_words + ", ".join(words)
