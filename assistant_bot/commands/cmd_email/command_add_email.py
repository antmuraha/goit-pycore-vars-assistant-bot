from ..user_command import UserCommand
from record_contact import RecordContact

class CommandAddEmail(UserCommand):
    def __init__(self):
        self.name = "add-email"
        self.description = "The add the email to the contact."
        self.pattern = "add-email [username] [email]"

    def input_validation(self, params, book):
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

        name, email = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_email(email)
            else:
                record = RecordContact(name)
                record.add_email(email)
                book[name] = record

            msg = "Note added to the contact."
            complete = False
            return (msg, complete)
        except FieldNameValueError:
            return ("Invalid name value.", False)
