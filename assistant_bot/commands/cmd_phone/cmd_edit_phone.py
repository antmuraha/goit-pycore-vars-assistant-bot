from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from address_book import AddressBook


class CommandEditPhone(UserCommand):
    def __init__(self):
        self.name = "edit-phone"
        self.description = "Edit the phone."
        self.pattern = "edit-phone [username] [phone] [new_phone]"

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
            msg = "Please enter a new phone."
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name, phone, new_phone = args

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                result = exist_record.edit_phone(phone, new_phone)
                if result:
                    msg = "Phone changed."
                    complete = False
                    return (msg, complete)
                
                msg = "The phone doesn't exist."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldPhoneValueError as e:
            return (f"Invalid phone value. {e}", False)
