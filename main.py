"""
Run this file to use the bot
"""
from pathlib import Path
from main_code import SaveHandler

from main_code.Bot import bot
import os
from main_code import bot_token

os.chdir(Path(__file__).parent.absolute())

print ("bot starting...")

async def wait():
    await bot.is_ready()

if __name__ == "__main__":
    print ("Hello ^^")

    print("(idk what I'm doing)")
    
    SaveHandler.folders_ready()
    
    bot.run(bot_token.get_token())
    
    print("Commands: ------------------------------------------------------------------------")
    print(bot.commands)
    for c in bot.commands:
        print(c.name)