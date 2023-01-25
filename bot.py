import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):

client = discord.Client(intents=intents)
client.run(token)