import discord
from discord import app_commands
from discord.ext import commands

class HugEveryone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hug-everyone", description="Hugs to everyone :3")
    async def hug_everyone(interaction: discord.Interaction):
        display_name = interaction.user.display_name
        embed = discord.Embed(title=f"{display_name} hugs everyone :3",)
        embed.set_image(url="https://c.tenor.com/SYsRdiK-T7gAAAAC/tenor.gif")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(HugEveryone(bot))