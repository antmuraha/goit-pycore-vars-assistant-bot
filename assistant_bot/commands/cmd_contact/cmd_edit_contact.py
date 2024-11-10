from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldName, FieldNameValueError
from address_book import AddressBook
from messages import Messages


class CommandEditContact(UserCommand):
    def __init__(self):
        self.name = "edit-contact"
        self.description = "Edit the contact's name."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "new_name", "help": Messages.HELP_FIELD_NEW_NAME.value, "type": str},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name
        new_name = args.new_name

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                renamed = exist_record.rename(new_name)
                if renamed:
                    book[new_name] = book[name]
                    del book[name]
                    msg = "Contact renamed."
                    complete = False
                    return (msg, complete)

            msg = "Contact does't exist."
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
