from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.anbiyo_keybord import (anbiyo_keybords,
anbiyo_keybord1,anbiyo_keybord2,anbiyo_keybord3,anbiyo_keybord4,anbiyo_keybord5,anbiyo_keybord6,anbiyo_keybord7)
from keyboards.inline.callback_data import anbiyo_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Anbiyo')
async def show_anbiyo(message: Message):
    await message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>",reply_markup=anbiyo_keybord1)

@dp.callback_query_handler(anbiyo_callback_data.filter())
async def show_anbiyo(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=anbiyo_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Anbiyo</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(21,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(21,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Anbiyo surasini oyatlarini tanlang</b>", reply_markup=anbiyo_keybord7)

    except:
        pass