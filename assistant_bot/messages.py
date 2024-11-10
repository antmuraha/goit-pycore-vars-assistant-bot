from enum import Enum


class Messages(Enum):
    HELP_FIELD_NAME = "The username of the contact"
    HELP_FIELD_NEW_NAME = "The new username of the contact"
    HELP_FIELD_PHONE = "The phone number of the contact"
    HELP_FIELD_NEW_PHONE = "The new phone number of the contact"
    HELP_FIELD_EMAIL = "The email of the contact"
    HELP_FIELD_NEW_EMAIL = "The new email of the contact"
    HELP_FIELD_ADDRESS  = "The address of the contact"
    HELP_FIELD_BIRTHDAY = "The birthday of the contact"
    HELP_FIELD_BIRTHDAY_DAYS = "future birthdays for N=7 days"

    HELP_FIELD_TITLE = "The title of the note"
    HELP_FIELD_NOTE_KEYWORDS = "Write key words in the book"
