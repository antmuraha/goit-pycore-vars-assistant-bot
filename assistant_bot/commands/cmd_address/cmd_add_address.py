from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldAddressValueError


class CommandAddAddress(UserCommand):
    def __init__(self):
        self.name = "add-address"
        self.description = "Add an address to the contact."
        self.pattern = "add-address [username] [address]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter an address."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]
        address = " ".join(args[1:])
        
        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_address(address)
                msg = "Address added to the contact."
            else: 
                msg = "Please create the contact before adding an address."
            
            complete = False
            return (msg, complete)
        except FieldAddressValueError as e:
            return (f"Invalid address value. {e}", False)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
