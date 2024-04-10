from pyrogram import Client, filters
from config import OWNER_ID
from config import CMD_HANDLER as cmd
import asyncio

from .help import *

@Client.on_message(filters.command("bsdk", cmd) & filters.me)