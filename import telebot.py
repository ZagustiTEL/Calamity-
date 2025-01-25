import telebot 
from telebot import types

bot = telebot.TeleBot('7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg')

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup()
    bat1=types.InlineKeyboardButton('Адоны для Calamity', callback_data='adon')
    bat2=types.InlineKeyboardButton('Классы', callback_data='klass')
    markup.row(bat1,bat2)
    file = open('Terraria_Calamity_Mod.jpg', 'rb')
    caption = 'Привет исследователь'
    bot.send_photo(message.chat.id,file,caption , reply_markup=markup )
   
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'adon':
        markup1 = types.InlineKeyboardMarkup()
        bat3 = types.InlineKeyboardButton('Calamity Overhul', url='https://terrariamods.wiki.gg/wiki/Calamity_Overhaul')
        bat4 = types.InlineKeyboardButton('Calamity Catalyst', url='https://terrariamods.wiki.gg/wiki/Catalyst')
        markup1.add(bat3, bat4)
        bot.edit_message_text(call.message.chat.id, "Выберите аддон:", reply_markup=markup1)

bot.polling(none_stop=True)
