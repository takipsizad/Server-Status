from discord.ext import commands
from mcstatus import MinecraftServer
from decouple import config

server = MinecraftServer.lookup(config('ADDRESS'))
bot = commands.bot(command_prefix=commands.when_mentioned_or("$"))


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name="status")
async def _status__(ctx):
    try:
        status = server.status()
        await ctx.send('Server is online') 
    except:
        await ctx.send('Server is offline')

@bot.command(name="ping")
async def __ping(ctx):
    try:
        ping = server.status()
        await ctx.send(f"The server replied in {ping.latency} ms")
    except:
        await ctx.send('Server is offline')

@bot.command(name="players")
async def __players(ctx):
    try:
        player = server.status()
        await ctx.send(f"The server has {player.players.online} players online")
    except:
        await ctx.send('Server is offline')

@bot.command(name="player-names")
async def player_names(ctx):
    try:
        name = server.query()
        await ctx.send("The server has the following players online: {0}".format(", ".join(name.players.names)))
    except:
        await ctx.send('Server is offline')







bot.run(config('TOKEN'))
