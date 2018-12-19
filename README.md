# Puddle-bot

A discord chat bot that will read a specific user's logs and create a Markov model. With this model, randomly-generated sentences will be created related to the model.

# Markov Model
The Markov Model is created using the "Markovify" chain generator.

# Requirements
Discord.py
Markovify
Python 3.4+
asyncio

# Getting Started
> python3 -m pip install -U discord.py
> pip3 install markovify
> python3 puddle-bot.py

# To call
> !logs
This will gather all messages in each channel in the server and seperate them by user in a text file.
>!talk @mentioned-username
This will output a set number of messages that is specified in range. 
