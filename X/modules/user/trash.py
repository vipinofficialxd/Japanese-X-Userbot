import heroku3
from os import getenv
from config import SUDO_USERS 
from config import OWNER_ID
from config import HEROKU_APP_NAME, HEROKU_API_KEY
from pyrogram import Client, filters
from pyrogram.types import Message

ok = []

@Client.on_message(filters.command("addsudo", ".") & filters.user(OWNER_ID))
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.reply_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ")
        return
    if user.id == client.me.id:
        return await ex.edit("*ᴘʀᴏᴍᴏᴛɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ.....**")

    try:
        if user.id in SUDO_USERS:
            return await ex.edit("ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ɪɴ ꜱᴜᴅᴏ")
        SUDO_USERS.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) ᴘʀᴏᴍᴏᴛᴇᴅ ᴛᴏ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ")
    
    except Exception as e:
        await ex.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
        return

@Client.on_message(
    filters.command(["sudolist"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gbanlist(client: Client, message: Message):
    users = SUDO_USERS
    ex = await message.edit_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if not users:
        return await ex.edit("ɴᴏ ᴜꜱᴇʀꜱ ʜᴀᴠᴇ ʙᴇᴇɴ ꜱᴇᴛ ʏᴇᴛ")
    gban_list = "**sᴜᴅᴏ ᴜꜱᴇʀs:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count}** `{i}`\n"
    return await ex.edit(gban_list)
