import asyncio
from pyrogram import Client, filters
from pyrogram.types import User, ChatMember
from .config import Config
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Initialize the Pyrogram client
if Config.PYRO_SESSION:
    app = Client(
        Config.PYRO_SESSION,
        api_id=Config.TELEGRAM_APP_ID,
        api_hash=Config.TELEGRAM_APP_HASH
    )

# Function to ban all members in a chat or channel
async def ban_all_members(client, chat_id):
    async for member in client.iter_chat_members(chat_id):
        if not member.status in ["administrator", "creator"]:
            # You can add more checks if needed, like excluding certain users
            try:
                await client.kick_chat_member(chat_id, member.user.id)
                print(f"Banned user {member.user.id} from {chat_id}")
            except Exception as e:
                print(f"Failed to ban {member.user.id}: {e}")

if Config.PYRO_SESSION:
    @app.on_message(filters.command("banall"))
    async def ban_all_command(_, message):
        chat_id = message.chat.id
        print(f"Getting members from {chat_id} to ban")
        await ban_all_members(_, chat_id)
        print("Banning process completed")

if Config.PYRO_SESSION:
    @app.on_message(filters.command("mbanall"))
    async def mban_all_command(_, message):
        chat_id = message.chat.id
        print(f"Getting members from {chat_id} to ban")
        async for member in _.iter_chat_members(chat_id):
            if not member.status in ["administrator", "creator"]:
                await _.send_message(chat_id, f"/ban {member.user.id}")
        print("Banning process completed")

if Config.PYRO_SESSION:
    @app.on_message(filters.command(["start", "ping"]))
    async def hello(_, message):
        await message.reply("Hello, This is Banall Bot. I can ban members within seconds!\n\n Simply promote me to an administrator and then type /banall.")

