from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from address_book import AddressBook
from messages import Messages


class CommandEditPhone(UserCommand):
    def __init__(self):
        self.name = "edit-phone"
        self.description = "Edit the phone."
        self.pattern = "edit-phone [username] [phone] [new_phone]"
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "phone", "help": Messages.HELP_FIELD_PHONE.value, "type": int},
            {"name": "new_phone", "help": Messages.HELP_FIELD_NEW_PHONE.value, "type": int},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name
        phone = args.phone
        new_phone = args.new_phone

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                result = exist_record.edit_phone(phone, new_phone)
                if result:
                    msg = "Phone changed."
                    complete = False
                    return (msg, complete)
                
                msg = "The phone doesn't exist."
                complete = False
                return (msg, complete)
            
            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldPhoneValueError as e:
            return (f"Invalid phone value. {e}", False)
