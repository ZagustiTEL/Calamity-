import os
import telebot
from telebot import types

TOKEN = '7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg'

bot = telebot.TeleBot(TOKEN)

# Главное меню
main_menu = types.InlineKeyboardMarkup(row_width=2)
button_adon = types.InlineKeyboardButton(text='Адоны для Calamity', callback_data='adon')
button_klass = types.InlineKeyboardButton(text='Классы', callback_data='klass')
button_boss = types.InlineKeyboardButton(text='Боссы', callback_data='boss')
main_menu.add(button_adon, button_klass, button_boss)

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
button_summoner = types.InlineKeyboardButton(text='Призыватель🦄', callback_data='summoner')
button_rogue = types.InlineKeyboardButton(text='Разбойник🥷', callback_data='rogue')
klass_menu.add(button_shooter, button_warrior, button_mag, button_summoner, button_rogue, button_back)

#Меню боссов
boss_menu = types.InlineKeyboardMarkup(row_width=2)
boss_menu_pre = types.InlineKeyboardButton(text='Пре-хардмодные боссы', callback_data='pre')
boss_menu_hard = types.InlineKeyboardButton(text='Хардмодные боссы', callback_data='hard')
boss_menu_posmun = types.InlineKeyboardButton(text='Пост-мунлордные боссы', callback_data='posmun')
button_back = types.InlineKeyboardButton(text='Назад', callback_data='back')
boss_menu.add(boss_menu_pre, boss_menu_hard, boss_menu_posmun, button_back)

# Меню пре-хардмодных боссов
boss_menu_pre = types.InlineKeyboardMarkup(row_width=2)
button_db = types.InlineKeyboardButton(text='Пустынный бич', callback_data='db')
button_kr = types.InlineKeyboardButton(text='Крабулон', callback_data='kr')
button_ry = types.InlineKeyboardButton(text='Разум улья', callback_data='ry')
button_per = types.InlineKeyboardButton(text='Перфораторы', callback_data='per')
button_gs = types.InlineKeyboardButton(text='Бог слизней', callback_data='gs')
button_back_boss = types.InlineKeyboardButton(text='Назад', callback_data='back_boss')
boss_menu_pre.add(button_db, button_kr, button_ry, button_per, button_gs, button_back_boss)

# Меню хардмодных боссов
boss_menu_hard = types.InlineKeyboardMarkup(row_width=2)
button_krio = types.InlineKeyboardButton(text='Криоген', callback_data='krio')
button_aqkva = types.InlineKeyboardButton(text='Акватический бич', callback_data='aqkva')
button_ser = types.InlineKeyboardButton(text='Серный элементаль', callback_data='ser')
button_klon_Kalam = types.InlineKeyboardButton(text='Клон Каламитас', callback_data='klon_Kalam')
button_anah_lev = types.InlineKeyboardButton(text='Анахита и Левиафан', callback_data='anah_lev')
button_astarm_areys = types.InlineKeyboardButton(text='Аструм Ареус', callback_data='astarm_areys')
button_chuma = types.InlineKeyboardButton(text='Разносчица чумы, Голиаф', callback_data='chuma')
button_razrusit = types.InlineKeyboardButton(text='Разрушитель', callback_data='razrusit')
button_astarm_deus = types.InlineKeyboardButton(text='Аструм Деус', callback_data='astarm_deus')
button_back_boss = types.InlineKeyboardButton(text='Назад', callback_data='back_boss')
boss_menu_hard.add(button_krio, button_aqkva, button_ser, button_klon_Kalam, button_anah_lev, button_astarm_areys, button_chuma, button_razrusit, button_astarm_deus, button_back_boss)

