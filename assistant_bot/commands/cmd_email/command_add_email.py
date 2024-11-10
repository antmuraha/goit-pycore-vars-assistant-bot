from ..user_command import UserCommand
from fields import FieldNameValueError, FieldEmailValueError
from messages import Messages

class CommandAddEmail(UserCommand):
    def __init__(self):
        self.name = "add-email"
        self.description = "Add the email to the contact."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "email", "help": Messages.HELP_FIELD_EMAIL.value, "type": str},
        ]


    def execute(self, args, book):
        name = args.name
        email = args.email

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_email(email)
                msg = "Email added to the contact."
            else:
                msg = "Please create the contact before adding an email."
            
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldEmailValueError as e:
            return (f"Invalid email value. {e}", False)
