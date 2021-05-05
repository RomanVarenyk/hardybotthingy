import discord
from discord import message
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
    await channel.send(f'{member} has left.')


@client.event
async def on_member_ban(guild, member):
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    if logs.target == member:
        print(f'{logs.user} has just banned {logs.target} (Time: {logs.created_at}), reason was: {logs.reason}')


@client.command()
@commands.has_role('Approved')
async def pd(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    role = ctx.guild.get_role(839295332730142731)  # role ID goes there
    await member.add_roles(role)
    await ctx.send(f"Successfully gave {member} the {role.name} role!")
    print(f"Successfully gave {member} the {role.name} role!")



@client.command()
async def ping(ctx):
    await ctx.send('The ping is ' + str(round(client.latency, 7)))
    print('The ping is ' + str(round(client.latency, 7)))

client.run('ODM4OTAyOTMzOTg1Njg5NjEw.YJB3PQ.Y7axtdIsXn9zHEaCITirZIfX_XE')