# Меню пост-мунлордных боссов
boss_menu_posmun = types.InlineKeyboardMarkup(row_width=2)
button_starzi = types.InlineKeyboardButton(text='Осквернённые стражи', callback_data='starzi')
button_dragon = types.InlineKeyboardButton(text='Псевдодракон', callback_data='dragon')
button_providens = types.InlineKeyboardButton(text='Провиденс', callback_data='providens')
button_starzi_god = types.InlineKeyboardButton(text='Страж Пожирателя богов', callback_data='strazi_god')
button_poltergast = types.InlineKeyboardButton(text='Полтергаст', callback_data='poltergeist')
button_star_ges = types.InlineKeyboardButton(text='Старый герцог', callback_data='star_ger')
button_dog = types.InlineKeyboardButton(text='Пожиратель богов', callback_data='dog')
button_yron = types.InlineKeyboardButton(text='Ярон, Дракон возрождения', callback_data='yron')
button_mehi = types.InlineKeyboardButton(text='Экзо-механизмы', callback_data='mehi')
button_kalamitas = types.InlineKeyboardButton(text='Высшая ведьма, Каламитас', callback_data='kalamitas')
button_back_ = types.InlineKeyboardButton(text='Назад', callback_data='back_boss')
boss_menu_posmun.add(button_starzi, button_dragon, button_providens, button_starzi_god, button_poltergast, button_star_ges, button_dog, button_yron, button_mehi, button_kalamitas, button_back_)


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
        
    elif call.data == 'boss':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Вы выбрали боссы',
                                 reply_markup=boss_menu)
    
    elif call.data == 'back':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             caption='Вы вернулись на главное меню:',
                             reply_markup=main_menu)
        
    elif call.data == 'back_boss':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Вы вернулись к боссам',
                                 reply_markup=boss_menu)
    
    elif call.data == 'pre':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Меню пре-хардмодных боссов',
                                 reply_markup=boss_menu_pre)
        
    elif call.data == 'hard':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Меню хардмодных боссов',
                                 reply_markup=boss_menu_hard)
        
    elif call.data == 'posmun':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Меню пост-мунлордных боссов',
                                 reply_markup=boss_menu_posmun)
    
    

# Классы в начало
    elif call.data == 'start_shooter':
        with open('классы/стрелок/photo_2025-01-22_19-34-58.jpg', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    
    elif call.data == 'start_warrior':
        with open('классы/воин/воин.jpg', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'start_mag':
        with open('классы/маг/маг copy.jpg', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    
    elif call.data == 'start_summoner':
        with open('классы/призыв/призыв.jpg', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'start_rogue':
        with open('классы/разбойник/разбойник.jpg', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    
# Пре-хардмодные боссы
    elif call.data == 'db':
        with open('босс/дохард/пб.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'kr':
        with open('босс/дохард/крабулон.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'ry':
        with open('босс/дохард/разум улья.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    
    elif call.data == 'per':
        with open('босс/дохард/перфораторы.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    
    elif call.data == 'gs':
        with open('босс/дохард/бог слизней.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
           
# Хардмодных боссов
    elif call.data == 'krio':
        with open('босс/хардмод/Снимок.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)
   
    elif call.data == 'ser':
        with open('босс/хардмод/1234.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'aqkva':
        with open('босс/хардмод/123.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'klon_Kalam':
        with open('босс/хардмод/124.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'anah_lev':
        with open('босс/хардмод/12.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo) 

    elif call.data == 'astarm_areys':
        with open('босс/хардмод/1.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'chuma':
        with open('босс/хардмод/12345.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'razrusit':
        with open('босс/хардмод/1245.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'astarm_deus':
        with open('босс/хардмод/142.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

# Пост-мунлордные боссов
    elif call.data == 'strazi':
        with open('босс/постмун/стражи.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'dragon':
        with open('босс/постмун/дракон.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'providens':
        with open('босс/постмун/провиденс.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'strazi_god':
        with open('босс/постмун/стражи дога.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'poltergeist':
        with open('босс/постмун/гаст.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'star_ger':
        with open('босс/постмун/герцог.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)   

    elif call.data == 'god':
        with open('босс/постмун/дог.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)   

    elif call.data == 'yron':
        with open('босс/постмун/ярон.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)

    elif call.data == 'mehi':
        with open('босс/постмун/межи.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo) 

    elif call.data == 'kalamitas':
        with open('босс/постмун/каламитос.PNG', 'rb') as photo:
            bot.send_photo(chat_id=call.message.chat.id, photo=photo)      
          
if __name__ == "__main__":
    bot.polling(none_stop=True)