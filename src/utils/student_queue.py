import yaml

from src.utils.embeds_manager import EmbedsManager
from src.utils.request import Request

with open('run/config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)


class StudentQueue:
    requests = []
    open = False

    @staticmethod
    def has_request(client_id: int):
        for request in StudentQueue.requests:
            if request.author == client_id:
                return True
        return False

    @staticmethod
    def add_request(request: Request):
        StudentQueue.requests.append(request)
        return len(StudentQueue.requests) - 1

    @staticmethod
    async def cancel_request(discord_client, client_id: int):
        request = [x for x in StudentQueue.requests if x.author == client_id][0]
        message = await discord_client.get_channel(tokens['request_channel_id']).fetch_message(request.message_id)
        user = await discord_client.fetch_user(request.author)
        await message.edit(
            embed=EmbedsManager.error_embed(
                f"New request from {user.name} for:\n{request.message}",
                "Request canceled"
            )
        )

        StudentQueue.requests = [x for x in StudentQueue.requests if x.author != client_id]

    @staticmethod
    async def remove_request(discord_client, client_id: int):
        request = [x for x in StudentQueue.requests if x.author == client_id][0]
        message = await discord_client.get_channel(tokens['request_channel_id']).fetch_message(request.message_id)
        user = await discord_client.fetch_user(request.author)
        await message.edit(
            embed=EmbedsManager.information_embed(
                f"New request from {user.name} for:\n{request.message}",
                "Request finished"
            )
        )

        StudentQueue.requests = [x for x in StudentQueue.requests if x.author != client_id]


    @staticmethod
    def get_place(client_id: int):
        for i in range(len(StudentQueue.requests)):
            if StudentQueue.requests[i].author == client_id:
                return i
        return -1
