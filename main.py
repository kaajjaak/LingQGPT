import domain.controller as controller

title, story = controller.generate_story_from_lingqs()
controller.add_story_to_collection(title, story)
