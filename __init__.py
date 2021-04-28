from mycroft import MycroftSkill, intent_file_handler


class Affirmation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('affirmation.intent')
    def handle_affirmation(self, message):
        self.speak_dialog('affirmation')


def create_skill():
    return Affirmation()

