from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError, FieldPhoneValueError


class CommandEditPhone(UserCommand):
    def __init__(self):
        self.name = "edit-phone"
        self.description = "The edit phone."
        self.pattern = "edit [username] [phone] [new_phone]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a phone."
            complete = False
            return (msg, complete)
        
        if len(params) == 2:
            msg = "Please enter a new_phone."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, phone, new_phone = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.edit_phone(phone, new_phone)
                msg = "Phone changed."
                complete = False
                return (msg, complete)

        except FieldPhoneValueError as e:
            return (f"Invalid phone value", False)
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
