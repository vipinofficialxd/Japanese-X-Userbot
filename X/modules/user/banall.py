from asyncio import sleep
from pyrogram types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from pyrogram functions.channels import EditBannedRequest
from X.utils import admin_cmd
from X import bot, CMD_HELP
error = []

@bot.on(admin_cmd(pattern=r"allban", outgoing=True))
async def testing(event):
    global error
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("**𝒀𝒐𝒖 𝑫𝒐𝒏❜𝒕 𝒉𝒂𝒗𝒆 𝑺𝒖𝒇𝒇𝒊𝒄𝒊𝒆𝒏𝒕 𝑹𝒊𝒈𝒉𝒕𝒔**")
        return
    await event.edit("**Dᴏɪɴɢ Nᴏᴛʜɪɴɢ 🙃🙂**")
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            error.append(str(e))
            pass
    await event.edit("**Nᴏᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ Hᴇʀᴇ 🙃🙂**")
    print (error)

