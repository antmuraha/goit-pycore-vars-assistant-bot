from .user_command import UserCommand
from notes_book import NotesBook
from address_book import AddressBook
from print_table import PrintTable


class CommandBookInfo(UserCommand):
    def __init__(self):
        self.name = "book-info"
        self.description = "General information about books"
        self.args = []

    def execute(self, args, books: list[AddressBook, NotesBook]):
        headers = ["Book", "Description", "Records"]
        rows = []
        rows.append(["Addresses book", "A book for managing contacts", len(books[0])])
        rows.append(["Notes book", "A book for managing notes", len(books[1])])
        table = PrintTable(headers=headers, rows=rows)
        return (table, False)
