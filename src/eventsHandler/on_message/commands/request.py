from typing import List

import discord
import yaml

from src.utils.embeds_manager import EmbedsManager
from src.utils.request import Request
from src.utils.student_queue import StudentQueue

with open('run/config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)


async def make_request(client: discord.Client, message: discord.Message, args: List[str]):
    author_id = message.author.id

    if not StudentQueue.open:
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "The student queue is currently disabled", "Request failed")
        )

    if StudentQueue.has_request(author_id):
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "Error, you have already done a request.\nYou can cancel it by typing `!cancel`")
        )

    # Create request object
    request = Request(author_id, ' '.join(args))

    # Step to sent
    msg = await client.get_channel(tokens['request_channel_id']).send(
        embed=EmbedsManager.complete_embed(
            f"New request from {message.author.display_name} :\n{request.message}",
            f"{message.author.display_name}"
        )
    )

    # Add msg id
    request.set_message_id(msg.id)

    # Send message to user
    place = StudentQueue.add_request(request)
    await message.channel.send(
        embed=EmbedsManager.complete_embed(
            f"You have been added to the question queue.\nThere are {place + 1} students waiting before you.",
            "Your request has been sent"
        )
    )

    # Add reaction
    await msg.add_reaction('🆗')

    def check(reaction, user):
        return str(reaction.emoji) == '🆗' and not user.bot and reaction.message.id == msg.id

    reaction, user = await client.wait_for('reaction_add', check=check)
    await msg.clear_reaction('🆗')
    await StudentQueue.remove_request(client, message.author.id)

    guild: discord.Guild = client.get_guild(tokens['guild_id'])

    # Create permission
    permissions = {
        guild.default_role: discord.PermissionOverwrite(
            read_messages=False,
        ), message.author: discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True,
        )
    }

    for teacher_id in tokens['teacher_ids']:
        teacher = await client.fetch_user(teacher_id)
        permissions[teacher] = discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True,
            manage_messages=True
        )

    permissions[client.user] = discord.PermissionOverwrite(
        read_messages=True,
        send_messages=True,
        manage_messages=True
    )
    category: discord.CategoryChannel = await guild.create_category(f"debug-{message.author.display_name}",
                                                                    overwrites=permissions, position=1)
    answer_channel = await category.create_text_channel(f"debug-{message.author.display_name}", overwrites=permissions)
    await category.create_voice_channel(f"debug-{message.author.display_name}", overwrites=permissions)

    await answer_channel.send(f"{message.author.mention}, {user.display_name} is here to help you.")
