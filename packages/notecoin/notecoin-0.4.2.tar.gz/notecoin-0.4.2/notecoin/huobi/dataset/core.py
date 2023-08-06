import os

from notedata.tables import SqliteTable


class TradeDetail(SqliteTable):
    def __init__(self, table_name='trade_detail', db_path=None, *args, **kwargs):
        if db_path is None:
            db_path = os.path.abspath(
                os.path.dirname(__file__)) + '/data/coin.db'

        super(TradeDetail, self).__init__(db_path=db_path, table_name=table_name, *args, **kwargs)
        self.columns = ['trade_id', 'ts', 'direction', 'price', 'amount']

    def create(self):
        self.execute("""
            create table if not exists {} (
               trade_id       BIGINT         
              ,amount         FLOAT 
              ,price          FLOAT
              ,ts             BIGINT
              ,direction      VARCHAR(5)
              ,primary key (trade_id)           
              )
            """.format(self.table_name))
