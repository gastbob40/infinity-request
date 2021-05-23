from datetime import datetime, timedelta

import discord


class EmbedsManager:

    @staticmethod
    def complete_embed(content, name="The command was successful."):
        embed = discord.Embed(color=0x19D773) \
            .set_author(icon_url="https://cdn0.iconfinder.com/data/icons/shift-free/32/Complete_Symbol-512.png",
                        name=name)
        embed.timestamp = datetime.now() - timedelta(hours=2)
        embed.description = content
        return embed

    @staticmethod
    def information_embed(content, name="Additional information."):
        embed = discord.Embed(color=0xEFCC00) \
            .set_author(icon_url="https://cdn0.iconfinder.com/data/icons/simply-orange-1/128/questionssvg-512.png",
                        name=name)
        embed.timestamp = datetime.now() - timedelta(hours=2)
        embed.description = content
        return embed

    @staticmethod
    def error_embed(content, name="An error has occurred."):
        embed = discord.Embed(color=0xD72727) \
            .set_author(icon_url="https://cdn0.iconfinder.com/data/icons/shift-free/32/Error-512.png",
                        name=name)
        embed.timestamp = datetime.now() - timedelta(hours=2)
        embed.description = content
        return embed
