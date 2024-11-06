from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError


class CommandGetUpcomingBirthdays(UserCommand):
    def __init__(self):
        self.name = "upcoming-birthdays"
        self.description = "The upcoming birthdays."
        self.pattern = "upcoming-birthdays [number]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        number = args

        try:
            result = book.get_upcoming_birthdays(number)
            if result:
                return (result, False)

            msg = f"There are no birthdays in {number} days."
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"Invalid name value", False)
