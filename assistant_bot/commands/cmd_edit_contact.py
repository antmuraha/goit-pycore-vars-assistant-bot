from .user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError


class CommandEditContact(UserCommand):
    def __init__(self):
        self.name = "edit-contact"
        self.description = "The edit contact."
        self.pattern = "edit [username] [new_username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a new_username."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, new_username = args

        try:
            exist_record = book.get(name)
            if exist_record:
                # TODO No relative method neither in AddressBook nor RecordContact
                exist_record.edit_contact(new_username)

            msg = "Contact changed."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
