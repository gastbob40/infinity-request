import discord
import yaml

from src.eventsHandler.on_message.on_message import OnMessage


class EventsHandler:

    @staticmethod
    async def on_message(client: discord.Client, message: discord.Message):
        await OnMessage.run(client, message)
