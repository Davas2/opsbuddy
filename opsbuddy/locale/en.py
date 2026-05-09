STRINGS = {
    # welcome
    "welcome.greeting":        "Hello, {username}! Welcome to OpsBuddy v{version}",
    "welcome.subtitle":        "Your assistant for Linux server administration.",
    "welcome.commands_title":  "Available commands:",
    "welcome.tip":             "Tip: use --help on any command for more details.",
    # command descriptions (welcome screen)
    "cmd.overview":   "System status: memory, disk, and containers",
    "cmd.processes":  "Top 15 processes by CPU usage",
    "cmd.disk":       "Partitions and largest directories",
    "cmd.network":    "Interfaces, open ports, and connectivity",
    "cmd.docker":     "Docker containers panel",
    "cmd.diagnose":   "Server health diagnostics",
    "cmd.explain":    "Explains the Linux commands behind each feature",
    "cmd.learn":      "Linux command reference guide",
    "cmd.language":   "Select the OpsBuddy language",
    # overview
    "overview.title":       "System Overview",
    "overview.memory":      "Memory",
    "overview.disk":        "Disk  (/)",
    "overview.docker":      "Docker",
    "overview.col_resource":"Resource",
    "overview.col_used":    "Used",
    "overview.col_avail":   "Available",
    "overview.col_total":   "Total",
    "overview.col_usage":   "Usage",
    "overview.docker_off":  "not installed",
    "overview.running":     "{n} running",
    "overview.stopped":     "{n} stopped",
    "overview.no_container":"no containers",
    # processes
    "processes.title":      "Active Processes (Top 15 by CPU)",
    "processes.col_pid":    "PID",
    "processes.col_name":   "Name",
    "processes.col_cpu":    "CPU %",
    "processes.col_mem":    "Mem %",
    "processes.col_status": "Status",
    # disk
    "disk.title_parts":     "Partitions",
    "disk.title_dirs":      "Largest directories in /",
    "disk.col_partition":   "Partition",
    "disk.col_mountpoint":  "Mount Point",
    "disk.col_used":        "Used",
    "disk.col_avail":       "Available",
    "disk.col_total":       "Total",
    "disk.col_usage":       "Usage",
    "disk.col_dir":         "Directory",
    "disk.col_size":        "Size",
    # network
    "network.title_ifaces": "Network Interfaces",
    "network.title_ports":  "Listening Ports",
    "network.title_conn":   "Connectivity",
    "network.col_iface":    "Interface",
    "network.col_ip":       "IP",
    "network.col_status":   "Status",
    "network.col_speed":    "Speed",
    "network.col_proto":    "Protocol",
    "network.col_port":     "Port",
    "network.col_process":  "Process",
    "network.active":       "active",
    "network.inactive":     "inactive",
    "network.ok":           "OK",
    "network.no_response":  "no response",
    # docker
    "docker.title":         "Docker",
    "docker.running":       "Running ({n})",
    "docker.stopped":       "Stopped ({n})",
    "docker.not_found":     "Docker not found or daemon is not running.",
    "docker.no_containers": "No containers found.",
    "docker.col_id":        "ID",
    "docker.col_name":      "Name",
    "docker.col_image":     "Image",
    "docker.col_status":    "Status",
    "docker.col_ports":     "Ports",
    "docker.col_cpu":       "CPU",
    "docker.col_mem":       "Mem",
    # diagnose
    "diagnose.title":       "System Diagnostics",
    "diagnose.running":     "Running diagnostics...",
    "diagnose.ok_all":      "All systems operating normally.",
    "diagnose.healthy":     "System healthy",
    "diagnose.warnings":    "Warning: issues detected",
    "diagnose.critical":    "Critical: problems detected",
    "diagnose.cpu":         "CPU",
    "diagnose.memory":      "Memory",
    "diagnose.disk":        "Disk",
    "diagnose.docker":      "Docker",
    "diagnose.network":     "Network",
    "diagnose.status_ok":   "  OK  ",
    "diagnose.status_warn": "  WARN",
    "diagnose.status_crit": "  CRIT",
    "diagnose.status_na":   "  N/A ",
    "diagnose.docker_ok":   "{n} container(s) running",
    "diagnose.docker_off":  "Docker not installed",
    "diagnose.docker_dead": "daemon is not responding",
    "diagnose.net_ok":      "connectivity OK ({host})",
    "diagnose.net_fail":    "no internet connectivity",
    "diagnose.cpu_detail":  "{pct:.0f}% usage  |  load avg: {load:.2f}",
    "diagnose.mem_detail":  "{used:.1f} GB / {total:.1f} GB  ({pct:.0f}%)",
    "diagnose.disk_detail": "{pct:.0f}% in use  (fullest partition: {path})",
    # explain
    "explain.not_found":    "Command '{cmd}' not found.",
    "explain.available":    "Available commands",
    "explain.flags_title":  "Main flags",
    # learn
    "learn.title":          "Linux command quick reference",
    "learn.subtitle":       "Use [cyan]opsbuddy learn <command>[/cyan] to see details, examples and flags.",
    "learn.not_found":      "Command '{cmd}' not found in the guide.",
    "learn.available":      "Available",
    "learn.flags":          "Main flags",
    "learn.examples":       "Examples",
    # language
    "language.title":       "Idioma / Language",
    "language.current":     "Current language: [bold cyan]{lang}[/bold cyan]",
    "language.choose":      "Choose the language",
    "language.saved":       "Language changed to [bold cyan]{lang}[/bold cyan]",
    "language.opt_pt":      "Português",
    "language.opt_en":      "English",
}

