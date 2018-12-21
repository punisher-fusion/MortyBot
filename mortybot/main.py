import discord
import random
import asyncio
import sys, traceback
from discord import opus
import datetime
from discord.ext import commands


TOKEN = ""

initial_extensions = ['rastreamento']

client = commands.Bot(command_prefix=['m.', 'mo.', 'mor.'])


@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    print('-----LRV------')
    print('---Punisher--')
    print('------17------')
    print('--------------')


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Não Foi Possivel Carregar As Cogs {extension}.', file=sys.stderr)
            traceback.print_exc()


client.run(TOKEN)
