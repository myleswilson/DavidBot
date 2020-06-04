'''
bot.py
    Name: DavidBot
    Runs on: Python 3.8.2
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

# Allows the user to talk to DavidBot. Uses ChatterBot.
@client.command(name = '=', help = 'Allows you to talk with DavidBot.')
async def smart(ctx, *, arg):
    bot = ChatBot('DavidBot')

    bot_input = bot.get_response(arg)
    response = bot.get_response(bot_input)
    final_msg = response

    await ctx.channel.send(final_msg)

# For testing.
@client.command(name = "test", help = "For testing.")
async def test(message):
    await message.channel.send('Working!')

# For testing input.
@client.command(name = "repeat", help = "For testing input.")
async def repeat(ctx, *, arg):
    await ctx.channel.send(arg)

client.run(TOKEN)
