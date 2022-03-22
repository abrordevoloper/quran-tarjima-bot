from loader import dp
from datetime import datetime
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.default.home_menu import home_menu
from keyboards.inline.callback_data import namoz_vaqtlari_callback_data
from keyboards.inline.namoz_vaqtlari_keybord import namoz_vaqtlari_keybord1,namoz_vaqtlari_keybords
import logging
from .surah import namoz_time
@dp.message_handler(text_contains='Namoz vaqtlari')
async def show_namoz(message: Message):
    await message.delete()
    await message.answer(f"<b>Viloyatlardan birini tanlang</b>",reply_markup=namoz_vaqtlari_keybord1)

@dp.callback_query_handler(namoz_vaqtlari_callback_data.filter())
async def show_namoz_time(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    await call.answer(cache_time=60)
    info = f"<b>{namoz_vaqtlari_keybords[callback_data['items']]}</b>\n"
    info+=f"<b>➖➖➖➖➖➖</b>\n"
    info+=namoz_time(callback_data['items'])
    await call.message.answer(info)
    await call.message.delete_reply_markup()