from ..user_command import UserCommand
from fields import FieldTitleValueError, FieldTextValueError
from notes_book import NotesBook
from text_editor import show_text_editor


class CommandEditNote(UserCommand):
    def __init__(self):
        self.name = "edit-note"
        self.description = "Edit the note's text."
        self.pattern = "edit-note [title]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: NotesBook):
        error = self.input_validation(args, book)
        if error:
            return error

        title = " ".join(args)

        try:
            exist_record = book.find_by_title(title)
            if exist_record:
                new_text = show_text_editor(exist_record.text.value)
                if new_text != exist_record.text.value:
                    exist_record.edit_text(new_text)
                    msg = "Note edited."
                    complete = False
                    return (msg, complete)
                msg = "Note is not changed"
                complete = False
                return (msg, complete)

            msg = "Note doesn't exist."
            complete = False
            return (msg, complete)

        except FieldTitleValueError as e:
            return (f"Invalid title value. {e}", False)
        except FieldTextValueError as e:
            return (f"Invalid text value. {e}", False)
