from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.yunus_keybord import (yunus_keybords,
     yunus_keybord1,yunus_keybord2,yunus_keybord3,yunus_keybord4,yunus_keybord5,yunus_keybord6,yunus_keybord7)
from keyboards.inline.callback_data import yunus_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Yunus')
async def show_yunus(message: Message):
    await message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>",reply_markup=yunus_keybord1)

@dp.callback_query_handler(yunus_callback_data.filter())
async def show_yunus(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=yunus_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Yunus</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(10,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(10,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord6)
        elif int(callback_data['items']) <= 109:
            await call.message.answer(f"<b>Yunus surasini oyatlarini tanlang</b>", reply_markup=yunus_keybord7)

    except:
          pass