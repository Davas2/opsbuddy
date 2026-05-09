import subprocess
import socket
import psutil
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from opsbuddy.i18n import t

console = Console()


def _status(value: float, warn: float, crit: float) -> str:
    if value >= crit:
        return t("diagnose.status_crit")
    if value >= warn:
        return t("diagnose.status_warn")
    return t("diagnose.status_ok")


def _check_cpu() -> tuple[str, str]:
    percent = psutil.cpu_percent(interval=0.5)
    load1, _, _ = psutil.getloadavg()
    cores = psutil.cpu_count()
    load_ratio = (load1 / cores * 100) if cores else 0
    status = _status(max(percent, load_ratio), warn=70, crit=90)
    detail = t("diagnose.cpu_detail", pct=percent, load=load1)
    return status, detail


def _check_memory() -> tuple[str, str]:
    mem = psutil.virtual_memory()
    status = _status(mem.percent, warn=75, crit=90)
    detail = t("diagnose.mem_detail", used=mem.used / (1024**3), total=mem.total / (1024**3), pct=mem.percent)
    return status, detail


def _check_disk() -> tuple[str, str]:
    worst_pct = 0.0
    worst_path = "/"
    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
            if usage.percent > worst_pct:
                worst_pct = usage.percent
                worst_path = part.mountpoint
        except PermissionError:
            pass
    status = _status(worst_pct, warn=75, crit=90)
    detail = t("diagnose.disk_detail", pct=worst_pct, path=worst_path)
    return status, detail


def _check_docker() -> tuple[str, str]:
    try:
        out = subprocess.check_output(
            ["docker", "ps", "-q"], stderr=subprocess.DEVNULL, text=True
        ).strip()
        running = len(out.splitlines()) if out else 0
        return t("diagnose.status_ok"), t("diagnose.docker_ok", n=running)
    except FileNotFoundError:
        return t("diagnose.status_na"), t("diagnose.docker_off")
    except subprocess.CalledProcessError:
        return t("diagnose.status_crit"), t("diagnose.docker_dead")


def _check_network() -> tuple[str, str]:
    for host, port in [("8.8.8.8", 53), ("1.1.1.1", 53)]:
        try:
            socket.setdefaulttimeout(2)
            socket.create_connection((host, port))
            return t("diagnose.status_ok"), t("diagnose.net_ok", host=host)
        except OSError:
            pass
    return t("diagnose.status_crit"), t("diagnose.net_fail")


def run() -> None:
    console.print()
    console.print(f"[bold cyan]{t('diagnose.running')}[/bold cyan]\n")

    checks = [
        (t("diagnose.cpu"),     *_check_cpu()),
        (t("diagnose.memory"),  *_check_memory()),
        (t("diagnose.disk"),    *_check_disk()),
        (t("diagnose.docker"),  *_check_docker()),
        (t("diagnose.network"), *_check_network()),
    ]

    table = Table(box=box.ROUNDED, show_header=False, expand=True, padding=(0, 1))
    table.add_column("Recurso", style="bold", width=12)
    table.add_column("Status", width=11, justify="center")
    table.add_column("Detalhe")

    for name, status, detail in checks:
        table.add_row(name, status, detail)

    ok_s    = t("diagnose.status_ok")
    warn_s  = t("diagnose.status_warn")
    crit_s  = t("diagnose.status_crit")

    issues = [c for c in checks if c[1] in (warn_s, crit_s)]

    overall_border = "green"
    overall_title  = f"[bold green]{t('diagnose.healthy')}[/bold green]"
    if any(c[1] == crit_s for c in checks):
        overall_border = "red"
        overall_title  = f"[bold red]{t('diagnose.critical')}[/bold red]"
    elif issues:
        overall_border = "yellow"
        overall_title  = f"[bold yellow]{t('diagnose.warnings')}[/bold yellow]"

    console.print(Panel(table, title=f"[bold cyan]{t('diagnose.title')}[/bold cyan]", border_style="cyan"))

    console.print()
    if issues:
        console.print(Panel(
            "\n".join(f"  • [bold]{c[0]}:[/bold] {c[2]}" for c in issues),
            title=overall_title,
            border_style=overall_border,
            padding=(0, 1),
        ))
    else:
        console.print(Panel(
            f"  {t('diagnose.ok_all')}",
            title=overall_title,
            border_style=overall_border,
            padding=(0, 1),
        ))
    console.print()
