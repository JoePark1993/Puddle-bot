import discord
import asyncio
import markovify
from constants import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!logs'):
        user_list = {}
        channels = message.server.channels
        for channel in channels:
            print("Working on " + channel.name)
            if channel.name == "isekaid":
                continue
            if channel.name =="test2":
                continue
            async for message in client.logs_from(channel, limit=10000):
                if message.author in user_list:
                    user_list[message.author] += (message.content + "\n")
                else:
                    user_list[message.author] = (message.content + "\n")
        for user in user_list:
            with open(user.name + ".txt", "w") as file:
                file.write(user_list[user])

    if message.content.startswith('!talk'):
        if message.mentions:
            filename = message.mentions[0].name
        with open(filename + ".txt") as file:
            text = file.read()

        text_model = markovify.NewlineText(text)

        for i in range(5):
            await client.send_message(message.channel, text_model.make_sentence(tries=100))

client.run(TOKEN)