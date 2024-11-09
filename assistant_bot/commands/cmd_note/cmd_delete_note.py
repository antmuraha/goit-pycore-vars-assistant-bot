from ..user_command import UserCommand
from fields import FieldTitleValueError


class CommandDeleteNote(UserCommand):
    def __init__(self):
        self.name = "delete-note"
        self.description = "Delete a note from the notebook."
        self.pattern = "delete-note [title]" 

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
       
    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error
        
        title = " ".join(args)

        try:
            exist_record = book.get(title)
            if exist_record:
                del book[title]
                # book.remove_record(title)
                msg = "Note removed."
                complete = False
                return (msg, complete)
            
            msg = "Note does not exist"
            complete = False
            return (msg, complete)
        except FieldTitleValueError as e:
            return (f"Invalid title value. {e}", False)
    