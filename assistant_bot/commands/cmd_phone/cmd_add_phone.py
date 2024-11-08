from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from address_book import AddressBook


class CommandAddPhone(UserCommand):
    def __init__(self):
        self.name = "add-phone"
        self.description = "Add a phone to the contact."
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

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name, phone = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_phone(phone)
                msg = "Phone added."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldPhoneValueError as e:
            return (f"Invalid phone value. {e}", False)

