from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError


class CommandAddPhone(UserCommand):
    def __init__(self):
        self.name = "add-phone"
        self.description = "The add phone."
        self.pattern = "add-phone [username] [phone]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a phone."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, phone = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_phone(phone)
                msg = "Phone added."
                complete = False
                return (msg, complete)
            
            msg = 'Contact not exist'
            complete = False
            return (msg, complete)

        except FieldPhoneValueError as e:
            return (f"Invalid phone value", False)

