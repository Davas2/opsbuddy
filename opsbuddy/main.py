import os
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from opsbuddy import __version__
from opsbuddy.i18n import t

app = typer.Typer(invoke_without_command=True, add_completion=False)
console = Console()


@app.callback()
def default(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is not None:
        return

    username = os.environ.get("USER") or os.environ.get("USERNAME") or "user"

    commands_table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    commands_table.add_column(style="bold green")
    commands_table.add_column(style="dim")

    commands_table.add_row("opsbuddy overview",   t("cmd.overview"))
    commands_table.add_row("opsbuddy processes",  t("cmd.processes"))
    commands_table.add_row("opsbuddy disk",       t("cmd.disk"))
    commands_table.add_row("opsbuddy network",    t("cmd.network"))
    commands_table.add_row("opsbuddy docker",     t("cmd.docker"))
    commands_table.add_row("opsbuddy diagnose",   t("cmd.diagnose"))
    commands_table.add_row("opsbuddy explain",    t("cmd.explain"))
    commands_table.add_row("opsbuddy learn",      t("cmd.learn"))
    commands_table.add_row("opsbuddy language",   t("cmd.language"))

    greeting = (
        f"[bold]{t('welcome.greeting', username=username, version=__version__)}[/bold]\n\n"
        f"{t('welcome.subtitle')}\n"
    )

    console.print(Panel(greeting, border_style="cyan", padding=(1, 2)))
    console.print(f"[bold cyan]{t('welcome.commands_title')}[/bold cyan]")
    console.print(commands_table)
    console.print(f"[dim]{t('welcome.tip')}[/dim]\n")


@app.command()
def overview() -> None:
    """Show system status: memory, disk and Docker containers."""
    from opsbuddy.commands.overview import run
    run()


@app.command()
def processes() -> None:
    """List top 15 processes by CPU usage."""
    from opsbuddy.commands.processes import run
    run()


@app.command()
def disk() -> None:
    """Show disk usage by partition and largest directories."""
    from opsbuddy.commands.disk import run
    run()


@app.command()
def network() -> None:
    """Show network interfaces, listening ports and connectivity."""
    from opsbuddy.commands.network import run
    run()


@app.command()
def docker() -> None:
    """Docker containers panel: status, CPU and memory."""
    from opsbuddy.commands.docker import run
    run()


@app.command()
def diagnose() -> None:
    """Server health diagnostics with OK/Warning/Critical status."""
    from opsbuddy.commands.diagnose import run
    run()


@app.command()
def explain(command: str = typer.Argument(..., help="Command name to explain (e.g. overview, disk, docker)")) -> None:
    """Explain the Linux commands behind each OpsBuddy feature."""
    from opsbuddy.commands.explain import run
    run(command)


@app.command()
def learn(command: str = typer.Argument(None, help="Linux command to learn (e.g. grep, ssh, docker). No argument lists all.")) -> None:
    """Linux command reference guide with descriptions, flags and examples."""
    from opsbuddy.commands.learn import run
    run(command)


@app.command()
def language() -> None:
    """Select the OpsBuddy language / Selecionar o idioma do OpsBuddy."""
    from opsbuddy.commands.language import run
    run()
