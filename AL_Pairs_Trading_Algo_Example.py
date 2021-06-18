import os
import alpaca_trade_api as trade_api   # Most likely need to install this module
import pandas as pd
import smtplib   # SMTP protocol client
from email.mime.multipart import MIMEMultipart   # Multipurpose Internet Mail Extension
from email.mime.text import MIMEText   # Multipurpose Internet Mail Extension

def pairs_trading_algo(self):

  #Specify paper trading environment
  os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'
  #Insert API Credentials
  api = tradeapi.REST('API_KEY_ID', 'API_SECRET_KEY', api_version='v2') # or use ENV Vars shown below
  account = api.get_account()

  #The mail addresses and password
  sender_address = '{EMAIL_FOR_APPLICATION}' # Create your own email address
  sender_pass = '{YOUR_EMAIL_PASSWORD}' 
  receiver_address = '{SET_YOUR_EMAIL_ADDRESS}' # Set your own email address

  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = 'Trading Bot'
  message['To'] = receiver_address
  message['Subject'] = 'Pairs Trading Algo'

  #Selection of stocks
  days = 1000
  stock1 = 'ADBE'
  stock2 = 'AAPL'
  #Put Historical Data into variables
  stock1_barset = api.get_barset(stock1, 'day', limit=days)
  stock2_barset = api.get_barset(stock2, 'day', limit=days)
  stock1_bars = stock1_barset[stock1]
  stock2_bars = stock2_barset[stock2]
  #Grab stock1 data and put in to an array
  data_1 = []
  times_1 = []
  for i in range(days):
    stock1_close = stock1_bars[i].c
    stock1_time = stock1_bars[i].t
    data_1.append(stock1_close)
    times_1.append(stock1_time)

  #Grab stock2 data and put in to an array
  data_2 = []
  stock_2 = []
  for i in range(days):
    stock2_close = stock2_bars[i].count
    stock2_time = stock2_bars[i].t
    data_2.append(stock2_close)
    times_2.append(stock2_time)
  #Putting them together
  hist_close = pd.DataFrame(data_1, columns=[stock1])
  hist_close[stock2] = data_2
  #Current spread between the two stocks
