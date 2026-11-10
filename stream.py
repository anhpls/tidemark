# 1. import the websocket library
import websocket
# 2. save the coinbase address in a variable
COINBASE_URL = "wss://advanced-trade-ws.coinbase.com"

# 3. write a function that runs when we connect
def on_open(ws):
    print("Connected!")
 
# 4. create the connection and give it the address + your function
ws = websocket.WebSocketApp(COINBASE_URL, on_open=on_open)

# 5. start it and keep it running
ws.run_forever()
