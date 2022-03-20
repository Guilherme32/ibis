"""
Íbis bot
~~~~~~~~

Vou tentar colocar a íbis de volta no mundo

No momento, to usando a versão de desenvolvimento pq é a q tem anotação
"""

import json
import os
import sys

print(os.environ)
print(os.path)
import discord
from discord.ext.commands import Bot, command, Context
from mainCog import MainCog


class Ibis(Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def on_ready(self) -> None:
        """Does the proper initialization for the async functions"""

        await self.init_cogs()
        await self.init_presence()

        print(f"logado como {self.user}")

    async def init_presence(self) -> None:
        """Sets the presence as something absolutely not menacing or sus"""

        activity = discord.Activity(state="Tramando a dominação mundial",
                                    name="a dominação mundial",
                                    type=discord.ActivityType.watching)
        await self.change_presence(activity=activity,
                                   status=discord.enums.Status.idle)

    async def init_cogs(self) -> None:
        """Loads all the cogs"""
        await self.add_cog(MainCog(self))


if __name__ == "__main__":
    if os.path.exists("config.json"):           # Running local
        with open("config.json", "r") as file:
            discord_key = json.load(file)["discord_key"]
    else:                                       # Running on heroku
        discord_key = os.environ.get("discord_key", None)

    if discord_key is None:
        print("No discord key found. Exiting program")
        sys.exit(-1)

    bot = Ibis("!")
    bot.run(discord_key)
