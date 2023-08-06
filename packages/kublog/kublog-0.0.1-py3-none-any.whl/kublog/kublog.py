import logging
import sys
from contextvars import copy_context
from typing import Optional
import os


TRACE_ID_KEY = 'trace_id'
TEST_ENV = 'test'
DEFAULT_FORMAT_STR = '%(levelname)s:%(filename)s:%(lineno)d: %(message)s'


class KubricLogAdapter(logging.LoggerAdapter):
    """
    This adapter checks for a trace_id in the current context. If a trace_id
    is available, it is prepended to the msg.
    """
    def process(self, msg, kwargs):
        # try to get trace_id from context vars
        context = copy_context()
        trace_id = None
        for item in context.items():
            # Ugly hack because contextvars doesn't provide a
            # dictionary like interface to get a contextvar by name.
            if item[0].name == TRACE_ID_KEY:
                trace_id = item[1]

        # add trace_id to msg if available and returns
        new_msg = f'[{trace_id}] {msg}' if trace_id else msg
        return new_msg, kwargs


class Colors:
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"


class ColorfulFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None,
                 style: str = '%', validate: bool = True) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt, style=style,
                         validate=validate)
        self.FORMATS = {
            logging.DEBUG: Colors.grey + fmt + Colors.reset,
            logging.INFO: Colors.grey + fmt + Colors.reset,
            logging.WARNING: Colors.yellow + fmt + Colors.reset,
            logging.ERROR: Colors.red + fmt + Colors.reset,
            logging.CRITICAL: Colors.bold_red + fmt + Colors.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name: str = None, handler: logging.Handler = None, level=logging.INFO,
               formatting: str = DEFAULT_FORMAT_STR, propagate: bool = False,
               print_trace_id: bool = True):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = propagate

    if handler is None:
        handler = sys.stdout
        new_handler = logging.StreamHandler(handler)
        new_handler.setLevel(level)

        # If APP_ENV is `test` or unset we use a colorful formatter 🌈.
        # Else we use a plain formatter to avoid passing ANSI color characters
        # into staging/prod env logs
        app_env = os.getenv('APP_ENV', TEST_ENV)
        if app_env == TEST_ENV:
            formatter = ColorfulFormatter(formatting)
        else:
            formatter = logging.Formatter(formatting)

        new_handler.setFormatter(formatter)
        if logger.hasHandlers():
            # To prevent the same stream handler from being added multiple times to the
            # same logger. If the same handler (stdout in this case) is added multiple
            # times to the same logger then each log will show up more and more times in
            # that stream.
            logger.handlers.clear()
    else:
        new_handler = handler
    logger.addHandler(new_handler)

    if print_trace_id:
        logger = KubricLogAdapter(logger, None)
    return logger
