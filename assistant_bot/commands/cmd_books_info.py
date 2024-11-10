from .user_command import UserCommand
from ..print_table import PrintTable


class CommandBooksInfo(UserCommand):
    def __init__(self):
        self.name = "books-info"
        self.description = "Show information and the number of records in both the address book and the notes book."
        self.pattern = "books-info"

    def execute(self, addressbook, notesbook):
        
        headers = ["Book", "Number of records", "Description"]
        rows = []
      
        rows.append(["Address book",
            f"{len(addressbook.data)}",
            "Contains all contact information stored in the address book.",
            f"Notes book",
            f"{len(notesbook.data)}",
            "Contains all notes and memos stored in the notes book"
            ])
        table = PrintTable(headers = headers, rows = rows)
        complete = False
        return (table, complete)
    

 