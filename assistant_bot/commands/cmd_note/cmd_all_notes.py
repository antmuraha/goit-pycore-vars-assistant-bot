from ..user_command import UserCommand
from notes_book import NotesBook


class CommandAllNotes(UserCommand):
    def __init__(self):
        self.name = "all-notes"
        self.description = "Display all notes for all contacts."
        self.pattern = "all-notes"

    def execute(self, args, book: NotesBook):
        all_notes = list(map(lambda n: f"{n}", book.values()))

        if len(all_notes):
            msg = f"{all_notes}"
        else:
            msg = "No notes found."

        complete = False
        return (msg, complete)
