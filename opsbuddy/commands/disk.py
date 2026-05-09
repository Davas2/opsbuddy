import subprocess
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from opsbuddy.i18n import t

console = Console()


def _bytes_to_human(value: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024:
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} PB"


def _bar(used: float, total: float, width: int = 20) -> str:
    if total == 0:
        return "[gray]N/A[/gray]"
    ratio = used / total
    filled = int(ratio * width)
    bar = "█" * filled + "░" * (width - filled)
    color = "green" if ratio < 0.7 else "yellow" if ratio < 0.9 else "red"
    return f"[{color}]{bar}[/{color}] {ratio:.0%}"


def _top_dirs(path: str = "/", limit: int = 10) -> list[tuple[str, str]]:
    try:
        result = subprocess.check_output(
            ["du", "-sh", "--", *[f"{path}/{d}" for d in ["home", "var", "usr", "opt", "tmp", "root"]]],
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        try:
            result = subprocess.check_output(
                ["du", "-sh", f"{path}/*"],
                stderr=subprocess.DEVNULL,
                shell=False,
                text=True,
            )
        except Exception:
            return []

    rows = []
    for line in result.strip().splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            rows.append((parts[1], parts[0]))
    return rows[:limit]


def run() -> None:
    partitions = psutil.disk_partitions(all=False)

    part_table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan", expand=True)
    part_table.add_column(t("disk.col_partition"), min_width=15)
    part_table.add_column(t("disk.col_mountpoint"), min_width=10)
    part_table.add_column(t("disk.col_used"), justify="right")
    part_table.add_column(t("disk.col_avail"), justify="right")
    part_table.add_column(t("disk.col_total"), justify="right")
    part_table.add_column(t("disk.col_usage"), min_width=26)

    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
        except PermissionError:
            continue
        part_table.add_row(
            p.device,
            p.mountpoint,
            _bytes_to_human(usage.used),
            _bytes_to_human(usage.free),
            _bytes_to_human(usage.total),
            _bar(usage.used, usage.total),
        )

    console.print(Panel(part_table, title=f"[bold cyan]{t('disk.title_parts')}[/bold cyan]", border_style="cyan"))

    dirs = _top_dirs("/")
    if dirs:
        console.print()
        console.print(Rule(f"[bold cyan]{t('disk.title_dirs')}[/bold cyan]", style="cyan"))
        dir_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
        dir_table.add_column(t("disk.col_dir"))
        dir_table.add_column(t("disk.col_size"), justify="right")
        for path, size in dirs:
            dir_table.add_row(path, f"[bold]{size}[/bold]")
        console.print(dir_table)
