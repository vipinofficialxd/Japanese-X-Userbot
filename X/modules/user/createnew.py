from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["create"], ["."]))
async def gcch(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit(f".ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    nobigey = await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ....")
    fuk = """ʙʏ - @Japanese_Userbot_Support

𝐑𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐑𝐞𝐠𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬❤️🔥

1 𝐍𝐨 𝐀𝐛𝐮𝐬𝐞 

2.𝐍𝐨 personal 𝐦𝐞𝐬𝐬𝐚𝐠𝐞

3.𝐍𝐨 𝐥𝐢𝐧𝐤𝐬

4.𝐃𝐨𝐧'𝐭 𝐅𝐢𝐠𝐡𝐭 

5.𝐑𝐞𝐬𝐩𝐞𝐜𝐭 𝐆𝐢𝐫𝐥𝐬 𝐥𝐢𝐤𝐞 𝐲𝐨𝐮𝐫 𝐒𝐢𝐬𝐭𝐞?ᴘ"""
    if group_type == "group": 
        _id = await client.create_supergroup(group_name, fuk)
        await nobigey.edit(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ....",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":  
        _id = await client.create_channel(group_name, fuk)
        await nobigey.edit(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ....",
            disable_web_page_preview=True,
        )
