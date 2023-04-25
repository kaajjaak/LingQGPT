import util.prompts as prompts
import api_wrappers.openai_api_wrapper as OpenAI


def write_story_from_words(words):
    prompt = prompts.prompt_get_short_text_from_words(words)
    response = OpenAI.write_text_from_prompt(prompt)
    return response["choices"][0]["text"]
