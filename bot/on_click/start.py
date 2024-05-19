from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from bot.states.buy_menu import BuyMenuSG
from bot.states.cabinet import CabinetSG


async def start_cabinet(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(state=CabinetSG.cabinet_menu, mode=StartMode.RESET_STACK)