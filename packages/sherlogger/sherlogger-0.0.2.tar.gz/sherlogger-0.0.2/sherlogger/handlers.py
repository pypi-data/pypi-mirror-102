from abc import ABC, abstractmethod
from datetime import datetime
from inspect import getframeinfo, stack

from .logger import Logger
from .models import BColors, LoggingLevel


class AbstractHandler(ABC):
    @abstractmethod
    def info(self, msg: str) -> None:
        pass

    @abstractmethod
    def debug(self, msg: str) -> None:
        pass

    @abstractmethod
    def warning(self, msg: str) -> None:
        pass

    @abstractmethod
    def error(self, msg: str) -> None:
        pass

    @abstractmethod
    def critical(self, msg: str) -> None:
        pass


class FileSystemHandler(AbstractHandler):
    def __init__(self, logger: Logger) -> None:
        self.stream = None
        self._logger = logger

    def _init_msg(self, msg: str, lineno: int, level):
        now_time = datetime.utcnow()
        file_name = self._logger.file_name
        msg_format = self._logger.config.formatter

        return msg_format.format(
            asctime=now_time,
            filename=file_name,
            lineno=lineno,
            levelname=level,
            message=msg,
        )

    def _write(self, msg: str, lineno: int, color, level):
        message = self._init_msg(msg=msg, lineno=lineno, level=level)
        if self.stream is None:
            print(color.value + message + BColors.ENDC.value)
            return

        if level.value[1] != "INFO":
            with open(
                self.stream + LoggingLevel.INFO.value[1].lower() + ".log", "a+"
            ) as f:
                f.write(message + "\n")

        with open(self.stream + level.value[1].lower() + ".log", "a+") as f:
            f.write(message + "\n")
            print(color.value + message + BColors.ENDC.value)

    def info(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.INFO.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        self._write(
            msg=msg, lineno=caller.lineno, color=BColors.OKBLUE, level=LoggingLevel.INFO
        )

    def debug(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.DEBUG.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        self._write(
            msg=msg,
            lineno=caller.lineno,
            color=BColors.OKCYAN,
            level=LoggingLevel.DEBUG,
        )

    def warning(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.WARNING.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        self._write(
            msg=msg,
            lineno=caller.lineno,
            color=BColors.WARNING,
            level=LoggingLevel.WARNING,
        )

    def error(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.ERROR.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        self._write(
            msg=msg, lineno=caller.lineno, color=BColors.FAIL, level=LoggingLevel.ERROR
        )

    def critical(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.CRITICAL.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        self._write(
            msg=msg,
            lineno=caller.lineno,
            color=BColors.FAIL,
            level=LoggingLevel.CRITICAL,
        )
