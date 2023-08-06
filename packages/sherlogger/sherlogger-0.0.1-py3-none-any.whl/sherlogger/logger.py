from .config import LoggerConfig
from .models import LoggingLevel


class Logger:
    def __init__(self):
        self.file_name = None
        self.config = LoggerConfig()
        self._iprocessable = _IProcessLogger(logger=self)

    def get_logger(self, file_name) -> "_IProcessLogger":
        self.file_name = file_name
        return self._iprocessable


class _IProcessLogger:
    def __init__(self, logger):
        self._logger = logger

    @property
    def config(self):
        return self._logger.config

    @property
    def file_name(self):
        return self._logger.file_name

    def basic_config(self, **kwargs):
        for field, value in kwargs.items():
            if not hasattr(self._logger.config, field):
                raise AttributeError(
                    "No {field} in config of logger.".format(field=field)
                )

            if field == "level":
                if not isinstance(value, str):
                    raise AttributeError("Level should be provided as string.")

                value = getattr(LoggingLevel, value)

            setattr(self._logger.config, field, value)

    def set_stream(self, stream: str, type_):
        self.process_handlers()

        for idx, handler in enumerate(self._logger.config.handlers):
            if not isinstance(handler, type_):
                continue

            if handler.__class__.__name__ == "TelegramHandler":
                self._logger.config.handlers[idx].token = stream

            self._logger.config.handlers[idx].stream = stream

    def process_handlers(self) -> None:
        for idx, handler in enumerate(self._logger.config.handlers):
            if not callable(handler):
                continue

            self._logger.config.handlers[idx] = handler(logger=self)

    def check_handlers(self):
        for idx, handler in enumerate(self._logger.config.handlers):
            if callable(handler):
                handler = handler(logger=self)
                self._logger.config.handlers[idx] = handler

            yield handler

    def info(self, msg):
        for handler in self.check_handlers():
            handler.info(msg=msg)

    def debug(self, msg):
        for handler in self.check_handlers():
            handler.debug(msg=msg)

    def warning(self, msg):
        for handler in self.check_handlers():
            handler.warning(msg=msg)

    def error(self, msg):
        for handler in self.check_handlers():
            handler.error(msg=msg)

    def critical(self, msg):
        for handler in self.check_handlers():
            handler.critical(msg=msg)
