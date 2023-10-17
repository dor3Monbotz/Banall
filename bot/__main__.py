from pyrogram import idle
from .config import Config
bot.start()
if Config.PYRO_SESSION:
   app.run()
idle()
bot.stop()
