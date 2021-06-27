import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("BOTOOTO READdYT")

    @commands.command()
    async def truth(self, ctx):
        await ctx.send("Dare")



def setup(client):
    client.add_cog(Example(client))