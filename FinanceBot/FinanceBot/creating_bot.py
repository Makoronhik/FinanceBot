import telebot
from telebot import types
from functions.get_names import get_names  # Импортируем функцию из другого файла
from main import main
from token_1 import TOKEN
from functions.main_menu import main_menu # Импортируем функцию из другого файла
from functions.process_ticker import process_ticker # Импортируем функцию из другого файла
from functions.handle_course import handle_course





API_TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(API_TOKEN)


# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш FinanceBot. Я помогу вам увеличить доходность вашего инвестиционного портфеля. Чтобы узнать обо всех моих функциях нажмите Меню")
    main_menu(message)

# Обработка нажатия кнопки "Поиск"
@bot.message_handler(func=lambda message: message.text == "Поиск 🔍")
def handle_search(message):
    msg = bot.reply_to(message, "Пожалуйста, напишите тикер интересующей вас компании, например тикер Росбанка - ROSB:")
    bot.register_next_step_handler(msg, process_ticker)
    


# Обработка нажатия кнопки "Инфо"
@bot.message_handler(func=lambda message: message.text == "Инфо ℹ️")
def handle_info(message):
    bot.reply_to(message, "FinanceBot создается как студенческий проект, целью которго является практика в коде на Python, работа с ML-моделями, знакомство с Git, и работа с TinkoffInvest API и TelegramBot API. Принцип работы: введите тикер компании например ROSB или TCSG, далее по тикеру выгружаются архивные данные по цене акций за последние 3 года со свечой 1 час, после чего создаётся таблица где будет стоимость акций по времени, макроэкономические параметры, показатели компании, и при помощи ML мы угадываем стоимость через 3, 6, 9, 12 месяцев ")
    
    main_menu(message)

# Обработка нажатия кнопки "Меню"
@bot.message_handler(func=lambda message: message.text == "Меню 📱")
def handle_menu(message):
    commands = (
        "/start - Запустить бота\n"
        "Поиск 🔍 - Найти информацию о компании\n"
        "Курс 📈 - Получить курс акций (пока не реализовано)\n"
        "Инфо ℹ️ - Получить информацию о боте\n"
        "Меню 📱 - Показать все команды\n"
        "Обновить 🔁 - Обновить данные"
    )
    bot.reply_to(message, f"Команды бота:\n{commands}")
    main_menu(message)

# Обработка нажатия кнопки "Обновить"
@bot.message_handler(func=lambda message: message.text == "Обновить 🔁")
def handle_refresh(message):
    try:
        get_names(TOKEN)  # Вызов функции get_names
        bot.reply_to(message, "Успешно получили данные обо всех новых FIGI и Ticker.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обновлении файла: {str(e)}")
    main_menu(message)


# Запуск бота
if __name__ == '__main__':
    bot.polling()

