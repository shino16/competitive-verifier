from logging import (
    CRITICAL,
    DEBUG,
    ERROR,
    WARNING,
    Filter,
    LogRecord,
    basicConfig,
    Handler,
)
from typing import Optional

import competitive_verifier.github as github
import colorlog


class GitHubActionsHandler(Handler):
    def __init__(self) -> None:
        super().__init__(DEBUG)

    def emit(self, record: LogRecord) -> None:
        message = record.getMessage()
        file = record.pathname
        line = record.levelno

        if record.levelno == DEBUG:
            github.print_debug(message, file=file, line=line)
        elif record.levelno == WARNING:
            github.print_warning(message, file=file, line=line)
        elif record.levelno == ERROR or record.levelno == CRITICAL:
            github.print_error(message, file=file, line=line)


class ExceptGitHubActionsFilter(Filter):
    def __init__(self) -> None:
        super().__init__()

    def filter(self, record: LogRecord) -> bool:
        return (
            record.levelno != DEBUG
            and record.levelno != WARNING
            and record.levelno != ERROR
            and record.levelno != CRITICAL
        )


def configure_logging(
    default_level: int = DEBUG,
    in_github_actions: Optional[bool] = None,
) -> None:
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s"
    )
    level = default_level

    colorlog_handler = colorlog.StreamHandler()
    colorlog_handler.setFormatter(formatter)
    handlers: list[Handler] = [colorlog_handler]

    if in_github_actions is None:
        in_github_actions = github.is_in_github_actions()

    if in_github_actions:
        handlers.append(GitHubActionsHandler())
        colorlog_handler.addFilter(ExceptGitHubActionsFilter())

    basicConfig(
        level=level,
        handlers=handlers,
    )