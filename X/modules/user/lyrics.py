import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message
import os
from config import OWNER_ID
from config import CMD_HANDLER as cmd

from .help import *

@Client.on_message(filters.command("lyrics", cmd) & filters.me)
async def get_lyrics(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text("please Use %20 in between your song if it's more then 1 word\nExample .lyrics tu%20hain%20kaha")
        return

    question = message.text.split(" ", maxsplit=1)[1]

    lyrics_url = f'https://lyrist.vercel.app/api/{question}'

    async with aiohttp.ClientSession() as session:
        async with session.get(lyrics_url) as request:
            if request.status == 404:
                return await message.reply_text("Lyrics not found for this song.")

            lyrics_data = await request.json()

            try:
                image = lyrics_data['image']
                lyrics = lyrics_data['lyrics']

                lyrics_file_path = f"{song_name}_lyrics.txt"
                with open(lyrics_file_path, "w", encoding="utf-8") as file:
                    file.write(lyrics)

                await client.send_document(
                    chat_id=message.chat.id,
                    document=lyrics_file_path,
                    caption=f"Lyrics for {lyrics_data['title']} by {lyrics_data['artist']}"
                )
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=image
                )

                os.remove(lyrics_file_path)

            except Exception as e:
                print(str(e))
                pass

add_command_help(
    "•─╼⃝𖠁 Lʏʀɪᴄs",
    [
        ["lyrics", "Get lyrics for a song."],
    ],
)
