import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto

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
button_catalist = types.InlineKeyboardButton(text='Calamity Catalist', callback_data='Catalyst')
button_overhaul = types.InlineKeyboardButton(text='Calamity Overhaul', callback_data='Overhaul')
button_wotg = types.InlineKeyboardButton(text='Wrath of the Gods', callback_data='Wrath_of_the_Gods')
button_back = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back')
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
boss_menu_pre = types.InlineKeyboardButton(text='Пре-хардмодные боссы😀', callback_data='pre')
boss_menu_hard = types.InlineKeyboardButton(text='Хардмодные боссы😐', callback_data='hard')
boss_menu_posmun = types.InlineKeyboardButton(text='Пост-мунлордные боссы💀', callback_data='posmun')
button_back = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back')
boss_menu.add(boss_menu_pre, boss_menu_hard, boss_menu_posmun, button_back)

# Меню пре-хардмодных боссов
boss_menu_pre = types.InlineKeyboardMarkup(row_width=2)
button_db = types.InlineKeyboardButton(text='Пустынный бич', callback_data='db')
button_kr = types.InlineKeyboardButton(text='Крабулон', callback_data='kr')
button_ry = types.InlineKeyboardButton(text='Разум улья', callback_data='ry')
button_per = types.InlineKeyboardButton(text='Перфораторы', callback_data='per')
button_gs = types.InlineKeyboardButton(text='Бог слизней', callback_data='gs')
button_back_boss = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_boss')
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
button_back_boss = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_boss')
boss_menu_hard.add(button_krio, button_aqkva, button_ser, button_klon_Kalam, button_anah_lev, button_astarm_areys, button_chuma, button_razrusit, button_astarm_deus, button_back_boss)

# Меню пост-мунлордных боссов
boss_menu_posmun = types.InlineKeyboardMarkup(row_width=2)
button_starzi = types.InlineKeyboardButton(text='Осквернённые стражи', callback_data='strazi')
button_dragon = types.InlineKeyboardButton(text='Псевдодракон', callback_data='dragon')
button_providens = types.InlineKeyboardButton(text='Провиденс', callback_data='providens')
button_signus = types.InlineKeyboardButton(text='Сигнус', callback_data='signus')
button_pusota = types.InlineKeyboardButton(text='Нескончаемая пустота', callback_data='pustota')
button_tcah = types.InlineKeyboardButton(text='Штормовой ткач', callback_data='tcah')
button_poltergast = types.InlineKeyboardButton(text='Полтергаст', callback_data='poltergeist')
button_star_ges = types.InlineKeyboardButton(text='Старый герцог', callback_data='star_ger')
button_dog = types.InlineKeyboardButton(text='Пожиратель богов', callback_data='dog')
button_yron = types.InlineKeyboardButton(text='Ярон, Дракон возрождения', callback_data='yron')
button_mehi = types.InlineKeyboardButton(text='Экзо-механизмы', callback_data='mehi')
button_kalamitas = types.InlineKeyboardButton(text='Высшая ведьма, Каламитас', callback_data='kalamitas')
button_back_ = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_boss')
boss_menu_posmun.add(button_starzi, button_dragon, button_providens, button_signus, button_pusota, button_tcah, button_poltergast, button_star_ges, button_dog, button_yron, button_mehi, button_kalamitas, button_back_)

# классы
warrior_menu = types.InlineKeyboardMarkup(row_width=2)
button_start_warrior = types.InlineKeyboardButton(text='Начало игры', callback_data='start_warrior')
button_medium_warrior = types.InlineKeyboardButton(text='Средина игры', callback_data='midle_warrior')
button_endgm_warrior = types.InlineKeyboardButton(text='Конец игры', callback_data='end_warrior')
bitton_back_klass = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_klass')
warrior_menu.add(button_start_warrior, button_medium_warrior, button_endgm_warrior, bitton_back_klass)

shooter_menu = types.InlineKeyboardMarkup(row_width=2)
button_start_shooter = types.InlineKeyboardButton(text='Начало игры', callback_data='start_shooter')
button_medium_shooter = types.InlineKeyboardButton(text='Средина игры', callback_data='midle_shooter')
button_endgm_shooter = types.InlineKeyboardButton(text='Конец игры', callback_data='end_shooter')
bitton_back_klass = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_klass')
shooter_menu.add(button_start_shooter, button_medium_shooter, button_endgm_shooter, bitton_back_klass)

