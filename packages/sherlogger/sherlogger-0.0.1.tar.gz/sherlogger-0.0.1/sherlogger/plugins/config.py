import configparser
from dataclasses import dataclass


@dataclass
class TelegramBot:
    token: str
    chat_ids: list


@dataclass
class Config:
    telegram_bot: TelegramBot


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        telegram_bot=TelegramBot(
            token=tg_bot["token"],
            chat_ids=tg_bot["chat_ids"].split(",")
            if "," in tg_bot["chat_ids"]
            else [tg_bot["chat_ids"]],
        ),
    )
