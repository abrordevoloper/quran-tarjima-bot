from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import fotiha_callback_data
fotiha_keybord = InlineKeyboardMarkup(row_width=4)

buttons = {
    '1':'1',    '2':'2',
    '3':'3',    '4':'4',
    '5':'5',    '6':'6',
    '7':'7',    "":""
}

for key,value in buttons.items():
    tugma = InlineKeyboardButton(text=key,callback_data=fotiha_callback_data.new(items=value))
    fotiha_keybord.insert(tugma)

tugma = InlineKeyboardButton(text='🔙 ortga',callback_data=fotiha_callback_data.new(items='back1'))
fotiha_keybord.insert(tugma)