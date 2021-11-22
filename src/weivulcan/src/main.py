import config
import discord
from random import choice
from datetime import datetime
from discord.ext import commands

# # #

intents = discord.Intents.default()
intents.members = True

# # #

bot = commands.Bot(command_prefix = config.PREFIX_0, intents = intents)
bot.remove_command(config.REMOVAL_0)

# # #

now = datetime.now()

# # #

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(config.MISSING_ARGUMENT)

# # #

@bot.command()
async def help(ctx):
    file = open(config.README, config.MODE, encoding=config.ENCODER)
    await ctx.send(file.read())
    file.close()

@bot.command()
async def ping(ctx):
    pong = round(bot.latency * 1000) - 100
    if pong >= config.LATENCY_LIST[5]:
        await ctx.send(f"{config.LATENCY} **{pong}**\n{config.LATENCY_MODE_1}")
    elif pong <= config.LATENCY_LIST[0]:
        await ctx.send(f"{config.LATENCY} **{pong}**\n{config.LATENCY_MODE_2}")
    elif config.LATENCY_LIST[4] >= pong >= config.LATENCY_LIST[3]:
        await ctx.send(f"{config.LATENCY} **{pong}**\n{config.LATENCY_MODE_3}")
    elif config.LATENCY_LIST[2] >= pong >= config.LATENCY_LIST[1]:
        await ctx.send(f"{config.LATENCY} **{pong}**\n{config.LATENCY_MODE_4}")
    else:
        pass

@bot.command()
async def time(ctx):
    if now.minute < 10:
        now.minute = str(now.minute)
        str_min = config.STR_MIN
        str_min += now.minute
        str_min = int(str_min)
        await ctx.send(f"**{config.HOUR}**: {now.hour}:{str_min}")
    else:
        await ctx.send(f"**{config.HOUR}**: {now.hour}:{now.minute}")

@bot.command()
async def date(ctx):
    await ctx.send(f"**{config.DATE}**: {now.day}.{now.month}.{now.year}")

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=config.KICK_REASON):
    try:
        await member.kick(reason = reason)
        await ctx.send(f"{member} {config.KICK_STATUS}")
    except:
        await ctx.send(f"{config.KICK_FAIL_1}\n{member} {config.KICK_FAIL_2}")

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=config.BAN_REASON):
    try:
        await member.ban(reason = reason)
        await ctx.send(f"{member} {config.BAN_STATUS}")
    except:
        await ctx.send(f"{config.BAN_FAIL_1}\n{member} {config.BAN_FAIL_2}")

@bot.command()
async def unban(ctx, *, member):
    banned = await ctx.guild.bans()
    name, disc = member.split(config.PREFIX_1)

    for ban_entry in banned:
        user = ban_entry.user

        if (user.name, user.discrminator) == (name, disc):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} {config.UNBAN_STATUS}")
            return

@bot.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def chat(ctx, *, question):
    if question[-1] != config.CHAT_PREFIXES[0]:
        await ctx.send(f"{config.CHAT}")
    else:
        await ctx.send(f"{choice(config.RESPONSES)}")


bot.run(config.TOKEN)