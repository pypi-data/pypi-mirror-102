from notecoin.huobi.client import MarketClient, TradeClient

#client = MarketClient()
#tickers = client.get_market_tickers()
trade = TradeClient()
history = trade.get_history_orders()

print(history)

print(history.data_dict)
print("end")
