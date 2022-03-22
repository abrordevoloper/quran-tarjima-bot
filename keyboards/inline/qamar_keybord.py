from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import qamar_callback_data
qamar_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1':'1',    '2':'2',
    '3':'3',    '4':'4',
    '5':'5',    '6':'6',
    '7':'7',    "8":"8",
    '9':'9',    '10':'10',
    '11':'11',  '12':'12',
    '13':'13',  '14':'14',
    '15':'15',  '16':'16'
}

for key,value in buttons1.items():
    tugma = InlineKeyboardButton(text=key,callback_data=qamar_callback_data.new(items=value))
    qamar_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=qamar_callback_data.new(items='back1'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=qamar_callback_data.new(items='next1'))
qamar_keybord1.insert(back_button)
qamar_keybord1.insert(next_button)

qamar_keybord2 = InlineKeyboardMarkup(row_width=4)
buttons2 = {
    '17':'17',    '18':'18',
    '19':'19',    '20':'20',
    '21':'21',    '22':'22',
    '23':'23',    '24':'24',
    '25':'25',    '26':'26',
    '27':'27',    '28':'28',
    '29':'29',    '30':'30',
    '31':'31',    '32':'32'
}

for key,value in buttons2.items():
    tugma = InlineKeyboardButton(text=key,callback_data=qamar_callback_data.new(items=value))
    qamar_keybord2.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=qamar_callback_data.new(items='back2'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=qamar_callback_data.new(items='next2'))
qamar_keybord2.insert(back_button)
qamar_keybord2.insert(next_button)

qamar_keybord3 = InlineKeyboardMarkup(row_width=4)
buttons3 = {
    '33':'33',    '34':'34',
    '35':'35',    '36':'36',
    '37':'37',    '38':'38',
    '39':'39',    '40':'40',
    '41':'41',    '42':'42',
    '43':'43',    '44':'44',
    '45':'45',    '46':'46',
    '47':'47',    '48':'48'
}

for key,value in buttons3.items():
    tugma = InlineKeyboardButton(text=key,callback_data=qamar_callback_data.new(items=value))
    qamar_keybord3.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=qamar_callback_data.new(items='back3'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=qamar_callback_data.new(items='next3'))
qamar_keybord3.insert(back_button)
qamar_keybord3.insert(next_button)

qamar_keybord4 = InlineKeyboardMarkup(row_width=4)
buttons4 = {
    '49':'49',    '50':'50',
    '51':'51',    '52':'52',
    '53':'53',    '54':'54',
    '55':'55'
}

for key,value in buttons4.items():
    tugma = InlineKeyboardButton(text=key,callback_data=qamar_callback_data.new(items=value))
    qamar_keybord4.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=qamar_callback_data.new(items='back4'))
qamar_keybord4.insert(back_button)

qamar_keybords = {
    'back4':qamar_keybord3,
    'back3':qamar_keybord2,
    'back2':qamar_keybord1,
    'next1':qamar_keybord2,
    'next2':qamar_keybord3,
    'next3':qamar_keybord4
            }
