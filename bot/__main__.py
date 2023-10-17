from pyrogram import idle, app
from .config import Config
bot.start()
if Config.PYRO_SESSION:
   app.run()
idle()
bot.stop()
