from loader import dp
from aiogram.types import Message,CallbackQuery
from keyboards.inline.shuaro_keybord import (shuaro_keybords,
shuaro_keybord1,shuaro_keybord2,shuaro_keybord3,shuaro_keybord4,shuaro_keybord5,
shuaro_keybord6,shuaro_keybord7,shuaro_keybord8,shuaro_keybord9,shuaro_keybord10,shuaro_keybord11,
shuaro_keybord12,shuaro_keybord13,shuaro_keybord14,shuaro_keybord15)

from keyboards.inline.callback_data import shuaro_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Shuaro')
async def show_shuaro(message: Message):
    await message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>",reply_markup=shuaro_keybord1)

@dp.callback_query_handler(shuaro_callback_data.filter())
async def show_shuaro(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=shuaro_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Shuaro</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(26,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(26,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord10)
        elif int(callback_data['items']) <= 176:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord11)
        elif int(callback_data['items']) <= 192:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord12)
        elif int(callback_data['items']) <= 208:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord13)
        elif int(callback_data['items']) <= 224:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord14)
        elif int(callback_data['items']) <= 227:
            await call.message.answer(f"<b>Shuaro surasini oyatlarini tanlang</b>", reply_markup=shuaro_keybord15)

    except:
        pass