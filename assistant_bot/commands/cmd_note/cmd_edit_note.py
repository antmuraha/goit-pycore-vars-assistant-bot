from ..user_command import UserCommand
from fields import FieldTitleValueError


class CommandEditNote(UserCommand):
    def __init__(self):
        self.name = "edit-note"
        self.description = "Edit the note."
        self.pattern = "edit-note [title] [new text]" 











    def input_validation(self, params):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        title = args

        try:
            exist_record = book.get(title)
            if exist_record:
                book.remove_record(title)
                msg = "Note removed."
                complete = False
                return (msg, complete)
        except FieldTitleValueError as e:
            return (f"Invalid title value", False)