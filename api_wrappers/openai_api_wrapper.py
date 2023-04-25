import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def write_text_from_words(words, model="text-davinci-003"):
    text = ""
    for word in words:
        text += f"{word} "
    return text