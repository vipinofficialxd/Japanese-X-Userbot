import sys
from pyrogram import Client, filters
from io import StringIO
from config import OWNER_ID
import traceback

@Client.on_message(filters.user(OWNER_ID) & filters.command(["eval"], ["."]))
def user_exec(client, message):
    if message.reply_to_message:
        code = message.reply_to_message.text.html if message.reply_to_message.text else ""
    else:
        try:
            code = message.text.html.split(" ", maxsplit=1)[1]
        except IndexError:
            code = ""

    if not code:
        message.edit("No code provided.")
        return

    result = StringIO()
    sys.stdout = result
    try:
        exec(code, globals(), locals(), timeout=10)  # Timeout set to 10 seconds
        output = result.getvalue()
        message.edit(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{output}</code>"
        )
    except Exception as e:
        message.edit(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Error:</b>\n"
            f"<code>{str(e)}</code>"
        )
    finally:
        sys.stdout = sys.__stdout__
