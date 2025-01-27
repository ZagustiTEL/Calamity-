import os
import telebot
from telebot import types

TOKEN = '7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg'

bot = telebot.TeleBot(TOKEN)

# Главное меню
main_menu = types.InlineKeyboardMarkup(row_width=2)
button_adon = types.InlineKeyboardButton(text='Адоны для Calamity', callback_data='adon')
button_klass = types.InlineKeyboardButton(text='Классы', callback_data='klass')
main_menu.add(button_adon, button_klass)

# Меню адонов
adon_menu = types.InlineKeyboardMarkup(row_width=2)
button_catalist = types.InlineKeyboardButton(text='Calamity Catalist', url='https://terrariamods.wiki.gg/wiki/Catalyst')
button_overhaul = types.InlineKeyboardButton(text='Calamity Overhaul', url='https://terrariamods.wiki.gg/wiki/Calamity_Overhaul')
button_wotg = types.InlineKeyboardButton(text='Wrath of the Gods', url='https://terrariamods.wiki.gg/wiki/Wrath_of_the_Gods')
button_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
adon_menu.add(button_catalist, button_overhaul, button_wotg, button_back)

# Меню классов
klass_menu = types.InlineKeyboardMarkup(row_width=2)
button_shooter = types.InlineKeyboardButton(text='Стрелок🏹', callback_data='shooter')
button_warrior = types.InlineKeyboardButton(text='Воин⚔️', callback_data='warrior')
button_mag = types.InlineKeyboardButton(text='Маг🧙', callback_data='mag')
button_summoner = types.InlineKeyboardButton(text='Призыватель🐴', callback_data='summoner')
button_rogue = types.InlineKeyboardButton(text='Разбойник🥷', callback_data='rogue')
klass_menu.add(button_shooter, button_warrior, button_mag, button_summoner, button_rogue, button_back)

@bot.message_handler(commands=['start'])
def handle_start(message):
    image_path = 'Terraria_Calamity_Mod.jpg'
    if not os.path.exists(image_path):
        bot.reply_to(message, "Извините, изображение недоступно.")
        return

    try:
        with open(image_path, 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption='Привет исследователь. Выберите категорию:',
                reply_markup=main_menu
            )
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при отправке изображения: {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'adon':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Вы выбрали адоны для Calamity',
                                 reply_markup=adon_menu)
        
    elif call.data == 'klass':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Вы выбрали классы в Calamity',
                                 reply_markup=klass_menu)
    
    elif call.data == 'back':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      reply_markup=main_menu)

if __name__ == "__main__":
    bot.polling(none_stop=True)
