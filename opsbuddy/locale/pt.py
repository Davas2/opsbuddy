STRINGS = {
    # welcome
    "welcome.greeting":        "Olá, {username}! Bem-vindo ao OpsBuddy v{version}",
    "welcome.subtitle":        "Seu assistente para administração de servidores Linux.",
    "welcome.commands_title":  "Comandos disponíveis:",
    "welcome.tip":             "Dica: use --help em qualquer comando para mais detalhes.",
    # command descriptions (welcome screen)
    "cmd.overview":   "Status do sistema: memória, disco e containers",
    "cmd.processes":  "Top 15 processos por uso de CPU",
    "cmd.disk":       "Partições e maiores diretórios",
    "cmd.network":    "Interfaces, portas abertas e conectividade",
    "cmd.docker":     "Painel de containers Docker",
    "cmd.diagnose":   "Diagnóstico de saúde do servidor",
    "cmd.explain":    "Explica os comandos Linux por trás de cada funcionalidade",
    "cmd.learn":      "Guia de referência de comandos Linux",
    "cmd.language":   "Seleciona o idioma do OpsBuddy",
    # overview
    "overview.title":       "Visão Geral do Sistema",
    "overview.memory":      "Memória",
    "overview.disk":        "Disco  (/)",
    "overview.docker":      "Docker",
    "overview.col_resource":"Recurso",
    "overview.col_used":    "Usado",
    "overview.col_avail":   "Disponível",
    "overview.col_total":   "Total",
    "overview.col_usage":   "Uso",
    "overview.docker_off":  "não instalado",
    "overview.running":     "{n} rodando",
    "overview.stopped":     "{n} parado(s)",
    "overview.no_container":"nenhum container",
    # processes
    "processes.title":      "Processos Ativos (Top 15 por CPU)",
    "processes.col_pid":    "PID",
    "processes.col_name":   "Nome",
    "processes.col_cpu":    "CPU %",
    "processes.col_mem":    "Mem %",
    "processes.col_status": "Status",
    # disk
    "disk.title_parts":     "Partições",
    "disk.title_dirs":      "Maiores diretórios em /",
    "disk.col_partition":   "Partição",
    "disk.col_mountpoint":  "Ponto de Montagem",
    "disk.col_used":        "Usado",
    "disk.col_avail":       "Disponível",
    "disk.col_total":       "Total",
    "disk.col_usage":       "Uso",
    "disk.col_dir":         "Diretório",
    "disk.col_size":        "Tamanho",
    # network
    "network.title_ifaces": "Interfaces de Rede",
    "network.title_ports":  "Portas em Escuta",
    "network.title_conn":   "Conectividade",
    "network.col_iface":    "Interface",
    "network.col_ip":       "IP",
    "network.col_status":   "Status",
    "network.col_speed":    "Velocidade",
    "network.col_proto":    "Protocolo",
    "network.col_port":     "Porta",
    "network.col_process":  "Processo",
    "network.active":       "ativa",
    "network.inactive":     "inativa",
    "network.ok":           "OK",
    "network.no_response":  "sem resposta",
    # docker
    "docker.title":         "Docker",
    "docker.running":       "Rodando ({n})",
    "docker.stopped":       "Parados ({n})",
    "docker.not_found":     "Docker não encontrado ou daemon não está rodando.",
    "docker.no_containers": "Nenhum container encontrado.",
    "docker.col_id":        "ID",
    "docker.col_name":      "Nome",
    "docker.col_image":     "Imagem",
    "docker.col_status":    "Status",
    "docker.col_ports":     "Portas",
    "docker.col_cpu":       "CPU",
    "docker.col_mem":       "Mem",
    # diagnose
    "diagnose.title":       "Diagnóstico do Sistema",
    "diagnose.running":     "Executando diagnóstico...",
    "diagnose.ok_all":      "Todos os sistemas operando normalmente.",
    "diagnose.healthy":     "Sistema saudável",
    "diagnose.warnings":    "Atenção: avisos detectados",
    "diagnose.critical":    "Atenção: problemas críticos detectados",
    "diagnose.cpu":         "CPU",
    "diagnose.memory":      "Memória",
    "diagnose.disk":        "Disco",
    "diagnose.docker":      "Docker",
    "diagnose.network":     "Rede",
    "diagnose.status_ok":   "  OK  ",
    "diagnose.status_warn": " AVISO",
    "diagnose.status_crit": " CRÍTICO",
    "diagnose.status_na":   "  N/A ",
    "diagnose.docker_ok":   "{n} container(s) rodando",
    "diagnose.docker_off":  "Docker não instalado",
    "diagnose.docker_dead": "daemon não está respondendo",
    "diagnose.net_ok":      "conectividade OK ({host})",
    "diagnose.net_fail":    "sem conectividade com a internet",
    "diagnose.cpu_detail":  "{pct:.0f}% de uso  |  load avg: {load:.2f}",
    "diagnose.mem_detail":  "{used:.1f} GB / {total:.1f} GB  ({pct:.0f}%)",
    "diagnose.disk_detail": "{pct:.0f}% em uso  (partição mais cheia: {path})",
    # explain
    "explain.not_found":    "Comando '{cmd}' não encontrado.",
    "explain.available":    "Comandos disponíveis",
    "explain.flags_title":  "Flags principais",
    # learn
    "learn.title":          "Referência rápida de comandos Linux",
    "learn.subtitle":       "Use [cyan]opsbuddy learn <comando>[/cyan] para ver detalhes, exemplos e flags.",
    "learn.not_found":      "Comando '{cmd}' não encontrado no guia.",
    "learn.available":      "Disponíveis",
    "learn.flags":          "Flags principais",
    "learn.examples":       "Exemplos",
    # language
    "language.title":       "Idioma / Language",
    "language.current":     "Idioma atual: [bold cyan]{lang}[/bold cyan]",
    "language.choose":      "Escolha o idioma",
    "language.saved":       "Idioma alterado para [bold cyan]{lang}[/bold cyan]",
    "language.opt_pt":      "Português",
    "language.opt_en":      "English",
}

