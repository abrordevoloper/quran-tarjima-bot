from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import asr_callback_data

asr_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1': '1', '2': '2',
    '3': '3'
}
for key, value in buttons1.items():
    tugma = InlineKeyboardButton(text=key, callback_data=asr_callback_data.new(items=value))
    asr_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga', callback_data=asr_callback_data.new(items='back1'))
asr_keybord1.insert(back_button)









