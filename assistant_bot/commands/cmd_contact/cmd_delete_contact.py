from ..user_command import UserCommand
from address_book import AddressBook
from fields import FieldNameValueError
from messages import Messages


class CommandDeleteContact(UserCommand):
    def __init__(self):
        self.name = "delete-contact"
        self.description = "Delete the contact from the address book."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name
        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                del book[name]
                msg = "Contact removed."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        
        except FieldNameValueError as e:
            return(f" Invalid name value. {e}", False)
