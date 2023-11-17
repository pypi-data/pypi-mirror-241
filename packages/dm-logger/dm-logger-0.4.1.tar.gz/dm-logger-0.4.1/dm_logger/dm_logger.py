from logging.handlers import RotatingFileHandler
from typing import Callable
import logging
import re
from .file_handlers import get_format_string, get_rotating_file_handler
from .stream_handlers import get_stdout_handler, get_stderr_handler
from .options import Options


class DMLogger:
    options: Options = Options
    _loggers: dict = {}
    _file_handlers: dict = {}

    def __init__(
        self,
        name: str,
        level: str = "DEBUG",
        write_logs: bool = True,
        print_logs: bool = True
    ):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        self._logger = logging.getLogger(name)
        level = logging.getLevelName(level.upper())
        self._logger.setLevel(level)
        options = DMLogger.options
        formatter = logging.Formatter(get_format_string(options), datefmt='%d-%m-%Y %H:%M:%S')

        if write_logs:
            if options.file_name in DMLogger._file_handlers:
                rotating_file_handler = DMLogger._file_handlers.get(options.file_name)
            else:
                rotating_file_handler = get_rotating_file_handler(options, formatter)
                DMLogger._file_handlers[options.file_name] = rotating_file_handler
            self._logger.addHandler(rotating_file_handler)

        if print_logs:
            self._logger.addHandler(get_stdout_handler(formatter))
            self._logger.addHandler(get_stderr_handler(formatter))

    def __new__(cls, name, *args, **kwargs):
        if name in cls._loggers:
            return cls._loggers[name]
        else:
            instance = super(DMLogger, cls).__new__(cls)
            cls._loggers[name] = instance
            return instance

    def debug(self, message: any = None, **kwargs) -> None:
        self._log(self._logger.debug, message, **kwargs)

    def info(self, message: any = None, **kwargs) -> None:
        self._log(self._logger.info, message, **kwargs)

    def warning(self, message: any = None, **kwargs) -> None:
        self._log(self._logger.warning, message, **kwargs)

    def error(self, message: any = None, **kwargs) -> None:
        self._log(self._logger.error, message, **kwargs)

    def critical(self, message: any = None, **kwargs) -> None:
        self._log(self._logger.critical, message, **kwargs)

    @staticmethod
    def _log(level_func: Callable, message: any, **kwargs) -> None:
        message = "-- " + str(message) if not (message is None) else ""
        if kwargs:
            dict_string = re.sub(r"'(\w+)':", r"\1:", str(kwargs))
            message = f"{dict_string} {message}"
        level_func(message, stacklevel=3)
