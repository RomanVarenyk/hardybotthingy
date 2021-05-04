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
async def on_member_ban(guild, member):
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    if logs.target == member:
        print(f'{logs.user} has just banned {logs.target} (The time is {logs.created_at}), and their reason for doing so is {logs.reason}')







client.run('ODM4OTAyOTMzOTg1Njg5NjEw.YJB3PQ.KLqjsVUQkiobUxxesHiziXQ4h0I')
