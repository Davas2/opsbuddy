import subprocess
import socket
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from opsbuddy.i18n import t

console = Console()


def _open_ports() -> list[tuple[str, int, str]]:
    rows = []
    try:
        conns = psutil.net_connections(kind="inet")
        pids = {p.pid: p.name() for p in psutil.process_iter(["pid", "name"])}
        for c in conns:
            if c.status == psutil.CONN_LISTEN and c.laddr:
                port = c.laddr.port
                name = pids.get(c.pid, "?") if c.pid else "?"
                rows.append(("TCP", port, name))
    except (psutil.AccessDenied, AttributeError):
        try:
            out = subprocess.check_output(["ss", "-tlnp"], stderr=subprocess.DEVNULL, text=True)
            for line in out.splitlines()[1:]:
                parts = line.split()
                if len(parts) >= 4:
                    addr = parts[3]
                    port = int(addr.rsplit(":", 1)[-1])
                    rows.append(("TCP", port, "?"))
        except Exception:
            pass
    return sorted(rows, key=lambda x: x[1])


def _connectivity_checks() -> list[tuple[str, bool]]:
    targets = [("8.8.8.8", "Google DNS"), ("1.1.1.1", "Cloudflare DNS")]
    results = []
    for host, label in targets:
        try:
            socket.setdefaulttimeout(2)
            socket.create_connection((host, 53))
            results.append((label, True))
        except OSError:
            results.append((label, False))
    return results


def run() -> None:
    ifaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    iface_table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan", expand=True)
    iface_table.add_column(t("network.col_iface"), min_width=12)
    iface_table.add_column(t("network.col_ip"), min_width=15)
    iface_table.add_column(t("network.col_status"), width=10)
    iface_table.add_column(t("network.col_speed"), justify="right", width=12)

    for name, addrs in ifaces.items():
        ipv4 = next((a.address for a in addrs if a.family == socket.AF_INET), "—")
        stat = stats.get(name)
        is_up = stat.isup if stat else False
        speed = f"{stat.speed} Mbps" if stat and stat.speed > 0 else "—"
        status_str = f"[green]{t('network.active')}[/green]" if is_up else f"[dim]{t('network.inactive')}[/dim]"
        iface_table.add_row(name, ipv4, status_str, speed)

    console.print(Panel(iface_table, title=f"[bold cyan]{t('network.title_ifaces')}[/bold cyan]", border_style="cyan"))

    ports = _open_ports()
    if ports:
        console.print()
        console.print(Rule(f"[bold cyan]{t('network.title_ports')}[/bold cyan]", style="cyan"))
        port_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
        port_table.add_column(t("network.col_proto"), width=10)
        port_table.add_column(t("network.col_port"), justify="right", width=8)
        port_table.add_column(t("network.col_process"))
        for proto, port, proc in ports[:20]:
            port_table.add_row(proto, str(port), proc)
        console.print(port_table)

    console.print()
    console.print(Rule(f"[bold cyan]{t('network.title_conn')}[/bold cyan]", style="cyan"))
    checks = _connectivity_checks()
    for label, ok in checks:
        icon = "[green]✔[/green]" if ok else "[red]✘[/red]"
        status = f"[green]{t('network.ok')}[/green]" if ok else f"[red]{t('network.no_response')}[/red]"
        console.print(f"  {icon}  {label}: {status}")
    console.print()
