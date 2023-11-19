from datetime import datetime
import requests
import time


class Message:
    """Message class to better store messages"""
    def __init__(self, content, id, channelid, author, mentions, timestamp):
        self.content = content
        self.id = id
        self.channelid = channelid
        self.author = author
        self.mentions = mentions
        self.timestamp = timestamp

    class Author:
        """Author of the message"""
        def __init__(self, username, id):
            self.username = username
            self.id = id

    class Mention:
        """Mention inside the message"""
        def __init__(self, username, id):
            self.username = username
            self.id = id




class Account:
    """Your account to run functions with"""
    def __init__(self, token=str):
        self.token = token

    def recent_message(self, channelid):
        """Returns recent message in channel using channelid"""
        channelid = str(channelid)
        response = requests.get(url=f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1", headers={"authorization": self.token})
        return parse_json(json=response.json())

    def guilds(self):
        """Returns the ids of all guilds the user is in"""
        guilds = []
        response = requests.get(url="https://discord.com/api/v10/users/@me/guilds", headers={"authorization": self.token})
        for guild in response.json():
            guilds.append(guild['id'])
        return(guilds)

    def channels(self, guildid):
        """WARNING: MAY STOP IF TOO MANY CHANNELS, Returns all the ids of all channels in the guild provied"""
        guildid = str(guildid)
        channels = []
        response = requests.get(url=f"https://discord.com/api/v10/guilds/{guildid}/channels",headers={"authorization": self.token})
        for channel in response.json():
            try:
                channels.append(channel["id"])
            except:
                time.sleep(5)

        return(channels)

    def before_message(self, message=Message):
        response = requests.get(url=f"https://discord.com/api/v9/channels/{message.channelid}/messages?before={message.id}", headers={"authorization": self.token})
        return(parse_json(response.json()))


def parse_json(json):
    global reply_message
    """converts json of message into Message class"""
    message_data = json[0]

    timestamp = datetime.fromisoformat(message_data.get("timestamp", "1970-01-01T00:00:00")[:-6])

    author_data = message_data.get("author", {})
    author = Message.Author(
        id=author_data.get("id", "0"),
        username=author_data.get("username", "Unknown")
    )

    mentions_data = message_data.get("mentions", [])
    mentions = [Message.Mention(
        id=mention.get("id", "0"),
        username=mention.get("username", "Unknown")
    ) for mention in mentions_data]




    message = Message(
        content=message_data.get("content", "None"),
        id=message_data.get("id", "0"),
        channelid=message_data.get("channel_id", "0"),
        author=author,
        mentions=mentions,
        timestamp=timestamp,
    )

    return message


