import sys
import re
import copy
import shlex
import argparse
from commands import UserCommand
from print_table import PrintTable


def get_parser(cmd: UserCommand):
    parser = argparse.ArgumentParser(
        prog=f"{cmd.name}",
        description=cmd.description,
        add_help=False
    )

    for arg in cmd.args:
        arg_copy = copy.copy(arg)
        arg_copy.pop("name")
        parser.add_argument(arg.get("name"), **arg_copy)

    return parser


def get_help_first_line(parser: argparse.ArgumentParser):
    full_usage = parser.format_usage()
    first_line = full_usage.splitlines()[0]
    first_line = re.sub(r"^usage:\s", "", first_line)
    return first_line


def parse_input(user_input: str, cmd: UserCommand, book) -> tuple[str | PrintTable, bool]:
    parser = get_parser(cmd)
    first_line = get_help_first_line(parser)

    if f"{user_input.strip()} -h" == cmd.name or f"{user_input.strip()} --help" == cmd.name:
        parser.print_help()

    try:
        arguments = shlex.split(user_input)
        args = parser.parse_args(arguments[1:])
        msg, complete = cmd.execute(args, book)
        return (msg, complete)
    except SystemExit:
        pass

    msg = ""
    complete = False
    return (msg, complete)
