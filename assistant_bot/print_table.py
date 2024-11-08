from rich.console import Console
from rich.table import Table


class PrintTable():
    def __init__(self, headers: list[str], rows: list[list[str]]):
        self.headers = headers
        self.rows = rows

    def show(self):
        table = Table()
        for header in self.headers:
            table.add_column(header, style="magenta")
        for idx, row in enumerate(self.rows):
            table.add_row(*list(map(lambda x: x.replace('None', ''), row)))
            if idx != len(self.rows) - 1:
                table.add_row(*list(map(lambda x: "", row)))
        console = Console()
        console.print(table)
        