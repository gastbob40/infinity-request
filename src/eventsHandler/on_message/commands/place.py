from typing import List

import discord

from src.utils.embeds_manager import EmbedsManager
from src.utils.student_queue import StudentQueue


async def get_place(client: discord.Client, message: discord.Message, args: List[str]):
    author_id = message.author.id

    if not StudentQueue.has_request(author_id):
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "Error, you didn't send any request.")
        )
    place = StudentQueue.get_place(author_id)
    await message.channel.send(
        embed=EmbedsManager.complete_embed(
            f"You are number {place} the question queue.",
            "Be patient."
        )
    )
