import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
import pathlib
path = pathlib.Path(__file__).parent.resolve()

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

bot_status = cycle(["Singing ♪♪♪", "Chilling 😇", "Sad... 🥺"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print(f'{client.user} has wake up !')
    change_status.start()

async def load():
    for file in os.listdir(os.path.join(path,'cogs')):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")

#@client.command(aliases=["lmao","huhu"]) ## command will be run if type in !lmao or !huhu or !clear


async def main():
    async with client:
        await load()
        await client.start('Enter your token here')

asyncio.run(main())

