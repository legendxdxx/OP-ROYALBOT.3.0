import glob
import os
import sys

from pathlib import Path
from telethon import Button, TelegramClient
from telethon.utils import get_peer_id

from royalbot import LOGS, bot, tbot
from royalbot.clients.session import Royal, R2, R3, R4, R5
from royalbot.config import Config
from royalbot.utils import join_it, load_module, logger_check, start_msg, update_sudo, plug_channel
from royalbot.version import __royal__ as royalver

hl = Config.HANDLER

ROYAL_PIC = "https://telegra.ph/file/cb0bd62632a3a2b6b2726.jpg"


# Client Starter
async def royals(session=None, client=None, session_name="Main"):
    if session:
        LOGS.info(f"••• Starting Client [{session_name}] •••")
        try:
            await client.start()
            return 1
        except:
            LOGS.error(f"Error in {session_name}!! Check & try again!")
            return 0
    else:
        return 0


# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as hell:
            path1 = Path(royal.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"royalbot/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))      


# Final checks after startup
async def royal_is_on(total):
    await update_sudo()
    await logger_check(bot)
    await start_msg(tbot, ROYAL_PIC, royalver, total)
    await join_it(bot)
    await join_it(R2)
    await join_it(R3)
    await join_it(R4)
    await join_it(R5)


# Royalbot starter...
async def start_royalbot():
    try:
        tbot_id = await tbot.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        bot.tgbot = tbot
        LOGS.info("••• Starting RoyalBot •••")
        C1 = await royals(Config.ROYALBOT_SESSION, bot, "ROYAL_SESSION")
        C2 = await royals(Config.SESSION_2, R2, "SESSION_2")
        C3 = await royals(Config.SESSION_3, R3, "SESSION_3")
        C4 = await royals(Config.SESSION_4, R4, "SESSION_4")
        C5 = await royals(Config.SESSION_5, R5, "SESSION_5")
        await tbot.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("••• RoyalBot Startup Completed •••")
        LOGS.info("••• Starting to load Plugins •••")
        await plug_load("royalbot/plugins/*.py")
        await plug_channel(bot, Config.PLUGIN_CHANNEL)
        LOGS.info("⚡ Your ROYALBOT Is Now Working ⚡")
        LOGS.info("Join @ROYALYSERBOT for Updates. Also join chat group to get help regarding to ROYALẞøT.")
        LOGS.info(f"» Total Clients = {str(total)} «")
        await royal_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


bot.loop.run_until_complete(start_royalbot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass


# royalbot
