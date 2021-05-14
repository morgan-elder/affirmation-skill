from mycroft import MycroftSkill, intent_file_handler


class Affirmation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('affirmation.intent')
    def handle_affirmation(self, message):
        self.speak_dialog('affirmation')
    
    @intent_file_handler('create.intent')
    def handle_createAffirmation(self, message):
        affirmation = self.get_response('create')
        file = open("./locale/en-us/affirmation.dialog", "a")
        file.write(affirmation + "\n")
        file.close()


def create_skill():
    return Affirmation()

