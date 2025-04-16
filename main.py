from keep_alive import keep_alive
keep_alive()  # Starts the small web server
from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

if __name__ == "__main__":
    Bot().run()
    
#Stelleron_Hunter
from keep_alive import keep_alive

keep_alive()  # This starts the web server

# Then start your bot normally
from bot import Bot
Bot().run()