LEARN_REGISTRY = {
    "ls": {
        "category": "Arquivos e Diretórios",
        "description": "Lista arquivos e diretórios. Um dos comandos mais usados no Linux — permite visualizar o conteúdo de um diretório com diferentes níveis de detalhe.",
        "flags": [
            ("-l", "formato detalhado: permissões, dono, tamanho e data"),
            ("-a", "mostra arquivos ocultos (que começam com ponto)"),
            ("-h", "tamanhos legíveis (KB, MB, GB) — use junto com -l"),
            ("-t", "ordena por data de modificação, mais recente primeiro"),
            ("-r", "inverte a ordem de listagem"),
        ],
        "examples": [
            ("ls -lah", "lista tudo com detalhes, incluindo ocultos e tamanhos legíveis"),
            ("ls -lt", "lista ordenado pelo mais recente"),
        ],
    },
    "cd": {
        "category": "Arquivos e Diretórios",
        "description": "Navega entre diretórios. Muda o diretório de trabalho atual.",
        "flags": [],
        "examples": [
            ("cd /var/log", "vai para o diretório /var/log"),
            ("cd ..", "volta um nível"),
            ("cd ~", "vai para o diretório home do usuário"),
            ("cd -", "volta para o diretório anterior"),
        ],
    },
    "pwd": {
        "category": "Arquivos e Diretórios",
        "description": "Exibe o caminho completo do diretório atual (Print Working Directory).",
        "flags": [],
        "examples": [
            ("pwd", "mostra onde você está no sistema de arquivos"),
        ],
    },
    "mkdir": {
        "category": "Arquivos e Diretórios",
        "description": "Cria um ou mais diretórios.",
        "flags": [("-p", "cria diretórios intermediários se não existirem")],
        "examples": [
            ("mkdir logs", "cria o diretório 'logs' no local atual"),
            ("mkdir -p /opt/app/logs", "cria toda a estrutura de diretórios de uma vez"),
        ],
    },
    "rm": {
        "category": "Arquivos e Diretórios",
        "description": "Remove arquivos ou diretórios. Cuidado: não há lixeira — a remoção é permanente.",
        "flags": [
            ("-r", "remove diretórios e seu conteúdo recursivamente"),
            ("-f", "força a remoção sem pedir confirmação"),
            ("-i", "pede confirmação antes de cada remoção"),
        ],
        "examples": [
            ("rm arquivo.txt", "remove o arquivo"),
            ("rm -rf /tmp/cache", "remove o diretório e tudo dentro dele sem confirmação"),
        ],
    },
    "cp": {
        "category": "Arquivos e Diretórios",
        "description": "Copia arquivos ou diretórios.",
        "flags": [
            ("-r", "copia diretórios recursivamente"),
            ("-p", "preserva permissões, dono e data de modificação"),
        ],
        "examples": [
            ("cp config.yml config.yml.bak", "cria uma cópia de backup"),
            ("cp -r /app/src /app/src_backup", "copia um diretório inteiro"),
        ],
    },
    "mv": {
        "category": "Arquivos e Diretórios",
        "description": "Move ou renomeia arquivos e diretórios.",
        "flags": [],
        "examples": [
            ("mv app.log app.log.old", "renomeia o arquivo"),
            ("mv /tmp/deploy.sh /opt/scripts/", "move o arquivo para outro diretório"),
        ],
    },
    "find": {
        "category": "Arquivos e Diretórios",
        "description": "Busca arquivos e diretórios no sistema com filtros avançados.",
        "flags": [
            ("-name", "busca por nome (aceita wildcards com aspas)"),
            ("-type f", "filtra apenas arquivos"),
            ("-type d", "filtra apenas diretórios"),
            ("-mtime -1", "modificados nas últimas 24 horas"),
            ("-size +100M", "maiores que 100 MB"),
        ],
        "examples": [
            ('find /var/log -name "*.log"', "encontra todos os arquivos .log em /var/log"),
            ("find /home -size +100M", "encontra arquivos maiores que 100 MB em /home"),
            ('find . -name "*.sh" -type f', "encontra scripts shell no diretório atual"),
        ],
    },
    "cat": {
        "category": "Arquivos e Diretórios",
        "description": "Exibe o conteúdo de um arquivo no terminal.",
        "flags": [("-n", "numera as linhas")],
        "examples": [
            ("cat /etc/hostname", "exibe o hostname do servidor"),
            ("cat -n script.sh", "exibe o script com números de linha"),
        ],
    },
    "tail": {
        "category": "Arquivos e Diretórios",
        "description": "Exibe as últimas linhas de um arquivo. Muito usado para acompanhar logs em tempo real.",
        "flags": [
            ("-n 50", "exibe as últimas 50 linhas"),
            ("-f", "segue o arquivo em tempo real (follow) — Ctrl+C para sair"),
        ],
        "examples": [
            ("tail -f /var/log/syslog", "monitora o log do sistema em tempo real"),
            ("tail -n 100 app.log", "exibe as últimas 100 linhas do log"),
        ],
    },
    "head": {
        "category": "Arquivos e Diretórios",
        "description": "Exibe as primeiras linhas de um arquivo.",
        "flags": [("-n 20", "exibe as primeiras 20 linhas")],
        "examples": [
            ("head -n 5 /etc/passwd", "mostra as 5 primeiras linhas do arquivo de usuários"),
        ],
    },
    "ps": {
        "category": "Sistema",
        "description": "Lista os processos em execução. Permite ver quem está rodando, quanto consome e há quanto tempo.",
        "flags": [
            ("a", "mostra processos de todos os usuários"),
            ("u", "exibe o dono e uso de CPU/memória"),
            ("x", "inclui processos sem terminal (daemons)"),
        ],
        "examples": [
            ("ps aux", "lista todos os processos do sistema com detalhes"),
            ("ps aux | grep nginx", "verifica se o nginx está rodando"),
        ],
    },
    "top": {
        "category": "Sistema",
        "description": "Monitor interativo de processos em tempo real. Mostra CPU, memória e os processos mais pesados.",
        "flags": [
            ("-u usuario", "filtra processos de um usuário específico"),
            ("-p PID", "monitora apenas um processo específico"),
        ],
        "examples": [
            ("top", "abre o monitor interativo (pressione 'q' para sair)"),
            ("top -u www-data", "monitora apenas os processos do usuário www-data"),
        ],
    },
    "kill": {
        "category": "Sistema",
        "description": "Envia um sinal a um processo, geralmente para encerrá-lo. Requer o PID do processo.",
        "flags": [
            ("-9", "força o encerramento imediato (SIGKILL)"),
            ("-15", "encerramento gracioso (SIGTERM) — padrão"),
        ],
        "examples": [
            ("kill 1234", "encerra o processo com PID 1234 de forma graciosa"),
            ("kill -9 1234", "força o encerramento do processo 1234"),
        ],
    },
    "uptime": {
        "category": "Sistema",
        "description": "Mostra há quanto tempo o servidor está ligado, quantos usuários estão conectados e o load average (carga média no último 1, 5 e 15 minutos).",
        "flags": [],
        "examples": [("uptime", "exibe tempo ligado e carga do sistema")],
    },
    "uname": {
        "category": "Sistema",
        "description": "Exibe informações sobre o sistema operacional e kernel.",
        "flags": [
            ("-a", "exibe todas as informações disponíveis"),
            ("-r", "mostra apenas a versão do kernel"),
        ],
        "examples": [
            ("uname -a", "exibe sistema, kernel, arquitetura e mais"),
            ("uname -r", "mostra a versão exata do kernel"),
        ],
    },
    "df": {
        "category": "Sistema",
        "description": "Exibe o uso de espaço em disco de cada partição montada.",
        "flags": [
            ("-h", "formata os tamanhos em unidades legíveis"),
            ("-T", "mostra o tipo de sistema de arquivos"),
        ],
        "examples": [
            ("df -h", "lista todas as partições com uso em formato legível"),
            ("df -h /var", "mostra o uso apenas da partição que contém /var"),
        ],
    },
    "du": {
        "category": "Sistema",
        "description": "Mostra o espaço em disco utilizado por arquivos e diretórios.",
        "flags": [
            ("-s", "exibe apenas o total do diretório (summary)"),
            ("-h", "formata em unidades legíveis"),
            ("--max-depth=1", "limita a profundidade da listagem"),
        ],
        "examples": [
            ("du -sh /var/log", "mostra o tamanho total de /var/log"),
            ("du -sh /var/*", "compara o tamanho de cada subdiretório em /var"),
        ],
    },
    "free": {
        "category": "Sistema",
        "description": "Exibe o uso de memória RAM e swap do sistema.",
        "flags": [
            ("-h", "formata em unidades legíveis"),
            ("-s 2", "atualiza a cada 2 segundos"),
        ],
        "examples": [
            ("free -h", "mostra memória total, usada e disponível"),
            ("free -h -s 2", "monitora a memória atualizando a cada 2 segundos"),
        ],
    },
    "chmod": {
        "category": "Permissões",
        "description": "Altera as permissões de acesso de arquivos e diretórios. As permissões definem quem pode ler, escrever e executar.",
        "flags": [("-R", "aplica as permissões recursivamente em um diretório")],
        "examples": [
            ("chmod +x script.sh", "torna o script executável"),
            ("chmod 644 arquivo.conf", "dono lê/escreve, grupo e outros só leem"),
            ("chmod 755 /opt/app", "dono tem controle total, outros podem ler e executar"),
        ],
    },
    "chown": {
        "category": "Permissões",
        "description": "Altera o dono e/ou grupo de arquivos e diretórios.",
        "flags": [("-R", "aplica recursivamente em um diretório")],
        "examples": [
            ("chown www-data arquivo.html", "transfere o arquivo para o usuário www-data"),
            ("chown www-data:www-data /var/www", "define dono e grupo"),
            ("chown -R deploy:deploy /opt/app", "transfere todo o diretório"),
        ],
    },
    "ping": {
        "category": "Rede",
        "description": "Testa a conectividade com um host enviando pacotes ICMP e medindo o tempo de resposta.",
        "flags": [
            ("-c N", "envia N pacotes e encerra"),
            ("-i N", "intervalo de N segundos entre pacotes"),
        ],
        "examples": [
            ("ping google.com", "testa conectividade continuamente (Ctrl+C para parar)"),
            ("ping -c 4 8.8.8.8", "envia 4 pacotes para o DNS do Google"),
        ],
    },
    "curl": {
        "category": "Rede",
        "description": "Faz requisições HTTP/HTTPS e transfere dados. Essencial para testar APIs e baixar arquivos.",
        "flags": [
            ("-I", "busca apenas os headers da resposta"),
            ("-o arquivo", "salva a resposta em um arquivo"),
            ("-s", "modo silencioso, sem barra de progresso"),
            ("-X POST", "define o método HTTP"),
            ("-H", "adiciona um header à requisição"),
        ],
        "examples": [
            ("curl https://api.exemplo.com/status", "faz uma requisição GET simples"),
            ("curl -I https://meusite.com", "verifica os headers e status HTTP"),
            ('curl -s https://api.exemplo.com | python3 -m json.tool', "formata JSON da resposta"),
        ],
    },
    "ssh": {
        "category": "Rede",
        "description": "Abre uma conexão segura com um servidor remoto.",
        "flags": [
            ("-i chave.pem", "usa uma chave privada específica"),
            ("-p 2222", "conecta em uma porta diferente da padrão (22)"),
            ("-L", "cria um túnel local (port forwarding)"),
        ],
        "examples": [
            ("ssh usuario@192.168.1.10", "conecta ao servidor como 'usuario'"),
            ("ssh -i ~/.ssh/id_rsa deploy@servidor.com", "conecta usando chave privada"),
        ],
    },
    "ss": {
        "category": "Rede",
        "description": "Exibe informações sobre sockets de rede. Substituto moderno do netstat.",
        "flags": [
            ("-t", "mostra conexões TCP"),
            ("-l", "mostra apenas sockets em escuta (listening)"),
            ("-n", "exibe endereços e portas como números"),
            ("-p", "mostra o processo associado a cada socket"),
        ],
        "examples": [
            ("ss -tlnp", "lista todas as portas TCP em escuta com o processo responsável"),
            ("ss -tlnp | grep 80", "verifica se algo está escutando na porta 80"),
        ],
    },
    "ip": {
        "category": "Rede",
        "description": "Gerencia interfaces de rede, rotas e endereços IP. Substituto moderno do ifconfig.",
        "flags": [],
        "examples": [
            ("ip addr", "lista todas as interfaces com seus endereços IP"),
            ("ip route", "exibe a tabela de rotas"),
        ],
    },
    "grep": {
        "category": "Texto",
        "description": "Busca padrões de texto dentro de arquivos ou na saída de outros comandos. Um dos mais poderosos do Linux.",
        "flags": [
            ("-i", "ignora maiúsculas/minúsculas"),
            ("-r", "busca recursivamente em diretórios"),
            ("-n", "mostra o número da linha onde o padrão foi encontrado"),
            ("-v", "inverte: mostra linhas que NÃO contêm o padrão"),
            ("-l", "mostra apenas os arquivos que contêm o padrão"),
        ],
        "examples": [
            ("grep 'error' /var/log/app.log", "busca a palavra 'error' no log"),
            ("grep -rn 'TODO' /opt/app/src", "encontra todos os TODOs no código-fonte"),
            ("ps aux | grep nginx", "verifica se o nginx está rodando"),
        ],
    },
    "awk": {
        "category": "Texto",
        "description": "Processa e transforma texto estruturado por colunas. Ideal para extrair campos específicos de saídas de comandos.",
        "flags": [],
        "examples": [
            ("ps aux | awk '{print $1, $2}'", "exibe apenas o usuário e PID de cada processo"),
            ("df -h | awk '{print $5, $6}'", "mostra uso percentual e ponto de montagem"),
        ],
    },
    "sed": {
        "category": "Texto",
        "description": "Editor de fluxo que substitui, insere ou remove texto em arquivos ou saídas de comandos.",
        "flags": [
            ("-i", "edita o arquivo diretamente (in-place)"),
        ],
        "examples": [
            ("sed 's/http/https/g' config.txt", "substitui todas as ocorrências de http por https"),
            ("sed -i 's/localhost/0.0.0.0/g' app.conf", "substitui direto no arquivo"),
        ],
    },
    "systemctl": {
        "category": "Serviços",
        "description": "Controla serviços do sistema no Linux moderno (systemd). Permite iniciar, parar, reiniciar e verificar o status de serviços.",
        "flags": [],
        "examples": [
            ("systemctl status nginx", "verifica se o nginx está rodando"),
            ("systemctl restart nginx", "reinicia o nginx"),
            ("systemctl enable nginx", "configura o nginx para iniciar automaticamente no boot"),
        ],
    },
    "journalctl": {
        "category": "Serviços",
        "description": "Lê os logs do systemd (journald). Permite consultar logs de qualquer serviço do sistema.",
        "flags": [
            ("-u serviço", "filtra logs de um serviço específico"),
            ("-f", "segue os logs em tempo real"),
            ("-n 50", "exibe as últimas 50 linhas"),
            ("--since '1 hour ago'", "logs da última hora"),
        ],
        "examples": [
            ("journalctl -u nginx -f", "acompanha os logs do nginx em tempo real"),
            ("journalctl -p err --since '1 hour ago'", "todos os erros da última hora"),
        ],
    },
    "docker ps": {
        "category": "Docker",
        "description": "Lista os containers Docker em execução.",
        "flags": [
            ("-a", "inclui containers parados"),
            ("-q", "exibe apenas os IDs"),
        ],
        "examples": [
            ("docker ps", "lista containers rodando"),
            ("docker ps -a", "lista todos os containers, incluindo parados"),
        ],
    },
    "docker logs": {
        "category": "Docker",
        "description": "Exibe os logs de saída de um container.",
        "flags": [
            ("-f", "segue os logs em tempo real"),
            ("--tail N", "exibe apenas as últimas N linhas"),
        ],
        "examples": [
            ("docker logs -f meu-container", "acompanha os logs em tempo real"),
            ("docker logs --tail 50 meu-container", "exibe as últimas 50 linhas"),
        ],
    },
    "docker exec": {
        "category": "Docker",
        "description": "Executa um comando dentro de um container em execução.",
        "flags": [("-it", "modo interativo com terminal — necessário para abrir um shell")],
        "examples": [
            ("docker exec -it meu-container bash", "abre um shell bash dentro do container"),
            ("docker exec meu-container env", "lista as variáveis de ambiente do container"),
        ],
    },
}

LEARN_CATEGORIES = [
    "Arquivos e Diretórios",
    "Sistema",
    "Permissões",
    "Rede",
    "Texto",
    "Serviços",
    "Docker",
]
