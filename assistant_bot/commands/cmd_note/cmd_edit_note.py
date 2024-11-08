from ..user_command import UserCommand
from fields import FieldTitleValueError, FieldTextValueError
from text_editor import show_text_editor


class CommandEditNote(UserCommand):
    def __init__(self):
        self.name = "edit-note"
        self.description = "Edit the text of the note."
        self.pattern = "edit-note [title]" 

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
        
        # if len(params) == 1:
        #     msg = "Please enter a new text."
        #     complete = False
        #     return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        title = args[0]
        # new_text = args[1]

        try:
            exist_record = book.get(title)
            if exist_record:
                new_text = show_text_editor("..")
                print(f"New text:", new_text)
                exist_record.edit_text(new_text)
                msg = "Note edited."
                complete = False
                return (msg, complete)
            
        except FieldTitleValueError as e:
            return (f"Invalid title value", False)
        except FieldTextValueError as e:
            return (f"Invalid text value", False)
