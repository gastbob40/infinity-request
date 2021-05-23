class Request:
    author: int
    message: str
    message_id: int
    channel_id: str or None

    def __init__(self, author, message):
        self.author = author
        self.message = message

    def set_channel(self, channel_id):
        self.channel_id = channel_id

    def set_message_id(self, message_id):
        self.message_id = message_id
