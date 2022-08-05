import os, dotenv, nextcord, requests, json, random
from os import system as sys
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord.abc import GuildChannel

class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(description="Ping")
    async def ping(self,ctx):
        em = nextcord.Embed(
            title = f"{self.bot.user.name} Ping",
            description = f'`📶` **{round (self.bot.latency * 1000)}**ms',
            color = 0xf43c60
        )
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Ping(bot))