from ..user_command import UserCommand
from fields import FieldTitleValueError, FieldTextValueError, FieldKeywordValueError
from notes_book import NotesBook
from extract_keywords import extract_keywords
from print_table import PrintTable
from messages import Messages


class CommandNoteExtractKeywords(UserCommand):
    def __init__(self):
        self.name = "note-extract-keywords"
        self.description = "Extract note keywords using NTLK (Natural Language Toolkit)"
        self.args = [
             {"name": "title", "help": Messages.HELP_FIELD_TITLE.value, "type": str},
             {"name": "--write", "help": Messages.HELP_FIELD_NOTE_KEYWORDS.value, "type": str, "default": False, "nargs": "?"},
        ]


    def execute(self, args, book: NotesBook):
        title = args.title
        write_keywords = args.write

        try:
            exist_record = book.get(title)
            if exist_record:
                keywords = extract_keywords(exist_record.text.value)

                if write_keywords:
                    keywords = list(map(lambda w: w[1], keywords))
                    exist_record.set_keywords(keywords)
                    msg = "Keywords for notation recorded"
                    complete = False
                    return (msg, complete)

                headers = ["Rank", "Keyword"]
                rows = []
                for item in keywords:
                    rows.append([
                        f"{round(item[0], 1)}",
                        f"{item[1]}",
                    ])
                table = PrintTable(headers=headers, rows=rows)
                complete = False
                return (table, complete)

            msg = "Note not exist."
            complete = False
            return (msg, complete)

        except FieldTitleValueError as e:
            return (f"Invalid title value. {e}", False)
        except FieldTextValueError as e:
            return (f"Invalid text value. {e}", False)
        except FieldKeywordValueError as e:
            return (f"Invalid keyword value. {e}", False)
