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
button_starzi_god = types.InlineKeyboardButton(text='Страж Пожирателя богов', callback_data='strazi_god')
button_poltergast = types.InlineKeyboardButton(text='Полтергаст', callback_data='poltergeist')
button_star_ges = types.InlineKeyboardButton(text='Старый герцог', callback_data='star_ger')
button_dog = types.InlineKeyboardButton(text='Пожиратель богов', callback_data='dog')
button_yron = types.InlineKeyboardButton(text='Ярон, Дракон возрождения', callback_data='yron')
button_mehi = types.InlineKeyboardButton(text='Экзо-механизмы', callback_data='mehi')
button_kalamitas = types.InlineKeyboardButton(text='Высшая ведьма, Каламитас', callback_data='kalamitas')
button_back_ = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back_boss')
boss_menu_posmun.add(button_starzi, button_dragon, button_providens, button_starzi_god, button_poltergast, button_star_ges, button_dog, button_yron, button_mehi, button_kalamitas, button_back_)

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
        with open('босс/дохард/пб.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Пустынный бич первый босс в Calamity вот видео с его атаками https://youtu.be/MMHesZE_x28?si=6b5_tiE01TiJ7vcj", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'kr':
        with open('босс/дохард/крабулон.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Один из первых боссов вот видео с его атаками https://youtu.be/ozzQ8Th9coc?si=I9NZa2uKU_Yb6p5m", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'ry':
        with open('босс/дохард/разум улья.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Разум улья предпоследний босс до хардмода вот видео с его атаками https://youtu.be/LOsvYxawTHU?si=VJUornNQhQvI3LzO", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'per':
        with open('босс/дохард/перфораторы.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Перфотраторы предпоследний босс до хардмода вот видео с его атаками https://youtu.be/wg3r_r31h0A?si=7eZxtn-TA9daOrhz", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'gs':
        with open('босс/дохард/бог слизней.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Бог слизней последний босс дохардмода в Calamity вот видео с его атаками https://youtu.be/TVwJASDZJgA?si=qsfKEvDIhuIK6MwU", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
           
# Хардмодных боссов
    elif call.data == 'krio':
        with open('босс/хардмод/Снимок.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Криоген первый босс в хардмоде вот видео с его атаками https://youtu.be/GNadDMOvrd4?si=LGJyVXflB_Lljbi1", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
   
    elif call.data == 'ser':
        with open('босс/хардмод/1234.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Серный элементаль второй босс в Calamity вот видео с её атаками https://youtu.be/r3X19hfCMDM?si=2h5Wgmqj9i9WimPH", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'aqkva':
        with open('босс/хардмод/123.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Акватический бич вот видео с его атаками https://youtu.be/ZQ9qX4EQTkY?si=82h1zB7LRbG_nXa-", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'klon_Kalam':
        with open('босс/хардмод/124.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Клон каламита, вот видео с его актаками https://youtu.be/zHoU1gIycpk?si=y-8gW6Myny2WGvB1", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'anah_lev':
        with open('босс/хардмод/12.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Анахита и Левиафан не простой босс для просмотра их атак вот видео https://youtu.be/1UrR1CV6lx0?si=gJoS5BO3TYyk7Ite", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None) 

    elif call.data == 'astarm_areys':
        with open('босс/хардмод/1.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Аструм Ареус один из боссов в Calamity вот видео с его атаками https://youtu.be/1UrR1CV6lx0?si=gJoS5BO3TYyk7Ite", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'chuma':
        with open('босс/хардмод/12345.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Галиаф один из последних боссов в хардмоде вот видео с его атаками https://youtu.be/AEoF7vENYWY?si=qPyQD5Wths9jl7m6", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)
    
    elif call.data == 'razrusit':
        with open('босс/хардмод/1245.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Разрушитель один из последних боссов в хардмоде вот видео с его атаками https://youtu.be/3ZXtmPsxw1A?si=6wYwxcxdX1OOIiUm", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'astarm_deus':
        with open('босс/хардмод/142.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Вот Аструм Деус последний босс в хардмоде вот видео с его атаками https://youtu.be/i-kv2t6YjHI?si=2v-zjJ4TPM9AOqW3", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

# Пост-мунлордные боссов
    elif call.data == 'strazi':
        with open('босс/постмун/стражи.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Осквернённые Стражи первый босс после лунного лорда вот видео с его атаками https://youtu.be/77ChD5MAwts?si=EZtiqx-2Sf1RF1hH", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'dragon':
        with open('босс/постмун/дракон.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Псевдодракон, для победы вот видео с его атаками https://youtu.be/P6vC9d0BdIg?si=0FfIH6rafgc-wM_7", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'providens':
        with open('босс/постмун/провиденс.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Провиденс, для победы вот видео с его атаками https://youtu.be/4vFTFLORwCU?si=QzPikT4geDrHXTKx", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'strazi_god':
        with open('босс/постмун/стражи дога.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Сигнус для победы вот видео с его атаками https://youtu.be/Zh1VezH6jMI?si=b7MWoJUe7g0bkVVf\n Бесконечная Пустота https://youtu.be/FLRapiQT0HY?si=Mf9ORWsEjkTnYy6I\nНебестный Ткач для победы вот видео с его атаками https://youtu.be/ERuU9sKOMb0?si=oJ0NBgDYX3dCfYCk", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'poltergeist':
        with open('босс/постмун/гаст.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Полтергаст, для победы вот видео с его атаками https://youtu.be/B0wzsFnhYig?si=bG64k-fOpYN9_oOn", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'star_ger':
        with open('босс/постмун/герцог.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Старый Герцог, для победы вот видео с его атаками https://youtu.be/ugwGDpglo1Y?si=Fn6FWM7EEREvWyLl", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)  

    elif call.data == 'dog':
        with open('босс/постмун/дог.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Пожиратель Богов, для победы вот видео с его атаками https://youtu.be/Btvgj88YhAs?si=62MApP88rYh3BtO_", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)   

    elif call.data == 'yron':
        with open('босс/постмун/ярон.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Ярон, для победы вот видео с его атаками https://youtu.be/ESNrpeqnLAU?si=pSCYg9hQFG8rjEAV", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'mehi':
        with open('босс/постмун/межи.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="Экзо-механизмы, для победы вот видео с его атаками https://youtu.be/uHXHwvWC9Gc?si=7fgUpsYbR1vNkHjC", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)

    elif call.data == 'kalamitas':
        with open('босс/постмун/каламитос.PNG', 'rb') as photo:
            msg = bot.send_photo(call.message.chat.id, photo, caption="ВысшаяВедьма, Каламитас последний босс в Calamity вот видео с её атаками https://youtu.be/5iPVy-a_ef4?si=-jOd4qcl9Ahw-YKi", reply_markup=generate_markup())
            bot.register_next_step_handler(msg, lambda message: None)      

if __name__ == "__main__":
    bot.polling(none_stop=True)