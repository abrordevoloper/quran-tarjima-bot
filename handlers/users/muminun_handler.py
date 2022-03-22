from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.muminun_keybord import (muminun_keybords,
muminun_keybord1,muminun_keybord2,muminun_keybord3,muminun_keybord4,muminun_keybord5,muminun_keybord6,muminun_keybord7,muminun_keybord8)
from keyboards.inline.callback_data import muminun_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Muminun')
async def show_muminun(message: Message):
    await message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>",reply_markup=muminun_keybord1)

@dp.callback_query_handler(muminun_callback_data.filter())
async def show_muminun(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=muminun_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Muminun</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(23,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(23,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord7)
        elif int(callback_data['items']) <= 118:
            await call.message.answer(f"<b>Muminun surasini oyatlarini tanlang</b>", reply_markup=muminun_keybord8)

    except:
        pass