# OpsBuddy

OpsBuddy is an open-source interactive CLI assistant designed to help developers, students, and system administrators understand and operate Linux servers more easily.

The project transforms the terminal into a guided environment where users can inspect system resources, analyze processes, manage containers, and learn Linux commands without needing to memorize complex syntax.

OpsBuddy acts as both an operational tool and an educational assistant for Linux and DevOps environments.

---

## Motivation

Working with Linux servers can be challenging, especially for beginners. Many users struggle to understand system metrics, interpret command outputs, or even know which command to use for a specific task.

OpsBuddy was created to bridge that gap by providing:

- A guided terminal experience
- Simplified infrastructure diagnostics
- Educational explanations of commands
- Interactive navigation inside the CLI

The goal is to make server operations more accessible while helping users learn how Linux systems work.

---

## Key Features

OpsBuddy provides an interactive terminal interface with multiple modules:

### System Overview

Displays a summary of system resources:

- CPU usage
- Memory usage
- Disk usage
- System uptime

---

### Memory Analysis

Helps users inspect memory consumption and identify processes using the most memory.

Example commands used internally:


free -h
ps aux --sort=-%mem


---

### CPU Monitoring

Displays system load and CPU usage.

Examples:


top
uptime


---

### Disk Usage

Displays disk usage information and helps identify directories consuming large amounts of storage.

Examples:


df -h
du -sh *


---

### Process Management

Allows users to inspect running processes.

Example:


ps aux


Users may optionally terminate processes if necessary.

---

### Docker Support

If Docker is installed, OpsBuddy can inspect containers.

Examples:


docker ps
docker logs
docker restart


---

### Network Diagnostics

Provides visibility into network configuration and open ports.

Examples:


ip a
ss -tulnp
ping


---

### System Diagnostics

OpsBuddy can run automated checks to detect potential system issues.

Example output:


Running diagnostics...

CPU usage: OK
Memory usage: OK
Disk usage: WARNING
Docker: running
Network: OK


---

### Learning Mode

OpsBuddy includes an educational module that explains common Linux commands.

Example:


Command: ls

Description:
Lists files and directories.

Example:
ls -lah

Options:
-l long format
-a show hidden files
-h human readable


---

## Installation

### Clone the repository


git clone https://github.com/yourusername/opsbuddy.git

cd opsbuddy


### Install dependencies


pip install -r requirements.txt


### Run the tool


python main.py


Future releases will support installation via:


pip install opsbuddy


---

## Example Interface


OpsBuddy - Server Assistant

1 - System Overview
2 - Memory Usage
3 - Disk Usage
4 - CPU Usage
5 - Processes
6 - Docker
7 - Networking
8 - Diagnostics
9 - Learn Linux Commands

0 - Exit


---

## Technology Stack

OpsBuddy is built with:

- Python
- Rich (terminal formatting)
- Typer (CLI framework)
- Prompt Toolkit / Questionary (interactive CLI)
- Psutil (system metrics)

---

## Project Structure


opsbuddy/

cli/
modules/
services/
utils/
config/
tutorials/

main.py


---

## Open Source

OpsBuddy is an open-source project and contributions are welcome.

The repository is hosted on GitHub and accepts:

- Pull requests
- Bug reports
- Feature suggestions
- Community improvements

---

## Contributing

We welcome contributions from the community.

Typical workflow:

1. Fork the repository
2. Create a new branch
3. Implement your feature or fix
4. Submit a pull request

---

## Roadmap

Planned future improvements include:

- AI-assisted troubleshooting
- Plugin architecture
- Kubernetes integration
- Cloud integrations
- Web dashboard
- Multi-server management

---

## Related Technologies

OpsBuddy is designed to work alongside modern infrastructure tools such as:

- Docker
- Kubernetes
- Prometheus
- Grafana

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute the software.

---

## Vision

The long-term vision of OpsBuddy is to become a universal DevOps terminal assistant that simplifie
