from ..user_command import UserCommand
from address_book import AddressBook
from print_table import PrintTable


class CommandFindByPhone(UserCommand):
    def __init__(self):
        self.name = "find-by-phone"
        self.description = "Find a contact by the entered phone."
        self.pattern = "find-by-phone [phone]"

    def input_validation(self, params):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
        

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args)
        if error:
            return error

        phone = args[0]

        found_contacts = []

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

