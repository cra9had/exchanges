from pprint import pprint

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.const.buy_menu import MY_CURRS_BTN_TEXTS, EXCHANGE_CURRS_BTN_TEXTS
from bot.states.buy_menu import BuyMenuSG


async def go_exchange_currency(callback: CallbackQuery, button: Button, manager: DialogManager):
    if 'ruble' in callback.data:
        manager.dialog_data['my_currency'] = MY_CURRS_BTN_TEXTS.get('ruble')


async def go_input_curr_value(callback: CallbackQuery, button: Button, manager: DialogManager):
    for key, value in EXCHANGE_CURRS_BTN_TEXTS.items():

        if key in callback.data:
            manager.dialog_data['exchange_currency'] = {'key': key, 'value': value}
