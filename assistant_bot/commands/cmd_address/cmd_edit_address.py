from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldAddressValueError


class CommandEditAddress(UserCommand):
    def __init__(self):
        self.name = "edit-address"
        self.description = "The edit address."
        # TODO check edit_address() pattern
        self.pattern = "edit-address [username] [new_address]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a new address."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args, book)
        if error:
            return error

        name, new_address = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.edit_address(new_address)
                msg = "Address successfully changed."
                complete = False
                return (msg, complete)
        except FieldAddressValueError as e:
            return (f"Invalid address value", False)
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
