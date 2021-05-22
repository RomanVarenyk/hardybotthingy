import discord
from discord.ext import commands, tasks
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True
badwords = ['fag', 'faggot', 'nigga', 'nigger']
client = commands.Bot(command_prefix=".", intents=intents)


now = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
now = now.replace("/", ".")
now = now.replace(":", ".")
file = open(f'Logs from ' + str(now) + ".txt", "a")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('no idea what to put here so this is here'))
    print('Startup succesful')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write('Startup succesful')
    filee.close()


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} has joined the server')
    filee.close()
    channel = client.get_channel(708316172310937652)
    await channel.send(f'{member} has joined.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} has left the server')
    filee.close()
    channel = client.get_channel(708316172310937652)
    await channel.send(f'{member} has left.')


@client.event
async def on_member_ban(guild, member):
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    if logs.target == member:
        filee = open(f'Logs from ' + str(now) + ".txt", "a")
        filee.write(f'\n {logs.user} has just banned {logs.target} (Time: {logs.created_at}), reason was: {logs.reason}')
        filee.close()
        print(f'{logs.user} has just banned {logs.target} (Time: {logs.created_at}), reason was: {logs.reason}')


@client.event
async def on_message(checkmessage):
    if checkmessage.content in badwords:
        print(f'{checkmessage.content} from {checkmessage.author} has beed deleted',
              f' Full string of message: {checkmessage}')
        filee = open(f'Logs from ' + str(now) + ".txt", "a")
        filee.write(f'\n {checkmessage.content} from {checkmessage.author} has beed deleted',
              f' Full string of message: {checkmessage}')
        filee.close()
        await checkmessage.delete()
    await client.process_commands(checkmessage)


@client.command()
@commands.has_role('Approved')
async def pd(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    role = ctx.guild.get_role(819652594245828628)  # role ID goes there
    await member.add_roles(role)
    await ctx.send(f"Successfully gave {member} the {role.name} role!")
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f"\n Successfully gave {member} the {role.name} role!")
    filee.close()
    print(f"Successfully gave {member} the {role.name} role!")


@client.command()
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)
    print(f'just purged {ammount} messages from {ctx.channel}             full string {ctx}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n just purged {ammount} messages from {ctx.channel}             full string {ctx}')
    filee.close()


@client.command()
async def ping(ctx):
    await ctx.send('The ping is ' + str(round(client.latency, 7)))
    print('The ping is ' + str(round(client.latency, 7)))
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write('\n The ping is ' + str(round(client.latency, 7)))
    filee.close()


@client.command()
@commands.has_role('Server staff (admin)')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.send(f'You were kicked from hardy ms discord for {reason}')
    print(f'{member} was kicked for: {reason}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} was kicked for: {reason}')
    filee.close()
    await member.kick(reason=reason)



@client.command()
@commands.has_role('Server staff (admin)')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.send(f'You were ban from hardy ms discord for {reason}')
    print(f'{member} was banned for: {reason}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} was banned for: {reason}')
    filee.close()
    await member.ban(reason=reason)


@client.command()
@commands.has_role('Approved')
async def suggest(ctx, member, *, suggestions):
    print(f'{ctx.author} suggested: {suggestions}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {ctx.author} suggested: {suggestions}')
    filee.close()
    channel = client.get_channel(709569397731360822)
    await channel.send(f'{ctx.author} suggested: {suggestions}')


@client.command()
@commands.has_role('Server staff (admin)')
async def unban(ctx, *, memberid):
    memberidint = int(memberid)
    bannedusers = await ctx.guild.bans()
    print(bannedusers)
    for ban_entry in bannedusers:
        user = ban_entry.user
        print(user.id)
        if user.id == memberidint:
            await ctx.guild.unban(user)
            print(f'{memberidint} was unbanned by {ctx.author}')
            filee = open(f'Logs from ' + str(now) + ".txt", "a")
            filee.write(f'\n {memberidint} was unbanned by {ctx.author}')
            filee.close()
            channel = client.get_channel(709569397731360822)
            await channel.send(f'{memberidint} was unbanned by {ctx.author}')
            break
        else:
            print(f'{memberidint} was not found or is not banned')

@client.event
async def on_message_delete(message):
    print(f'{message.content} was deleted. Full string: {message}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {message.content} was deleted. Full string: {message}')
    filee.close()
@client.event
async def on_message_edit(before, after):
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {before.author} has edit the messaage from {before.content} to {after.content}. The  full string of before and after. {before} ........... and after {after}')
    filee.close()
    print(f'{before.author} has edit the messaage from {before.content} to {after.content}. The  full string of before and after. {before} ........... and after {after}')



client.run('TOKEN HERE')
