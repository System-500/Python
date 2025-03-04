import telebot
from telebot import types
bot= telebot.TeleBot('TG code')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hi.webp','rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("як справи?")

    markup.add(item1)
    bot.send_message(message.chat.id, "Привіт,{0.first_name}!\nЯ-<b>{1.first_name}</b>, створений аби повторювати за тобою. ".format(message.from_user, bot.get_me()),
              parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):

    if message.text == "як справи?":

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Класно",callback_data='good' )
        item2 = types.InlineKeyboardButton("Не дуже",callback_data='bad' )
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Дякую що запитав,супер.Ти сам як?', reply_markup=markup)
    else:
         bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good' :
                bot.send_message(call.message.chat.id, 'Це дуже добре')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Головне заспокійся і не плач, буває всяке')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="як справи?",
                                  reply_markup=None)



    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)


