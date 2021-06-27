import discord
from discord import client
from discord.ext import commands
import random

class Roast(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def roast(self, ctx, * , member : discord.Member = None):
        responses = ["Light travels faster than sound, which is why you seemed bright until you spoke.",
        "I’ll never forget the first time we met. But I’ll keep trying.",
        "Hold still. I’m trying to imagine you with a personality.",
        "Don’t be ashamed of who you are. That’s your parents’ job.",
        "You bring everyone so much joy… when you leave the room.",
        "thought of you today. It reminded me to take out the trash.",
        "You are like a cloud. When you disappear, it’s a beautiful day."]
        mention_user = ctx.author.mention 
        if member == None:
            await ctx.send(f"{format(mention_user)}, {random.choice(responses)}")
            return
        else:
            await ctx.send(f"{member.mention}, {random.choice(responses)}")
            return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
             await ctx.send("There is no member by this name DUMBASS!")

def setup(client):
    client.add_cog(Roast(client))