LEARN_REGISTRY = {
    "ls": {
        "category": "Files and Directories",
        "description": "Lists files and directories. One of the most used Linux commands — lets you view directory contents with different levels of detail.",
        "flags": [
            ("-l", "detailed format: permissions, owner, size and date"),
            ("-a", "shows hidden files (starting with a dot)"),
            ("-h", "human-readable sizes (KB, MB, GB) — use with -l"),
            ("-t", "sorts by modification date, newest first"),
            ("-r", "reverses the listing order"),
        ],
        "examples": [
            ("ls -lah", "list everything with details, including hidden files and readable sizes"),
            ("ls -lt", "list sorted by most recent"),
        ],
    },
    "cd": {
        "category": "Files and Directories",
        "description": "Navigates between directories. Changes the current working directory.",
        "flags": [],
        "examples": [
            ("cd /var/log", "go to the /var/log directory"),
            ("cd ..", "go up one level"),
            ("cd ~", "go to the user's home directory"),
            ("cd -", "go back to the previous directory"),
        ],
    },
    "pwd": {
        "category": "Files and Directories",
        "description": "Displays the full path of the current directory (Print Working Directory).",
        "flags": [],
        "examples": [
            ("pwd", "shows where you are in the filesystem"),
        ],
    },
    "mkdir": {
        "category": "Files and Directories",
        "description": "Creates one or more directories.",
        "flags": [("-p", "creates intermediate directories if they don't exist")],
        "examples": [
            ("mkdir logs", "creates the 'logs' directory in the current location"),
            ("mkdir -p /opt/app/logs", "creates the entire directory structure at once"),
        ],
    },
    "rm": {
        "category": "Files and Directories",
        "description": "Removes files or directories. Warning: there is no trash — deletion is permanent.",
        "flags": [
            ("-r", "removes directories and their contents recursively"),
            ("-f", "forces removal without confirmation"),
            ("-i", "asks for confirmation before each removal"),
        ],
        "examples": [
            ("rm file.txt", "removes the file"),
            ("rm -rf /tmp/cache", "removes the directory and everything inside without confirmation"),
        ],
    },
    "cp": {
        "category": "Files and Directories",
        "description": "Copies files or directories.",
        "flags": [
            ("-r", "copies directories recursively"),
            ("-p", "preserves permissions, owner and modification date"),
        ],
        "examples": [
            ("cp config.yml config.yml.bak", "creates a backup copy"),
            ("cp -r /app/src /app/src_backup", "copies an entire directory"),
        ],
    },
    "mv": {
        "category": "Files and Directories",
        "description": "Moves or renames files and directories.",
        "flags": [],
        "examples": [
            ("mv app.log app.log.old", "renames the file"),
            ("mv /tmp/deploy.sh /opt/scripts/", "moves the file to another directory"),
        ],
    },
    "find": {
        "category": "Files and Directories",
        "description": "Searches for files and directories in the system with advanced filters.",
        "flags": [
            ("-name", "search by name (accepts wildcards in quotes)"),
            ("-type f", "filter files only"),
            ("-type d", "filter directories only"),
            ("-mtime -1", "modified in the last 24 hours"),
            ("-size +100M", "larger than 100 MB"),
        ],
        "examples": [
            ('find /var/log -name "*.log"', "find all .log files in /var/log"),
            ("find /home -size +100M", "find files larger than 100 MB in /home"),
            ('find . -name "*.sh" -type f', "find shell scripts in the current directory"),
        ],
    },
    "cat": {
        "category": "Files and Directories",
        "description": "Displays the contents of a file in the terminal.",
        "flags": [("-n", "numbers the lines")],
        "examples": [
            ("cat /etc/hostname", "displays the server hostname"),
            ("cat -n script.sh", "displays the script with line numbers"),
        ],
    },
    "tail": {
        "category": "Files and Directories",
        "description": "Displays the last lines of a file. Widely used to follow logs in real time.",
        "flags": [
            ("-n 50", "displays the last 50 lines"),
            ("-f", "follows the file in real time — Ctrl+C to stop"),
        ],
        "examples": [
            ("tail -f /var/log/syslog", "monitors the system log in real time"),
            ("tail -n 100 app.log", "displays the last 100 lines of the log"),
        ],
    },
    "head": {
        "category": "Files and Directories",
        "description": "Displays the first lines of a file.",
        "flags": [("-n 20", "displays the first 20 lines")],
        "examples": [
            ("head -n 5 /etc/passwd", "shows the first 5 lines of the users file"),
        ],
    },
    "ps": {
        "category": "System",
        "description": "Lists running processes. Lets you see what's running, how much it consumes and for how long.",
        "flags": [
            ("a", "shows processes from all users"),
            ("u", "displays the owner and CPU/memory usage"),
            ("x", "includes processes without a terminal (daemons)"),
        ],
        "examples": [
            ("ps aux", "lists all system processes with details"),
            ("ps aux | grep nginx", "checks if nginx is running"),
        ],
    },
    "top": {
        "category": "System",
        "description": "Interactive real-time process monitor. Shows CPU, memory and the heaviest processes.",
        "flags": [
            ("-u user", "filters processes of a specific user"),
            ("-p PID", "monitors only a specific process"),
        ],
        "examples": [
            ("top", "opens the interactive monitor (press 'q' to quit)"),
            ("top -u www-data", "monitors only www-data user processes"),
        ],
    },
    "kill": {
        "category": "System",
        "description": "Sends a signal to a process, usually to terminate it. Requires the process PID.",
        "flags": [
            ("-9", "forces immediate termination (SIGKILL)"),
            ("-15", "graceful termination (SIGTERM) — default"),
        ],
        "examples": [
            ("kill 1234", "gracefully terminates process with PID 1234"),
            ("kill -9 1234", "forces termination of process 1234"),
        ],
    },
    "uptime": {
        "category": "System",
        "description": "Shows how long the server has been running, how many users are connected and the load average (system load over the last 1, 5 and 15 minutes).",
        "flags": [],
        "examples": [("uptime", "displays uptime and system load")],
    },
    "uname": {
        "category": "System",
        "description": "Displays information about the operating system and kernel.",
        "flags": [
            ("-a", "displays all available information"),
            ("-r", "shows only the kernel version"),
        ],
        "examples": [
            ("uname -a", "displays system, kernel, architecture and more"),
            ("uname -r", "shows the exact kernel version"),
        ],
    },
    "df": {
        "category": "System",
        "description": "Displays disk space usage for each mounted partition.",
        "flags": [
            ("-h", "formats sizes in human-readable units"),
            ("-T", "shows the filesystem type"),
        ],
        "examples": [
            ("df -h", "lists all partitions with usage in readable format"),
            ("df -h /var", "shows usage only for the partition containing /var"),
        ],
    },
    "du": {
        "category": "System",
        "description": "Shows disk space used by files and directories.",
        "flags": [
            ("-s", "displays only the directory total (summary)"),
            ("-h", "formats in human-readable units"),
            ("--max-depth=1", "limits listing depth"),
        ],
        "examples": [
            ("du -sh /var/log", "shows the total size of /var/log"),
            ("du -sh /var/*", "compares the size of each subdirectory in /var"),
        ],
    },
    "free": {
        "category": "System",
        "description": "Displays RAM and swap memory usage.",
        "flags": [
            ("-h", "formats in human-readable units"),
            ("-s 2", "updates every 2 seconds"),
        ],
        "examples": [
            ("free -h", "shows total, used and available memory"),
            ("free -h -s 2", "monitors memory updating every 2 seconds"),
        ],
    },
    "chmod": {
        "category": "Permissions",
        "description": "Changes file and directory access permissions. Permissions define who can read, write and execute.",
        "flags": [("-R", "applies permissions recursively to a directory")],
        "examples": [
            ("chmod +x script.sh", "makes the script executable"),
            ("chmod 644 file.conf", "owner reads/writes, group and others read only"),
            ("chmod 755 /opt/app", "owner has full control, others can read and execute"),
        ],
    },
    "chown": {
        "category": "Permissions",
        "description": "Changes the owner and/or group of files and directories.",
        "flags": [("-R", "applies recursively to a directory")],
        "examples": [
            ("chown www-data file.html", "transfers the file to user www-data"),
            ("chown www-data:www-data /var/www", "sets owner and group"),
            ("chown -R deploy:deploy /opt/app", "transfers the entire directory"),
        ],
    },
    "ping": {
        "category": "Network",
        "description": "Tests connectivity to a host by sending ICMP packets and measuring response time.",
        "flags": [
            ("-c N", "sends N packets and stops"),
            ("-i N", "interval of N seconds between packets"),
        ],
        "examples": [
            ("ping google.com", "tests connectivity continuously (Ctrl+C to stop)"),
            ("ping -c 4 8.8.8.8", "sends 4 packets to Google DNS"),
        ],
    },
    "curl": {
        "category": "Network",
        "description": "Makes HTTP/HTTPS requests and transfers data. Essential for testing APIs and downloading files.",
        "flags": [
            ("-I", "fetches only the response headers"),
            ("-o file", "saves the response to a file"),
            ("-s", "silent mode, no progress bar"),
            ("-X POST", "sets the HTTP method"),
            ("-H", "adds a header to the request"),
        ],
        "examples": [
            ("curl https://api.example.com/status", "makes a simple GET request"),
            ("curl -I https://mysite.com", "checks HTTP headers and status"),
            ('curl -s https://api.example.com | python3 -m json.tool', "formats JSON response"),
        ],
    },
    "ssh": {
        "category": "Network",
        "description": "Opens a secure connection to a remote server.",
        "flags": [
            ("-i key.pem", "uses a specific private key for authentication"),
            ("-p 2222", "connects on a non-default port (default: 22)"),
            ("-L", "creates a local tunnel (port forwarding)"),
        ],
        "examples": [
            ("ssh user@192.168.1.10", "connects to the server as 'user'"),
            ("ssh -i ~/.ssh/id_rsa deploy@server.com", "connects using private key"),
        ],
    },
    "ss": {
        "category": "Network",
        "description": "Displays network socket information. Modern replacement for netstat.",
        "flags": [
            ("-t", "shows TCP connections"),
            ("-l", "shows only listening sockets"),
            ("-n", "displays addresses and ports as numbers"),
            ("-p", "shows the process associated with each socket"),
        ],
        "examples": [
            ("ss -tlnp", "lists all listening TCP ports with the responsible process"),
            ("ss -tlnp | grep 80", "checks if anything is listening on port 80"),
        ],
    },
    "ip": {
        "category": "Network",
        "description": "Manages network interfaces, routes and IP addresses. Modern replacement for ifconfig.",
        "flags": [],
        "examples": [
            ("ip addr", "lists all interfaces with their IP addresses"),
            ("ip route", "displays the routing table"),
        ],
    },
    "grep": {
        "category": "Text",
        "description": "Searches for text patterns inside files or in the output of other commands. One of the most powerful Linux tools.",
        "flags": [
            ("-i", "case-insensitive search"),
            ("-r", "searches recursively in directories"),
            ("-n", "shows the line number where the pattern was found"),
            ("-v", "inverts: shows lines that do NOT contain the pattern"),
            ("-l", "shows only filenames that contain the pattern"),
        ],
        "examples": [
            ("grep 'error' /var/log/app.log", "searches for 'error' in the log"),
            ("grep -rn 'TODO' /opt/app/src", "finds all TODOs in the source code"),
            ("ps aux | grep nginx", "checks if nginx is running"),
        ],
    },
    "awk": {
        "category": "Text",
        "description": "Processes and transforms column-structured text. Ideal for extracting specific fields from command outputs.",
        "flags": [],
        "examples": [
            ("ps aux | awk '{print $1, $2}'", "displays only the user and PID of each process"),
            ("df -h | awk '{print $5, $6}'", "shows percentage usage and mount point"),
        ],
    },
    "sed": {
        "category": "Text",
        "description": "Stream editor that substitutes, inserts or removes text in files or command outputs.",
        "flags": [("-i", "edits the file directly (in-place)")],
        "examples": [
            ("sed 's/http/https/g' config.txt", "replaces all occurrences of http with https"),
            ("sed -i 's/localhost/0.0.0.0/g' app.conf", "replaces directly in the file"),
        ],
    },
    "systemctl": {
        "category": "Services",
        "description": "Controls system services on modern Linux (systemd). Lets you start, stop, restart and check the status of services.",
        "flags": [],
        "examples": [
            ("systemctl status nginx", "checks if nginx is running"),
            ("systemctl restart nginx", "restarts nginx"),
            ("systemctl enable nginx", "configures nginx to start automatically on boot"),
        ],
    },
    "journalctl": {
        "category": "Services",
        "description": "Reads systemd logs (journald). Lets you query logs from any system service.",
        "flags": [
            ("-u service", "filters logs of a specific service"),
            ("-f", "follows logs in real time"),
            ("-n 50", "displays the last 50 lines"),
            ("--since '1 hour ago'", "logs from the last hour"),
        ],
        "examples": [
            ("journalctl -u nginx -f", "follows nginx logs in real time"),
            ("journalctl -p err --since '1 hour ago'", "all errors from the last hour"),
        ],
    },
    "docker ps": {
        "category": "Docker",
        "description": "Lists running Docker containers.",
        "flags": [
            ("-a", "includes stopped containers"),
            ("-q", "displays only IDs"),
        ],
        "examples": [
            ("docker ps", "lists running containers"),
            ("docker ps -a", "lists all containers, including stopped ones"),
        ],
    },
    "docker logs": {
        "category": "Docker",
        "description": "Displays the output logs of a container.",
        "flags": [
            ("-f", "follows logs in real time"),
            ("--tail N", "displays only the last N lines"),
        ],
        "examples": [
            ("docker logs -f my-container", "follows logs in real time"),
            ("docker logs --tail 50 my-container", "displays the last 50 lines"),
        ],
    },
    "docker exec": {
        "category": "Docker",
        "description": "Executes a command inside a running container.",
        "flags": [("-it", "interactive mode with terminal — required to open a shell")],
        "examples": [
            ("docker exec -it my-container bash", "opens a bash shell inside the container"),
            ("docker exec my-container env", "lists the container's environment variables"),
        ],
    },
}

LEARN_CATEGORIES = [
    "Files and Directories",
    "System",
    "Permissions",
    "Network",
    "Text",
    "Services",
    "Docker",
]
