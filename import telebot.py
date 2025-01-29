from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
import os

API_TOKEN = '7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Главное меню
main_menu = InlineKeyboardMarkup(row_width=2)
button_adon = InlineKeyboardButton('Адоны для Calamity', callback_data='adon')
button_klass = InlineKeyboardButton('Классы', callback_data='klass')
main_menu.insert(button_adon)
main_menu.insert(button_klass)

# Меню адонов
adon_menu = InlineKeyboardMarkup(row_width=2)
button_catalist = InlineKeyboardButton('Calamity Catalist', url='https://terrariamods.wiki.gg/wiki/Catalyst')
button_overhaul = InlineKeyboardButton('Calamity Overhaul', url='https://terrariamods.wiki.gg/wiki/Calamity_Overhaul')
button_wotg = InlineKeyboardButton('Wrath of the Gods', url='https://terrariamods.wiki.gg/wiki/Wrath_of_the_Gods')
button_back = InlineKeyboardButton('Назад', callback_data='back')
adon_menu.insert(button_catalist)
adon_menu.insert(button_overhaul)
adon_menu.insert(button_wotg)
adon_menu.insert(button_back)

# Меню классов
klass_menu = InlineKeyboardMarkup(row_width=2)
button_shooter = InlineKeyboardButton('Стрелок🏹', callback_data='shooter')
button_warrior = InlineKeyboardButton('Воин⚔️', callback_data='warrior')
button_mag = InlineKeyboardButton('Маг🧙', callback_data='mag')
button_summoner = InlineKeyboardButton('Призыватель🐴', callback_data='summoner')
button_rogue = InlineKeyboardButton('Разбойник🥷', callback_data='rogue')
klass_menu.insert(button_shooter)
klass_menu.insert(button_warrior)
klass_menu.insert(button_mag)
klass_menu.insert(button_summoner)
klass_menu.insert(button_rogue)
klass_menu.insert(button_back)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    image_path = 'Terraria_Calamity_Mod.jpg'
    if not os.path.exists(image_path):
        await message.answer("Извините, изображение недоступно.")
        return
    
    try:
        with open(image_path, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption='Привет исследователь. Выберите категорию:',
                reply_markup=main_menu
            )
    except Exception as e:
        await message.answer(f"Произошла ошибка при отправке изображения: {e}")

@dp.callback_query_handler()
async def inline_callback(query: types.CallbackQuery):
    data = query.data
    if data == 'adon':
        await bot.edit_message_caption(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            caption='Вы выбрали адоны для Calamity',
            reply_markup=adon_menu
        )
    elif data == 'klass':
        await bot.edit_message_caption(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            caption='Вы выбрали классы в Calamity',
            reply_markup=klass_menu
        )
    elif data == 'back':
        await bot.edit_message_reply_markup(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            reply_markup=main_menu
        )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
