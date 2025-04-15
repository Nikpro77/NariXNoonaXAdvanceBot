#Stelleron_Hunter


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

START_PIC = os.environ.get("START_PIC", "https://litter.catbox.moe/cyhhso.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://litter.catbox.moe/cyhhso.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "True") == "True" else False  #For Enable Token 

#TOKEN = False if os.environ.get('TOKEN', "FALSE") == 'FALSE' else False # For disable Token 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>Hᴇʟʟᴏ!! Wᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</a> Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ\n\nHᴇʟᴘʟɪɴᴇ @EternalsHelplineBot\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!</a></blockquote></b>"

ABOUT_TXT = "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ: <a href=https://t.me/Stelleron_Hunter>sᴛᴇʟʟᴇʀᴏɴ</a>\n◈ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_cruise_netflix>ᴇᴛᴇʀɴᴀʟs</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢs : <a href=https://t.me/+VxWwaMA6g_JkNTA9>ᴏɴɢᴏɪɴɢ</a>\n◈ᴇᴄᴄʜɪ ᴅᴇx : <a href=https://t.me/Ecchi_Dex>ᴇᴄᴄʜɪ</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href=https://t.me/EternalsHelplineBot>ʜᴇʟᴘʟɪɴᴇ</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>𝐇𝐞𝐲!! {mention} 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐂𝐨𝐦𝐦𝐮𝐧𝐢𝐭𝐲. 𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐨𝐮𝐫 𝐜𝐨𝐦𝐦𝐮𝐧𝐢𝐭𝐲, 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐝𝐨 𝐬𝐨 𝐛𝐲 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐢𝐧𝐠 𝐭𝐨 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥. @Stelleron_Hunter\n\n𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐲𝐨𝐮𝐫 𝐒𝐮𝐩𝐩𝐨𝐫𝐭</blockquote></b>")
try:
    ADMINS=[7654385403]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote>Hᴇʟʟᴏ!! {mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</a>  Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ʙᴏᴛ ᴀɢᴀɪɴ, Fᴏʀ Oɴɢᴏɪɴɢ Aɴɪᴍᴇ ~ <a href=https://t.me/Anime_Eternals>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢs </a> Jᴏɪɴ Tʜɪs Cʜᴀɴɴᴇʟ</blockquote></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Anime_Eternals</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b><blockquote>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Stelleron_Hunter !!\n\n👋Hᴇʏ Fʀɪᴇɴᴅ,🚫Dᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇs ᴛᴏ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ I'ᴍ ᴏɴʟʏ Fɪʟᴇ Sʜᴀʀᴇ ʙᴏᴛ!</blockquote></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7654385403)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
