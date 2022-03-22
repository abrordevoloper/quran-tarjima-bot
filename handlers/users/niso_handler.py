from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.niso_keybord import (niso_keybords,
    niso_keybord1,niso_keybord2,niso_keybord3,niso_keybord4,niso_keybord5,
    niso_keybord6,niso_keybord7,niso_keybord8,niso_keybord9,niso_keybord10,niso_keybord11
    )
from keyboards.inline.callback_data import niso_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Niso')
async def show_imron(message: Message):
    await message.answer(f"<b>Niso surasini oyatlarini tanlang</b>",reply_markup=niso_keybord1)

@dp.callback_query_handler(niso_callback_data.filter())
async def show_niso(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=niso_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Niso</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(4,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(4,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord10)
        elif int(callback_data['items']) <= 176:
            await call.message.answer(f"<b>Niso surasini oyatlarini tanlang</b>", reply_markup=niso_keybord11)
    except:
        pass