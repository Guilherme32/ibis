from discord.ext.commands import Cog, command, Bot, Context


class MainCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f"We have logged in as {self.bot.user}")

    @command()
    async def ping(self, ctx: Context):
        await ctx.message.channel.send(f"pong")

