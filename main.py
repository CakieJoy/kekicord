# SPDX-License-Identifier: MIT
# Copyright (c) 2026 CakieJoy


import discord
from discord import app_commands
from discord.ext import commands
import dotenv

COMMANDS = [
    "hug-everyone"
] # * Don't need add cogs. and .py just write file name
# TODO : move this to config


intents = discord.Intents.default()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=None, intents=intents,)
    async def setup_hook(self):
        await self.load_extension("cogs.hug-everyone")
        await self.tree.sync()
        print("Slash commands synced with Discord")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Bot succesfully logged as {bot.user}")

bot.run(dotenv.get_key(dotenv.find_dotenv(), "DEBUG_DISCORD_TOKEN"))