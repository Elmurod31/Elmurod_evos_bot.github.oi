import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

handlers_router = Router()

@handlers_router.message(CommandStart())
async def command_start_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    await message.answer_photo(img, caption=f"Salom {full_name} 😊")