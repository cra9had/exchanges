'''
Кабинет пользователя:

    Доступен для выполнения операций по обмену криптовалюты и фиатных денег.
    Имеет две кнопки: "Купить" и "Поддержка".
'''

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button, Url, SwitchTo
from aiogram_dialog.widgets.text import Const
from bot.const.cabinet import SUPPORT_BTN_TEXT, BUY_BTN_TEXT, SUPPORT_BTN_URL, CABINET_MSG_TEXT
from bot.on_click.cabinet import start_buy_menu
from bot.states.cabinet import CabinetSG
from bot.states.start import StartSG

cabinet = Dialog(
    Window(
        Const(CABINET_MSG_TEXT),
        Row(
            Button(text=Const(BUY_BTN_TEXT), id="buy_btn_click", on_click=start_buy_menu),
            Url(text=Const(SUPPORT_BTN_URL), id='support_btn_click', url=Const(SUPPORT_BTN_URL)),
        ),
        state=CabinetSG.cabinet_menu,
    ),
)
