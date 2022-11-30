import telebot
from datetime import datetime as dt
import math

value = ''
old_value = ''

bot = telebot.TeleBot('5633053717:AAFbzV8UKlbgjPSUwkCBRlWaSZ2o47en_-A')
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('', callback_data='no'),
             telebot.types.InlineKeyboardButton('C',callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5',callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton('Pi', callback_data=math.pi),
             telebot.types.InlineKeyboardButton('e', callback_data=math.e),
             telebot.types.InlineKeyboardButton("^", callback_data='**'))

keyboard.row(telebot.types.InlineKeyboardButton('', callback_data='no'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(",", callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))



@bot.message_handler(commands=['start','calculater'])
def getMessage(message):
    global  value, old_value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)
    print(message)
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{message.from_user.id}  {message.from_user.first_name}\n')


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value
    global   old_value
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value !='':
            value = value[:len(value)-1]
    elif data == '=':
        try:
            time = dt.now().strftime('%D %H:%M')
            with open('log.txt', 'a', encoding='utf-8') as file:
                file.write(f'{time}: {value} = {str(eval(value))}\n')

            value = str(eval(value))

        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value!= '') or ('0' != old_value and value ==''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
    old_value = value
    if value == 'Ошибка!': value

bot.polling(none_stop=False, interval=0)
