import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print('Startup succesful')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    channel = client.get_channel(838951796386168866)
    await channel.send(f'{member} has joined.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    channel = client.get_channel(838951796386168866)
    await channel.send(f'{member} has lefts.')

@client.event
async def on_member_ban(member):
    print(f'{member} has been banned by ')

client.run('ODM4OTAyOTMzOTg1Njg5NjEw.YJB3PQ.KLqjsVUQkiobUxxesHiziXQ4h0I')
