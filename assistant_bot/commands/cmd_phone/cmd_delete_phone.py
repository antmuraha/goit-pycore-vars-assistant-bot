from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from address_book import AddressBook
from messages import Messages


class CommandDeletePhone(UserCommand):
    def __init__(self):
        self.name = "delete-phone"
        self.description = "Delete the phone."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "phone", "help": Messages.HELP_FIELD_PHONE.value, "type": int},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name
        phone = args.phone

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                removed = exist_record.remove_phone(phone)
                if removed:
                    msg = "Phone deleted."
                    complete = False
                    return (msg, complete)
                
                msg = "Phone doesn't exist."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return(f"Invalid name value. {e}", False)
        except FieldPhoneValueError as e:
            return(f"Invalid phone value. {e}", False)