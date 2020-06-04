# main.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('DavidBot')(
    "ChatBot Input"
    storage_adapter = "chatterbot.storage.SQLStorageAdapter"
    logic_adapters=[
        "cahtterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter"
    output_adapter="chatterbot.output.VariableOutputTypeAdapter"
    database_uri='sqlite:///database.db'
)

while True:
    try:
        bot_input = bot.get_response(input("You: "))
        print("Bot", bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
