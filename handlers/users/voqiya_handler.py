from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.voqiya_keybord import (voqiya_keybords,
voqiya_keybord1,voqiya_keybord2,voqiya_keybord3,voqiya_keybord4,voqiya_keybord5,voqiya_keybord6
    )
from keyboards.inline.callback_data import voqiya_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Voqiya')
async def show_voqiya(message: Message):
    await message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>",reply_markup=voqiya_keybord1)

@dp.callback_query_handler(voqiya_callback_data.filter())
async def show_voqiya(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=voqiya_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Voqiya</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(56,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(56,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>", reply_markup=voqiya_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>", reply_markup=voqiya_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>", reply_markup=voqiya_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>", reply_markup=voqiya_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>", reply_markup=voqiya_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Voqiya surasini oyatlarini tanlang</b>", reply_markup=voqiya_keybord6)

    except:
        pass