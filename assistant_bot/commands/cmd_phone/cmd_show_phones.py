from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError
from address_book import AddressBook
from messages import Messages


class CommandShowPhones(UserCommand):
    def __init__(self):
        self.name = "show-phones"
        self.description = "Display all phones."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name

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
