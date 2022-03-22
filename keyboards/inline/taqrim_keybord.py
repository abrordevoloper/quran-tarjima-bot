from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import taqrim_callback_data

taqrim_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1':'1',    '2':'2',
    '3':'3',    '4':'4',
    '5':'5',    '6':'6',
    '7':'7',    "8":"8",
    '9':'9',    '10':'10',
    '11':'11',    '12':'12'
            }
for key,value in buttons1.items():
    tugma = InlineKeyboardButton(text=key,callback_data=taqrim_callback_data.new(items=value))
    taqrim_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=taqrim_callback_data.new(items='back1'))
taqrim_keybord1.insert(back_button)
