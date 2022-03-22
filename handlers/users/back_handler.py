from loader import dp
from aiogram.types import Message
from keyboards.default.home_menu import home_menu

@dp.message_handler(text_contains='ortga')
async def show_back(message: Message):
    await message.answer(f"menyu tanglang",reply_markup=home_menu)