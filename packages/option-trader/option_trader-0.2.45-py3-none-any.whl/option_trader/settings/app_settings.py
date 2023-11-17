from pathlib import Path

from option_trader.consts import strategy

OPTION_TRADER = 'option_trader'

def OPTION_TRADER_BASE_DIR():
    p = str(Path().resolve())
    l = p.find(OPTION_TRADER)   
    if l >= 0:
        return p[: l + len(OPTION_TRADER)]       
    else:
        return None        

import os

SERVICE_ROOT_DIR    = OPTION_TRADER_BASE_DIR()
SITE_ROOT_DIR       = os.path.join(SERVICE_ROOT_DIR,'sites')
DATA_ROOT_DIR       = os.path.join(SITE_ROOT_DIR,   'data')
CHART_ROOT_DIR      = os.path.join(DATA_ROOT_DIR,   'charts')
MAIL_ROOT_DIR       = os.path.join(DATA_ROOT_DIR,   'mail')
LOG_ROOT_DIR        = os.path.join(DATA_ROOT_DIR,   'logs')
SITE_USER_DIR       = 'users'
GMAIL_CREDENTIALS   = "credentials-optiontrading-bot.json"
GMAIL_SCOPES        = ['https://mail.google.com/']
#TRADINGBOT_HOME_DIR = SITE_ROOT_DIR+'/src'

TREND_WINDOW_SIZE = 7
USE_PANDA = False
TRADE_IB = False

LINE_CHANNEL_SECRET = '628e7b113c8927a8a81e6e5f34412ffe'
LINE_USER_ID = '628e7b113c8927a8a81e6e5f34412ffe'
LINE_BOT_BASIC_ID = '@713hvlic'
LINE_CHANNEL_ACCESS_TOKEN = 'eNyfeZLsU7MbVSU8oWu+iryZ6yzVuO575vB71iNtjBbbNznkoPfsTbxhz+hbHX1m745hV/Zm90r4/fsUFTKeB9I5axHBQC4jRPMqAxniBO2wkVzdNs9X28czaoKixH1lxaefvcLEtFkZMqy2qNs8vwdB04t89/1O/w1cDnyilFU='
LINE_NOTIFICATION_TOKEN = '2IXx92MpbbYfkdkpXAp5dHtopLWlxwqRM68SMuJClpD'


DEFAULT_SITE_STRATEGY_LIST = strategy.ALL_STRATEGY
DEFAULT_SITE_WATCHLIST = ['MSFT', 'AAPL', 'AMZN', 'BLDR', 'GOOGL', 'NFLX', 'META', 'SPY', 'QQQ']
DEFAULT_SITE_NOTIFICATION_TOKEN = LINE_NOTIFICATION_TOKEN
DEFAULT_SITE_ADMIN_EMAIL = 'jim.huang.bellevue@gmail.com'

TIMEZONE   ='US/Eastern'
DATABASES  ='sqlite3'
DEFAULT_ACCOUNT_INITIAL_BALANCE = 100000
TARGET_PROB=50
PRICE_RANGE_PREDICT_ALGO = strategy.PRICE_RANGE_BY_OPTION_STRADDLE
PREDICT_WINDOW = 20

LOGGER_NAME =  '__name__' #'debug_level_log'

GOOGLE_OUTH_CLIENT_ID_1 = "844605684221-9h4gvh5r7m23956uvg5pmrtf28ejblv0.apps.googleusercontent.com"
GOOGLE_OUTH_SECRETE_1 = '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'
GOOGLE_OUTH_CLIENT_ID = '375362083246-s8roson74k1cj5g8t6g95h4dogsdbt2d.apps.googleusercontent.com'
GOOGLE_OUTH_SECRETE = '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'


#MY_GMAIL_USER = "jim.huang.bellevue@gmail.com"
#MY_GMAIL_PASSWORD = "sdhbjsuhudmvuugp"

MY_GMAIL_USER       =  "optiontrader.bot@gmail.com"
MY_GMAIL_PASSWORD   =  "cjtzmcanwnfkgaqw"

MIN_OPEN_INTEREST = 0
MIN_DAYS_TO_EXPIRE = 2
MAX_DAYS_TO_EXPIRE = 365
MAX_BID_ASK_SPREAD = 3

STOCK_RANGE_PREDICT_DAYS = 90
CD_ANNUAL_RATE  = 5
TARGET_ANNUAL_RETURN = 20

OPEN_AI_KEY = "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"

if __name__ == '__main__':

    print(DATA_ROOT_DIR)

    #import re
    #p = str(Path().resolve())
    #print(p)
    #match = re.search(r"[^a-zA-Z]("+OPTION_TRADER+")[^a-zA-Z]", p)        
    #if match != None:
    #    l = match.start(1) + len(OPTION_TRADER)
    #    print(p[:l])


    #print(DATA_ROOT_DIR)