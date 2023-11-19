# ruff: noqa: F401
from os import getenv
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv
from loguru import Message, Record, logger
from rich.console import Console, ConsoleOptions, Group, JustifyMethod, OverflowMethod
from rich.text import Text

from maxgradient.gradient import Gradient

CWD = Path.cwd()
load_dotenv(CWD / ".env")
LOG_DIR = CWD / "logs"
if not LOG_DIR.exists():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
if len(list(LOG_DIR.iterdir())) > 5:
    log_levels: list[str] = [
        "debug.log",
        "info.log",
        "warning.log",
        "error.log",
        "critical.log",
    ]
    for level in log_levels:
        path: Path = LOG_DIR / level
        if not path.exists():
            with open(path, "w", encoding="utf-8") as outfile:
                outfile.write("")


console = Console()
FORMAT: str = """{time:hh:mm:ss:SSS A} | {file.name: ^13} |  \
    Line {line: ^5} | {level: ^8} ﰲ  {message}"""


def rich_filter(record: Record) -> bool:
    """Filter log records to only those that have a rich message."""
    log_to_console: int = int(record["extra"]["log_to_console"])
    level = record["level"].no
    return level >= log_to_console


logger.remove()
loggers = logger.configure(
    handlers=[
        dict(  # 1 - debug.log
            sink=LOG_DIR / "debug.log",
            level="DEBUG",
            format=FORMAT,
            backtrace=True,
            diagnose=True,
            colorize=True,
        ),
        dict(  # 2 - info.log
            sink=LOG_DIR / "info.log",
            level="INFO",
            format=FORMAT,
            backtrace=True,
            diagnose=True,
            coolorize=True,
        ),
        dict(  # 3 - warning.log
            sink=LOG_DIR / "warning.log",
            level="WARNING",
            format=FORMAT,
            backtrace=True,
            diagnose=True,
            colorize=True,
        ),
        dict(  # 4 - error.log
            sink=LOG_DIR / "error.log",
            level="ERROR",
            format=FORMAT,
            backtrace=True,
            diagnose=True,
            colorize=True,
        ),
        dict(  # 5 - critical.log
            sink=LOG_DIR / "critical.log",
            level="CRITICAL",
            format=FORMAT,
            backtrace=True,
            diagnose=True,
            colorize=True,
        ),
        dict(  # 6 - console
            sink=lambda msg: console.log(
                Gradient(msg, colors=["#afff00", "#8ddd00", "#6ccc00", "#00ff00"]),
                log_locals=True,
            ),
            level="DEBUG",
            format="{message}",
            backtrace=True,
            diagnose=True,
            colorize=True,
            filter=rich_filter,
        ),
    ],
    extra={"run": getenv("RUN"), "log_to_console": getenv("LOG_TO_CONSOLE")},
    activation=[("maxgradient.*", False)],
)
log = logger.bind()
