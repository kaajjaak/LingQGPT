base_prompt_short_easy = "Write me a short story in basic Japanese using simple vocabulary and grammar."
use_words = "Please use the following words in the correct context as I am trying to learn them: "
use_theme = "The theme of the story should be: "
title_prompt = "Start your response with \"Title: \" and then a title for your story in English."
level_prompt = "On the next line of your prompt, please write the level of the Japanese used in the story, use this scale: 1-6, 1 is absolute beginner, 6 is native speaker, in this format: \"Level: <1-6>\"."


def prompt_get_short_text_from_words(words):
    return base_prompt_short_easy + "\n" + title_prompt + "\n" + level_prompt + "\n" + use_words + ", ".join(words)


def prompt_get_short_text_from_words_and_theme(words, theme):
    return base_prompt_short_easy + "\n" + title_prompt + "\n" + level_prompt + "\n" + use_theme + theme + use_words + ", ".join(words)
