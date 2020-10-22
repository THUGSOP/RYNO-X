import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "RYNO-X User"
PM_IMG = "https://telegra.ph/file/04a43e5aa4ec612b92af6.mp4"
pm_caption = "🔥🔥**RYNO-X IS ONLINE🔥🔥\n\n\n"

pm_caption += f"⚔️⚔️**MASTER**⚔️⚔️       : {DEFAULTUSER}\n\n"

pm_caption += "🛡️🛡️**TELETHON**🛡️🛡️   : 1.15.0 \n\n"

pm_caption += "😈😈**RYNO-X**😈😈         : __V-1.1__\n\n"

pm_caption += "⚠️⚠️**CHANNEL**⚠️⚠️     : [ᴊᴏɪɴ](https://t.me/OFFICIALRYNOX)\n\n"

pm_caption += "🔱🔱**GROUP**🔱🔱.         : [ᴊᴏɪɴ](https://t.me/RYNOXCHAT)\n\n"

pm_caption += "😎😎**LICENSE**😎😎       : [ӀíϲҽղՏҽ](https://github.com/RYNO-X/RYNOUSER/blob/master/LICENSE)\n\n"

pm_caption += "🔥🔥**CREATOR🔥🔥      : [RYNO-X OWNER](https://t.me/HUNTER_YUVRAJ)\n\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/OFFICIALRYNOX)\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
