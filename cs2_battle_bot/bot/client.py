import discord

client = discord.Bot(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
