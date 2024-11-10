from ..user_command import UserCommand
from address_book import AddressBook
from print_table import PrintTable
from fields import FieldPhoneValueError
from messages import Messages


class CommandFindByPhone(UserCommand):
    def __init__(self):
        self.name = "find-by-phone"
        self.description = "Find a contact by the entered phone number."
        self.args = [
            {"name": "phone", "help": Messages.HELP_FIELD_PHONE.value, "type": str},
        ]   

    def execute(self, args, book: AddressBook):
        phone = args.phone

        found_contacts = []

        try:
            for name, contact in book.items():
                if any(ph.value == phone for ph in contact.phones):
                    found_contacts.append(contact)

            if found_contacts:
                for contact in found_contacts:
                    headers=["Name", "Phone", "Email", "Address", "Birthday"]
                    rows = [[
                        f"{contact.name}",
                        ", ".join(contact.show_phones()),
                        f"{contact.email}",
                        f"{contact.address}",
                        f"{contact.birthday}"
                        ]]
                    table = PrintTable(headers = headers, rows = rows)
                    table.show()
                
                return (None, False)

            msg = "No contacts found matching the provided phone number."
            complete = False
            return (msg, complete)

        except FieldPhoneValueError as e:
            return (f"Invalid email value. {e}", False)