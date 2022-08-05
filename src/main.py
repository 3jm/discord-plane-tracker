import os, dotenv, nextcord, requests, json, random, colorama
from colorama import Fore, Back, Style
from os import system as sys
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord.abc import GuildChannel
colorama.init()

dotenv.load_dotenv()
token = os.getenv('TOKEN')
api_key = os.getenv('API_KEY')

# intents (REQUIRED)
intents = nextcord.Intents.all()
plane = commands.Bot(command_prefix='pt!', intents=intents)
sys('cls')
print(Fore.LIGHTYELLOW_EX + 'Loading Commands..' + Style.RESET_ALL)
@plane.event
async def on_ready():
    for filename in os.listdir('./src/commands'):
        if filename.endswith('.py'):
            try:
                plane.load_extension(f'commands.{filename[:-3]}')
                print(f"{Fore.GREEN}[✅]{Style.RESET_ALL} {filename}")
            except Exception as e:
                print(f"{Fore.RED}[❌]{Style.RESET_ALL} {filename} - {e}")
    print(Fore.LIGHTYELLOW_EX + 'Loading Error Handler..' + Style.RESET_ALL)
    for filename in os.listdir('./src/handlers'):
        if filename.endswith('.py'):
            try:
                plane.load_extension(f'handlers.{filename[:-3]}')
                print(f"{Fore.GREEN}[✅]{Style.RESET_ALL} {filename}")
            except Exception as e:
                print(f"{Fore.RED}[❌]{Style.RESET_ALL} {filename} - {e}")
    print(f"{Fore.GREEN}\n[✅]{Style.RESET_ALL} {plane.user} is ready!")

plane.run(token)