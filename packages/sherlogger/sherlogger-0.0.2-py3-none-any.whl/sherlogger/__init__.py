from inspect import getmodule, stack

from .handlers import FileSystemHandler
from .logger import Logger, LoggerConfig
from .plugins.telegram.handlers import TelegramHandler

_frame = stack()[-1]
_module = getmodule(_frame[0])

_module_name = "__main__"
if _module is not None:
    _module_name = _module.__file__.split("/")[-1]

sherlog = Logger()

logger = sherlog.get_logger(_module_name)
logger.basic_config(handlers=[FileSystemHandler], level="INFO")
logger.set_stream("./", FileSystemHandler)


def get_telegram_logger(filename: str, ini_file_path: str):
    _tlogger = sherlog.get_logger(filename)
    _tlogger.basic_config(handlers=[TelegramHandler], level="INFO", plugins_ini_path=ini_file_path)
    return _tlogger


__all__ = [
    "logger",
    "sherlog",
    "LoggerConfig",
    "FileSystemHandler",
    "get_telegram_logger",
]
