from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.kahf_keybord import (kahf_keybords,
kahf_keybord1,kahf_keybord2,kahf_keybord3,kahf_keybord4,kahf_keybord5,kahf_keybord6,kahf_keybord7)
from keyboards.inline.callback_data import kahf_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Kahf')
async def show_kahf(message: Message):
    await message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>",reply_markup=kahf_keybord1)

@dp.callback_query_handler(kahf_callback_data.filter())
async def show_kahf(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=kahf_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Kahf</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(18,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(18,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord6)
        elif int(callback_data['items']) <= 110:
            await call.message.answer(f"<b>Kahf surasini oyatlarini tanlang</b>", reply_markup=kahf_keybord7)

    except:
        pass