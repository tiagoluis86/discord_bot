import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready(): #once the Client has made the connection and prepared the data
    for guild in client.guilds:
    if guild.name == GUILD:
        break


    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


#client.run(TOKEN)

try:
    client.run('OTYwOTA4MjExNjk3OTAxNjQ4.YkxRgg.qDGWovGQzT8aVZHp7INCoK64sSY')
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")