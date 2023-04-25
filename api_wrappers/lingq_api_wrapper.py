import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("LINGQ_API_KEY")

headers = {
    'Authorization': f'Token {key}',
    'Content-Type': 'application/json'
}


def get_languages():
    response = requests.get('https://www.lingq.com/api/v2/languages', headers=headers)
    return [language for language in response.json() if language['knownWords'] > 0]


def get_contexts():
    # Get contexts from the API
    response = requests.get('https://www.lingq.com/api/v2/contexts', headers=headers)
    return response.json()


def get_lingqs(language_code="ja"):
    # Get lingqs from the API
    response = requests.get(f'https://www.lingq.com/api/v2/{language_code}/cards/', headers=headers)
    return response.json()


def get_courses_by_language(language_code="ja"):
    # Get courses from the API
    response = requests.get(f'https://www.lingq.com/api/v2/{language_code}/collections/my/', headers=headers)
    return response.json()


def get_lessons_by_course(language_code="ja", course_id=0):
    # Get lessons from the API
    response = requests.get(f'https://www.lingq.com/api/v2/{language_code}/collections/{course_id}', headers=headers)
    return response.json()


def get_lesson(language_code="ja", lesson_id=0):
    # Get lesson from the API
    response = requests.get(f'https://www.lingq.com/api/v2/{language_code}/cards/{lesson_id}', headers=headers)
    return response.json()


def get_lingqs_from_lesson(language_code="ja", lesson_id=0):
    # Get lingqs from the API
    payload = {
        "lesson": lesson_id
    }
    response = requests.get(f'https://www.lingq.com/api/v3/{language_code}/lessons/{lesson_id}', headers=headers)
    return response.json()


def get_lesson_info(language_code="ja", lesson_id=0):
    payload = {
        "lesson": lesson_id
    }
    # Get lesson info from the API
    response = requests.get(f'https://www.lingq.com/api/v3/{language_code}/lessons/counters', headers=headers,
                            params=payload)
    return response.json()


def get_lingqs_to_learn(language_code="ja", page_size=100, search_criteria="startsWith", sort="importance",
                        status=[1, 2], page=1):
    payload = {
        "page": page,
        "page_size": page_size,
        "search_criteria": search_criteria,
        "sort": sort,
        "status": status,
    }
    response = requests.get(f'https://www.lingq.com/api/v3/{language_code}/cards', headers=headers, params=payload)
    return response.json()


def create_collection(title, description, language_code="ja"):
    payload = {
        "title": title,
        "description": description,
        "hasPrice": False,
        "isFeatured": False,
        "language": language_code,
        "sellAll": False,
        "sourceURLEnabled": False,
        "tags": [],
    }
    response = requests.post(f"https://www.lingq.com/api/v3/{language_code}/collections/", headers=headers,
                             json=payload)
    print(response)
    print(response.json())
    return response.json()


def create_lesson():
    pass


def create_lesson_in_collection(title, text, collection=1288847, description="", language_code="ja"):
    payload = {
        "collection": collection,
        "description": description,
        "language": language_code,
        "save": True,
        "status": "private",
        "text": text,
        "title": title
    }
    response = requests.post(f"https://www.lingq.com/api/v3/{language_code}/lessons/import/", headers=headers, json=payload)
