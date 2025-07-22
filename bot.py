import telebot
from telebot import types
import time

bot = telebot.TeleBot('7868895704:AAF556dZg4oBG2y-wMJYpumA2bgcXk1AE4g')

# Функція створення клавіатури
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("🔁 Почати заново")
    btn1 = types.KeyboardButton("Про мене")
    btn2 = types.KeyboardButton("Кошторис")
    btn3 = types.KeyboardButton("Зв'язок")
    btn4 = types.KeyboardButton("Завершити роботу")
    markup.row(btn0)
    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4)
    return markup

# /start команда
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт, вдячний за звернення!", reply_markup=main_menu())

# Обробка кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "🔁 Почати заново":
        bot.send_message(message.chat.id, "Привіт, вдячний за звернення!", reply_markup=main_menu())
    
    elif message.text == "Про мене":
        bot.send_message(message.chat.id,
            "🤖 Привіт! Я займаюся створенням Telegram-ботів під ключ.\n\n"
            "📌 Що я вмію:\n"
            "— Боти для продажів (каталог, замовлення, оплата)\n"
            "— Боти для прийому заявок\n"
            "— Авторассылка повідомлень\n"
            "— Боти з адмінкою (веб або через ТГ)\n"
            "— Зв’язок із Google Таблицями, базами даних\n"
            "— Парсинг, аналітика, антиспам\n"
            "— Авторизація через Telegram\n\n"
            "Працюю швидко, чітко та за доступною ціною 💼"
        )
    
    elif message.text == "Кошторис":
        bot.send_message(message.chat.id,
            "💵 Орієнтовні ціни на боти:\n\n"
            "🔹 Простий бот (команди, кнопки) — 200–800 грн\n"
            "🔹 Бот для замовлень (запис в таблицю, форма) — 700–1500 грн\n"
            "🔹 Бот-магазин з каталогом — 1500–3000 грн\n"
            "🔹 Бот з адмін-панеллю або базою даних — 2500–5000 грн\n"
            "🔹 Складні рішення з API, авторизацією тощо — 5000–7000 грн+\n\n"
            "Ціна залежить від складності задачі.\n"
            "Можна зробити поетапну розробку або тестову демо-версію ✅"
        )
    
    elif message.text == "Зв'язок":
        bot.send_message(message.chat.id,
            "Мій юзернейм телеграм: @rthijk\n"
            "Або за номером телефону: 095-746-54-33"
        )

    elif message.text == "Завершити роботу":
        bot.send_message(message.chat.id, "Дякую за звернення! Гарного дня! ☀️")
    
    else:
        bot.send_message(message.chat.id, "До зустрічі!")

# Запуск polling з обробкою помилок для стабільності
while True:
    try:
        bot.polling(non_stop=True, timeout=20, interval=0)
    except Exception as e:
        print(f"Помилка polling: {e}")
        time.sleep(5)
