from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldAddressValueError
from messages import Messages


class CommandAddAddress(UserCommand):
    def __init__(self):
        self.name = "add-address"
        self.description = "Add an address to the contact."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "address", "help": Messages.HELP_FIELD_ADDRESS.value, "type": str},
        ]

    def execute(self, args, book):
        name = args.name
        address = args.address
        
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
