from ..user_command import UserCommand
from address_book import AddressBook
from print_table import PrintTable


class CommandShowContact(UserCommand):
    def __init__(self):
        self.name = "show-contact"
        self.description = "The show contact."
        self.pattern = "show-contact [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]

        exist_record = book.find_by_name(name)
        if exist_record:
            headers=["Name", "Phone", "Email", "Address", "Birthday"]
            rows = [
                f"{exist_record.name}",
                ", ".join(exist_record.show_phones()),
                f"{exist_record.email}",
                f"{exist_record.address}",
                f"{exist_record.birthday}"
                ]
            table = PrintTable(headers = headers, rows = rows)
            return (table, False)

        msg = "Contact not exist"
        complete = False
        return (msg, complete)

