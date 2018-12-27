import discord
import praw
from discord.ext import commands

TOKEN = 'NTI3Njc4MDM0MTI0NDcyMzMw.DwaHMw.NYQHBQ45WoPIKU_tV_h1-iwCh1s'

client = commands.Bot(command_prefix = 'c!')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='on version 1.0.0'))
    print('Bot is online')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)

@client.command(pass_prefix=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name=':tools: Moderation Commands', value='c!kick <user> c!ban <user> c!mute <mutes a user> c!unmute <unmutes user> c!clear <number of messages>', inline=False)
    embed.add_field(name=':smile: Fun Commands', value='c!say <say what you want it to say> c!meme <gives a random meme> c!triggerd <gives a triggered image of user>', inline=False)

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def clear(ctx, number):
    mgs = [] 
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command()
async def meme():
    await client.say(https://www.reddit.com/r/dankmemes/)

client.run(TOKEN)
