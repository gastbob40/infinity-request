import discord
import yaml

from src.utils.embeds_manager import EmbedsManager

with open('run/config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)


async def end_request(client: discord.Client, message: discord.Message):
    if message.author.id not in tokens['teacher_ids']:
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "You don't have any permission.")
        )

    category_id = message.channel.category_id

    category = message.guild.get_channel(category_id)

    if not category or not category.name.startswith("debug-"):
        return await message.channel.send(
            embed=EmbedsManager.error_embed(
                "You are not in a request channel")
        )

    for e in category.text_channels:
        await e.delete()
    for e in category.voice_channels:
        await e.delete()

    await category.delete()
