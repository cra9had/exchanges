from pprint import pprint

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.const.buy_menu import MY_CURRS_BTN_TEXTS, EXCHANGE_CURRS_BTN_TEXTS
from bot.states.buy_menu import BuyMenuSG
from bot.states.cabinet import CabinetSG


async def go_exchange_currency(callback: CallbackQuery, button: Button, manager: DialogManager):
    if 'ruble' in callback.data:
        my_currency = MY_CURRS_BTN_TEXTS.get('ruble')
    else:
        my_currency = 'no_curr_val'

    manager.dialog_data['my_currency'] = {'text': my_currency}


async def go_input_curr_value(callback: CallbackQuery, button: Button, manager: DialogManager):
    for key, value in EXCHANGE_CURRS_BTN_TEXTS.items():

        if key in callback.data:
            manager.dialog_data['exchange_currency'] = {'key': key, 'name': value}


async def input_delivery_type(callback: CallbackQuery, button: Button, manager: DialogManager):
    if 'standart_delivery' in callback.data:
        manager.dialog_data['delivery_type'] = 'standart'
    elif 'fast_delivery' in callback.data:
        manager.dialog_data['delivery_type'] = 'fast'


async def start_to_menu_after_payment(callback: CallbackQuery, button: Button, manager: DialogManager) -> None:
    await manager.start(state=CabinetSG.cabinet_menu, mode=StartMode.RESET_STACK)
