"""
Íbis bot
~~~~~~~~

Vou tentar colocar a íbis de volta no mundo

No momento, to usando a versão de desenvolvimento pq é a q tem anotação
"""

import json

import discord
from discord.ext.commands import Bot, command, Context
from mainCog import MainCog


class Ibis(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await self.add_cog(MainCog(self))
        print(f"logado como {self.user}")


bot = Ibis("!")

activity = discord.Activity(state="Tramando a dominação mundial", name="a dominação mundial", type=discord.ActivityType.watching)

with open("config.json", "r") as file:
    config = json.load(file)

bot.run(config["discord_key"])
