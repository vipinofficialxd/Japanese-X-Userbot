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

# Credits: NOBITA XD  AND TRYTOLIVEALONE 
# Copyright (C) 2024 JAPANESE X USERBOT 
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 



from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from X.helpers.basic import *
from X.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER
from config import SUDO_USERS
from X.utils import *
from urllib.parse import quote

import requests
import os
import json
import random

from .help import *


@Client.on_message(
    filters.command(["ai"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def openai(client: Client, message: Message):
    def chat_with_api(model, prompt):
    url = f"https://tofu-api.onrender.com/chat/{model}/{prompt}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["code"] == 2:
            return data["content"]
        else:
            return "Error: Unable to get response from the API"
    else:
        return "Error: Unable to connect to the API"

add_command_help(
    "•─╼⃝𖠁 ᴏᴘᴇɴᴀɪ",
    [
        ["ai", "Tᴏ Aꜱᴋ Sᴏᴍᴇᴛʜɪɴɢ Tᴏ Cʜᴀᴛ Gᴘᴛ"],
    ],
)
