from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError
from address_book import AddressBook


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

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name, phone = args

        exist_record = book.find_by_name(name)
        if exist_record:
            removed = exist_record.remove_phone(phone)
            if removed:
                msg = "Phone removed."
                complete = False
                return (msg, complete)
            
            msg = "Phone not exist."
            complete = False
            return (msg, complete)
        
        msg = "Contact not exist"
        complete = False
        return (msg, complete)