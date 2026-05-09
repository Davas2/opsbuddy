import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from opsbuddy.i18n import t

console = Console()


def run() -> None:
    procs = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent", "status"]):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    psutil.cpu_percent(interval=0.5)
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent", "status"]):
        try:
            info = p.info
            for existing in procs:
                if existing["pid"] == info["pid"]:
                    existing["cpu_percent"] = info["cpu_percent"]
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    top = sorted(procs, key=lambda x: x["cpu_percent"] or 0, reverse=True)[:15]

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan", expand=True)
    table.add_column(t("processes.col_pid"), justify="right", style="dim", width=7)
    table.add_column(t("processes.col_name"), min_width=20)
    table.add_column(t("processes.col_cpu"), justify="right", width=8)
    table.add_column(t("processes.col_mem"), justify="right", width=8)
    table.add_column(t("processes.col_status"), width=10)

    for p in top:
        cpu = p["cpu_percent"] or 0
        mem = p["memory_percent"] or 0
        cpu_color = "green" if cpu < 50 else "yellow" if cpu < 80 else "red"
        mem_color = "green" if mem < 5 else "yellow" if mem < 15 else "red"
        status = p["status"] or "?"
        status_color = "green" if status == "running" else "dim"

        table.add_row(
            str(p["pid"]),
            p["name"] or "?",
            f"[{cpu_color}]{cpu:.1f}[/{cpu_color}]",
            f"[{mem_color}]{mem:.1f}[/{mem_color}]",
            f"[{status_color}]{status}[/{status_color}]",
        )

    console.print(Panel(table, title=f"[bold cyan]{t('processes.title')}[/bold cyan]", border_style="cyan"))
