"""
Logger utilities for setting up detailed logging configurations.
"""

import logging
from typing import Optional


def setup_detailed_logger(
    log_file: Optional[str] = "detailed_log.log", log_level: int = logging.DEBUG
) -> logging.Logger:
    """
    Configures a detailed logger that includes file name, line number, function name, and timestamp.

    :param log_file: The name of the file to write logs to (default: 'detailed_log.log').
    :param log_level: The minimum logging level (default: logging.DEBUG).
    :return: A configured logger object.
    """
    log = logging.getLogger(__name__)  # Renamed to 'log' to avoid outer scope conflict
    log.setLevel(log_level)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(console_handler)

    return log


# Usage of the logger function
logger = setup_detailed_logger(log_file="app_log.log", log_level=logging.DEBUG)
