import telebot
import requests
from functions.main_menu import main_menu
from telebot import types



TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(TOKEN)



def get_currency_rates():
  url = f"https://openexchangerates.org/api/latest.json?app_id=aa6485066b6848b6b1dc7f494929e06f"
  response = requests.get(url)
  data = response.json()
  return data
