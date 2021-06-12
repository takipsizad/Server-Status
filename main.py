import discord
from mcstatus import MinecraftServer
from decouple import config

server = MinecraftServer.lookup(config('ADDRESS'))
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$status'):
        try:
            status=server.status()
            await message.channel.send('Server is online')
        except:
            await message.channel.send('Server is offline')

    if message.content.startswith('$ping'):
        try:
            ping=server.status()
            await message.channel.send("The server replied in {0} ms".format(ping.latency))
        except:
            await message.channel.send('Server is offline')

    if message.content.startswith('$players'):
        try:
            player = server.status()
            await message.channel.send("The server has {0} players online".format(player.players.online))
        except:
            await message.channel.send('Server is offline')

    if message.content.startswith('$player-names'):
        try:
            name = server.query()
            await message.channel.send("The server has the following players online: {0}".format(", ".join(name.players.names)))
        except:
            await message.channel.send('Server is offline')


client.run(config('TOKEN'))
