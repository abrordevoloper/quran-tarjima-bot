from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.soffat_keybord import (soffat_keybords,
soffat_keybord1,soffat_keybord2,soffat_keybord3,soffat_keybord4,soffat_keybord5,
soffat_keybord6,soffat_keybord7,soffat_keybord8,soffat_keybord9,soffat_keybord10,soffat_keybord11,soffat_keybord12)
from keyboards.inline.callback_data import soffat_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Soffat')
async def show_soffat(message: Message):
    await message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>",reply_markup=soffat_keybord1)

@dp.callback_query_handler(soffat_callback_data.filter())
async def show_soffat(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=soffat_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Soffat</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(37,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(37,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord10)
        elif int(callback_data['items']) <= 176:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord11)
        elif int(callback_data['items']) <= 182:
            await call.message.answer(f"<b>Soffat surasini oyatlarini tanlang</b>", reply_markup=soffat_keybord12)

    except:
        pass
