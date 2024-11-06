from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError


class CommandAddBirthday(UserCommand):
    def __init__(self):
        self.name = "add-birthday"
        self.description = "The add birthday."
        self.pattern = "add [username] [birthday]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a birthday."
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name, birthday = args

        try:
            exist_record = book.get(name)
            if exist_record:
                exist_record.add_birthday(birthday)

            msg = "Birthday added."
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value", False)
