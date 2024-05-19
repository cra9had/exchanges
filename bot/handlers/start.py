from aiogram.types import Message

from aiogram import Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Добро пожаловать в магазин обмена!"
    )
