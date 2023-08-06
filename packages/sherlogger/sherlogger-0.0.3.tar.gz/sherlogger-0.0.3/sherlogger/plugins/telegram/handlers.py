import asyncio
from datetime import datetime
from inspect import getframeinfo, stack

import aiohttp

from sherlogger.handlers import AbstractHandler
from sherlogger.logger import Logger
from sherlogger.models import BColors, LoggingLevel
from sherlogger.plugins.config import load_config

from .executor import run_in_separated_thread


class TelegramHandler(AbstractHandler):
    def __init__(self, logger: Logger):
        # Define logger
        self._logger = logger

        # Load configs of telegram bot
        self.config = load_config(self._logger.config.plugins_ini_path)
        self.chat_ids = self.config.telegram_bot.chat_ids
        self.token = self.config.telegram_bot.token

    def _init_msg(self, msg, lineno, level):
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

    async def _post(self, msg):
        for chat_id in self.chat_ids:
            payload = {"chat_id": chat_id, "text": msg, "parse_mode": "HTML"}
            url = "https://api.telegram.org/bot{api_token}/sendMessage".format(
                api_token=self.token
            )

            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=payload) as _:
                    await asyncio.sleep(0)

    def info(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.INFO.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        message = self._init_msg(msg=msg, lineno=caller.lineno, level=LoggingLevel.INFO)
        print(BColors.OKBLUE.value + message + BColors.ENDC.value)

        run_in_separated_thread(self._post, message)

    def debug(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.DEBUG.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        message = self._init_msg(
            msg=msg, lineno=caller.lineno, level=LoggingLevel.DEBUG
        )
        print(BColors.OKCYAN.value + message + BColors.ENDC.value)

        run_in_separated_thread(self._post, message)

    def warning(self, msg) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.WARNING.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        message = self._init_msg(
            msg=msg, lineno=caller.lineno, level=LoggingLevel.WARNING
        )
        print(BColors.WARNING.value + message + BColors.ENDC.value)

        run_in_separated_thread(self._post, message)

    def error(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.ERROR.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        message = self._init_msg(
            msg=msg, lineno=caller.lineno, level=LoggingLevel.ERROR
        )
        print(BColors.FAIL.value + message + BColors.ENDC.value)

        run_in_separated_thread(self._post, message)

    def critical(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.CRITICAL.value[0]:
            return

        caller = getframeinfo(stack()[-1][0])
        message = self._init_msg(
            msg=msg, lineno=caller.lineno, level=LoggingLevel.CRITICAL
        )
        print(BColors.FAIL.value + message + BColors.ENDC.value)

        run_in_separated_thread(self._post, message)
