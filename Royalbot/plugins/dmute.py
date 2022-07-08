@royal_cmd(
    pattern="dmute( (.*)|$)",
)
async def startmute(event):
    xx = await event.eor("`Muting...`")
    input_ = event.pattern_match.group(1).strip()
    if input_:
        try:
            userid = await event.client.parse_id(input_)
        except Exception as x:
            return await xx.edit(str(x))
    elif event.reply_to_msg_id:
        reply = await event.get_reply_message()
        userid = reply.sender_id
        if reply.out or userid in [royalbot.me.id, asst.me.id]:
            return await xx.eor("`You cannot mute yourself or your assistant bot.`")
    elif event.is_private:
        userid = event.chat_id
    else:
        return await xx.eor("`Reply to a user or add their userid.`", time=5)
    chat = await event.get_chat()
    if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
        if not chat.admin_rights.delete_messages:
            return await xx.eor("`No proper admin rights...`", time=5)
    elif "creator" not in vars(chat) and not event.is_private:
        return await xx.eor("`No proper admin rights...`", time=5)
    if is_muted(event.chat_id, userid):
        return await xx.eor("`This user is already muted in this chat.`", time=5)
    mute(event.chat_id, userid)
    await xx.eor("`Successfully muted...`", time=3)
