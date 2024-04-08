import sys
from pyrogram import Client, filters
from io import StringIO
from config import OWNER_ID

@Client.on_message(filters.user(OWNER_ID) & filters.command(["eval"], ["."]))
def user_exec(client, message):
    reply = message.reply_to_message
    code = ""
    try:
        code = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        try:
            code = message.text.split(" \n", maxsplit=1)[1]
        except IndexError:
            pass

    result = sys.stdout = StringIO()
    try:
        exec(code)

        message.edit(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result.getvalue()}</code>"
        )
    except:
        message.edit(
            f"<b>Code:</b>\n"
            f"<code>```python{code}```</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>"
        )
