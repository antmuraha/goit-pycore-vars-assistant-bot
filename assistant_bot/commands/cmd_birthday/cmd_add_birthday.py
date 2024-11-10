from address_book import AddressBook
from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldBirthdayValueError
from messages import Messages


class CommandAddBirthday(UserCommand):
    def __init__(self):
        self.name = "add-birthday"
        self.description = "Add a birthday to the contact."
        self.args = [
            {"name": "name", "help": Messages.HELP_FIELD_NAME.value, "type": str},
            {"name": "birthday", "help": Messages.HELP_FIELD_BIRTHDAY.value, "type": str},
        ]

    def execute(self, args, book: AddressBook):
        name = args.name
        birthday = args.birthday

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                exist_record.add_birthday(birthday)
                msg = "Birthday added."
                complete = False
                return (msg, complete)

            msg = "A contact with this name doesn't exist yet."
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value. {e}", False)
        except FieldBirthdayValueError as e:
            return (f"Invalid birthday value. {e}", False)
