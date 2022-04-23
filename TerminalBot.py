# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
BotToken = open("C:/Token/Terminal.txt", "r").readlines()

import Main
import discord
from discord.ext import commands

client = commands.Bot(".")

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    activity = discord.Game(name=f"don't break my computer please babes 👁️", type=3)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)

@client.event
async def on_message(message):
    if message.content.startswith("str://"):
        Script = message.content.split("\n")
        Script[0] = Script[0].replace("str://", "")

        Tick = 0
        while Tick < len(Script):
            if Script[Tick].startswith("open"):
                Response = [
                    "Heya! Thank you for your interest in StrScrTerminal for Discord.",
                    "You have just tried to call the `open` command. It's a valid command however unfortunately- To help prevent abuse, We've had to disable this ):",
                    "Users can easily spam servers with the bot, when the command is run. Sorry. If the item you're trying to run is **super** important, You'll have to run the lines manually sorry"
                ]
            Response = Main.botRunLine(Script[Tick])
            print("RESPSNOE", Response)
            TTick = 0
            while TTick < len(Response):
                print(Response)
                await message.reply(Response[TTick])
                TTick += 1
            Tick += 1
            # Main.SetGR([])

client.run(BotToken[0])