rogue_menu = types.InlineKeyboardMarkup(row_width=2)
button_start_rogue = types.InlineKeyboardButton(text='Начало игры', callback_data='start_rogue')
button_medium_rogue = types.InlineKeyboardButton(text='Средина игры', callback_data='midle_rogue')
button_endgm_rogue = types.InlineKeyboardButton(text='Конец игры', callback_data='end_rogue')
bitton_back_klass = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_klass')
rogue_menu.add(button_start_rogue, button_medium_rogue, button_endgm_rogue, bitton_back_klass)

mag_menu = types.InlineKeyboardMarkup(row_width=2)
button_start_mag = types.InlineKeyboardButton(text='Начало игры', callback_data='start_mag')
button_medium_mag = types.InlineKeyboardButton(text='Средина игры', callback_data='midle_mag')
button_endgm_mag = types.InlineKeyboardButton(text='Конец игры', callback_data='end_mag')
bitton_back_klass = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_klass')
mag_menu.add(button_start_mag, button_medium_mag, button_endgm_mag, bitton_back_klass)

summoner_menu = types.InlineKeyboardMarkup(row_width=2)
button_start_summoner = types.InlineKeyboardButton(text='Начало игры', callback_data='start_summoner')
button_medium_summoner = types.InlineKeyboardButton(text='Средина игры', callback_data='midle_summoner')
button_endgm_summoner = types.InlineKeyboardButton(text='Конец игры', callback_data='end_summoner')
bitton_back_klass = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_klass')
summoner_menu.add(button_start_summoner, button_medium_summoner, button_endgm_summoner, bitton_back_klass)

def generate_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Закрыть", callback_data="delete"))
    return markup

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

@bot.message_handler(commands=['help'])
def help_message(message):
    image_path = 'Без названия.jfif'  
    msg = bot.send_photo(
        chat_id=message.chat.id,
        photo=open(image_path, 'rb'),
        caption='Привет это бот который поможет разобраться в моде на Terraria под названием Calamity Mod.\nЭтот бот поможет помочь с вопросом какие предметы лучше собирать на разных этапах игры.\n Также бот покажет всех доступных боссов в моде и покажет как их убить.\nЧтобы начать введите /start'
    )

@bot.message_handler(commands=['web'])
def help_message(message):
    image_path = 'hq720.jpg'  
    msg = bot.send_photo(
        chat_id=message.chat.id,
        photo=open(image_path, 'rb'),
        caption="Вот ссылки для установки аддонов для Calamity и сам мод\nCalamity Mod https://steamcommunity.com/sharedfiles/filedetails/?id=2824688072\nCalamity Mod Music https://steamcommunity.com/sharedfiles/filedetails/?id=2824688266\nCalamity's Vanities https://steamcommunity.com/sharedfiles/filedetails/?id=2824688804&searchtext=\nCalamity Mod Infernum Mode https://steamcommunity.com/sharedfiles/filedetails/?id=3015412343&searchtext=\nCatalyst Mod https://steamcommunity.com/sharedfiles/filedetails/?id=2838015851&searchtext=\nCalamity: Wrath of the Gods https://steamcommunity.com/sharedfiles/filedetails/?id=2995193002&searchtext=\nCalamity Overhaul https://steamcommunity.com/sharedfiles/filedetails/?id=3161388997&searchtext=\nCalamity Ranger Expansion (Стрелок бедствия) https://steamcommunity.com/sharedfiles/filedetails/?id=2860270524&searchtext="
    )

