from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError
# TODO Validation in class fields.field_address ->  import FieldAddressValueError


class CommandEditAddress(UserCommand):
    def __init__(self):
        self.name = "edit-address"
        self.description = "The address contact."
        # TODO check edit_address() pattern
        self.pattern = "edit [username] [new_address]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a new_address."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, new_address = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.edit_address(new_address)

            msg = "Address changed."
            complete = False
            return (msg, complete)
        # except FieldAddressValueError as e:
        #     return (f"Invalid address value", False)
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
