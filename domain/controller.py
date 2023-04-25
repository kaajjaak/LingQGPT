import re

import domain.lingq_domain as LingQ
import domain.openai_domain as OpenAI


def generate_story_from_lingqs():
    lingqs = LingQ.get_most_important_lingqs(30)
    text = OpenAI.write_story_from_words(lingqs)
    title_regex = r'Title:(.+)\n'
    title_match = re.search(title_regex, text)

    if title_match:
        title = title_match.group(1).strip()
        story_start = title_match.end()
        story = text[story_start:].strip()
        return title, story
    else:
        return None, None


def add_collection_to_lingq(title, description, language="ja"):
    collection = LingQ.create_collection(title, description, language)
    return collection


def add_story_to_collection(title, text, language="ja", description="", collection_id=None):
    LingQ.add_story_to_collection(title, text)
