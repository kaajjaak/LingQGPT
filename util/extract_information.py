import re


def text_to_title_level_story(text):
    title_regex = r'Title:(.+)\n'
    title_match = re.search(title_regex, text)
    level_regex = r'Level:(.+)\n'
    level_match = re.search(level_regex, text)

    title = title_match.group(1).strip() if title_match else None
    level = level_match.group(1).strip() if level_match else None

    if level_match:
        story_start = level_match.end()
        story = text[story_start:].strip()
    else:
        story = None

    return title, story, level