from ..user_command import UserCommand
from notes_book import NotesBook
from record_contact import RecordContact
from fields import FieldTitleValueError, FieldTextValueError

from text_editor import show_text_editor

class CommandAddNote(UserCommand):
    def __init__(self):
        self.name = "add-note"
        self.description = "Add a note to the notebook."
        self.pattern = "add-note [title]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: NotesBook):
        error = self.input_validation(args, book)
        if error:
            return error

        title = args[0]
        text = show_text_editor('')

        try:
            book.add_record(title, text)
            msg = "Note added."
            complete = False
            return (msg, complete)
        except FieldTitleValueError as e:
            return (f"Invalid title or text value. {e}", False)
        except FieldTextValueError as e:
            return (f"Invalid text value. {e}", False)