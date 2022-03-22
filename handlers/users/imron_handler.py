from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.imron_keybord import (imron_keybords,
    imron_keybord1,imron_keybord2,imron_keybord3,imron_keybord4,imron_keybord5,
    imron_keybord6,imron_keybord7,imron_keybord8,imron_keybord9,imron_keybord10,
    imron_keybord11,imron_keybord12,imron_keybord13)

from keyboards.inline.callback_data import imron_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Imron')
async def show_imron(message: Message):
    await message.answer(f"<b>Imron surasini oyatlarini tanlang</b>",reply_markup=imron_keybord1)

@dp.callback_query_handler(imron_callback_data.filter())
async def show_imron(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=imron_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Imron</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(3,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(3,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord10)
        elif int(callback_data['items']) <= 176:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord11)
        elif int(callback_data['items']) <= 192:
            await call.message.answer(f"<b>Imron surasini oyatlarini tanlang</b>", reply_markup=imron_keybord12)
        elif int(callback_data['items']) <= 200:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=imron_keybord13)

    except:
        pass