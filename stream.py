# import websocket lib
import websocket
import json
# save coinbase address
COINBASE_URL = "wss://advanced-trade-ws.coinbase.com"

# connect
def on_open(ws):
    print("Connected!")
    subscribe_message = {
        "type": "subscribe",
        "product_ids": ["BTC-USD"],
        "channel": "level2"
    }
    subscribe_text = json.dumps(subscribe_message) # make dictionary into text
    ws.send(subscribe_text) # pass the text

def on_message():
    pass

# create connection to URL and run connect func
ws = websocket.WebSocketApp(COINBASE_URL, on_open=on_open)

# start and keep running
ws.run_forever()

