from rich.console import Console
from rich.table import Table


class PrintTable():
    def __init__(self, headers: list[str], rows: list[list[str]], without_empty_rows = False):
        self.headers = headers
        self.rows = rows
        self.without_empty_rows = without_empty_rows

    def show(self):
        table = Table()
        for header in self.headers:
            table.add_column(header, style="magenta")
        for idx, row in enumerate(self.rows):
            table.add_row(*list(map(lambda x: x.replace('None', '').replace('[', '\['), row)))
            if not self.without_empty_rows and idx != len(self.rows) - 1:
                table.add_row(*list(map(lambda x: "", row)))
        console = Console()
        console.print(table)
        