# This file is a template for new commands.
# Everyone can use it.
# Please don't load this file in main.py!
import discord
from discord import app_commands
from discord.ext import commands

class commandName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="command-name", description="Description of the command")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def command_name(self, interaction: discord.Interaction):
        pass
        # * codes of your command

async def setup(bot):
    await bot.add_cog(commandName(bot))

# * to load here 'await self.load_extension("cogs.command-file")' in main.py setup hook

# * For embed:

embed = discord.Embed(
    title="title here",
    description="description here",
    color=discord.Color.red())
embed.set_image(url="direct link") # For image

interaction.response.send_message(embed=embed) # For show embed

# * For plain text:

interaction.response.send_message("text here")

# * For buttons:

class Button(discord.ui.View):
    def __init__(self):
        super().__init__#(timeout=60) * for timeout in seconds

    @discord.ui.button(label="Example Button", style=discord.ButtonStyle.blurple, emoji="⚡")
    async def buton_tiklandi(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Clicked example button someone tests templat.py :3", ephemeral=True) #* ephemeral means : only user can see message

interaction.response.send_message(view=Button()) # * For show button(s)