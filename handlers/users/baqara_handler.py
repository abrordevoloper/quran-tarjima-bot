from loader import dp
from aiogram.types import Message,CallbackQuery
from keyboards.inline.baqara_keybord import (baqara_keybords,
    baqara_keybord1,baqara_keybord2,baqara_keybord3,baqara_keybord4,baqara_keybord5,baqara_keybord6,
    baqara_keybord7,baqara_keybord8,baqara_keybord9,baqara_keybord10,baqara_keybord11,baqara_keybord12,
    baqara_keybord13,baqara_keybord14,baqara_keybord15,baqara_keybord16,baqara_keybord17,baqara_keybord18
                                            )

from keyboards.inline.callback_data import baqara_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Baqara')
async def show_baqara(message: Message):
    await message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>",reply_markup=baqara_keybord1)

@dp.callback_query_handler(baqara_callback_data.filter())
async def show_baqara(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=baqara_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Baqara</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(2,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(2,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord8)
        elif int(callback_data['items']) <= 144:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord9)
        elif int(callback_data['items']) <= 160:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord10)
        elif int(callback_data['items']) <= 176:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord11)
        elif int(callback_data['items']) <= 192:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord12)
        elif int(callback_data['items']) <= 208:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord13)
        elif int(callback_data['items']) <= 224:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord14)
        elif int(callback_data['items']) <= 240:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord15)
        elif int(callback_data['items']) <= 256:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord16)
        elif int(callback_data['items']) <= 272:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord17)
        elif int(callback_data['items']) <= 286:
            await call.message.answer(f"<b>Baqara surasini oyatlarini tanlang</b>", reply_markup=baqara_keybord18)

    except:
        pass