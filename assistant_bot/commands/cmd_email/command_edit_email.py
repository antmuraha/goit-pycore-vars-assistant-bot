from ..user_command import UserCommand
from fields import FieldNameValueError, FieldEmailValueError
from messages import Messages

class CommandEditEmail(UserCommand):
    def __init__(self):
        self.name = "edit-email"
        self.description = "Edit the email of the contact."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "new_email", "help": Messages.HELP_FIELD_NEW_EMAIL.value, "type": str},
        ]

    def execute(self, args, book):
        name = args.name
        new_email = args.new_email

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.edit_email(new_email)
                msg = "Email updated."
            else:
                msg = "Please create the contact before editing an email."
            
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldEmailValueError:
            return (f"Invalid email value. {e}", False)
