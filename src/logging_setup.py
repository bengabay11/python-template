import logging
from typing import TextIO

import colorlog

LOG_COLORS = {
    "DEBUG": "white",
    "INFO": "bold_green",
    "WARNING": "bold_yellow",
    "ERROR": "bold_red",
    "CRITICAL": "bold_white,bg_red",
}


def create_colored_stream_handler() -> colorlog.StreamHandler[TextIO]:
    handler = colorlog.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        "%(bold_black)s%(asctime)s%(reset)s "
        "%(log_color)s%(levelname)s%(reset)s - "
        "%(cyan)s%(name)s%(reset)s - "
        "%(light_white)s%(message)s%(reset)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors=LOG_COLORS,
        style="%",
    )
    handler.setFormatter(formatter)
    return handler


def add_logger_handlers(logger: logging.Logger) -> None:
    handlers = [
        create_colored_stream_handler(),
    ]
    for handler in handlers:
        if not isinstance(handler, logging.Handler):
            error_message = f"Expected logging.Handler, got {type(handler).__name__}"
            raise TypeError(error_message)
        logger.addHandler(handler)


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    add_logger_handlers(logger)
    return logger
