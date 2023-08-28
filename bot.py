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

bot = discord.Bot()

TOKEN = TOKEN = os.getenv('DISORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

#<<<<< HEAD

#client.run(TOKEN)

class Bot:
    def __innit__(self, commandName):
        self.commandName = commandName

async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run('my token goes here')

#>>>>>>> 6b8fe9f5b3ab9cc60d79ca568a3e9521a68ab0ce
