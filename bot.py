# bot.py
#pip install python-decouple
#pip install discord
import os
from typing import Any
from decouple import config
import discord


TOKEN = ""

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

class Bot:
    def __innit__(self, commandName):
        self.commandName = commandName