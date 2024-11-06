from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError


class CommandShowBirthday(UserCommand):
    def __init__(self):
        self.name = "show-birthday"
        self.description = "The show birthday."
        self.pattern = "show-birthday [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        name = args

        try:
            exist_record = book.get(name)
            # TODO implement a show_birthday() method in RecordContact class
            if exist_record:
                exist_record.show_birthday(name)
                return(exist_record.birthday, False)

            msg = "Contact not exist"
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value", False)

