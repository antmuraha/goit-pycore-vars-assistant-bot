# from fields import FieldTitle, FieldText

class RecordNote:
    '''
    A class to store information about a note, including title and text.
    '''

    def __init__(self, title, text):
        self.title = title
        self.text = text
        # self.title = FieldTitle(title)
        # self.text = FieldText(text)

    def __str__(self):
        return f"Note Title: {self.title}\nNote Text: {self.text}"

    def __repr__(self):
        return f"RecordNote(title={self.title}, text={self.text})"
    
    
    