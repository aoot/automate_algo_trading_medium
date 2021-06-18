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
  sender_address = 'trading.algo15@gmail.com' # Create your own email address
  sender_pass = '{YOUR_EMAIL_PASSWORD}' 
  receiver_address = '{SET_YOUR_EMAIL_ADDRESS}' # Set your own email address

  #Setup the MIME