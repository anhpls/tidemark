# Tidemark

Tidemark connects to Coinbase's live market data feed and keeps a copy of the BTC-USD order book in memory, updated in real time. Right now it prints the best bid, best offer, and spread every time the book changes.

## Why I built this

I trade on the side and wanted to understand what's actually going on underneath the price you see in an app. I also worked with real time data streams during my internship and wanted to go deeper on that. The end goal is to make the book building part fast enough to measure in nanoseconds by rewriting it in C++.

## What it does right now

- Connects to Coinbase's public WebSocket feed (no API key needed)
- Subscribes to the `level2` channel for BTC-USD
- Builds the full order book from the first snapshot message, then applies every update after that
- Prints the best bid, best offer, and spread on every update
- Checks the sequence number on every message and warns if one was skipped

Example output:
```
Connected!
Best Bid: 74707.96  Best Offer: 74708.12  Spread: 0.16
Best Bid: 74707.96  Best Offer: 74708.05  Spread: 0.09
```

## How to run it

```bash
git clone https://github.com/anhpls/tidemark.git
cd tidemark
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python stream.py
```

Press Ctrl+C to stop.

## Roadmap

- [x] Connect to Coinbase and subscribe to level2
- [x] Build the order book from snapshot + updates
- [x] Show best bid, best offer, spread
- [x] Detect missed messages using sequence numbers
- [ ] Rebuild the book automatically after a missed message
- [ ] Check for a crossed book (best bid >= best offer)
- [ ] Faster way to find the best bid/offer than scanning every price
- [ ] Record the feed to a file and replay it for testing
- [ ] Rewrite the book logic in C++ and benchmark it
