from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError
from fields import FieldText

class CommandAddNote(UserCommand):
    def __init__(self):
        self.name = "add-note"
        self.description = "The add note to a contact."
        self.pattern = "add-note [username] [note]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
        
        if len(params) == 1:
            msg = "Please enter the note's text."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        username = args[0]
        note = args[1]

        try:
            book.add_record(username, note)

            msg = "Note added to the notebook."
            complete = False
            return (msg, complete)
        except FieldNameValueError:
            return ("Invalid username or text value.", False)
