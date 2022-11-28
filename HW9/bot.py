import telebot

bot = telebot.Telebot("5624749670:AAFLPcL1eMzrL-mJ_SOJ3EH1L1Ako-Touu8", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()