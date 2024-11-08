from ..user_command import UserCommand
from notes_book import NotesBook
from print_table import PrintTable


class CommandAllNotes(UserCommand):
    def __init__(self):
        self.name = "all-notes"
        self.description = "Display all notes."
        self.pattern = "all-notes"

    def execute(self, args, book: NotesBook):
        all_notes = list(map(lambda n: f"{n}", book.values()))

        if len(all_notes):
            headers = ["Title", "Text", "Keywords"]
            rows = []
            for note in book.values():
                rows.append([
                    f"{note.title}",
                    f"{note.text}"[:100] + ("..." if len(note.text.value) > 100 else ""),
                    ", ".join([f"{k}" for k in note.keywords]),
                ])
            table = PrintTable(headers=headers, rows=rows)
            msg = table
        else:
            msg = "No notes found."

        complete = False
        return (msg, complete)
