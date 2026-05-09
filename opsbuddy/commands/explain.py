from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich.text import Text
from rich import box
import typer

console = Console()

REGISTRY: dict[str, dict] = {
    "overview": {
        "description": "Resume o estado geral do servidor: memória, disco e containers.",
        "commands": [
            {
                "cmd": "free -h",
                "what": "Exibe o uso de memória RAM e swap do sistema.",
                "flags": [
                    ("-h", "formata os valores em unidades legíveis (KB, MB, GB)"),
                ],
            },
            {
                "cmd": "df -h",
                "what": "Mostra o espaço usado e disponível em cada partição montada.",
                "flags": [
                    ("-h", "formata os valores em unidades legíveis"),
                ],
            },
            {
                "cmd": "docker ps -q",
                "what": "Lista apenas os IDs dos containers que estão rodando.",
                "flags": [
                    ("-q", "exibe somente os IDs, sem cabeçalho (quiet mode)"),
                ],
            },
            {
                "cmd": "docker ps -aq",
                "what": "Lista os IDs de todos os containers, incluindo os parados.",
                "flags": [
                    ("-a", "inclui containers parados (all)"),
                    ("-q", "exibe somente os IDs (quiet mode)"),
                ],
            },
        ],
    },
    "processes": {
        "description": "Lista os processos que mais consomem CPU no momento.",
        "commands": [
            {
                "cmd": "ps aux",
                "what": "Exibe todos os processos em execução com detalhes de CPU e memória.",
                "flags": [
                    ("a", "mostra processos de todos os usuários"),
                    ("u", "exibe o dono do processo e uso de recursos"),
                    ("x", "inclui processos sem terminal associado (daemons)"),
                ],
            },
            {
                "cmd": "top -bn1",
                "what": "Captura um snapshot do monitor de processos sem modo interativo.",
                "flags": [
                    ("-b", "executa em modo batch (não interativo)"),
                    ("-n1", "captura apenas 1 iteração e encerra"),
                ],
            },
        ],
    },
    "disk": {
        "description": "Exibe uso de disco por partição e identifica diretórios grandes.",
        "commands": [
            {
                "cmd": "df -h",
                "what": "Lista todas as partições montadas com espaço usado e disponível.",
                "flags": [
                    ("-h", "formata os valores em unidades legíveis"),
                ],
            },
            {
                "cmd": "du -sh /diretorio/*",
                "what": "Mostra o tamanho de cada subdiretório dentro de um caminho.",
                "flags": [
                    ("-s", "resume o tamanho total de cada argumento (summary)"),
                    ("-h", "formata os valores em unidades legíveis"),
                ],
            },
        ],
    },
    "network": {
        "description": "Inspeciona interfaces de rede, portas abertas e conectividade.",
        "commands": [
            {
                "cmd": "ip addr",
                "what": "Lista todas as interfaces de rede com seus endereços IP.",
                "flags": [],
            },
            {
                "cmd": "ss -tlnp",
                "what": "Exibe todas as portas TCP em escuta e o processo que as ocupa.",
                "flags": [
                    ("-t", "filtra somente conexões TCP"),
                    ("-l", "mostra apenas sockets em escuta (listening)"),
                    ("-n", "exibe portas como números, sem resolver nomes"),
                    ("-p", "mostra o processo dono de cada socket"),
                ],
            },
            {
                "cmd": "ping -c 3 8.8.8.8",
                "what": "Testa a conectividade com a internet enviando pacotes ICMP.",
                "flags": [
                    ("-c 3", "envia exatamente 3 pacotes e encerra"),
                ],
            },
        ],
    },
    "docker": {
        "description": "Exibe o painel completo de containers Docker com uso de recursos.",
        "commands": [
            {
                "cmd": "docker ps -a --format json",
                "what": "Lista todos os containers (rodando e parados) em formato JSON.",
                "flags": [
                    ("-a", "inclui containers parados (all)"),
                    ("--format json", "saída estruturada em JSON para fácil parsing"),
                ],
            },
            {
                "cmd": "docker stats --no-stream --format json",
                "what": "Captura um snapshot do uso de CPU e memória de cada container.",
                "flags": [
                    ("--no-stream", "captura apenas uma leitura e encerra (sem atualização contínua)"),
                    ("--format json", "saída estruturada em JSON"),
                ],
            },
        ],
    },
    "diagnose": {
        "description": "Verifica a saúde geral do servidor e aponta problemas.",
        "commands": [
            {
                "cmd": "uptime",
                "what": "Mostra há quanto tempo o servidor está ligado e o load average.",
                "flags": [],
            },
            {
                "cmd": "free -h",
                "what": "Verifica se o uso de memória está em nível preocupante.",
                "flags": [
                    ("-h", "formata os valores em unidades legíveis"),
                ],
            },
            {
                "cmd": "df -h",
                "what": "Verifica se alguma partição está com pouco espaço disponível.",
                "flags": [
                    ("-h", "formata os valores em unidades legíveis"),
                ],
            },
            {
                "cmd": "docker ps -q",
                "what": "Confirma se o daemon do Docker está respondendo.",
                "flags": [
                    ("-q", "retorna apenas IDs — se falhar, o daemon não está rodando"),
                ],
            },
            {
                "cmd": "ping -c 1 8.8.8.8",
                "what": "Checa conectividade básica com a internet.",
                "flags": [
                    ("-c 1", "envia apenas 1 pacote para uma verificação rápida"),
                ],
            },
        ],
    },
}


def run(command: str) -> None:
    key = command.lower().strip()

    if key not in REGISTRY:
        available = ", ".join(f"[cyan]{k}[/cyan]" for k in REGISTRY)
        console.print(
            f"\n[red]Comando '[bold]{command}[/bold]' não encontrado.[/red]\n"
            f"Comandos disponíveis: {available}\n"
        )
        raise typer.Exit(1)

    entry = REGISTRY[key]

    console.print()
    console.print(Panel(
        f"[bold]{entry['description']}[/bold]",
        title=f"[bold cyan]opsbuddy {key}[/bold cyan]",
        border_style="cyan",
        padding=(0, 2),
    ))

    for i, item in enumerate(entry["commands"]):
        console.print()
        console.print(Rule(f"[bold green]{item['cmd']}[/bold green]", style="green"))
        console.print(f"  {item['what']}\n")

        if item["flags"]:
            table = Table(box=box.SIMPLE, show_header=True, header_style="bold", padding=(0, 2))
            table.add_column("Flag", style="bold yellow", min_width=12)
            table.add_column("Descrição")
            for flag, desc in item["flags"]:
                table.add_row(flag, desc)
            console.print(table)

    console.print()
