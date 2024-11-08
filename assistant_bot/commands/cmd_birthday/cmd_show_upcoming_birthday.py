from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError


class CommandGetUpcomingBirthdays(UserCommand):
    def __init__(self):
        self.name = "upcoming-birthdays"
        self.description = "Show upcoming birthdays."
        self.pattern = "upcoming-birthdays [number]"

    def input_validation(self, params):
        pass
        # if len(params) == 0:
        #     msg = self.get_enter_command_message()
        #     complete = False
        #     return (msg, complete)

    def execute(self, args, book):
        error = self.input_validation(args)
        if error:
            return error

        number = args[0] or 7

        result = book.show_upcoming_birthday(number)
  
        if result:
            return (result, False)

        msg = f"There are no birthdays in {number} days."
        complete = False
        return (msg, complete)

