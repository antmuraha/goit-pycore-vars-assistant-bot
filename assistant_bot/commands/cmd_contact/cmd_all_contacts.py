from ..user_command import UserCommand
from ...record_contact import RecordContact
from ...fields import FieldNameValueError, FieldPhoneValueError


class CommandAllContacts(UserCommand):
    def __init__(self):
        self.name = "all-contacts"
        self.description = "The all contacts."
        self.pattern = "all-contacts"

    def execute(self, args, book):
        msg = f"All book: {book}"
        complete = False
        return (msg, complete)

 