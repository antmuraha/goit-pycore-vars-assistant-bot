import pickle
from address_book import AddressBook
from notes_book import NotesBook
from constants import default_filename


def save_data(book, filename=default_filename):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=default_filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Return a new address book if the file is not found
        return (AddressBook(), NotesBook())
