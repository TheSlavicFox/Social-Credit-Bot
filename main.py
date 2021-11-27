from discord.ext import commands
import discord
import levelsys

cogs = [levelsys]

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

for i in range(len(cogs)):
    ##set up cogs
    print("uhhh")

client.run("no token for you guys lol")