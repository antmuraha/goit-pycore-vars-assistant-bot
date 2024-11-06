from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError, FieldPhoneValueError


class CommandAddContact(UserCommand):
    def __init__(self):
        self.name = "show-contact"
        self.description = "The show contact."
        self.pattern = "show [username]"

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
                #TODO implement method show_contact() 
                exist_record.show_contact(name)

            # TODO decide what to write in a msg 
            # No message is needed, but for consistency with the signature.
            msg = " "
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value", False)
