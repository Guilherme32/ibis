"""
Íbis bot
~~~~~~~~

Vou tentar colocar a íbis de volta no mundo

No momento, to usando a versão de desenvolvimento pq é a q tem anotação
"""

import json
import os
import sys

import discord
from discord.ext.commands import Bot, command, Context
from mainCog import MainCog


class Ibis(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await self.add_cog(MainCog(self))
        print(f"logado como {self.user}")


if __name__ == "__main__":
    bot = Ibis("!")

    if os.path.exists("config.json"):           # Running local
        with open("config.json", "r") as file:
            discord_key = json.load(file)["discord_key"]
    else:                                       # Running on heroku
        discord_key = os.environ.get("discord_key", None)

    if discord_key is None:
        print("No discord key found. Exiting program")
        sys.exit(-1)

    activity = discord.Activity(state="Tramando a dominação mundial", name="a dominação mundial", type=discord.ActivityType.watching)

    bot.run(discord_key)
