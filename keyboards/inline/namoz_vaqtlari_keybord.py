from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import namoz_vaqtlari_callback_data
namoz_vaqtlari_keybord1 = InlineKeyboardMarkup(row_width=2)

buttons1 = {
    '🕌 Toshkent shahri':'tashkent',
    '🕌 Andijon viloyati':'andijan',
    "🕌 Farg'ona viloyati":'fergana',
    '🕌 Namangan viloyati':"namangan",
    "🕌 Sirdaryo viloyati": 'gulistan',
    "🕌 Jizzax viloyati":'jizzakh',
    "🕌 Samarqand viloyati":'samarkand',
    "🕌 Buxoro viloyati":'bukhara',
    "🕌 Qashqadaryo viloyati":'qarshi',
    "🕌 Surxondaryo viloyati":'termez',
    "🕌 Navoiy viloyati":'navoi',
    "🕌 Xorazm viloyati":'urgench',
    "🕌 Qoraqalpog'iston respublikasi":'nukus'

}
for key, value in buttons1.items():
    tugma = InlineKeyboardButton(text=key, callback_data=namoz_vaqtlari_callback_data.new(items=value))
    namoz_vaqtlari_keybord1.insert(tugma)

namoz_vaqtlari_keybords = {
'tashkent':'🕌 Toshkent shahri',
'andijan':'🕌 Andijon viloyati',
"fergana":"🕌 Farg'ona viloyati",
'namangan':'🕌 Namangan viloyati',
'gulistan':"🕌 Sirdaryo viloyati",
'jizzakh':"🕌 Jizzax viloyati",
'samarkand':"🕌 Samarqand viloyati",
'bukhara':"🕌 Buxoro viloyati",
'qarshi':"🕌 Qashqadaryo viloyati",
'termez':"🕌 Surxondaryo viloyati",
'navoi':"🕌 Navoiy viloyati",
'urgench':"🕌 Xorazm viloyati",
'nukus':"🕌 Qoraqalpog'iston respublikasi"
}
