import subprocess
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from opsbuddy.i18n import t

console = Console()


def _bytes_to_gb(value: int) -> str:
    return f"{value / (1024 ** 3):.1f} GB"


def _bar(used: float, total: float, width: int = 20) -> str:
    if total == 0:
        return "[gray]N/A[/gray]"
    ratio = used / total
    filled = int(ratio * width)
    bar = "█" * filled + "░" * (width - filled)
    color = "green" if ratio < 0.7 else "yellow" if ratio < 0.9 else "red"
    return f"[{color}]{bar}[/{color}] {ratio:.0%}"


def _docker_info() -> tuple[int, int]:
    try:
        running = subprocess.check_output(
            ["docker", "ps", "-q"], stderr=subprocess.DEVNULL, text=True
        ).strip()
        total = subprocess.check_output(
            ["docker", "ps", "-aq"], stderr=subprocess.DEVNULL, text=True
        ).strip()
        running_count = len(running.splitlines()) if running else 0
        total_count = len(total.splitlines()) if total else 0
        return running_count, total_count
    except (FileNotFoundError, subprocess.CalledProcessError):
        return -1, -1


def run() -> None:
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    docker_running, docker_total = _docker_info()

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan", expand=True)
    table.add_column(t("overview.col_resource"), style="bold", min_width=12)
    table.add_column(t("overview.col_used"), justify="right")
    table.add_column(t("overview.col_avail"), justify="right")
    table.add_column(t("overview.col_total"), justify="right")
    table.add_column(t("overview.col_usage"), min_width=26)

    table.add_row(
        t("overview.memory"),
        _bytes_to_gb(mem.used),
        _bytes_to_gb(mem.available),
        _bytes_to_gb(mem.total),
        _bar(mem.used, mem.total),
    )
    table.add_row(
        t("overview.disk"),
        _bytes_to_gb(disk.used),
        _bytes_to_gb(disk.free),
        _bytes_to_gb(disk.total),
        _bar(disk.used, disk.total),
    )

    if docker_running >= 0:
        docker_bar = _bar(docker_running, docker_total) if docker_total > 0 else f"[gray]{t('overview.no_container')}[/gray]"
        table.add_row(
            t("overview.docker"),
            t("overview.running", n=docker_running),
            t("overview.stopped", n=docker_total - docker_running),
            f"{docker_total} total",
            docker_bar,
        )
    else:
        table.add_row(
            t("overview.docker"),
            "[dim]—[/dim]", "[dim]—[/dim]", "[dim]—[/dim]",
            f"[yellow]{t('overview.docker_off')}[/yellow]",
        )

    console.print(Panel(table, title=f"[bold cyan]{t('overview.title')}[/bold cyan]", border_style="cyan"))
