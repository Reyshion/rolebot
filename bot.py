#<<<<<<< HEAD
# bot.py
#pip install python-decouple
#pip install discord
import os
from typing import Any
from decouple import config
#=====>>>>>>> 6b8fe9f5b3ab9cc60d79ca568a3e9521a68ab0ce
import discord
import os

# Load Variables from .env
from .env import loadEnv
loadEnv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = TOKEN = os.getenv('DISORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        
client = MyClient()
client.run('my token goes here')

#>>>>>>> 6b8fe9f5b3ab9cc60d79ca568a3e9521a68ab0ce
