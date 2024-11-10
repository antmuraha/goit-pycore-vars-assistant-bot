from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError
from messages import Messages
from print_table import PrintTable


class CommandGetUpcomingBirthdays(UserCommand):
    def __init__(self):
        self.name = "upcoming-birthdays"
        self.description = "Show upcoming birthdays."
        self.args = [
            {"name": "days", "help": Messages.HELP_FIELD_BIRTHDAY_DAYS.value, "type": int, "default": 7, "nargs": "?"},
        ]

    def execute(self, args, book):
        days = args.days
        result = book.show_upcoming_birthday(days)

        if result:
            headers = ["Name", "Congratulation date"]
            rows = []
            for contact in result:
                rows.append([f"{contact['name']}",
                    f"{contact['congratulation_date']}"
                    ])
            table = PrintTable(headers = headers, rows = rows)
            complete = False
            return (table, complete)

        msg = f"There are no birthdays in {days} days."
        complete = False
        return (msg, complete)

