from telethon.utils import get_peer_id
from telethon.tl.functions.users import GetFullUserRequest

from .session import Royal, R2, R3, R4, R5
from royalbot.sql.gvar_sql import gvarstat


async def clients_list():
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await royal.get_me()
    user_ids.append(main_id.id)

    try:
        if H2 is not None:
            id2 = await R2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if H3 is not None:
            id3 = await R3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if H4 is not None:
            id4 = await R4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if H5 is not None:
            id5 = await R5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        ForGo10God = uid.user.id
        Royal_USER = uid.user.first_name
        royal_mention = f"[{Royal_USER}](tg://user?id={ForGo10God})"
    else:
        client = await event.client.get_me()
        uid = get_peer_id(client)
        ForGo10God = uid
        Royal_USER = client.first_name
        royal_mention = f"[{Royal_USER}](tg://user?id={ForGo10God})"
    return ForGo10God, Royal_USER, royal_mention
