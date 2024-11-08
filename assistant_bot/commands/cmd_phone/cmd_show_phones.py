from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError
from address_book import AddressBook


class CommandShowPhones(UserCommand):
    def __init__(self):
        self.name = "show-phones"
        self.description = "Display all phones."
        self.pattern = "show-phones [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name, = args

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                phones = exist_record.show_phones()
                msg = ", ".join(phones)
                complete = False
                return (msg, complete)

            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
