from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from address_book import AddressBook
from messages import Messages


class CommandAddPhone(UserCommand):
    def __init__(self):
        self.name = "add-phone"
        self.description = "Add a phone to the contact."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "phone", "help": Messages.HELP_FIELD_PHONE.value, "type": int},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name
        phone = args.phone

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_phone(phone)
                msg = "Phone added."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldPhoneValueError as e:
            return (f"Invalid phone value. {e}", False)

