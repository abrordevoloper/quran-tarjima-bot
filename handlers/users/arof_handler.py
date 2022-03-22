from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.arof_keybord import (arof_keybords,
    arof_keybord1,arof_keybord2,arof_keybord3,arof_keybord4,arof_keybord5,
    arof_keybord6,arof_keybord7,arof_keybord8,arof_keybord9,arof_keybord10,arof_keybord11,
    arof_keybord12,arof_keybord13
    )
from keyboards.inline.callback_data import arof_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Arof')
async def show_arof(message: Message):
    await message.answer(f"<b>Arof surasini oyatlarini tanlang</b>",reply_markup=arof_keybord1)

@dp.callback_query_handler(arof_callback_data.filter())
async def show_arof(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=arof_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Arof</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(7,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(7,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord10)
        elif int(callback_data['items']) <= 176:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord11)
        elif int(callback_data['items']) <= 192:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord12)
        elif int(callback_data['items']) <= 206:
            await call.message.answer(f"<b>Arof surasini oyatlarini tanlang</b>", reply_markup=arof_keybord13)

    except:
        pass