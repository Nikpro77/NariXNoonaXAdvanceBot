from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

if __name__ == "__main__":
    Bot().run()
#Stelleron_Hunter
import asyncio
from bot import Bot

if __name__ == "__main__":
    bot = Bot()
    asyncio.run(bot.start())  # or bot.run(), depending on your bot logic
