import discord
from discord.ext import commands

class Example2(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hi!")


def setup(client):
    client.add_cog(Example2(client))