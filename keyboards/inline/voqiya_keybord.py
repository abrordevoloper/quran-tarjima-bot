from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import voqiya_callback_data

voqiya_keybord1 = InlineKeyboardMarkup(row_width=4)

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
    tugma = InlineKeyboardButton(text=key,callback_data=voqiya_callback_data.new(items=value))
    voqiya_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=voqiya_callback_data.new(items='back1'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=voqiya_callback_data.new(items='next1'))
voqiya_keybord1.insert(back_button)
voqiya_keybord1.insert(next_button)

voqiya_keybord2 = InlineKeyboardMarkup(row_width=4)
buttons2 = {
    '17':'17',    '18':'18',
    '19':'19',    '20':'20',
    '21':'21',    '22':'22',
    '23':'23',    '24':'24',
    '25':'25',    '26':'26',
    '27':'27',    '28':'28',
    '29':'29',    '30':'30',
    '31':'31',      '32':'32'
}

for key,value in buttons2.items():
    tugma = InlineKeyboardButton(text=key,callback_data=voqiya_callback_data.new(items=value))
    voqiya_keybord2.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=voqiya_callback_data.new(items='back2'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=voqiya_callback_data.new(items='next2'))
voqiya_keybord2.insert(back_button)
voqiya_keybord2.insert(next_button)

voqiya_keybord3 = InlineKeyboardMarkup(row_width=4)
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
    tugma = InlineKeyboardButton(text=key,callback_data=voqiya_callback_data.new(items=value))
    voqiya_keybord3.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=voqiya_callback_data.new(items='back3'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=voqiya_callback_data.new(items='next3'))
voqiya_keybord3.insert(back_button)
voqiya_keybord3.insert(next_button)

voqiya_keybord4 = InlineKeyboardMarkup(row_width=4)
buttons4 = {
    '49':'49',
    '50':'50',    '51':'51',
    '52':'52',    '53':'53',
    '54':'54',    '55':'55',
    '56':'56',    '57':'57',
    '58':'58',    '59':'59',
    '60':'60',    '61':'61',
    '62':'62',    '63':'63', '64':'64'
}

for key,value in buttons4.items():
    tugma = InlineKeyboardButton(text=key,callback_data=voqiya_callback_data.new(items=value))
    voqiya_keybord4.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=voqiya_callback_data.new(items='back4'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=voqiya_callback_data.new(items='next4'))
voqiya_keybord4.insert(back_button)
voqiya_keybord4.insert(next_button)

voqiya_keybord5 = InlineKeyboardMarkup(row_width=4)
buttons5 = {
    '65': '65',
    '66': '66', '67': '67',
    '68': '68', '69': '69',
    '70': '70', '71': '71',
    '72': '72', '73': '73',
    '74': '74', '75': '75',
    '76': '76', '77': '77',
    '78': '78', '79': '79', '80':'80'
}

for key,value in buttons5.items():
    tugma = InlineKeyboardButton(text=key,callback_data=voqiya_callback_data.new(items=value))
    voqiya_keybord5.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=voqiya_callback_data.new(items='back5'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=voqiya_callback_data.new(items='next5'))
voqiya_keybord5.insert(back_button)
voqiya_keybord5.insert(next_button)

voqiya_keybord6 = InlineKeyboardMarkup(row_width=4)
buttons6 = {
    '81':'81',
    '82':'82',    '83':'83',
    '84':'84',    '85':'85',
    '86':'86',    '87':'87',
    '88':'88',    '89':'89',
    '90':'90',    '91':'91',
    '92':'92',    '93':'93',
    '94':'94',    '95':'95', '96':'96'
}

for key,value in buttons6.items():
    tugma = InlineKeyboardButton(text=key,callback_data=voqiya_callback_data.new(items=value))
    voqiya_keybord6.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=voqiya_callback_data.new(items='back6'))
voqiya_keybord6.insert(back_button)

voqiya_keybords = {
    'back6':voqiya_keybord5,
    'back5':voqiya_keybord4,
    'back4':voqiya_keybord3,
    'back3':voqiya_keybord2,
    'back2':voqiya_keybord1,
    'next1':voqiya_keybord2,
    'next2':voqiya_keybord3,
    'next3':voqiya_keybord4,
    'next4':voqiya_keybord5,
    'next5':voqiya_keybord6

            }
