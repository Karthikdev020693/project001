import yfinance as yf
from datetime import datetime, timedelta

class Stocks:

    def __init__(self) -> None:
        pass

    def get_nifty50stocks(self):

        nifty_50_stocks = [
            'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS', 
            'ICICIBANK.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'BAJFINANCE.NS', 'ITC.NS',
            'LT.NS', 'BHARTIARTL.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'MARUTI.NS',
            'SUNPHARMA.NS', 'HCLTECH.NS', 'WIPRO.NS', 'ULTRACEMCO.NS', 'NTPC.NS',
            'POWERGRID.NS', 'TITAN.NS', 'TECHM.NS', 'INDUSINDBK.NS', 'ONGC.NS',
            'COALINDIA.NS', 'GRASIM.NS', 'JSWSTEEL.NS', 'ADANIPORTS.NS', 'M&M.NS',
            'TATASTEEL.NS', 'HEROMOTOCO.NS', 'DRREDDY.NS', 'DIVISLAB.NS', 'CIPLA.NS',
            'BRITANNIA.NS', 'HDFCLIFE.NS', 'BAJAJFINSV.NS', 'SHREECEM.NS', 'EICHERMOT.NS',
            'BPCL.NS', 'APOLLOHOSP.NS', 'BAJAJ-AUTO.NS', 'SBILIFE.NS', 'TATAMOTORS.NS',
            'UPL.NS', 'VEDL.NS', 'HINDALCO.NS', 'DABUR.NS'
        ]

        return nifty_50_stocks

    def get_stock_info(self, symbol):
        
        stock = yf.Ticker(symbol)

        stock_info = stock.info

        return stock_info
    
    def get_price_at(self, symbol, start_date, end_date):

        data = yf.download(symbol, start=start_date, end=end_date)

        return data

    
    def get_price_data(self, symbol):

        data = {}

        end_date = datetime.now().date()

        start_date = end_date - timedelta(days=365)
        
        price_data = self.get_price_at(symbol, start_date, end_date)

        print(price_data)

        return price_data
    
    def get_return_data(self, symbol, days):

        price_data = self.get_price_data(symbol)

        last_close = price_data.iloc[-1]['Close']

        return_days = - abs(days)

        prev_close = price_data.iloc[return_days]['Close']

        print(f"prev close { prev_close }, highest close ")

        return self.calculate_return(prev_close, last_close)
    
    def calculate_return(self, past_price, current_price):
        return ((current_price - past_price) / past_price) * 100



