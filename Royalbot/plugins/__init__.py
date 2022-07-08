import datetime
import time

from royalbot import *
from royalbot.clients import *
from royalbot.config import Config
from royalbot.helpers import *
from royalbot.utils import *
from royalbot.random_strings import *
from royalbot.version import __royal__
from royalbot.sql.gvar_sql import gvarstat
from telethon import version

royal_logo = "./royalbot/resources/pics/royalbot_logo.jpg"
cjb = "./royalbot/resources/pics/cjb.jpg"
restlo = "./royalbot/resources/pics/rest.jpeg"
shuru = "./royalbot/resources/pics/shuru.jpg"
shhh = "./royalbot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
royal_ver = __royal__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "ROYALYSERBOT"
my_group = Config.MY_GROUP or "ROYALUBOT_SUPPORT"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/ROYALYSERBOT"
royal_channel = f"[ROYALẞøT]({chnl_link})"
grp_link = "https://t.me/ROYALUBOT_SUPPORT"
royal_grp = f"[ROYALẞøT SUPPORT]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
*...ROYALẞøT...*
#Update soon...
