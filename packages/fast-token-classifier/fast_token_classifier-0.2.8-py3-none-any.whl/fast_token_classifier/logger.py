import logging
from typing import Optional

from rich.logging import RichHandler
from typeguard import typechecked


@typechecked
def get_console_logger(name: Optional[str] = "my_logger", sep: str = "-") -> logging.Logger:
    """This is used to create a logger object."""

    # Create logger if it doesn't exist
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler with formatting
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            f"%(asctime)s {sep} %(name)s {sep} [%(levelname)s] {sep} %(message)s",
            datefmt="%y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)

        # Add console handler to the logger
        logger.addHandler(console_handler)

    return logger


@typechecked
def get_rich_logger(name: Optional[str] = "richLogger") -> logging.Logger:
    """This is used to create a logger object with RichHandler."""

    # Create logger if it doesn't exist
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler with formatting
        console_handler = RichHandler(
            rich_tracebacks=True,
            level=logging.DEBUG,
            log_time_format="%y-%m-%d %H:%M:%S",
        )
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(f"%(message)s")
        console_handler.setFormatter(formatter)

        # Add console handler to the logger
        logger.addHandler(console_handler)

    return logger
