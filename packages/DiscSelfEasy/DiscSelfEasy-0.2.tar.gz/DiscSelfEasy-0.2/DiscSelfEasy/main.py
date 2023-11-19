from datetime import datetime
import requests
import time

# (´･ω･`) This is our Message class, it's where we store all the info about a Discord message!
class Message:
    def __init__(self, content, id, channelid, author, mentions, timestamp, replied_to=None):
        self.content = content
        self.id = id
        self.channelid = channelid
        self.author = author
        self.mentions = mentions
        self.timestamp = timestamp
        self.replied_to = replied_to  # (≧∇≦)b This is the new part! It holds the message we replied to!

    class Author:
        # (・_・;) This is our Author class, it's kind of like a mini-version of a Discord user!
        def __init__(self, username, id):
            self.username = username
            self.id = id

    class Mention:
        # (o_o) Mentions! When someone tags you in a message, this is where it gets noted.
        def __init__(self, username, id):
            self.username = username
            self.id = id

# (∩︵∩) And here's our Account class, it's like... your passport to do things in Discord!
class Account:
    def __init__(self, token=str):
        self.token = token

    # (´･Д･)」Let's find the most recent message in a channel, shall we?
    def recent_message(self, channelid):
        channelid = str(channelid)
        response = requests.get(url=f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1", headers={"authorization": self.token})
        return parse_json(json=response.json())

    # Here we get all the guilds (servers) you're in! (⊙ヮ⊙)
    def guilds(self):
        guilds = []
        response = requests.get(url="https://discord.com/api/v10/users/@me/guilds", headers={"authorization": self.token})
        for guild in response.json():
            guilds.append(guild['id'])
        return guilds

    # Finding all channels in a guild can be tough... (＞﹏＜)
    def channels(self, guildid):
        guildid = str(guildid)
        channels = []
        response = requests.get(url=f"https://discord.com/api/v10/guilds/{guildid}/channels",headers={"authorization": self.token})
        for channel in response.json():
            try:
                channels.append(channel["id"])
            except:
                time.sleep(5)  # (^_^メ) Gotta rest a bit if there's too much info!

        return channels

    # (っ˘̩╭╮˘̩)っ Here's how we find the message before a given one...
    def before_message(self, message=Message):
        response = requests.get(url=f"https://discord.com/api/v9/channels/{message.channelid}/messages?before={message.id}", headers={"authorization": self.token})
        return parse_json(response.json())

    # Let's send a message! (ง'̀-'́)ง
    def send_message(self, content, channelid):
        channelid = str(channelid)
        try:
            requests.post(url=f"https://discord.com/api/v9/channels/{channelid}/messages", headers={"authorization": self.token}, data={'content': content})
            return True
        except:
            return False

# Parsing JSON like a boss! (︶︹︺)
def parse_json(json):
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

    # Here's the new bit! We check if there's a replied-to message and handle it! (･o･)
    replied_to_data = message_data.get("referenced_message", None)
    replied_to = parse_json([replied_to_data]) if replied_to_data else None

    message = Message(
        content=message_data.get("content", "None"),
        id=message_data.get("id", "0"),
        channelid=message_data.get("channel_id", "0"),
        author=author,
        mentions=mentions,
        timestamp=timestamp,
        replied_to=replied_to  # Adding the replied-to message here! ヽ(´▽｀)/
    )

    return message

# Don't forget to put your token! (づ｡◕‿‿◕｡)づ
# account = Account(token="TOKEN")