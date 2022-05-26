"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.

You shall follow all the terms of the MIT License (./LICENSE).
"""

import discord
from discord import *
from datetime import datetime
from time import sleep

from extensions import on_start_screen


def time_now():
    time = datetime.now()
    current_time = time.strftime("%y-%m-%d %H:%M:%S")
    now = current_time + " >"
    return now


TOKEN = input(f"{time_now()} Please input your bot token: ")

bot = discord.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print(f"{time_now()} Logged in as {bot.user}")
    USER_ID = input(f"{time_now()} Please input USER ID: ")
    MESSAGE = input(f"{time_now()} Please input the spam message: ")
    user = await bot.fetch_user(USER_ID)
    while True:
        await user.send(MESSAGE)
        print(f"{time_now()} Spammed {user} with {MESSAGE}")
        sleep(0.8)

bot.run(TOKEN)
