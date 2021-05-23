import discord
import yaml

from src.eventsHandler.eventsHandler import EventsHandler

with open('run/config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)

client = discord.Client()


@client.event
async def on_ready():
    print(f"Connected as {client.user.display_name}")


@client.event
async def on_message(message: discord.Message):
    await EventsHandler.on_message(client, message)


if __name__ == '__main__':
    client.run(tokens['discord_token'])
