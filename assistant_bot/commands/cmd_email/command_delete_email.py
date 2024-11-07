from ..user_command import UserCommand
from fields import FieldNameValueError, FieldEmailValueError

class CommandDeleteEmail(UserCommand):
    def __init__(self):
        self.name = "delete-email"
        self.description = "Delete a contact's email address."
        self.pattern = "delete-email [username]"

    def input_validation(self, params):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.remove_email()
                msg = "Contact's email deleted."
            else:
                msg = "Сontact not found."
            
            complete = False
            return (msg, complete)
        except FieldNameValueError:
            return ("Invalid name value.", False)

