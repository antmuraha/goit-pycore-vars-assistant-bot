from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from messages import Messages


class CommandAddContact(UserCommand):
    def __init__(self):
        self.name = "add-contact"
        self.description = "Add the contact to the address book."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "phone", "help": Messages.HELP_FIELD_PHONE.value, "type": int},
        ]

    def execute(self, args, book):
        name = args.name
        phone = args.phone

        try:
            exist_record = book.get(name)
            if exist_record:
                msg = "Contact is exist."
                complete = False
                return (msg, complete)
            else:
                record = RecordContact(name)
                record.add_phone(phone)
                book[name] = record

            msg = "Contact added."
            complete = False
            return (msg, complete)
        except FieldPhoneValueError as e:
            return (f"Invalid phone value. {e}", False)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
