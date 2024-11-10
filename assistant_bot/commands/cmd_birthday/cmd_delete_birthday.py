from address_book import AddressBook
from ..user_command import UserCommand
from fields import FieldNameValueError
from messages import Messages


class CommandDeleteBirthday(UserCommand):
    def __init__(self):
        self.name = "delete-birthday"
        self.description = "Delete the contact's birthday."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
        ]


    def execute(self, args, book: AddressBook):
        name = args.name

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                value = exist_record.show_birthday()
                if value:
                    exist_record.delete_birthday()
                    return (f"Birthday deleted.", False)

                msg = "You haven't added a birthday yet."
                complete = False
                return (msg, complete)

            msg = "Contact doesn't exist."
            complete = False
            return (msg, complete)
        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
