import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Startup succesful')

client.run('ODM4OTAyOTMzOTg1Njg5NjEw.YJB3PQ.KLqjsVUQkiobUxxesHiziXQ4h0I')
