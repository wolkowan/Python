#!/usr/bin/python
import telebot

bot = telebot.TeleBot("5872074889:AAEmfJDQ4Cc5kytFmCvAeDloCeiVDVGk4Zc", parse_mode=None)



@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()