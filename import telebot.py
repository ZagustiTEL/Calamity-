import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = '7737738429:AAE4itTACHj3DT3XBTQX9UFY-Txts6LKYWg'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню
main_menu = InlineKeyboardMarkup(row_width=2)
button_adon = InlineKeyboardButton(text='Адоны для Calamity', callback_data='adon')
button_klass = InlineKeyboardButton(text='Классы', callback_data='klass')
main_menu.add(button_adon, button_klass)

# Меню адонов
adon_menu = InlineKeyboardMarkup(row_width=2)
button_catalist = InlineKeyboardButton(text='Calamity Catalist', url='https://terrariamods.wiki.gg/wiki/Catalyst')
button_overhaul = InlineKeyboardButton(text='Calamity Overhaul', url='https://terrariamods.wiki.gg/wiki/Calamity_Overhaul')
button_wotg = InlineKeyboardButton(text='Wrath of the Gods', url='https://terrariamods.wiki.gg/wiki/Wrath_of_the_Gods')
button_back = InlineKeyboardButton(text='Назад', callback_data='back')
adon_menu.add(button_catalist, button_overhaul, button_wotg, button_back)

# Меню классов
klass_menu = InlineKeyboardMarkup(row_width=2)
button_shooter = InlineKeyboardButton(text='Стрелок🏹', callback_data='shooter')
button_warrior = InlineKeyboardButton(text='Воин⚔️', callback_data='warrior')
button_mag = InlineKeyboardButton(text='Маг🧙', callback_data='mag')
button_summoner = InlineKeyboardButton(text='Призыватель🐴', callback_data='summoner')
button_rogue = InlineKeyboardButton(text='Разбойник🥷', callback_data='rogue')
klass_menu.add(button_shooter, button_warrior, button_mag, button_summoner, button_rogue, button_back)

@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    image_path = 'Terraria_Calamity_Mod.jpg'
    if not os.path.exists(image_path):
        await message.reply("Извините, изображение недоступно.")
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
        await message.reply(f"Произошла ошибка при отправке изображения: {e}")

@dp.callback_query_handler(lambda call: call.data == 'adon')
async def callback_adon(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption='Вы выбрали адоны для Calamity',
        reply_markup=adon_menu
    )

@dp.callback_query_handler(lambda call: call.data == 'klass')
async def callback_klass(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption='Вы выбрали классы в Calamity',
        reply_markup=klass_menu
    )

@dp.callback_query_handler(lambda call: call.data == 'back')
async def callback_back(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=main_menu)

@dp.callback_query_handler(lambda call: call.data == 'shooter')
async def callback_shooter(call: types.CallbackQuery):
    with open('photo_2025-01-22_19-34-58.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo)

@dp.callback_query_handler(lambda call: call.data == 'warrior')
async def callback_warrior(call: types.CallbackQuery):
    with open('воин.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo)

@dp.callback_query_handler(lambda call: call.data == 'mag')
async def callback_mag(call: types.CallbackQuery):
    with open('маг.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo)

@dp.callback_query_handler(lambda call: call.data == 'summoner')
async def callback_summoner(call: types.CallbackQuery):
    with open('призыв.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo)

@dp.callback_query_handler(lambda call: call.data == 'rogue')
async def callback_rogue(call: types.CallbackQuery):
    with open('разбойник.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)       
