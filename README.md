# Puddle-bot

A discord chat bot that will create a Markov model based on a user's messages. With this model, the bot will attempt to generate random sentences that sound like the user. 

## Markov Model
The Markov Model is created using the "Markovify" chain generator.

## Getting Started

Puddle-bot depends on the following packages. Please install them before using Puddle-bot. 

### Depedencies

[Discord.py](https://github.com/Rapptz/discord.py)

[Markovify](https://github.com/jsvine/markovify)

Python 3.4+


### Installing

```
python3 -m pip install -U discord.py

pip3 install markovify
```

## Usage
This command will gather all messages in each channel in the server and write them by user to text files. Please run this before any other commands or else they will not work!

```
!getmsgs
```

This command will generate random messages using the mentioned user's Markov model.


```
!talk @mentioned-user
```


## Contributors
-Joseph Park ([@JoePark1993](https://github.com/JoePark1993/))
-Fei Yao Li  ([@fli136](https://github.com/fli136/))
