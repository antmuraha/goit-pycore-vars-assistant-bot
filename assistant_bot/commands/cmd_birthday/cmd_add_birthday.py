from address_book import AddressBook
from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldBirthdayValueError


class CommandAddBirthday(UserCommand):
    def __init__(self):
        self.name = "add-birthday"
        self.description = "The add birthday."
        self.pattern = "add-birthday [username] [birthday]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a birthday."
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]
        birthday = args[1]

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                exist_record.add_birthday(birthday)
                msg = "Birthday added."
                complete = False
                return (msg, complete)

            msg = "Contact with this name does not exist yet."
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value", False)
        except FieldBirthdayValueError as e:
            return (f"Invalid birthday value. {e}", False)
