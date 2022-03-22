from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.maryam_keybord import (maryam_keybords,
maryam_keybord1,maryam_keybord2,maryam_keybord3,maryam_keybord4,maryam_keybord5,maryam_keybord6,maryam_keybord7)
from keyboards.inline.callback_data import maryam_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Maryam')
async def show_maryam(message: Message):
    await message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>",reply_markup=maryam_keybord1)

@dp.callback_query_handler(maryam_callback_data.filter())
async def show_maryam(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=maryam_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Maryam</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(19,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(19,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord6)
        elif int(callback_data['items']) <= 98:
            await call.message.answer(f"<b>Maryam surasini oyatlarini tanlang</b>", reply_markup=maryam_keybord7)

    except:
        pass