from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError


class CommandShowContact(UserCommand):
    def __init__(self):
        self.name = "show-contact"
        self.description = "The show contact."
        self.pattern = "show-contact [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name = args

        exist_record = book.get(name)
        if exist_record:
            return (f'{exist_record}', False)

        msg = "Contact not exist"
        complete = False
        return (msg, complete)

