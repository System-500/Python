import telebot
from telebot import types
bot = telebot.TeleBot('TG code')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Jak się masz?")

    markup.add(item1)
    bot.send_message(message.chat.id, "Cześć, {0.first_name}!\nJestem <b>{1.first_name}</b>, stworzony, aby powtarzać za tobą.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == "Jak się masz?":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Świetnie", callback_data='good')
        item2 = types.InlineKeyboardButton("Nie za bardzo", callback_data='bad')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Dzięki za zapytanie, super. A ty jak?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'To bardzo dobrze')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Najważniejsze to się uspokoić i nie płakać, zdarza się')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Jak się masz?",
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
