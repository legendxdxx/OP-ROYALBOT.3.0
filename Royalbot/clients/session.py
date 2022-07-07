import sys

from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from royalbot.config import Config


if Config.ROYALBOT_SESSION:
    session = StringSession(str(Config.ROYALBOT_SESSION))
else:
    session = "Royalbot"

try:
    Royal = TelegramClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"ROYALBOT_SESSION - {e}")
    sys.exit()


if Config.SESSION_2:
    session2 = StringSession(str(Config.SESSION_2))
    R2 = TelegramClient(
        session=session2,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    R2 = None


if Config.SESSION_3:
    session3 = StringSession(str(Config.SESSION_3))
    R3 = TelegramClient(
        session=session3,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    R3 = None


if Config.SESSION_4:
    session4 = StringSession(str(Config.SESSION_4))
    R4 = TelegramClient(
        session=session4,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    R4 = None


if Config.SESSION_5:
    session5 = StringSession(str(Config.SESSION_5))
    R5 = TelegramClient(
        session=session5,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    R5 = None


Royalbot = TelegramClient(
    session="Royal-TBot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
