import discord
import os
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='$help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):

        await message.channel.send('Hello!')
    if message.content.startswith('$ping'):

        await message.channel.send('pong')
    if message.content.startswith('$pong'):
            
        await message.channel.send('ping')
    if message.content.startswith('$help'):

        await message.channel.send('$hello - Says hello\n$ping - Says pong\n$pong - Says ping')

client.run(TOKEN)