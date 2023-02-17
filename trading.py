from datetime import datetime
import MetaTrader5 as mt5
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

account_id = 
account_pw = ""
server = ""

if not mt5.initialize(login = account_id, password = account_pw, server=server):
    print("initialize() failed" , mt5.last_error())
    mt5.shutdown()
else:
    print("MetaTrader5 initialized successfully")

api_id = 
api_hash = ''
bot_token = ''
client = TelegramClient('session_name', api_id, api_hash)

print("--------------------------------------------------------- Waiting for message... -------------------------------------------------------")

@client.on(events.NewMessage(outgoing=False)) # all incoming messages
async def my_event_handler(event):  
    newMessage = event.message.message # this is only a telegram message content, its what u see on telegram 

    sender = await event.get_sender()
    #print(sender.id) # sender Id
    #print(sender.username) # sender username
    #print(sender) # all the information
    print("----------------------------------------------------Message: --------------------------------------------")
    print(newMessage)
    if sender.id == 123456789 #The ID from who you're getting the signal
        print("====================================== " + str(datetime.now()) + " ======================================")
        print("=============================================== Message: ================================================")
        print(newMessage)
        print('================================================ END ===================================================')
        await client.send_message('<phone_number_where>', newMessage) #add a phone number if you want to forward the signal
        doOrder(newMessage)

def doOrder(message):
    message = message.split("\n")

    # Check if message is a limit order
    if message[0].lower().__contains__("limit"):
        print("Limit order, not supported yet", message[0])
        return

    # Check if message is a buy or sell order
    if not message[0].lower().__contains__("sell") and not message[0].lower().__contains__("buy"):
        print("Not a buy or sell order", message[0])
        return

    lot = 0.1
    # Get symbol
    symbol = message[0].split(" ")[0].upper()
    if symbol == "XAUUSD":
        symbol = "GOLD" # this depend on which broker you're using and how they call the Gold symbol
        lot = 0.01 # since Gold is expensive i use lot 0.01
    symbolInfo = mt5.symbol_info(symbol)
    if symbolInfo is None:
        print(symbol, "not found, can not call order_check()")
        return

    takeProfit = 0
    stopLoss = 0
    

    # Get stop loss and take profit
    for i in range(1, len(message)):
        if message[i].lower().__contains__("stop loss"):
            stopLoss = float(message[i].split(": ")[1].split(" ")[0])
        if message[i].lower().__contains__("take profit") and takeProfit == 0:
            takeProfit = float(message[i].split(": ")[1].split(" ")[0])

    # Check if stop loss and take profit are valid
    type = mt5.ORDER_TYPE_SELL if message[0].lower().__contains__("sell") else mt5.ORDER_TYPE_BUY

    deviation = 20

    # Order Options
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": type,
        "sl": stopLoss,
        "tp": takeProfit,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script is running :)",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Send a trading request
    result = mt5.order_send(request)
    print("1. order_send(): by {} {} {} lots at {} with deviation={} points".format(symbol, "sell" if type == mt5.ORDER_TYPE_SELL else "buy", lot, symbolInfo.ask, deviation))

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("1. order_send failed, comment={}".format(result.comment))


with client:
    client.run_until_disconnected()
    print('Shutting down...')
    mt5.shutdown()

