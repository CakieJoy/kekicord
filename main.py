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

@bot.tree.command(name="hug-everyone", description="Hugs to everyone :3")
async def hug_everyone(interaction: discord.Interaction):
    display_name = interaction.user.display_name
    embed = discord.Embed(title=f"{display_name} hugs everyone! 🤗",)
    embed.set_image(url="https://c.tenor.com/SYsRdiK-T7gAAAAC/tenor.gif")

    await interaction.response.send_message(embed=embed)

bot.run(dotenv.get_key(dotenv.find_dotenv(), "DEBUG_DISCORD_TOKEN"))