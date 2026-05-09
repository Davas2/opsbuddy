from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from opsbuddy import config
from opsbuddy.i18n import t

console = Console()

OPTIONS = [
    ("pt", "Português"),
    ("en", "English"),
]


def run() -> None:
    current = config.get("language") or "pt"

    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    table.add_column(style="bold cyan", width=4)
    table.add_column(style="bold", width=4)
    table.add_column()

    for i, (code, label) in enumerate(OPTIONS, 1):
        marker = "[green]✔[/green]" if code == current else " "
        table.add_row(f"[dim]{i}[/dim]", marker, label)

    console.print()
    console.print(Panel(
        table,
        title=f"[bold cyan]{t('language.title')}[/bold cyan]",
        border_style="cyan",
        subtitle=t("language.current", lang=current),
        padding=(0, 1),
    ))

    console.print(f"\n  {t('language.choose')} (1-{len(OPTIONS)}): ", end="")
    try:
        choice = input().strip()
        index = int(choice) - 1
        if not (0 <= index < len(OPTIONS)):
            raise ValueError
    except (ValueError, EOFError):
        console.print("\n  [yellow]Opção inválida. / Invalid option.[/yellow]\n")
        return

    code, label = OPTIONS[index]
    config.set("language", code)
    console.print(f"\n  {t('language.saved', lang=label)}\n")
