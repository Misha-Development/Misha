import json

from pymongo import MongoClient

with open('bot/resources/database.json' , 'r') as read_file:
    data = json.load(read_file)
    read_file.close()


def connectClient():
    client = MongoClient(data['host'], int(data['port']))
