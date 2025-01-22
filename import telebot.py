import telebot

bot = telebot.TeleBot('7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет исследователь")

bot.polling(none_stop=True) 
