'''
 bot.py
 Runs on: Python 3
 Author: Myles
 Date of creation: 06/3/2020
 Last update: 06/3/2020
'''

import os
import random
import asyncio
import pickle
import os
import discord

from discord.ext import commands
from dotenv import load_dotenv
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = '', case_insensitive = True)

# Prints in console when the Discord bot is connected.
@client.event
async def on_ready():
    print(f'{client.user.name} has connected! Yay!')

# For testing.
@client.command(name = "test", help = "For testing.")
async def test(message):
    await message.channel.send('Working!')

client.run(TOKEN)
