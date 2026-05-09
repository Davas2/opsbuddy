import json
from pathlib import Path

_CONFIG_DIR = Path.home() / ".opsbuddy"
_CONFIG_FILE = _CONFIG_DIR / "config.json"

_DEFAULTS = {"language": "pt"}


def load() -> dict:
    if not _CONFIG_FILE.exists():
        return dict(_DEFAULTS)
    try:
        return {**_DEFAULTS, **json.loads(_CONFIG_FILE.read_text())}
    except (json.JSONDecodeError, OSError):
        return dict(_DEFAULTS)


def save(data: dict) -> None:
    _CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    _CONFIG_FILE.write_text(json.dumps(data, indent=2))


def get(key: str):
    return load().get(key, _DEFAULTS.get(key))


def set(key: str, value) -> None:
    data = load()
    data[key] = value
    save(data)
