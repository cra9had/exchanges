from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from bot.on_click.start import start_cabinet
from bot.states.start import StartSG
from bot.const.start import WELCOME_MSG_TEXT, CABINET_BTN_TEXT

start = Dialog(
    Window(
        Const(WELCOME_MSG_TEXT),
        Row(
            Button(Const(CABINET_BTN_TEXT), id='from_start_to_cabinet_click', on_click=start_cabinet)
        ),
        state=StartSG.start,
    ),
)
