import heapq

class OrderBook:
    def __init__(self): self.bids, self.asks, self.trades = [], [], []
    def limit_buy(self, px, qty):
        while qty > 0 and self.asks and self.asks[0][0] <= px:
            apx, aqty = heapq.heappop(self.asks)
            fill = min(qty, aqty); self.trades.append((apx, fill)); qty -= fill
            if aqty > fill: heapq.heappush(self.asks, (apx, aqty - fill))
        if qty > 0: heapq.heappush(self.bids, (-px, qty))
    def limit_sell(self, px, qty):
        while qty > 0 and self.bids and -self.bids[0][0] >= px:
            nbpx, bqty = heapq.heappop(self.bids)
            fill = min(qty, bqty); self.trades.append((-nbpx, fill)); qty -= fill
            if bqty > fill: heapq.heappush(self.bids, (nbpx, bqty - fill))
        if qty > 0: heapq.heappush(self.asks, (px, qty))

if __name__ == "__main__":
    ob = OrderBook(); ob.limit_sell(100, 10); ob.limit_buy(102, 6)
    assert ob.trades == [(100, 6)] and ob.asks[0] == (100, 4)
    print("[PASS] 091_limit_order_book")
