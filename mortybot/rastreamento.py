import discord
import requests
import json
from discord.ext import commands
from correios import Correios

class Rastreamento:
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rastrear(self,ctx):
        








def setup(client):
    print("[Rastreamento] Carregado.")
    client.add_cog(Rastreamento(client))
