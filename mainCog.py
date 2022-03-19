from discord.ext.commands import Cog, command, Bot, Context


class MainCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def ping(self, ctx: Context):
        """A basic command, responds a ping with a pong. Mostly for testing"""
        await ctx.message.channel.send(f"pong")

