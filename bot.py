import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):

    async def on_ready(self):
        print(f'We have logged in as {client.user}')

    async def on_message(self, message):
        print(f"Message Found: {message.content} from {message.author} in {message.channel}") 

        if message.author == client.user:
            return
        
        if "hello" in message.content.lower():
            print(f"Command recognized: hello")
            await message.channel.send("Hello!")

        if client.user in message.mentions:
            print("Bot mentioned")
            await message.channel.send("I was mentioned!")

        if message.content == "react":
            print("react command recognized")
            await message.add_reaction("👍")
            await message.add_reaction("👽")

    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing {user}")
        
client = DevPSUBot(intents=intents)
client.run(token)