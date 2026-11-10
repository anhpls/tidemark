# import websocket lib
import websocket
import json
# save coinbase address
COINBASE_URL = "wss://advanced-trade-ws.coinbase.com"

bids = {} # populate with active bids
offers = {} # populate with active offers

# update book with incoming data of offer/bid + price + quantity
def update_book(side, price, quantity):
    if side == "bid": 
        book_side = bids # target bids dict
    else:
        book_side = offers # target offers dict

    if quantity == 0: # if 0, then must remove this price level since it does not exist anymore
        book_side.pop(price, None) # pop the existing price or None
    else:
        book_side[price] = quantity # if not 0, then update price with the quantity in respective side

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

    for event in data["events"]: # search in events
        for update in event["updates"]: 
            # convert to price_level and new_quantity from str to float
            price_float = float(update["price_level"])
            quantity_float = float(update["new_quantity"])
            update_book(update["side"], price_float, quantity_float)
    if bids and offers:
        best_bid = max(bids)
        best_offer = min(offers)
        spread = best_offer - best_bid
        print(f"Best Bid: {best_bid:.2f}  Best Offer: {best_offer:.2f}  Spread: {spread:.2f}")


# create connection to URL and run connect func
ws = websocket.WebSocketApp(COINBASE_URL, on_open=on_open, on_message=on_message)

# start and keep running
ws.run_forever()

