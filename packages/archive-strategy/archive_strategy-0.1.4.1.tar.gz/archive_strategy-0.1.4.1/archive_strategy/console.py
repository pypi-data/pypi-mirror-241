"""Console logger for the archiver."""
from rich.console import Console
from rich.theme import Theme

archiver_theme = Theme({"info": "dim cyan", "warning": "orange1", "danger": "bold red"})
logger = Console(theme=archiver_theme, width=250)
