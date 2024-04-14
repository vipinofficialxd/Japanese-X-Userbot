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

async def gUpload_handler(_, message: Message):
    download_message = await user.get_message_to_download(message)
    if not download_message:
        return await message.reply_text('Media required')
    elif download_message.empty:
        top_message = await message.reply_text(
            'Required message is empty, searching for the correct one...'
        )
        download_message = await user.get_message_to_download(message, True)
        if not download_message or message.empty:
            return await top_message.edit_text('message iteration ended.')
        
        await top_message.edit_text('Next message found! \n' + user.html_mono(download_message.link))

    if download_message.link and __MESSAGE_LINK_TO_DRIVE_CACHE.get(download_message.link, None):
        return await message.reply_text(
            f'File is ready to download.\n' + user.html_normal(__MESSAGE_LINK_TO_DRIVE_CACHE[download_message.link]))
    
    target_cmd = ' '.join(message.command[1:])
    if target_cmd and target_cmd.find('https:') != -1 and target_cmd.find('http:') != -1:
        file_path = os.path.abspath(os.path.expanduser(' '.join(target_cmd[1:]) or './'))
    else:
        file_path = os.path.abspath(os.path.expanduser('./'))
    
    if os.path.isdir(file_path):
        file_path = os.path.join(file_path, '')

    text = 'Downloading...'
    reply = await message.reply_text(text)
    try:
        file_path = await download_message.download(file_path, progress=progress_callback, progress_args=(reply, text, False))
    except user.exceptions.MediaInvalid:
        return await message.reply_text('Download cancelled!')
    
    g_drive = getattr(user, 'g_drive', None)
    if not isinstance(g_drive, GoogleDrive):
        try:
            g_auth: GoogleAuth = GoogleAuth(settings_file='gdrive_settings.yaml')
            g_drive: GoogleDrive = GoogleDrive(g_auth)
            user.g_auth = g_auth
            user.g_drive = g_drive
        except Exception as e: 
            return await user.reply_exception(message, e=e)
    
    file_metadata = {
        'title': os.path.basename(file_path)
    }
    if user.scp_config.gdrive_upload_folder_id:
        file_metadata['parents'] = [{'id': user.scp_config.gdrive_upload_folder_id}]
    
    try:
        g_file = g_drive.CreateFile(file_metadata)
        # Read file and set it as the content of this instance.
        g_file.SetContentFile(file_path)
        g_file.Upload()  # Upload the file.
    except Exception as e:
        return await user.reply_exception(message, e=e)
    
    __MESSAGE_LINK_TO_DRIVE_CACHE[download_message.link] = g_file['webContentLink']
    await reply.edit_text(f'File is ready to download.\n' + user.html_normal(g_file['webContentLink']))