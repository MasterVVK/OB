from telebot import TeleBot, types
from yookassa import Configuration, Payment

# Настройки бота и ЮKassa
TOKEN = ''
bot = TeleBot(TOKEN)

# Конфигурация ЮKassa
shop_id = '371138'
secret_key = 'test_fo-_hU2Yy5bRR8GKE1K-B8hcGXWq4Jnf6fCIZrQPzHE'
Configuration.account_id = shop_id
Configuration.secret_key = secret_key

def create_payment(amount, currency, return_url, description):
    """ Создать платеж через ЮKassa и возвратить объект платежа или None при ошибке. """
    try:
        payment = Payment.create({
            "amount": {
                "value": amount,
                "currency": currency
            },
            "confirmation": {
                "type": "redirect",
                "return_url": return_url
            },
            "capture": True,
            "description": description
        })
        return payment
    except Exception as e:
        print(f"Ошибка при создании платежа: {e}")
        return None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pay_button = types.KeyboardButton('Оплатить')
    markup.add(pay_button)
    bot.send_message(message.chat.id, "Для оплаты нажмите кнопку 'Оплатить'", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Оплатить")
def handle_payment(message):
    amount = "100.00"  # Сумма платежа
    currency = "RUB"  # Валюта платежа
    return_url = "https://t.me/ForPG_bot"  # URL возврата
    description = f"Платеж на {amount} руб."  # Формируем описание с использованием f-string

    payment = create_payment(amount, currency, return_url, description)
    if payment and payment.confirmation and payment.confirmation.confirmation_url:
        markup = types.InlineKeyboardMarkup()
        pay_button = types.InlineKeyboardButton('Перейти к оплате', url=payment.confirmation.confirmation_url)
        markup.add(pay_button)
        bot.send_message(message.chat.id, "Перейдите по ссылке для оплаты:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Не удалось создать платеж, пожалуйста, попробуйте позже.")

bot.polling(none_stop=True)
