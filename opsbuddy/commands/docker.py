import subprocess
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from opsbuddy.i18n import t

console = Console()


def _run(args: list[str]) -> str | None:
    try:
        return subprocess.check_output(
            ["docker"] + args, stderr=subprocess.DEVNULL, text=True
        ).strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def _containers() -> list[dict] | None:
    out = _run(["ps", "-a", "--format", "json"])
    if out is None:
        return None
    rows = []
    for line in out.splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return rows


def _stats() -> dict[str, dict]:
    out = _run(["stats", "--no-stream", "--format", "json"])
    if not out:
        return {}
    result = {}
    for line in out.splitlines():
        try:
            s = json.loads(line)
            result[s.get("ID", "")[:12]] = s
        except json.JSONDecodeError:
            pass
    return result


def run() -> None:
    containers = _containers()

    if containers is None:
        console.print(Panel(
            f"[yellow]{t('docker.not_found')}[/yellow]",
            title=f"[bold cyan]{t('docker.title')}[/bold cyan]",
            border_style="cyan",
        ))
        return

    if not containers:
        console.print(Panel(
            f"[dim]{t('docker.no_containers')}[/dim]",
            title=f"[bold cyan]{t('docker.title')}[/bold cyan]",
            border_style="cyan",
        ))
        return

    stats = _stats()
    running = [c for c in containers if "running" in c.get("State", "").lower()]
    stopped = [c for c in containers if "running" not in c.get("State", "").lower()]

    def _render_group(title: str, items: list[dict], show_stats: bool) -> None:
        if not items:
            return
        console.print(Rule(f"[bold cyan]{title}[/bold cyan]", style="cyan"))
        table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan", expand=True)
        table.add_column(t("docker.col_id"), width=13, style="dim")
        table.add_column(t("docker.col_name"), min_width=18)
        table.add_column(t("docker.col_image"), min_width=18)
        table.add_column(t("docker.col_status"), min_width=10)
        table.add_column(t("docker.col_ports"), min_width=14)
        if show_stats:
            table.add_column(t("docker.col_cpu"), justify="right", width=8)
            table.add_column(t("docker.col_mem"), justify="right", width=10)

        for c in items:
            cid = c.get("ID", "")[:12]
            name = c.get("Names", "?")
            image = c.get("Image", "?")
            state = c.get("State", "?")
            ports = c.get("Ports", "—") or "—"

            if "running" in state.lower():
                state_str = "[green]running[/green]"
            elif "exited" in state.lower():
                state_str = "[red]exited[/red]"
            else:
                state_str = f"[yellow]{state}[/yellow]"

            row = [cid, name, image, state_str, ports]
            if show_stats:
                s = stats.get(cid, {})
                row += [s.get("CPUPerc", "—"), s.get("MemUsage", "—")]

            table.add_row(*row)

        console.print(table)

    console.print()
    _render_group(t("docker.running", n=len(running)), running, show_stats=True)
    if running and stopped:
        console.print()
    _render_group(t("docker.stopped", n=len(stopped)), stopped, show_stats=False)
    console.print()
