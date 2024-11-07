from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from rich.table import Table
from rich.console import Console
from io import StringIO

# Create a Console instance that writes to a StringIO buffer
console_output = StringIO()
console = Console(file=console_output)

# Define your table using rich
table = Table(title="Sample Rich Table")

# Add columns
table.add_column("ID", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Age", justify="center", style="green")

# Add rows
table.add_row("1", "Alice", "23")
table.add_row("2", "Bob", "30")
table.add_row("3", "Charlie", "27")

# Print the table to the console buffer
console.print(table)

# Get the content from the buffer
formatted_table = console_output.getvalue()

print(formatted_table)

# Display the table using prompt_toolkit
# print_formatted_text(FormattedText([(None, formatted_table)]))
