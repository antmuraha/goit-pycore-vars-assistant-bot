from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError


class CommandDeleteContact(UserCommand):
    def __init__(self):
        self.name = "delete-contact"
        self.description = "The delete contact."
        self.pattern = "delete-contact [username]" 

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name = args

        try:
            exist_record = book.get(name)
            if exist_record:
                # Check realisation of AddressBook method: remove_record_by_name()
                exist_record.remove_record_by_name(name)
                msg = "Contact removed."
                complete = False
                return (msg, complete)
          
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
        