import discord
from discord import app_commands
from discord.ext import commands
import dotenv


intents = discord.Intents.default()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=None, intents=intents,)
    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced with Discord")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Bot succesfully logged as {bot.user}")


bot.run(dotenv.get_key(dotenv.find_dotenv(), "DEBUG_DISCORD_TOKEN"))