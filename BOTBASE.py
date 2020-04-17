import discord
from discord.ext import commands
from discord import channel

client = discord.Client()
e= discord.Embed(title='foo')

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("HEYYYYYYY")
    if message.content.startswith("scry"):
        await message.channel.send("es HOMO")
    if message.content.startswith("anna"):
        await message.channel.send("es feminazi")
    if message.content.startswith("ana"):
        await message.channel.send("ANA SAVATER SEIER ES UNA FEMINASI AJKEROSA JAJASALU2")
    if message.content.startswith("foto"):
        await message.channel.send("https://imgur.com/gallery/OnjoPRY")
    if message.content.startswith("poce"):
        await message.channel.send("MI PUTO PADRE")
    



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('TOKEN')