from mycroft import MycroftSkill, intent_file_handler
import pathlib


class Affirmation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('affirmation.intent')
    def handle_affirmation(self, message):
        self.speak_dialog('affirmation')
    
    @intent_file_handler('create.intent')
    def handle_createAffirmation(self, message):
        affirmation = self.get_response('create')
        path = Path().absolute()
        path = path / 'locale' / 'en-us' / 'affirmation.dialog'
        self.write_affirmation_to_file(path, affirmation)
    
    
    def write_affirmation_to_file(self, path, line):
        with self.file_system.open(path, "a") as file:
            file.write(line)


def create_skill():
    return Affirmation()

