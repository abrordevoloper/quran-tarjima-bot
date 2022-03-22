from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.haqqa_keybord import (haqqa_keybords,
haqqa_keybord1,haqqa_keybord2,haqqa_keybord3,haqqa_keybord4)
from keyboards.inline.callback_data import haqqa_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Haqqa')
async def show_haqqa(message: Message):
    await message.answer(f"<b>Haqqa surasini oyatlarini tanlang</b>",reply_markup=haqqa_keybord1)

@dp.callback_query_handler(haqqa_callback_data.filter())
async def show_haqqa(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=haqqa_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Haqqa</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(69,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(69,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Haqqa surasini oyatlarini tanlang</b>", reply_markup=haqqa_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Haqqa surasini oyatlarini tanlang</b>", reply_markup=haqqa_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Haqqa surasini oyatlarini tanlang</b>", reply_markup=haqqa_keybord3)
        elif int(callback_data['items']) <= 52:
            await call.message.answer(f"<b>Haqqa surasini oyatlarini tanlang</b>", reply_markup=haqqa_keybord4)

    except:
        pass