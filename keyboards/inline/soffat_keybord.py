from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import soffat_callback_data
soffat_keybord1 = InlineKeyboardMarkup(row_width=4)

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
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back1'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next1'))
soffat_keybord1.insert(back_button)
soffat_keybord1.insert(next_button)

soffat_keybord2 = InlineKeyboardMarkup(row_width=4)
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
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord2.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back2'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next2'))
soffat_keybord2.insert(back_button)
soffat_keybord2.insert(next_button)

soffat_keybord3 = InlineKeyboardMarkup(row_width=4)
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
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord3.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back3'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next3'))
soffat_keybord3.insert(back_button)
soffat_keybord3.insert(next_button)

soffat_keybord4 = InlineKeyboardMarkup(row_width=4)
buttons4 = {
    '49':'49',    '50':'50',
    '51':'51',    '52':'52',
    '53':'53',    '54':'54',
    '55':'55',    '56':'56',
    '57':'57',    '58':'58',
    '59':'59',    '60':'60',
    '61':'61',    '62':'62',
    '63':'63',    '64':'64'
}

for key,value in buttons4.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord4.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back4'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next4'))
soffat_keybord4.insert(back_button)
soffat_keybord4.insert(next_button)

soffat_keybord5 = InlineKeyboardMarkup(row_width=4)
buttons5 = {
    '65':'65',
    '66':'66',    '67':'67',
    '68':'68',    '69':'69',
    '70':'70',    '71':'71',
    '72':'72',    '73':'73',
    '74':'74',    '75':'75',
    '76':'76',    '77':'77',
    '78':'78',    '79':'79', '80':'80'

}

for key,value in buttons5.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord5.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back5'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next5'))
soffat_keybord5.insert(back_button)
soffat_keybord5.insert(next_button)

soffat_keybord6 = InlineKeyboardMarkup(row_width=4)
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
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord6.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back6'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next6'))
soffat_keybord6.insert(back_button)
soffat_keybord6.insert(next_button)

soffat_keybord7 = InlineKeyboardMarkup(row_width=4)
buttons7 = {
    '97':'97',
    '98':'98',    '99':'99',
    '100':'100',    '101':'101',
    '102':'102',    '103':'103',
    '104':'104',    '105':'105',
    '106':'106',    '107':'107',
    '108':'108',    '109':'109',
    '110':'110',    '111':'111', '112':'112'

}

for key,value in buttons7.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord7.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back7'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next7'))
soffat_keybord7.insert(back_button)
soffat_keybord7.insert(next_button)

soffat_keybord8 = InlineKeyboardMarkup(row_width=4)
buttons8 = {
    '113':'113',
    '114':'114',    '115':'115',
    '116':'116',    '117':'117',
    '118':'118',    '119':'119',
    '120':'120',    '121':'121',
    '122':'122',    '123':'123',
    '124':'124',    '125':'125',
    '126':'126',    '127':'127', '128':'128'

}

for key,value in buttons8.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord8.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back8'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next8'))
soffat_keybord8.insert(back_button)
soffat_keybord8.insert(next_button)

soffat_keybord9 = InlineKeyboardMarkup(row_width=4)
buttons9 = {
    '129':'129',
    '130':'130',    '131':'131',
    '132':'132',    '133':'133',
    '134':'134',    '135':'135',
    '136':'136',    '137':'137',
    '138':'138',    '139':'139',
    '140':'140',    '141':'141',
    '142':'142',    '143':'143', '144':'144'

}

for key,value in buttons9.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord9.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='back9'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='next9'))
soffat_keybord9.insert(back_button)
soffat_keybord9.insert(next_button)

soffat_keybord10 = InlineKeyboardMarkup(row_width=4)
buttons10 = {
    '145':'145',
    '146':'146',    '147':'147',
    '148':'148',    '149':'149',
    '150':'150',    '151':'151',
    '152':'152',    '153':'153',
    '154':'154',    '155':'155',
    '156':'156',    '157':'157',
    '158':'158',    '159':'159', '160':'160'

}

for key,value in buttons10.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord10.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='backten'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='nextten'))
soffat_keybord10.insert(back_button)
soffat_keybord10.insert(next_button)

soffat_keybord11 = InlineKeyboardMarkup(row_width=4)
buttons11 = {
    '161':'161',
    '162':'162',    '163':'163',
    '164':'164',    '165':'165',
    '166':'166',    '167':'167',
    '168':'168',    '169':'169',
    '170':'170',    '171':'171',
    '172':'172',    '173':'173',
    '174':'174',    '175':'175', '176':'176'

}

for key,value in buttons11.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord11.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='backeleven'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=soffat_callback_data.new(items='nexteleven'))
soffat_keybord11.insert(back_button)
soffat_keybord11.insert(next_button)

soffat_keybord12 = InlineKeyboardMarkup(row_width=4)
buttons12 = {
    '177':'177',
    '178':'178',    '179':'179',
    '180':'180',    '181':'181',
    '182':'182'

}

for key,value in buttons12.items():
    tugma = InlineKeyboardButton(text=key,callback_data=soffat_callback_data.new(items=value))
    soffat_keybord12.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=soffat_callback_data.new(items='backtwele'))
soffat_keybord12.insert(back_button)

soffat_keybords = {
    'backtwele':soffat_keybord11,
    'backeleven':soffat_keybord10,
    'backten':soffat_keybord9,
    'back9':soffat_keybord8,
    'back8':soffat_keybord7,
    'back7':soffat_keybord6,
    'back6':soffat_keybord5,
    'back5':soffat_keybord4,
    'back4':soffat_keybord3,
    'back3':soffat_keybord2,
    'back2':soffat_keybord1,
    'next1':soffat_keybord2,
    'next2':soffat_keybord3,
    'next3':soffat_keybord4,
    'next4':soffat_keybord5,
    'next5':soffat_keybord6,
    'next6':soffat_keybord7,
    'next7':soffat_keybord8,
    'next8':soffat_keybord9,
    'next9':soffat_keybord10,
    'nextten':soffat_keybord11,
    'nexteleven':soffat_keybord12
            }
