from collections import UserDict
from record_note import RecordNote


class NotesBook(UserDict):
    '''
    A class for storing and managing notes.
    '''

    def __init__ (self):
        self.data = {}
    
    def __str__(self):
        if not self.data:
            return "No notes available."
        
        notes = "\n".join([f"Title: {note.title}, Content: {note.text[:30]}..." for note in self.data])
        return f"Notes: \n{notes}"

    def __repr__(self):
        notes = ", ".join([repr(note) for note in self.data.values()])
        return f"NotesBook{{{notes}}}"
    
    def add_record(self, note: RecordNote):
        self.data[note.title.value] = note

    def remove_record(self, title):
        return self.data.pop(title)
 
    def find_by_title(self, title):
        return self.data.get(title)

