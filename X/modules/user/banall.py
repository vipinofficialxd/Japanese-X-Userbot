from pyrogram import Client, filters
from config import OWNER_ID
from config import CMD_HANDLER as cmd

@Client.on_message(filters.command("banall", cmd) & filters.me)
async def banall(client, message):
    if not message.from_user:
        return
    ok = await message.edit("Getting Chat Members......")
    mem = []
    async for x in client.get_chat_members(message.chat.id):
        mem.append(x.user.id)
    try:
        await ok.edit("Banning Chat Members....")
    except:
        await message.reply("Bannin Chat Members")
    a = 0
    b = 0
    for y in mem:
        try:
            await client.ban_chat_member(message.chat.id, y)
            a += 1
        except:
            b += 1
            pass
    try:
        await ok.edit(f"**Done ✅**\n\n{a} Banned..!!\n \n{b} Failed..!!")
    except:
        await message.reply(f"**Done ✅\n\n{a} Banned..!!\n \n {b} Failed..!!")

add_command_help(
    "•─╼⃝𖠁 ʙᴀɴᴀʟʟ",
    [
        ["banall", "Tᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ."],
    ],
)