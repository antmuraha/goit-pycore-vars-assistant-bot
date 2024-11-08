from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from address_book import AddressBook


class CommandDeletePhone(UserCommand):
    def __init__(self):
        self.name = "delete-phone"
        self.description = "Delete the phone."
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

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name, phone = args

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                removed = exist_record.remove_phone(phone)
                if removed:
                    msg = "Phone deleted."
                    complete = False
                    return (msg, complete)
                
                msg = "Phone doesn't exist."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return(f"Invalid name value. {e}", False)
        except FieldPhoneValueError as e:
            return(f"Invalid phone value. {e}", False)