import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message
from jikanpy import Jikan
from googletrans import Translator

from X.helpers.PyroHelpers import GetChatID, ReplyCheck
from .help import *

jikan = Jikan()
translator = Translator()

@Client.on_message(filters.command(["anime"], ".") & filters.me)
async def anime_search(bot: Client, message: Message):
    text = message.text.split(maxsplit=1)[1]
    anime = jikan.search('anime', text)['results'][0]
    background = anime['background']
    synopsis = anime['synopsis']
    translated_background = await translate(background, 'en')
    translated_synopsis = await translate(synopsis, 'hi')

    AnimeInfo = f"""
🎀 • *Title:* {anime['title']}
🎋 • *Format:* {anime['type']}
📈 • *Status:* {anime['status'].upper().replace('_', ' ')}
🍥 • *Total Episodes:* {anime['episodes']}
🎈 • *Duration:* {anime['duration']}
✨ • *Based on:* {anime['source'].upper()}
💫 • *Released:* {anime['aired']['from']}
🎗 • *Finished:* {anime['aired']['to']}
🎐 • *Popularity:* {anime['popularity']}
🎏 • *Favorites:* {anime['favorites']}
🎇 • *Rating:* {anime['score']}
🏅 • *Rank:* {anime['rank']}
♦ • *Trailer:* {anime['trailer_url']}
🌐 • *URL:* {anime['url']}
🎆 • *Background:* {translated_background}
❄ • *Synopsis:* {translated_synopsis}
"""

    await asyncio.gather(
        message.delete(),
        bot.send_message(GetChatID(message), AnimeInfo, reply_to_message_id=ReplyCheck(message))
    )

async def translate(text, dest):
    translation = translator.translate(text, dest=dest)
    return translation.text


add_command_help(
    "•─╼⃝𖠁 ANIME",
    [
       ["genshin", "Gɪᴠᴇ genshin."],
       ["swimsuit", "Gɪᴠᴇ swimsuit ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["schoolswimsuit", "Gɪᴠᴇ schoolswimsuit ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["white", "Gɪᴠᴇ white ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["barefoot", "Gɪᴠᴇ barefoot ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["touhou", "Give touhou animation."],
       ["gamecg", "Give gamecg animation."],
       ["hololive", "Give hololive animation."],
       ["uncensored", "Give uncensored animation."],
       ["sunglasses", "Give sunglasses animation."],
        ],
)



