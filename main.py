import domain.controller as controller

title, story, level = controller.generate_story_from_lingqs(15, 1)
# title, story, level = controller.generate_story_from_lingqs_and_theme(20, 1, "technology")
print(title)
print(story)
print(level)
print(controller.add_story_to_collection(title, story, level=level))
