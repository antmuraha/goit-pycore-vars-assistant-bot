from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldNameValueError, FieldPhoneValueError
from print_table import PrintTable


class CommandAllContacts(UserCommand):
    def __init__(self):
        self.name = "all-contacts"
        self.description = "Show all contacts in the address book."
        self.pattern = "all-contacts"
        self.args = []

    def execute(self, args, book):
        if len(book) == 0:
            msg = "No contacts found."
            complete = False
            return (msg, complete)

        headers = ["Name", "Phone", "Email", "Address", "Birthday"]
        rows = []
        for contact in book.values():
            rows.append([f"{contact.name}",
                ", ".join(contact.show_phones()),
                f"{contact.email}",
                f"{contact.address}",
                f"{contact.birthday}"
                ])
        table = PrintTable(headers = headers, rows = rows)
        complete = False
        return (table, complete)

 