# main.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('DavidBot')

conv = open('chats.txt', 'r').readlines()

trainer = ListTrainer(bot);

trainer.train(conv)

while True:
    try:
        bot_input = bot.get_response(input("You: "))
        print("Bot", bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
