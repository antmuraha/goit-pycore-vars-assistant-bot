from ..user_command import UserCommand
from ..record_contact import RecordContact
from ...fields import FieldNameValueError
# TODO Validation in class fields.field_address ->  import FieldAddressValueError


class CommandAddAddress(UserCommand):
    def __init__(self):
        self.name = "add-address"
        self.description = "The add address."
        self.pattern = "add [username] [address]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a address."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, address = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_address(address)

            msg = "Address added."
            complete = False
            return (msg, complete)
        # except FieldAddressValueError as e:
        #     return (f"Invalid address value", False)
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
