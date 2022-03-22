from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.rum_keybord import (rum_keybords,
rum_keybord1,rum_keybord2,rum_keybord3,rum_keybord4)
from keyboards.inline.callback_data import rum_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Rum')
async def show_rum(message: Message):
    await message.answer(f"<b>Rum surasini oyatlarini tanlang</b>",reply_markup=rum_keybord1)

@dp.callback_query_handler(rum_callback_data.filter())
async def show_rum(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=rum_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Rum</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(30,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(30,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Rum surasini oyatlarini tanlang</b>", reply_markup=rum_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Rum surasini oyatlarini tanlang</b>", reply_markup=rum_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Rum surasini oyatlarini tanlang</b>", reply_markup=rum_keybord3)
        elif int(callback_data['items']) <= 60:
            await call.message.answer(f"<b>Rum surasini oyatlarini tanlang</b>", reply_markup=rum_keybord4)

    except:
        pass