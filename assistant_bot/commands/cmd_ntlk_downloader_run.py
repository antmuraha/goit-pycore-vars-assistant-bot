from .user_command import UserCommand
from extract_keywords import run_nltk_downloader


class CommandNltkDownloaderRun(UserCommand):
    def __init__(self):
        self.name = "nltk-downloader-run"
        self.description = "The NLTK corpus and module downloader.\nThis module defines several interfaces which can be used to download corpora, models, and other data packages that can be used with NLTK."
        self.args = []

    def execute(self, args, book):

        try:
            run_nltk_downloader()
        except Exception as e:
            print(f"{e}")

        return ("", False)
