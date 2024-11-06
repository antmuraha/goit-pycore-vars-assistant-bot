from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError


class CommandDeletePhone(UserCommand):
    def __init__(self):
        self.name = "delete-phone"
        self.description = "The delete phone."
        self.pattern = "delete-phone [username] [phone]" 

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
                exist_record.remove_phone(phone)
                msg = "Phone removed."
                complete = False
                return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value", False)