from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from bot.states.buy_menu import BuyMenuSG


async def start_buy_menu(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(state=BuyMenuSG.choose_my_currency, mode=StartMode.RESET_STACK)
