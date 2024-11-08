from ..user_command import UserCommand
from address_book import AddressBook
from print_table import PrintTable
from fields import FieldEmailValueError

class CommandFindByEmail(UserCommand):
    def __init__(self):
        self.name = "find-by-email"
        self.description = "Find a contact by the entered email address."
        self.pattern = "find-by-email [email]"

    def input_validation(self, params):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)
        

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args)
        if error:
            return error

        email = args[0]

        found_contacts = []

        try:
            for name, contact in book.items():
                if (contact.email.value == email):
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

            msg = "No contacts found matching the provided email."
            complete = False
            return (msg, complete)
        
        except FieldEmailValueError as e:
            return (f"Invalid email value. {e}", False)

