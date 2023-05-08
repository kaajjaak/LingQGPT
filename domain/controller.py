import re

import domain.lingq_domain as LingQ
import domain.openai_domain as OpenAI

import re

from util.extract_information import text_to_title_level_story


def generate_story_from_lingqs(amount=10, page=1):
    lingqs = LingQ.get_most_important_lingqs(amount, page=page)
    text = OpenAI.write_story_from_words(lingqs)
    return text_to_title_level_story(text)


def generate_story_from_lingqs_and_theme(amount=10, page=1, theme=""):
    lingqs = LingQ.get_most_important_lingqs(amount, page=page)
    text = OpenAI.write_story_from_words_and_theme(lingqs, theme)
    return text_to_title_level_story(text)


def add_collection_to_lingq(title, description, language="ja"):
    collection = LingQ.create_collection(title, description, language)
    return collection


def add_story_to_collection(title, text, language="ja", description="", level=1):
    if title is None:
        title = "Untitled"
    return LingQ.add_story_to_collection(title, text, language, description, level)["lessonURL"]


def generate_story_from_file(filename, amount=10):
    words = LingQ.get_words_from_file(filename)[:amount]
    text = OpenAI.write_story_from_words(words)
    return text_to_title_level_story(text)


def recheck_words_from_file(filename, amount):
    LingQ.persist_words_status(filename, LingQ.check_words_status(LingQ.get_words_from_file(filename)[:amount]))


def recheck_all_words_from_file(filename):
    LingQ.persist_words_status(filename, LingQ.check_words_status(LingQ.get_words_from_file(filename)))
