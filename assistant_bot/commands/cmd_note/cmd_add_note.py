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
            msg = "Please enter a note."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, note = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_note(note)
            else:
                record = RecordContact(name)
                record.add_note(note)
                book[name] = record

            msg = "Note does not exist."
            complete = False
            return (msg, complete)
        except FieldNoteValueError:
            return ("Invalid note value.", False)
        except FieldNameValueError:
            return ("Invalid name value.", False)
