from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler


class FocusDefinition(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require('definition.focus'))
    def handle_focus_def(self):
        self.speak_dialog('definition.focus')

    @intent_handler(IntentBuilder("").require('focus.departments'))
    def handle_focus_dep(self):
        self.speak_dialog('definition.departments')

    @intent_handler(IntentBuilder("").require('focus.field'))
    def handle_focus_fields(self):
        self.speak_dialog('definition.field')

    @intent_handler(IntentBuilder("").require('focus.history'))
    def handle_focus_history(self):
        self.speak_dialog('definition.history')


def create_skill():
    return FocusDefinition()
