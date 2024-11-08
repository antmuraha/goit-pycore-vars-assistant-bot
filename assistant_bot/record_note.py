from fields import FieldText, FieldKeyword


class RecordNote:
    '''
    A class to store information about a note, including text.
    '''

    def __init__(self, text):
        self.text = FieldText(text)
        self.keywords: list[FieldKeyword] = []

    def __str__(self):
        return f"Note text: {self.text} Keywords:{self.keywords}"

    def __repr__(self):
        return f"RecordNote(text={self.text[:30]!r}, Keywords:{self.keywords})"

    def edit_text(self, new_text):
        self.text = FieldText(new_text)

    def set_keywords(self, keywords: list[str]):
        new_keywords = []
        for word in keywords:
            new_keywords.append(FieldKeyword(word))
        self.keywords = new_keywords
