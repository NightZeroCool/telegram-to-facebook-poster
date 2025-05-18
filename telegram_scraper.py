from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
channel_username = os.getenv("TELEGRAM_CHANNEL")

def get_telegram_posts(limit=5):
    client = TelegramClient('anon', api_id, api_hash)
    client.start()
    posts = []
    with client:
        history = client(GetHistoryRequest(
            peer=channel_username,
            limit=limit,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        for message in history.messages:
            if message.message:
                posts.append(message.message)
    return posts