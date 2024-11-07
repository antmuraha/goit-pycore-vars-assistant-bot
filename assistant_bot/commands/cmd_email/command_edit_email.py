from ..user_command import UserCommand
from fields import FieldNameValueError, FieldEmailValueError

class CommandEditEmail(UserCommand):
    def __init__(self):
        self.name = "edit-email"
        self.description = "Edit the email to the contact."
        self.pattern = "edit-email [username] [email]"

    def input_validation(self, params):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
        
        if len(params) == 1:
            msg = "Please enter a new email."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args)
        if error:
            return error

        name = args[0]
        new_email = args[1]

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.edit_email(new_email)
                msg = "Email updated successfully."
            else:
                msg = "Please create the contact before editing an email."
            
            complete = False
            return (msg, complete)
        except FieldNameValueError:
            return ("Invalid name value.", False)
        except FieldEmailValueError:
            return ("Invalid email value.", False)
