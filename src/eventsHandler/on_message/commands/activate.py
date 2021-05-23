from typing import List

import discord
import yaml

from src.utils.embeds_manager import EmbedsManager
from src.utils.student_queue import StudentQueue

with open('run/config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)


async def enable(client: discord.Client, message: discord.Message, args: List[str]):
    if message.author.id not in tokens['teacher_ids']:
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "You don't have any permission.")
        )

    StudentQueue.open = True

    return await message.channel.send(
        embed=EmbedsManager.complete_embed(
            "The request queue is now enable")
    )


async def disable(client: discord.Client, message: discord.Message, args: List[str]):
    if message.author.id not in tokens['teacher_ids']:
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "You don't have any permission.")
        )

    StudentQueue.open = False

    return await message.channel.send(
        embed=EmbedsManager.complete_embed(
            "The request queue is now disable")
    )
