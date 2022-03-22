from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import mulk_callback_data

mulk_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1':'1',    '2':'2',
    '3':'3',    '4':'4',
    '5':'5',    '6':'6',
    '7':'7',    "8":"8",
    '9':'9',    '10':'10',
    '11':'11',    '12':'12',
    '13':'13',    '14':'14',
    '15':'15',  '16':'16'
            }
for key,value in buttons1.items():
    tugma = InlineKeyboardButton(text=key,callback_data=mulk_callback_data.new(items=value))
    mulk_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=mulk_callback_data.new(items='back1'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=mulk_callback_data.new(items='next1'))
mulk_keybord1.insert(back_button)
mulk_keybord1.insert(next_button)

mulk_keybord2 = InlineKeyboardMarkup(row_width=4)
buttons2 = {
    '17':'17',    '18':'18',
    '19':'19',    '20':'20',
    '21':'21',    '22':'22',
    '23':'23',    '24':'24',
    '25':'25',    '26':'26',
    '27':'27',    '28':'28',
    '29':'29',    '30':'30'
}

for key,value in buttons2.items():
    tugma = InlineKeyboardButton(text=key,callback_data=mulk_callback_data.new(items=value))
    mulk_keybord2.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=mulk_callback_data.new(items='back2'))
mulk_keybord2.insert(back_button)

mulk_keybords = {
    'back2':mulk_keybord1,
    'next1':mulk_keybord2

            }
