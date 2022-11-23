import discord
import with_db
import commands
import autorole
from discord.ext import commands as dis_commands
#12
with_db.create_table()

TOKEN = "MTA0NDA1ODY5ODgxMDY1NDc1MQ.G83xcS.T93eo7qTNbV4irUS9_WsE_eCzYDaSN8VujV6Dc"
VCI = 1044638181275996261 #VERIFY_CHAT_ID
CCI = 1044639388715454544 #COMMAND_CHANNEL_ID

intents = discord.Intents.all()
bot = dis_commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_member_join(member):
    await autorole.when_join(member);

@bot.event
async def on_member_ban(guild, member):
    commands.delete_user(member.id)

@bot.event
async def on_member_leave(member):
    pass

@bot.event
async def on_raw_reaction_add(payload):
    global VCI
    if(payload.channel_id == VCI):
        await autorole.when_verify(payload.member)

@bot.command()
async def warn(ctx, id):
    global CCI
    if(ctx.message.channel.id == CCI):
        await commands.warn(ctx, id)

@bot.command()
async def referer(ctx, id):
    global CCI
    if(ctx.message.channel.id == CCI):
        await commands.set_referer(ctx, id)

bot.run(TOKEN)