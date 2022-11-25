import telebot
import random

'''from telebot import types # для указание типов  '''

token = '5872074889:AAEmfJDQ4Cc5kytFmCvAeDloCeiVDVGk4Zc'
bot = telebot.TeleBot('5872074889:AAEmfJDQ4Cc5kytFmCvAeDloCeiVDVGk4Zc')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     s = message.text
#     c = 'абв'
#     user_mes = list(filter(lambda s: not c in s, s.split()))
#     user_mes = ' '.join(user_mes)
#     bot.send_message(message.chat.id, user_mes)

candies = 0
max_candies = 28


@bot.message_handler(commands=["game"])
def game(message):
    global candies
    candies = 101
    bot.send_message(message.chat.id, f'На столе {candies} конфет ')


@bot.message_handler(content_types=["text"])
def inputs(message):
    global candies
    if candies <= 0:
        bot.send_message(message.chat.id, 'Игра окончена! ')
        return
    else:
        bot.send_message(message.chat.id, 'Возьмите конфеты! ')

    try:
        can = int(message.text)
        candies = candies - can
        bot.send_message(message.chat.id, f'На столе {candies} конфет ')
        ran_can = random.randint(1, max_candies)
        candies = candies - ran_can
        bot.send_message(message.chat.id, f'Бот взял {ran_can}, на столе {candies} конфет ')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Введите число! ')


bot.polling(none_stop=True, interval=0)
