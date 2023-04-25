import api_wrappers.lingq_api_wrapper as LingQ


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
