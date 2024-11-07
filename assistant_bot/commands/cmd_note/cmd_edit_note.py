from ..user_command import UserCommand
from fields import FieldTitleValueError, FieldTextValueError


class CommandEditNote(UserCommand):
    def __init__(self):
        self.name = "edit-note"
        self.description = "Edit the text of the note."
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
        
        title, text = args

        try:
            exist_record = book.get(title)
            if exist_record:
                exist_record.edit_text(text)
                msg = "Note edited."
                complete = False
                return (msg, complete)
        except FieldTitleValueError as e:
            return (f"Invalid title value", False)
        except FieldTextValueError as e:
            return (f"Invalid text value", False)
    