from dotenv import load_dotenv
import os
import telebot
import requests

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, use /help to see the list of available commands.')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Commands: \n /start \n /help')
    # bot.reply_to(message, 'Commands: \n /start \n /help \n /BTCBUSD \n /ETHBUSD \n /XTZBUSD \n /XTZBIDR \n /BUSDBIDR')


@bot.message_handler(commands=['BTCBUSD'])
def btc(message):
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCBUSD'
    response = requests.get(url)
    data = response.json()
    price = float(data['price'])
    bot.reply_to(message, f'The current price of Bitcoin is {price:,.2f} BUSD.')

@bot.message_handler(commands=['ETHBUSD'])
def btc(message):
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHBUSD'
    response = requests.get(url)
    data = response.json()
    price = float(data['price'])
    bot.reply_to(message, f'The current price of Ethereum is {price:,.2f} BUSD.')


@bot.message_handler(commands=['XTZBUSD'])
def btc(message):
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=XTZBUSD'
    response = requests.get(url)
    data = response.json()
    price = float(data['price'])
    bot.reply_to(message, f'The current price of Tezos is {price:,.2f} BUSD.')


@bot.message_handler(commands=['XTZBIDR'])
def btc(message):
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=XTZBUSD'
    response = requests.get(url)
    data = response.json()
    XTZinUSD = float(data['price'])
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BUSDBIDR'
    response = requests.get(url)
    data = response.json()
    USDtoIDR = float(data['price'])
    bot.reply_to(message, f'The current price of Tezos is {XTZinUSD * USDtoIDR:,.2f} BIDR.')


@bot.message_handler(commands=['BUSDBIDR'])
def btc(message):
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BUSDBIDR'
    response = requests.get(url)
    data = response.json()
    price = float(data['price'])
    bot.reply_to(message, f'The current price of BUSD is {price:,.2f} BIDR.')


bot.infinity_polling(logger_level=10)
# It's worth noting that in python-telegram-bot (telebot) library, logging.CRITICAL is 1 and logging.ERROR is 40 , logging.WARNING is 30, logging.INFO is 20, and logging.DEBUG is 10.
