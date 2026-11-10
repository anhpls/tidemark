# import websocket lib
import websocket
import json
# save coinbase address
COINBASE_URL = "wss://advanced-trade-ws.coinbase.com"

# runs once we connect; subscribe to the BTC order book
def on_open(ws):
    print("Connected!")
    subscribe_message = {
        "type": "subscribe",
        "product_ids": ["BTC-USD"],
        "channel": "level2"
    }
    subscribe_text = json.dumps(subscribe_message) # make dictionary into text
    ws.send(subscribe_text) # pass the text

# runs every time coinbase sends a msg
def on_message(ws, msg: str):
    data = json.loads(msg) # load into dict from string

    if data["channel"] != "l2_data": # skip anything that isn't order book data
        return 

    for event in data["events"]:
        for update in event["updates"]:
            print(event["type"], update["side"], update["price_level"], update["new_quantity"])
        

# create connection to URL and run connect func
ws = websocket.WebSocketApp(COINBASE_URL, on_open=on_open, on_message=on_message)

# start and keep running
ws.run_forever()

