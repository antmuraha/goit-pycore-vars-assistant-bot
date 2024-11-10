from ..user_command import UserCommand
from address_book import AddressBook
from print_table import PrintTable
from fields import FieldPhoneValueError
from messages import Messages


class CommandFindByAddress(UserCommand):
    def __init__(self):
        self.name = "find-by-address"
        self.description = "Find a contact by the entered address."
        self.args = [
            {"name": "address", "help": Messages.HELP_FIELD_ADDRESS.value, "type": str},
        ]   

    def execute(self, args, book: AddressBook):
        address = args.address

        found_contacts = []
        for name, contact in book.items():
            if contact.address is not None and address in str(contact.address):
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

        msg = "No contacts found matching the provided address."
        complete = False
        return (msg, complete)
