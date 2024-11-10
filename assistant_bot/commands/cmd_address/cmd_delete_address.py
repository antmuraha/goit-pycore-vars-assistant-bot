from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldAddressValueError
from messages import Messages


class CommandDeleteAddress(UserCommand):
    def __init__(self):
        self.name = "delete-address"
        self.description = "Delete an address from the contact."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
        ]

    def execute(self, args, book):
        name = args.name

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.remove_address()
                msg = "Address deleted."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
            
        except FieldAddressValueError as e:
            return (f"Invalid address value. {e}", False)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)