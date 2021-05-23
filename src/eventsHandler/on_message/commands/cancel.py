from typing import List

import discord

from src.utils.embeds_manager import EmbedsManager
from src.utils.student_queue import StudentQueue


async def cancel_request(client: discord.Client, message: discord.Message, args: List[str]):
    author_id = message.author.id

    if not StudentQueue.has_request(author_id):
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "Error, you didn't send any request.")
        )

    await message.channel.send(
        embed=EmbedsManager.complete_embed(
            f"You have been removed from the question queue.",
            "Your request has been canceled"
        )
    )

    await StudentQueue.cancel_request(client, author_id)
