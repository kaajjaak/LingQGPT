import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_text_from_prompt(prompt, model="text-davinci-003"):
    r = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=1000,
    )
    return r