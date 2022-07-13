import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, InputMessagesFilterDocument

from royalbot import *
from royalbot.clients import *
from royalbot.helpers import *
from royalbot.config import *
from royalbot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from royalbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import royalbot.utils

        path = Path(f"hellbot/plugins/{shortname}.py")
        name = "royalbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Royalbot - Successfully imported " + shortname)
    else:
        import hellbot.utils

        path = Path(f"hellbot/plugins/{shortname}.py")
        name = "royalbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Royal
        mod.R1 = Royal
        mod.R2 = R2
        mod.R3 = R3
        mod.R4 = R4
        mod.R5 = R5
        mod.Royal = Royal
        mod.Royalbot = Royalbot
        mod.tbot = RoyalBot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = royalbot.utils
        mod.Config = Config
        mod.borg = bot
        mod.royalbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_royal = delete_royal
        mod.eod = delete_royal
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.royal_cmd = royal_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = royalbot.utils
        sys.modules["userbot"] = royalbot
        # support for paperplaneextended
        sys.modules["userbot.events"] = royalbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["royalbot.plugins." + shortname] = mod
        LOGS.info("⚡ ROYALBOT ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"royalbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel:
        LOGS.info("⚡ ROYALẞØT ⚡ - PLUGIN CHANNEL DETECTED.")
        LOGS.info("⚡ ROYALẞØT ⚡ - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"royalbot/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "royalbot/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# royalbot
