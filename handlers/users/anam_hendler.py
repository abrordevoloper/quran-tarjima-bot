from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.anam_keybord import (anam_keybords,
    anam_keybord1,anam_keybord2,anam_keybord3,anam_keybord4,anam_keybord5,
    anam_keybord6,anam_keybord7,anam_keybord8,anam_keybord9,anam_keybord10,anam_keybord11
    )
from keyboards.inline.callback_data import anam_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Anam')
async def show_anam(message: Message):
    await message.answer(f"<b>Anam surasini oyatlarini tanlang</b>",reply_markup=anam_keybord1)

@dp.callback_query_handler(anam_callback_data.filter())
async def show_anam(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=anam_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Anam</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(6,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(6,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord10)
        elif int(callback_data['items']) <= 165:
            await call.message.answer(f"<b>Anam surasini oyatlarini tanlang</b>", reply_markup=anam_keybord11)
    except:
        pass