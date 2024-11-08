from ..user_command import UserCommand
from address_book import AddressBook
from fields import FieldNameValueError


class CommandDeleteContact(UserCommand):
    def __init__(self):
        self.name = "delete-contact"
        self.description = "Delete the contact from the address book."
        self.pattern = "delete-contact [username]" 

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]
        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                del book[name]
                msg = "Contact removed."
                complete = False
                return (msg, complete)
            
            msg = "Contact not exist."
            complete = False
            return (msg, complete)
        
        except FieldNameValueError as e:
            return(f" Invalid name value. {e}", False)
