from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError


class CommandAddContact(UserCommand):
    def __init__(self):
        self.name = "add-contact"
        self.description = "The add contact."
        self.pattern = "add-contact [username] [phone]"

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

        name = args[0]
        phone = args[1]
        
        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_phone(phone)
            else:
                record = RecordContact(name)
                record.add_phone(phone)
                book[name] = record

            msg = "Contact added."
            complete = False
            return (msg, complete)
        except FieldPhoneValueError as e:
            return (f"Invalid phone value. {e}", False)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
 