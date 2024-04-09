import asyncio

from pyrogram import Client, filters
from config import OWNER_ID
from config import CMD_HANDLER as cmd

from .help import *

@Client.on_message(filters.command("bsdk", cmd) & filters.me)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "gulli":
    await event.edit("gulli")
    animation_chars = [
            "**OK**",
            "**SUNN MADERCHOD**",
            "`TERI MAA KA BHOSDA`",
            "`BEHEN K LUND`",
            "**TERI MAA KA DUD**",
            "`MERA LAWDA LELE TU AGAR CHAIYE TOH`",
            "`GAANDU`",
            "**CHUTIYA**",
            "`TERI MAA KI CHUT PE JCB CHADHAA DUNGA`",
            "**SAMJHAA LAWDE**",
            "**YA DU TERE GAAND ME TAPAA TAP😂**",
            "`TERI BEHEN MERA ROZ LETI HAI`",
            "`TERI GF K SAATH MMS BANAA CHUKA HU🙈🤣🤣`",
            "`TU CHUTIYA TERA KHANDAAN CHUTIYA`",
            "**Yeahhhhhh**",
            "`AUR KITNA BOLU BEY MANN BHAR GAYA MERA🤣`",
            "**Ab nikal ja jaake chkko k saath hilaa**",
            "`😂😂😂🤣🤣`"
        ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
      
add_command_help(
    "•─╼⃝𖠁 BSDK",
    [
        ["bsdk", "ᴛᴏ BSDK ᴀʙᴜꜱᴇ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ."],
    ],
)
