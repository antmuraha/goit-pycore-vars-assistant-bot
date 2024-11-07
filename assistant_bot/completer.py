import os
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
import constants


class MultiStepCompleter(Completer):
    def __init__(self, commands: list[str]):
        self.step = 0  # Track the current step
        self.first_choice = None  # Track the choice made in the first step
        self.commands = commands

    def get_completions(self, document, complete_event):
        text = document.text.strip()
        words = text.split()
        options = [x for x in self.commands if x.startswith(words[0])]

        for key in options:
            yield Completion(key, start_position=-len(text))


def load_history_from_file(history):
    filename = constants.history_file
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                history.append_string(line.strip())


history = InMemoryHistory()
load_history_from_file(history)
session = PromptSession(history=history)


def save_history_to_file():
    filename = constants.history_file
    with open(filename, 'w') as f:
        for item in history.get_strings():
            f.write(item + '\n')


def completer(commands: list[str]):
    # Initialize session and completer
    completer = MultiStepCompleter(commands)

    # Capture input and provide completions
    text = session.prompt("Enter a command: ", completer=completer)
    return text
