from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldAddressValueError


class CommandDeleteAddress(UserCommand):
    def __init__(self):
        self.name = "delete-address"
        self.description = "Delete an address from the contact."
        self.pattern = "delete-address [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)


    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.remove_address()
                msg = "Address deleted."
                complete = False
                return (msg, complete)
            
        except FieldAddressValueError as e:
            return (f"Invalid address value. {e}", False)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)