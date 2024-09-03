from lumibot.brokers import Alcapa
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PKT5G97RTZV9JZO9OBCI"
API_SECRET = "edtEt9iEQpL735o37OPP8mhAKYIeex1Ez9TpA9JV"
BASE_URL = "https://paper-api.alpaca.markets/v2"


ALCAPA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET":API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self, symbol:str='SPY'):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        
    def on_trading_iteration(self):
        if self.last_trade ==None:
            order = self.create_order(
                self.symbol,
                10,
                "buy",
                type="market"
            )
            self.submit_order(order)
            self.last_trade = "buy"
        

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

broker = Alcapa(ALCAPA_CREDS)
strategy =MLTrader(name='mlstart', broker=broker,
                   parameters={"symbol":"SPY"})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol":"SPY"}
)