@bot.message_handler(func=lambda message: True)
def handle_unknown_messages(message):
    bot.reply_to(message, 'Я не знаю, как ответить на это сообщение. Попробуйте ввести /start, /help или /web.')

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
                                 caption='Боссы — это сильные противники, требующие особых усилий для победы. Они делятся на несколько типов:\n1. Призываемые боссы — вызываются игроком через специальные предметы в определённых местах.(Пустынный Бич,Крабулон,Разрушитель и другие)\n2. Вражеские боссы — появляются автоматически после выполнения игроками конкретных действий(Анахита и Левиафан, Перфораторы, Разум улья и другие).\n3. Боссы событий — доступны только во время специальных игровых мероприятий.\n4. Мини-боссы — менее сложные версии обычных боссов, встречающиеся в разных локациях игры.\nПобеждая босса, игроки получают значимый прогресс в игре, получаю новуое оружие, броню и аксессуары.',
                                 reply_markup=boss_menu)
    
    elif call.data == 'back':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Вы вернулись на главное меню:',
                                 reply_markup=main_menu)

      
    if call.data == 'back_boss':
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
    
    elif call.data == 'back_klass':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                caption='Вы вернулись к классам:',
                                reply_markup=klass_menu)

    elif call.data == 'warrior':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Воин (Warrior) - класс, использующий оружие ближнего боя. Отличается от других классов самым большим показателем защиты и стабильным количеством урона. В кооперативе задачей является отвлечение монстров и боссов, принятие урона на себя, защита менее бронированных классов. Вот три основных сетапа на него',
                                 reply_markup=warrior_menu)
    
    elif call.data == 'shooter':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Стрелок (Ranger) — класс, использующий оружие дальнего боя. Отличается от других классов тем, что ему нужны боеприпасы для атаки. Имеет среднюю степень защиты. В кооперативе его задачей является нанесение урона на расстоянии, вместе с магом. Вот три основных сетапа на него',
                                 reply_markup=shooter_menu)

    elif call.data == 'mag':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Маг (Sorcerer) — класс, использующий оружие, наносящее магический урон, а также специальную броню, которая повышает силу магических атак, запас маны, шанс критического удара магическими атаками. Отличается от других классов пониженной защитой и высоким уроном. Для атаки необходима мана, которая автоматически пополняется со временем, либо может быть восстановлена специальными зельями или аксессуарами, что делает его непростым и достаточно затратным персонажем на многих стадиях игры. Вот три основных сетапа на него',
                                 reply_markup=mag_menu)

    elif call.data == 'rogue':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption='Разбойник (Rogue) - новый класс, добавляемый Calamity Mod. Также он имеет новую уникальную механику Скрытности (Stealth), даваемую комплектами брони на разбойника. Вот три основных сетапа на него',
                                 reply_markup=rogue_menu)

    elif call.data == 'summoner':
        bot.edit_message_caption(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 caption=' Призыватель (Summoner) — этот класс в отличие от других наносит большую часть урона не напрямую, а при помощи призванных существ - прислужников (например, слизней, пигмеев и шершней).',
                                 reply_markup=summoner_menu)

    elif call.data == 'delete':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    
    # Классы в начало
    elif call.data == 'start_shooter':
        with open('классы/стрелок/photo_2025-01-22_19-34-58.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на стрелка в начале", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'Overhaul':
        with open('Overhaul.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Мод Calamity Overhaul направлен на всестороннюю оптимизацию и расширение игрового процесса мода Calamity.\nПереработка оружия: Почти все орудия были переработаны, в них появились новые магазины и системы отдачи, что сделало бой более реалистичным.\nИнформацию о всех предметах можно найти перейдя по ссылке https://terrariamods.wiki.gg/wiki/Calamity_Overhaul", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'Catalyst':
        with open('Logo_(Catalyst).webp', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="The Catalyst Mod — это дополнение Calamity Mod, действие которого происходит в альтернативной вселенной, добавляющей новые предметы, врагов и супербосса в виде Астрагельдона.\nОзнакомиться со всеми предметами можно перейти по ссылке https://terrariamods.wiki.gg/wiki/Catalyst", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'Wrath_of_the_Gods':
        with open('images.jfif', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Wrath of the Gods — это неофициальный аддон для мода Calamity, который представляет супербоссов Noxus и Nameless Deity после игры.Основное внимание мода уделяется созданию вышеупомянутых сражений с боссами, а также другого побочного контента, чтобы наполнить его плотью, включая кат-сцены, специальные семена и подмиры.\nОзнакомиться со всеми предметами можно перейти по ссылке https://terrariamods.wiki.gg/wiki/Wrath_of_the_Gods", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'start_warrior':
        with open('классы/воин/воин.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на воина в начале", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'start_mag':
        with open('классы/маг/маг copy.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на мага в начале", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'start_summoner':
        with open('классы/призыв/призыв.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на призывателя в начале", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'start_rogue':
        with open('классы/разбойник/разбойник.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на разбойника в начале", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

# Классы середина
    elif call.data == 'midle_shooter':
        with open('классы/стрелок/1.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на стрелка в середине", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'midle_warrior':
        with open('классы/воин/8.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на воина в середине", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data =='midle_mag':
        with open('классы/маг/photo_2025-02-04_17-25-46.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на мага в середине", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data =='midle_summoner':
        with open('классы/призыв/photo_2025-02-04_17-26-52.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на призывателя в середине", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data =='midle_rogue':
        with open('классы/разбойник/1.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на разбойника в середине", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
            
# Классы конец
    elif call.data == 'end_shooter':
        with open('классы/стрелок/rjytw.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на стрелка в конце", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'end_warrior':
        with open('классы/воин/11.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на воина в конце", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'end_mag':
        with open('классы/маг/2.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на мага в конце", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'end_summoner':
        with open('классы/призыв/2.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на призывателя в конце", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'end_rogue':
        with open('классы/разбойник/photo_2025-02-04_17-24-35.jpg', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Рекомендуемые предметы на разбойника в конце", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
# Пре-хардмодные боссы
    elif call.data == 'db':
        with open('босс/дроп/пб1.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Это пре-хардмодный босс. Предполагается, что он будет одним из первых боссов, с которыми сразится игрок, и считается самым слабым из всех боссов, добавленных модификацией Calamity. Он рассчитан на сражение перед Глаз Ктулху Глазом Ктулху и после Король слизней Короля Слизней, но всё же может представлять значительную сложность для новых игроков, имеющих только базовое снаряжение.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'kr':
        with open('босс/дроп/кр1.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Крабулон (от англ. Crabulon) — это пре-хардмодный босс. Представляет собой гигантского серого краба с множеством грибных светящихся наростов.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'ry':
        with open('босс/дроп/ру.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Разум улья (От англ. The Hive Mind) — это пре-хардмодный босс, c которым можно сразится в искажении. У него есть неподвижная первая фаза и вторая фаза с телепортациями. Является альтерантивой Перфораторы Перфораторам для искажения.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'per':
        with open('босс/дроп/пер.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Перфораторы (англ. The Perforators) — это группа пре-хардмодных боссов, с которыми можно сразиться в багрянце. Представляют трёх червей разного вида, размера и поведения, а также главного улья. Являются багряной альтернативой Разум улья разума улья.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'gs':
        with open('босс/дроп/бс.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Бог слизней (The Slime God) — это пре-хардмодный босс, с которыми можно сразиться где угодно в любое время суток. Босс состоит из трёх основных частей: Ebonian Paladin map Эбонитовый паладин, Crimulan Paladin Багротановый паладин, и само Slime God Core map ядро. При использовании Перегруженная слякоть перегруженной слякоти появятся все три, независимо от того, содержит ли созданный мир багрянец или искажение.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
           
# Хардмодных боссов
    elif call.data == 'krio':
        with open('босс/дроп/крио.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Криоген (От англ. Cryogen) — это хардмодный босс, с которым можно сразится в снежном или ледяном биоме. Битва содержит множество фаз атак, а также множество снарядов и призываемых врагов. После победой над Криогеном освободится Архимаг Архимага, а также появится возможность добыть Крионитовая руда крионитовую руду в ледяном биоме.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
   
    elif call.data == 'ser':
        with open('босс/дроп/сэ.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Серный элементаль (Brimstone Elemental) — это хардмодный босс, с которым можно сразится в серной скале. В её поведении прослеживаются три характерные формы, различающиеся по уровню агрессии и способам нападения.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'aqkva':
        with open('босс/дроп/аб.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Акватический бич (англ. Aquatic Scourge) — это босс, с которым можно сразиться в сернистом море на любом этапе игры, но полагается, что с ним нужно сражаться в хардмоде. Является гидратированной и мутировавшей версией Пустынный бич Пустынного бича, они имеют сходство в своих выпадаемых предметов, но при этом существенно различаются в своем поведении.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'klon_Kalam':
        with open('босс/дроп/кк.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Клон Каламитас (Calamitas Clone) — это хардмодный босс, с которым можно сразиться ночью. Она является значимым боссом в середине хардмода, с которым игрок должен сразиться вскоре перед Плантера Плантерой или в качестве альтернативы ей.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'anah_lev':
        with open('босс/дроп/аил.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Левиафан и Анахита (Anahita and Leviathan) — это дуэт боссов, с которыми можно сразиться на любом этапе игры, но предполагается, что игрок будет сражаться с ними в хардмоде. Рекомендуется с ними сражаться только после получения пост-Плантера Плантерной экипировке, так как бой очень сложен и игроку придётся держать контроль не только над двумя противниками, но и их многочисленными прислужниками.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None) 

    elif call.data == 'astarm_areys':
        with open('босс/дроп/аа.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Аструм Ареус (От англ. Astrum Aureus) — это хардмодный босс. После победы над ним где-то в мире упадет метеорит астральной инфекции.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'chuma':
        with open('босс/дроп/гал.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Разносчица чумы, Голиаф (От Англ. The Plaguebringer Goliath) — это хардмодный босс и главная сила чумы, распространившейся на джунгли после поражения Голем Голема", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'razrusit':
        with open('босс/дроп/раз.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Разрушитель (от англ. Ravager) — хардмодный босс, с которым можно сразиться на поверхности в любое время суток. Помимо уникальных выпадаемых оружия и аксессуаров, его предназначение — служить эффективным, хотя и не всегда простым, средством получения Сплав жизни сплавов жизни, Ядро бедствия ядер бедствия и других материалов через Мясистая жеода мясистые жеоды После убийства Провиденс, Осквернённая богиня Провиденс Разрушитель становится сильнее: его урон и здоровье увеличиваются, а при убийстве самого Разрушителя можно будет получить Кровавый камень кровавый камень через Некромантическая жеода некромантические жеоды", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'astarm_deus':
        with open('босс/дроп/ад.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Аструм Деус (От Англ. Astrum Deus) - это хардмодный босс, которого нужно победить, чтобы получить возможность добывать Астральная руда Астральную руду. Вначале он представляет собой большого червя, подобно Уничтожитель Уничтожителю, но позже в ходе боя раздваивается.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

# Пост-мунлордные боссов
    elif call.data == 'strazi':
        with open('босс/дроп/стражи.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Осквернённые стражи (от англ. Profaned Guardians) — это пост-мунлордный босс, с которым можно сразится в освящении или в преисподней. Их необходимо убить, чтобы получить Осквернённое ядро осквернённое ядро, используемое для призыва Провиденс, Осквернённая богиня Провиденс, осквернённой богнини. Из каждого стража также выпадает уникальная 'реликвия'. Осквернённые стражи также призываются во время битвы с Провиденс, Оскверненной Богиней. Во время этого сражения они не будут атаковать игрока, вместо этого они будут давать Провиденс баффы.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'dragon':
        with open('босс/дроп/дракон.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Псевдодракон (от англ. Dragonfolly) — это босс с которым можно сразиться в джунглях. Хотя с ним можно сражаться в любое время после разрушения Солнечная башня солнечной башни, он предназначен для сражения вскоре после Лунный лорд Лунного лорда. Из него выпадают Лучезарное перо лучезарные перья, которые нужны для изготовления Благословлённое яйцо феникса благословлённого яйца феникса, предмета, призывающего Ярон, Дракон возрождения Ярона, Дракона возрождения, а также для создания Комплект Сильвы комплекта Сильвы.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'providens':
        with open('босс/дроп/пров.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Провиденс, Осквернённая богиня (От англ. Providence, the Profaned Goddess) — это пост-мунлордный босс с которым можно сразиться в преисподней или в освящении. Победив Провиденс, игрок получит Божественная жеода божественные жеоды, а также Руна Кос руну Кос, используемый для призыва боссов руны Кос . Кроме того, в мире появится Цветонитовая руда Цветонитовая руда, а Разрушитель Разрушитель и враги серной скалы будут усилены и из них начнут выпадать Кровавый камень кровавые камни.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'signus':
        with open('босс/дроп/сигнус.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Сигнус, Посланник Пожирателя (Signus, Envoy of the Devourer) — это пост-мунлордный босс и один из боссов руны Кос. При его убийстве можно получить Искривлённая пустота искривлённую пустоту, которая является материалом используемого для создания Космический червь космического червя, и также другие предметы.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'pustota':
        with open('босс/дроп/пустота.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Нескончаемая пустота (От Англ. Ceaseless Void) — это пост-мунлордный босс. Является одним из cтражей пожирателя. Из него выпадает Тёмная плазма Тёмная плазма, которая является материалом для изготовления Космический червь космического червя.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'tcah':
        with open('босс/дроп/ткач.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Штормовой ткач (От англ. Storm Weaver) — это пост-мунлордный босс, и один из боссов руны Кос. При его убийстве выпадает Бронированный панцирь бронированные панцири, которые нужны для создания Космический червь космического червя и некоторых других предметов.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'poltergeist':
        with open('босс/дроп/гаст.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Полтергаст (От англ. Polterghast) — это пост-мунлордный босс, с которым можно сразится в темнице. Хотя босс и является необязательным для продвижения по прогрессу мода, настоятельно рекомендуется сразиться с ним, прежде чем бросать вызов Пожиратель богов Пожирателю богов. Победив Полтергаста, игрок получит Губительная душа губительные души, материал, используемый для создания мощного вооружения. Дополнительно, после победы над ним, начнёт выпадать оружие из мини-боссов в бездне, а также будет разблокирован последний уровень события Кислотный дождь.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'star_ger':
        with open('босс/дроп/стгер.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Старый герцог (The Old Duke) — это пост-мунлордный босс, с которым можно сразиться в Сернистом море. Хотя это и необязательно, рекомендуется сражаться с ним перед Пожиратель богов Пожирателем богов.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)  

    elif call.data == 'dog':
        with open('босс/постмун/дог.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Пожиратель богов (англ. The Devourer of Gods) — это пост-мунлордный босс, который предназначен для сражения после победы над всеми боссами руны Кос. Бой с этим боссом длительный и сложный, он состоит из нескольких фаз и множества разнообразных атак и действий. Победив его, игрок получит Космилитовый слиток Космилитовые слитки, необходимый материал для создания, используемый для изготовления разнообразного снаряжения в конце игры. Тыквенная луна, Морозная луна и Солнечное затмение также значительно усложнятся, что приведет к выпадению из врагов Кошмарное топливо Кошмарного топлива, Эндотермическая энергия Эндотермической энергии и Фрагмент тёмного солнца Фрагментов тёмного солнца соответственно, которые также являются необходимыми материалами для создания в позднем этапе игры.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)   

    elif call.data == 'yron':
        with open('босс/дроп/ярон.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="рон, Дракон возрождения (англ. Yharon, Dragon of Rebirth) (также известный как Ярон, Восходящий феникс, когда его здоровье опускается ниже 55%) — ключевой пост-мунлордный босс, с которым можно сразиться на поверхности. Сражение с ним предполагается после убийства Пожиратель богов Пожирателя богов. Перед его призывом игрок должен хорошо вооружиться и подготовиться, так как босс невероятно сложен. Убийство Ярона наградит игрока Фрагмент души Ярона Фрагментами души Ярона и создаст в мире Ауритовая руда Ауритовую руду, давая игроку доступ к сильнейшему снаряжению.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'mehi':
        with open('босс/дроп/мехи.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Экзо-механизмы (от англ. Exo Mechs) - пост-мунлордный босс, с которым можно сразиться после убийства Yharon Map Icon Ярона и примерно в то же время, что и с Supreme Calamitas map Высшей ведьмой, Каламитас. Битва происходит с тремя экзо-мехами: ВП-01 Артемида, ВП-03 Аполлон, ВМ-05 Танатос и ВУ-09 Арес. На данный момент они являются одними из самых сложных боссов в моде. Победа над ними даст игроку Exo Prism экзо-призмы - материал, который участвует в создании эндгейм снаряжения.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'kalamitas':
        with open('босс/дроп/ввк.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Высшая ведьма, Каламитас (Supreme Witch, Calamitas) — это пост-мунлордный босс, с которым можно сразиться где угодно и в какое угодно время суток после поражения Ярон, Дракон возрождения Ярона, Дракона возрождения и который предназначен для сражения примерно в то же время, что и Экзо-механизмы Экзо-механизмы. В настоящее время она является одним из самых сложных боссов в модификации Calamity. Победа над ней превратит её в НИПа — Серная ведьма Серную ведьму, которая открывает доступ к Зачарованию.", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)      

if __name__ == "__main__":
    bot.polling(none_stop=True)
