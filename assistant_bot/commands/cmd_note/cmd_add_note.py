from ..user_command import UserCommand
from notes_book import NotesBook
from record_contact import RecordContact
from fields import FieldTitleValueError, FieldTextValueError
from text_editor import show_text_editor
from messages import Messages

class CommandAddNote(UserCommand):
    def __init__(self):
        self.name = "add-note"
        self.description = "Add a note to the notebook."
        self.args = [
             {"name": "title", "help": Messages.HELP_FIELD_TITLE.value, "type": str},
        ]

    def execute(self, args, book: NotesBook):
        title = args.title

        record = book.find_by_title(title)
        if record:
            msg = "A note with this name already exists"
            complete = False
            return (msg, complete)

        try:
            text = show_text_editor('')
            book.add_record(title, text)
            msg = "Note added."
            complete = False
            return (msg, complete)
        except FieldTitleValueError as e:
            return (f"Invalid title or text value. {e}", False)
        except FieldTextValueError as e:
            return (f"Invalid text value. {e}", False)