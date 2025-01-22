import telebot
from telebot import types

bot = telebot.TeleBot('7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg')

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup()
    file = open('Terraria_Calamity_Mod.jpg', 'rb')
    caption = 'Привет исследователь'
    bot.send_photo(message.chat.id,file,caption)

bot.polling(none_stop=True) 
