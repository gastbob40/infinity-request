import discord

from src.eventsHandler.on_message.commands.activate import disable, enable
from src.eventsHandler.on_message.commands.cancel import cancel_request
from src.eventsHandler.on_message.commands.end_request import end_request
from src.eventsHandler.on_message.commands.place import get_place
from src.eventsHandler.on_message.commands.request import make_request


class OnMessage:
    @staticmethod
    async def run(client: discord.Client, message: discord.Message):
        if message.author.bot:
            return

        if message.content and message.content[0] != '!':
            return

        command = message.content.split()[0][1:]
        args = message.content.split()[1:]

        if command == 'request':
            await make_request(client, message, args)
        elif command == 'cancel':
            await cancel_request(client, message, args)
        elif command == 'place':
            await get_place(client, message, args)
        elif command == 'close':
            await end_request(client, message)
        elif command == 'enable':
            await enable(client, message, args)
        elif command == 'disable':
            await disable(client, message, args)
