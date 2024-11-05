from .user_command import UserCommand


class CommandHello(UserCommand):
    def __init__(self):
        self.name = "hello"
        self.description = ""
        self.pattern = "hello"

    def execute(self, args, book):
        msg = "How can I help you?"
        complete = False
        return (msg, complete)
