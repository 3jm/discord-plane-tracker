import os, dotenv, nextcord, requests, json, random
from os import system as sys
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord.abc import GuildChannel

dotenv.load_dotenv()
token = os.getenv('TOKEN')
api_key = os.getenv('API_KEY')

# intents (REQUIRED)
intents = nextcord.Intents.all()
plane = commands.Bot(command_prefix='pt!', intents=intents)

@plane.event
async def on_ready():
    print("Plane tracker is ready")

@plane.command(description="Ping")
async def ping(ctx):
    em = nextcord.Embed(
        title = f"{plane.user.name} Ping",
        description = f'`📶` **{round (plane.latency * 1000)}**ms',
        color = 0xf43c60
    )
    await ctx.send(embed=em)

plane.run(token)