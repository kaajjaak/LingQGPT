import domain.controller as controller

controller.recheck_words_from_file("decks_converted", 5)
title, story, level = controller.generate_story_from_file_and_theme("decks_converted", 5, "love")
# title, story, level = controller.generate_story_from_lingqs_and_theme(20, 1, "technology")
print(title)
print(story)
print(level)
print(controller.add_story_to_collection(title, story, level=level))
