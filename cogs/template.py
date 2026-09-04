import discord
from discord import app_commands
from discord.ext import commands

class commandName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="command-name", description="Description of the command")
    async def command_name(interaction: discord.Interaction):
        pass
        # * codes of your command

async def setup(bot):
    await bot.add_cog(commandName(bot))

# * to load here 'await self.load_extension("cogs.command-file")' in main.py setup hook