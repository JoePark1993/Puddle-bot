import discord
import asyncio
import markovify
import traceback
import os
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
    if message.content.startswith('!getmsgs'):
        user_list = {}
        channels = message.server.channels
        for channel in channels:
            print("Working on " + channel.name)
            if channel.name == "isekaid":
                continue
            if channel.name == "test2":
                continue
            async for message in client.logs_from(channel, limit=11000):
                if message.author in user_list:
                    user_list[message.author].append(message.content)
                else:
                    user_list[message.author] = [message.content]
        print("Done getting messages")
        for user in user_list:
            print("Writing file for " + user.name)
            try:
                with open(user.name + user.id + ".txt", "w") as file:
                    for msg in user_list[user]:
                        file.write("%s\n" % msg)
            except IOError:
                print(traceback.format_exc())
        print("Done!")

    if message.content.startswith('!talk'):
        if message.mentions:
            filename = message.mentions[0].name
            user_id = message.mentions[0].id
            try:
                with open(filename + user_id + ".txt", "r") as file:
                    text = file.read()
                    text_model = markovify.NewlineText(text)
                    try:
                        for i in range(5):
                            await client.send_message(message.channel, text_model.make_sentence(tries=100))
                    except discord.HTTPException:
                        await client.send_message(message.channel, "Generated null message.")
            except IOError:
                print("File not found")

client.run(TOKEN)
