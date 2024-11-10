from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldAddressValueError
from messages import Messages


class CommandEditAddress(UserCommand):
    def __init__(self):
        self.name = "edit-address"
        self.description = "Edit the contact's address."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "address", "help": Messages.HELP_FIELD_ADDRESS.value, "type": str},
        ]

    def execute(self, args, book):
        name = args.name
        new_address = args.address

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.edit_address(new_address)
                msg = "Address updated."
                complete = False
                return (msg, complete)
        except FieldAddressValueError as e:
            return (f"Invalid address value. {e}", False)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
