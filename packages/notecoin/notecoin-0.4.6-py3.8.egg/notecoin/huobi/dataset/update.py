import time

from notecoin.huobi.client import GenericClient, MarketClient
from notecoin.huobi.dataset.core import SymbolInfo, TradeDetail
from notetool.tool.secret import read_secret
from tqdm import tqdm


class TradeUpdate:
    def __init__(self):
        api_key = read_secret(cate1='coin', cate2='huobi', cate3='api_key')
        secret_key = read_secret(cate1='coin', cate2='huobi', cate3='secret_key')
        self.market = MarketClient(api_key=api_key, secret_key=secret_key)
        self.generic = GenericClient(api_key=api_key, secret_key=secret_key)
        self.tradeDB = TradeDetail(db_path='/root/workspace/tmp/coin/huobi.db')
        self.symbolDB = SymbolInfo(db_path='/root/workspace/tmp/coin/huobi.db')
        self.symbolDB.create()
        self.tradeDB.create()

    def insert_symbol(self):
        symbols = self.generic.get_exchange_symbols()
        self.symbolDB.insert_list(symbols.dict_data['data'])
        print(self.symbolDB.select('select count(1) as num from ' + self.symbolDB.table_name))

    def insert_trade(self, symbol):
        history = self.market.get_history_trade(symbol=symbol, size=2000)
        datas = history.dict_data['data']
        result = []
        [result.extend(data['data']) for data in datas]
        for res in result:
            res['trade_id'] = res['trade-id']

        self.tradeDB.insert_list(result)

    def insert_trades(self):
        symbols = self.symbolDB.select("select symbol from {} where state ='online'".format(self.symbolDB.table_name))
        for symbol in tqdm(symbols):
            try:
                symbol = symbol['symbol']
                self.insert_trade(symbol)
            except Exception as e:
                print(e)

        print(self.tradeDB.select('select count(1) as num from ' + self.tradeDB.table_name))

    def run(self):
        while True:
            self.insert_symbol()
            self.insert_trades()
            time.sleep(60)


update = TradeUpdate()
update.run()
