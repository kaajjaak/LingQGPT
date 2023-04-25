import api_wrappers.lingq_api_wrapper as LingQ


def get_most_important_lingqs(amount=10):
    lingqs = LingQ.get_lingqs_to_learn("ja", page_size=amount)
    words = [word for word in lingqs["results"]]
    terms = [term["term"] for term in words]
    return terms

