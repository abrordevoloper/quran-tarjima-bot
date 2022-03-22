from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import nosr_callback_data

nosr_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1': '1', '2': '2',
    '3': '3'
}
for key, value in buttons1.items():
    tugma = InlineKeyboardButton(text=key, callback_data=nosr_callback_data.new(items=value))
    nosr_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga', callback_data=nosr_callback_data.new(items='back1'))
nosr_keybord1.insert(back_button)










