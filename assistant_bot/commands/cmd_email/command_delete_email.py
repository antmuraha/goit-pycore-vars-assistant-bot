from ..user_command import UserCommand
from fields import FieldNameValueError, FieldEmailValueError
from messages import Messages

class CommandDeleteEmail(UserCommand):
    def __init__(self):
        self.name = "delete-email"
        self.description = "Delete a contact's email."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
        ]

    def execute(self, args, book):
        name = args.name

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.remove_email()
                msg = "Email deleted."
            else:
                msg = "Сontact not found."
            
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)

