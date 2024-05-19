"""
Операция "Купить":

    - По нажатию кнопки "Купить" открывается меню выбора валюты для оплаты (в текущей версии - рубль).

    - После выбора валюты пользователем, отображается меню с валютами для
    обмена (криптовалюты, евро, доллар).

    - Пользователь вводит сумму для обмена в рублях.

    - Бот использует интеграцию с сервисами для получения актуального курса и расчета комиссии, формируя сумму для обмена.

    - После нажатия кнопки "Продолжить", пользователь должен ввести реквизиты для получения валюты (адрес кошелька или номер иностранной карты).

    - Пользователю предлагается выбрать способ доставки (быстрая или стандартная).
"""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button, Url, SwitchTo, Column, Next
from aiogram_dialog.widgets.text import Const, Format

from bot.const.buy_menu import CHOOSE_MY_CURR_TEXT, CHOOSE_EXCHANGE_CURR_TEXT, EXCHANGE_CURRS_BTN_TEXTS
from bot.const.cabinet import SUPPORT_BTN_TEXT, BUY_BTN_TEXT, SUPPORT_BTN_URL, CABINET_MSG_TEXT
from bot.getters.buy_menu import get_my_currency, get_all_currs_choice
from bot.on_click.buy_menu import go_exchange_currency, go_input_curr_value
from bot.on_click.cabinet import start_buy_menu
from bot.states.buy_menu import BuyMenuSG

buy_menu = Dialog(
    Window(
        Const(CHOOSE_MY_CURR_TEXT),
        Column(
            Next(text=Const("Рубль ₽"), id='ruble_to_exchange_click', on_click=go_exchange_currency),
        ),
        state=BuyMenuSG.choose_my_currency,
    ),
    Window(
        Format("Вы выбрали {my_currency}"),
        Const(CHOOSE_EXCHANGE_CURR_TEXT),
        Column(
            *(Next(text=Const(exch_curr_value), id=f'{exch_curr_key}_click', on_click=go_input_curr_value) for exch_curr_key, exch_curr_value in EXCHANGE_CURRS_BTN_TEXTS.items())
        ),
        state=BuyMenuSG.choose_to_change_currency,
        getter=get_my_currency,
    ),

    Window(
        Format("Вы теперь тут: {my_currency} {exchange_currency}"),
        getter=get_all_currs_choice,
        state=BuyMenuSG.input_my_currency_value,
    ),
)
