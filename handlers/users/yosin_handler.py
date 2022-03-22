from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.yosin_keybord import (yosin_keybords,
yosin_keybord1,yosin_keybord2,yosin_keybord3,yosin_keybord4,yosin_keybord5,yosin_keybord6)
from keyboards.inline.callback_data import yosin_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Yosin')
async def show_yosin(message: Message):
    await message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>",reply_markup=yosin_keybord1)

@dp.callback_query_handler(yosin_callback_data.filter())
async def show_yosin(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=yosin_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Yosin</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(36,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(36,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>", reply_markup=yosin_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>", reply_markup=yosin_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>", reply_markup=yosin_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>", reply_markup=yosin_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>", reply_markup=yosin_keybord5)
        elif int(callback_data['items']) <= 83:
            await call.message.answer(f"<b>Yosin surasini oyatlarini tanlang</b>", reply_markup=yosin_keybord6)

    except:
        pass