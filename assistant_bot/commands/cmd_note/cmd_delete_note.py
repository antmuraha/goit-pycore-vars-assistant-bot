from ..user_command import UserCommand
from fields import FieldTitleValueError
from messages import Messages


class CommandDeleteNote(UserCommand):
    def __init__(self):
        self.name = "delete-note"
        self.description = "Delete a note from the notebook."
        self.args = [
             {"name": "title", "help": Messages.HELP_FIELD_TITLE.value, "type": str},
        ]

    def execute(self, args, book):
        title = args.title

        try:
            exist_record = book.get(title)
            if exist_record:
                del book[title]
                # book.remove_record(title)
                msg = "Note removed."
                complete = False
                return (msg, complete)
            
            msg = "Note doesn't exist."
            complete = False
            return (msg, complete)
        except FieldTitleValueError as e:
            return (f"Invalid title value. {e}", False)
    