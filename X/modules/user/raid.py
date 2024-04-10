#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, RAID
from config import OWNER_ID
from config import CMD_HANDLER as cmd

from .help import *

@Client.on_message(filters.command("raid", cmd) & filters.me)
async def raid(x: Client, message: Message):  
    NOBI = message.text.split(" ")

    if len(NOBI) > 2:
        ok = await x.get_users(NOBI[2])  
        id = ok.id
        if id in MASTERS:
            await message.reply_text("𝐧𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐠𝐮𝐲𝐬 𝐢𝐬 𝐭𝐡𝐞 𝐦𝐚𝐬𝐭𝐞𝐫 𝐨𝐟 𝐣𝐚𝐩𝐚𝐧𝐞𝐬𝐞ʀ ☠️")
        elif id == OWNER_ID:
            await message.reply_text("𝐧𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐠𝐮𝐲 𝐢𝐬 𝐨𝐰𝐧𝐞𝐫 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 🥀")
        elif id in OWNER_ID:
            await message.reply_text("𝐧𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐠𝐮𝐲 𝐢𝐬 𝐬𝐮𝐝𝐨 𝐮𝐬𝐞𝐫 💗")
        else:
            counts = int(NOBI[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await x.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(NOBI) == 2):
        user_id = message.reply_to_message.from_user.id
        ok = await x.get_users(user_id)
        id = ok.id
        if id in MASTERS:
            await message.reply_text("𝐧𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐠𝐮𝐲𝐬 𝐢𝐬 𝐭𝐡𝐞 𝐦𝐚𝐬𝐭𝐞𝐫 𝐨𝐟 𝐣𝐚𝐩𝐚𝐧𝐞𝐬𝐞 ☠️")
        elif id == OWNER_ID:
            await message.reply_text("𝐧𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐠𝐮𝐲 𝐢𝐬 𝐨𝐰𝐧𝐞𝐫 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 🥀")
        elif id in OWNER_ID:
            await message.reply_text("𝐧𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐠𝐮𝐲 𝐢𝐬 𝐬𝐮𝐝𝐨 𝐮𝐬𝐞𝐫 💗")
        else:
            counts = int(NOBI[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await x.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".𝐫𝐚𝐢𝐝 𝟏𝟎 <𝐮ꜱ𝐞𝐫𝐧𝐚𝐦𝐞 𝐨𝐟 𝐮ꜱ𝐞𝐫> <𝐫𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚 𝐮ꜱ𝐞𝐫>")




add_command_help(
    "•─╼⃝𖠁 raid",
    [
        ["raid", "Tᴏ raid ᴀʟʟ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ."],
    ],
)
