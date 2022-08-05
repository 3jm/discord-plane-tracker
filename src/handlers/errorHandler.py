import os, dotenv, nextcord, requests, json, random, colorama
from colorama import Fore, Back, Style
from os import system as sys
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord.abc import GuildChannel

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Unknown command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have permission to use this command.")
        
def setup(bot):
    bot.add_cog(ErrorHandler(bot))