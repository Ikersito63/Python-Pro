import discord
import random


intents = discord.Intents.default()s
intents.message_content = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi")
    elif message.content.startswith('bye'):
        await message.channel.send("u5g66f784")
    else:
        await message.channel.send(message.content)
@client.event 
async def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
client.run(Token)
