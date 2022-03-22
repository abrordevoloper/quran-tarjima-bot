from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import naba_callback_data

naba_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1': '1', '2': '2',
    '3': '3', '4': '4',
    '5': '5', '6': '6',
    '7': '7', "8": "8",
    '9': '9', '10': '10',
    '11': '11', '12': '12',
    '13': '13', '14': '14',
    '15': '15', '16': '16'
}
for key, value in buttons1.items():
    tugma = InlineKeyboardButton(text=key, callback_data=naba_callback_data.new(items=value))
    naba_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga', callback_data=naba_callback_data.new(items='back1'))
next_button = InlineKeyboardButton(text='keyingisi', callback_data=naba_callback_data.new(items='next1'))
naba_keybord1.insert(back_button)
naba_keybord1.insert(next_button)

naba_keybord2 = InlineKeyboardMarkup(row_width=4)
buttons2 = {
    '17': '17', '18': '18',
    '19': '19', '20': '20',
    '21': '21', '22': '22',
    '23': '23', '24': '24',
    '25': '25', '26': '26',
    '27': '27', '28': '28',
    '29': '29', '30': '30',
    '31': '31', '32': '32'
}

for key, value in buttons2.items():
    tugma = InlineKeyboardButton(text=key, callback_data=naba_callback_data.new(items=value))
    naba_keybord2.insert(tugma)

back_button = InlineKeyboardButton(text='ortga', callback_data=naba_callback_data.new(items='back2'))
next_button = InlineKeyboardButton(text='keyingisi', callback_data=naba_callback_data.new(items='next2'))
naba_keybord2.insert(back_button)
naba_keybord2.insert(next_button)

naba_keybord3 = InlineKeyboardMarkup(row_width=4)
buttons3 = {
    '33': '33', '34': '34',
    '35': '35', '36': '36',
    '37': '37', '38': '38',
    '39': '39', '40': '40'
}

for key, value in buttons3.items():
    tugma = InlineKeyboardButton(text=key, callback_data=naba_callback_data.new(items=value))
    naba_keybord3.insert(tugma)

back_button = InlineKeyboardButton(text='ortga', callback_data=naba_callback_data.new(items='back3'))
naba_keybord3.insert(back_button)

naba_keybords = {
    'back3': naba_keybord2,
    'back2': naba_keybord1,
    'next1': naba_keybord2,
    'next2': naba_keybord3

}










