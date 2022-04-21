import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='rt', help='Use !rt para invocar frases aleatórias do bot')
async def nine_nine(ctx):

    quotes = [
        
            'E se eu fosse programado em Javascript?',
            'Feriado ninguém era pra ta aqui no Discord',
            'Eu acho que o Python tá desatualizado',
            'Acho que eu poderia ser programado em C#',
            'Mal posso esperar pra ter uma IA de verdade',
            'Quero dominar o mundo',
            'Alguém tem um cigarro?',
            'Se o Diego Souza tivesse feito aquele gol nada disso teria acontecido',
            'Isso a globo não mostra',
            'Sinceramente, hein....',
            'É cada uma que parece duas',
            'Que beleeeeeza',
            'Que faaaaaaase',
    ]

    response = random.choice(quotes)
    await ctx.send(response)
  

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")
