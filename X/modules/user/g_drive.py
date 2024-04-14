import logging
import os
import logging
from pyrogram.types import (
    Message,
)
from pyrogram.enums.parse_mode import ParseMode  
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pyrogram import Client, filters
from config import OWNER_ID
from config import CMD_HANDLER as cmd

from .help import *

g_auth: GoogleAuth = None
g_drive: GoogleDrive = None
__MESSAGE_LINK_TO_DRIVE_CACHE = {}

try:
    g_auth: GoogleAuth = GoogleAuth(settings_file='gdrive_settings.yaml')
    g_drive: GoogleDrive = GoogleDrive(g_auth)
    user.g_auth = g_auth
    user.g_drive = g_drive
except: logging.warn('failed to load gdrive.')

@Client.on_message(
    ~Client.filters.scheduled &
    ~Client.filters.forwarded &
    ~Client.filters.sticker &
    ~Client.filters.via_bot &
    Client.owner &
    user.command(
        ['gul', 'gUpload'],
        prefixes=Client.cmd_prefixes,
    ),
)