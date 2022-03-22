from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.qasos_keybord import (qasos_keybords,
qasos_keybord1,qasos_keybord2,qasos_keybord3,qasos_keybord4,qasos_keybord5,qasos_keybord6)
from keyboards.inline.callback_data import qasos_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Qasos')
async def show_qasos(message: Message):
    await message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>",reply_markup=qasos_keybord1)

@dp.callback_query_handler(qasos_callback_data.filter())
async def show_qasos(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=qasos_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Qasos</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(28,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(28,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>", reply_markup=qasos_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>", reply_markup=qasos_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>", reply_markup=qasos_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>", reply_markup=qasos_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>", reply_markup=qasos_keybord5)
        elif int(callback_data['items']) <= 88:
            await call.message.answer(f"<b>Qasos surasini oyatlarini tanlang</b>", reply_markup=qasos_keybord6)

    except:
        pass