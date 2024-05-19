import asyncio
import logging
import sys
from dotenv import load_dotenv, find_dotenv
from os import getenv
import logging
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from dotenv import load_dotenv, find_dotenv
from bot.dialogs.start import start
from bot.dialogs.cabinet import cabinet
from bot.dialogs.buy_menu import buy_menu
from bot.handlers.default_cmd import router as start_router
from bot.handlers.payment import router as payment_router
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv(find_dotenv(".env"))

TOKEN = getenv("BOT_TOKEN")
operators = getenv("OPERATORS").split(',') or []

dp = Dispatcher(operators=operators)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    setup_dialogs(dp)
    dp.include_routers(start_router, payment_router)

    # MAIN ROUTER REGISTRATION MUST BE UPPER THAN AIOGRAM_DIALOG routers
    dp.include_routers(start, cabinet, buy_menu)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
