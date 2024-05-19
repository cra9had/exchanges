import asyncio
import logging
import sys
from dotenv import load_dotenv, find_dotenv
from os import getenv
import logging
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from dotenv import load_dotenv, find_dotenv
from bot.dialogs.start import start_dialog
from bot.handlers.default_cmd import router as start_router
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv(find_dotenv(".env"))

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    setup_dialogs(dp)
    dp.include_routers(start_router)

    # MAIN ROUTER REGISTRATION MUST BE UPPER THAN AIOGRAM_DIALOG routers
    dp.include_routers(start_dialog)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
