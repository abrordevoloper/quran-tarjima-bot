from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types  import Message
from loader import dp
from keyboards.default.home_menu import home_menu
from keyboards.default.menukeybord import menu

@dp.message_handler(CommandStart())
async def bot_start(message: Message):

   info = f"Assalomu aleykum, {message.from_user.full_name}\n"
   info+= f"<b>QURAN TARJIMA</b> botiga xush kelibsiz"
   await message.answer(info,reply_markup=home_menu)

@dp.message_handler(text_contains='Quron tarjima')
async def show_quron(message: Message):
   await message.delete()
   try:
      await message.delete_reply_markup()
   except:
      pass
   await message.answer("Quron suralaridan birini tanlang",reply_markup=menu)


