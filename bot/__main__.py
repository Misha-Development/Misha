import json

from bot.misha_bot import MishaBot

with open('bot-secrets.json', 'r') as read_file:
    data = json.load(read_file)
    read_file.close()

bot_token = data['BotToken']
MishaBot(command_prefix='-m').run(bot_token)
