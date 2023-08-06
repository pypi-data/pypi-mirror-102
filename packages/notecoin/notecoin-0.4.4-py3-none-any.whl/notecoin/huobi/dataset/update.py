from notecoin.huobi.client import GenericClient, MarketClient
from notecoin.huobi.dataset.core import SymbolInfo, TradeDetail
from notetool.tool.secret import read_secret


class TradeUpdate:
    def __init__(self):
        api_key = read_secret(cate1='coin', cate2='huobi', cate3='api_key')
        secret_key = read_secret(cate1='coin', cate2='huobi', cate3='secret_key')
        self.market = MarketClient(api_key=api_key, secret_key=secret_key)
        self.generic = GenericClient(api_key=api_key, secret_key=secret_key)
        self.tradeDB = TradeDetail(db_path='/root/workspace/tmp/coin/huobi.db')
        self.symbolDB = SymbolInfo(db_path='/root/workspace/tmp/coin/huobi.db')
        self.tradeDB.create()

    def run_symbol(self):
        symbols = self.generic.get_exchange_symbols()
        self.symbolDB.insert_list(symbols['data'])
        print(self.symbolDB.select('select count(1) as num from '+self.symbolDB.table_name))

    def run(self):
        history = self.market.get_history_trade(symbol='ethusdt', size=2)
        datas = history.dict_data['data']
        result = []
        [result.extend(data['data']) for data in datas]
        for res in result:
            res['trade_id'] = res['trade-id']

        self.tradeDB.insert_list(result)
        print(result)
        print(self.tradeDB.select('select count(1) as num from '+self.tradeDB.table_name))
        print("end")


update = TradeUpdate()
update.run_symbol()
