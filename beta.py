from datetime import datetime
import time
import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
phone_Where_to_forward = ''
api_id = your_api_id
api_hash = 'your_api_hash'
bot_token = 'bot_Token'
client = TelegramClient('anon', api_id, api_hash)
group = ['123123123'] # some id of channels
sender_id = 'senders_id'


print("--------------------------------------------------------- Waiting for message... -------------------------------------------------------")
@client.on(events.NewMessage(outgoing=False)) # all incoming messages
async def my_event_handler(event):  
    newMessage = event.message.message # this is only a telegram message content, its what u see on telegram 
    sender = await event.get_sender()
    if sender.id == sender_id:
        print("====================================== " + str(datetime.now()) + " ======================================")
        print("=============================================== Message: ================================================")
        print(newMessage)
        print('================================================= END ===================================================')
        await client.send_message(phone_Where_to_forward, newMessage)

with client:
    client.run_until_disconnected()
