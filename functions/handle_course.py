import telebot
from telebot import types
from functions.get_names import get_names  # Импортируем функцию из другого файла
from main import main
from token_1 import TOKEN
from functions.main_menu import main_menu # Импортируем функцию из другого файла
from functions.process_ticker import process_ticker # Импортируем функцию из другого файла
from datetime import datetime
import requests

# Замените 'YOUR_API_TOKEN' на токен, полученный от BotFather
API_TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(API_TOKEN)



# Обработка нажатия кнопки "Курс"
@bot.message_handler(func=lambda message: message.text == "Курс 📈")
def handle_course(message):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    currencies = ''
    for currency in response['Valute']:
       if currency['CharCode'] == 'RUB':
         continue
       rate = f'{currency["Value"]:.4f} ({currency["Name"]})'
       currencies += f'{rate}\n'
       return currencies
    rates = handle_course()
    bot.reply_to(message,f'Текущие курсы валют:\n{rates}')
    main_menu(message)