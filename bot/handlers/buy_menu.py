from aiogram.enums import ContentType, ParseMode
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

from bot.states.cabinet import CabinetSG


async def input_my_curr_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    try:
        my_currency_value = int(message.text)
    except ValueError:
        return

    dialog_manager.dialog_data['my_currency'].update(value=my_currency_value)
    await dialog_manager.next()


async def input_credentials_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    dialog_manager.dialog_data['my_credentials'] = message.text
    await dialog_manager.next()


async def input_payment_detals(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    await dialog_manager.next()


async def after_payment_to_menu_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    await dialog_manager.start(state=CabinetSG.cabinet_menu, mode=StartMode.RESET_STACK)
