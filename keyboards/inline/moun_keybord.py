from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import moun_callback_data

moun_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1': '1', '2': '2',
    '3': '3', '4': '4',
    '5': '5', '6': '6',
    '7': '7'
}
for key, value in buttons1.items():
    tugma = InlineKeyboardButton(text=key, callback_data=moun_callback_data.new(items=value))
    moun_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga', callback_data=moun_callback_data.new(items='back1'))
moun_keybord1.insert(back_button)







