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

# Allows the user to talk to DavidBot. Uses ChatterBot.
@client.command(name = '.', help = 'Allows you to talk with DavidBot.')
async def smart(ctx, arg):
    bot = ChatBot('DavidBot')

    conv = open('chats.txt', 'r').readlines()
    trainer = ListTrainer(bot);
    trainer.train(conv)

    bot_input = bot.get_response(arg)
    response = bot.get_response(bot_input)
    final_msg = response

    await ctx.channel.send(final_msg)

client.run(TOKEN)
