import discord
from discord.ext.commands import Cog, command, Bot, Context
import os


class MainCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def ping(self, ctx: Context):
        """A basic command, responds a ping with a pong. Mostly for testing"""
        await ctx.message.channel.send("pong")

    @Cog.listener("on_raw_reaction_add")
    async def correct_message_channel(self,
                                      payload: discord.RawReactionActionEvent):
        """After a message is reacted to with one of the correcting reactions
        - 'chat' or 'meme'- the message is moved to the correct channel.

        This is done to easily move a message sent to the wrong channel.
        """
        # Channel ids gathered from the server
        emoji_name = payload.emoji.name.lower()
        if emoji_name == "meme":
            target_channel = self.bot.get_channel(552592208528801795)
        elif emoji_name == "chat":
            target_channel = self.bot.get_channel(307465506862923786)
        else:
            return

        og_channel = self.bot.get_channel(payload.channel_id)
        msg = await og_channel.fetch_message(payload.message_id)

        print(msg)
        print(msg.content)
        print(self.bot.intents)
        files = []
        for file in msg.attachments:
            filename = file.filename
            await file.save(filename)
            files.append(discord.File(filename))

        text = f"Essa mensagem foi enviada por {msg.author.mention} no " \
               f"canal{og_channel.mention} e {payload.member.mention} pediu " \
               f"para que eu a movesse para cá\n"
        text += f"> {msg.content}\n"

        await target_channel.send(content=text, files=files)
        await msg.delete()

        for file in files:
            os.remove(file.filename)
