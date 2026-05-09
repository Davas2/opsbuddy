import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich.syntax import Syntax
from rich import box
from opsbuddy.i18n import t, learn_registry

console = Console()


def _list_all(registry: dict, categories: list[str]) -> None:
    console.print()
    console.print(Panel(
        f"[bold]{t('learn.title')}[/bold]\n[dim]{t('learn.subtitle')}[/dim]",
        border_style="cyan",
        padding=(0, 2),
    ))

    for category in categories:
        cmds = {k: v for k, v in registry.items() if v["category"] == category}
        if not cmds:
            continue

        console.print()
        console.print(Rule(f"[bold cyan]{category}[/bold cyan]", style="cyan"))

        table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
        table.add_column(style="bold green", min_width=18)
        table.add_column(style="dim")

        for name, entry in cmds.items():
            first_sentence = entry["description"].split(".")[0] + "."
            table.add_row(name, first_sentence)

        console.print(table)

    console.print()


def run(command: str | None) -> None:
    registry, categories = learn_registry()

    if not command:
        _list_all(registry, categories)
        return

    key = command.lower().strip()

    if key not in registry:
        available = ", ".join(f"[cyan]{k}[/cyan]" for k in registry)
        console.print(
            f"\n[red]{t('learn.not_found', cmd=command)}[/red]\n"
            f"{t('learn.available')}: {available}\n"
        )
        raise typer.Exit(1)

    entry = registry[key]

    console.print()
    console.print(Panel(
        f"[bold]{entry['description']}[/bold]",
        title=f"[bold cyan]{key}[/bold cyan]  [dim]— {entry['category']}[/dim]",
        border_style="cyan",
        padding=(0, 2),
    ))

    if entry["flags"]:
        console.print()
        console.print(Rule(f"[bold]{t('learn.flags')}[/bold]", style="dim"))
        table = Table(box=box.SIMPLE, show_header=True, header_style="bold", padding=(0, 2))
        table.add_column("Flag", style="bold yellow", min_width=18)
        table.add_column("Descrição" if t("learn.flags") == "Flags principais" else "Description")
        for flag, desc in entry["flags"]:
            table.add_row(flag, desc)
        console.print(table)

    if entry["examples"]:
        console.print()
        console.print(Rule(f"[bold]{t('learn.examples')}[/bold]", style="dim"))
        for cmd, desc in entry["examples"]:
            console.print(f"  [dim]{desc}[/dim]")
            console.print(Syntax(f"  $ {cmd}", "bash", theme="monokai", background_color="default"))
            console.print()
