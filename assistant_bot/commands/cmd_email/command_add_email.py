from ..user_command import UserCommand
from fields import FieldNameValueError, FieldEmailValueError

class CommandAddEmail(UserCommand):
    def __init__(self):
        self.name = "add-email"
        self.description = "Add the email to the contact."
        self.pattern = "add-email [username] [email]"

    def input_validation(self, params):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
        
        if len(params) == 1:
            msg = "Please enter an email."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]
        email = args[1]

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_email(email)
                msg = "Email added to the contact."
            else:
                msg = "Please create the contact before adding an email."
            
            complete = False
            return (msg, complete)
        except FieldNameValueError:
            return ("Invalid name value.", False)
        except FieldEmailValueError:
            return ("Invalid email value.", False)
